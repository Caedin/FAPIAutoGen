import sqlalchemy
from urllib.parse import quote_plus
import os
from utils import column_mappings

class SqlManager():
    def __init__(self, schema=None):
        server = os.getenv("MSSQL_SERVER")
        database = os.getenv("MSSQL_DATABASE")
        user = os.getenv("MSSQL_USER")
        password = os.getenv("MSSQL_PASSWORD")
        conn = quote_plus(f"DRIVER={{FreeTDS}};SERVER={server};DATABASE={database};UID={user};PWD={password};PORT=1433")
        self.engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % conn)
        if schema is not None:
            self.schema = schema
        self.id_columns = {}

    def _dereference_columns(self, schema, table, data):
        id_column = self.get_id_column(schema, table)
        data = dict(data)
        data = {column_mappings[k]: v for k, v in data.items()}
        data_lower = {k.lower(): v for k, v in data.items() if k.lower() != id_column}
        valid_columns = set([x.lower() for x in list(self.engine.execute(f'SELECT TOP 1 * FROM {schema}.{table}').keys())]) - set(id_column)
        cols = [x for x in data_lower.keys() if x in valid_columns]
        return data_lower, cols

    def _execute_query(self, text, params):
        conn = self.engine.connect()
        try:
            txn = conn.begin()
            result = conn.execute(text, **params)
            columns = result.keys()
            result = result.fetchall()
            txn.commit()
        finally:
            conn.close()
        return result, columns

    def get_id_column(self, schema, table):
        schema, table = schema.lower(), table.lower()
        if f'{schema}.{table}' not in self.id_columns:
            valid_columns = set([x.lower() for x in list(self.engine.execute(f'SELECT TOP 1 * FROM {schema}.{table}').keys())])
            if 'id' in valid_columns:
                self.id_columns[f'{schema}.{table}'] = 'id'
            elif f'{table}id' in valid_columns:
                self.id_columns[f'{schema}.{table}'] = f'{table}id'
        return self.id_columns[f'{schema}.{table}']


    def get(self, schema, table, id = None, params = None):
        if id != ":":
            id_column = self.get_id_column(schema, table)
            params[id_column] = id
        
        text = sqlalchemy.sql.text(
            f'''
            SELECT * FROM {schema}.{table} WHERE 
            {' AND '.join([f" {key} = :{key}" for key in params] + [" 1 = 1 "])}
            '''
        )
        return self._execute_query(text, params)

    def put(self, schema, table, id, data):
        id_column = self.get_id_column(schema, table)
        data_lower, cols = self._dereference_columns(schema, table, data)
        text = sqlalchemy.sql.text(
            f'''
            UPDATE {schema}.{table} SET {', '.join([f"{col}=:{col}" for col in cols])} OUTPUT Inserted.* WHERE {id_column} = :id
            '''
        )
        data_lower['id'] = id
        return self._execute_query(text, data_lower)

    def delete(self, schema, table, id):
        id_column = self.get_id_column(schema, table)
        text = sqlalchemy.sql.text(
            f'''
            DELETE FROM {schema}.{table} OUTPUT DELETED.* WHERE {id_column} = :id
            '''
        )
        return self._execute_query(text, {'id' : id})

    def post(self, schema, table, data):
        data_lower, cols = self._dereference_columns(schema, table, data)
        text = sqlalchemy.sql.text(
            f'''
            INSERT INTO {schema}.{table} ({', '.join(cols)}) OUTPUT Inserted.* VALUES
            ({','.join([f":{col}" for col in cols])})
            '''
        )

        return self._execute_query(text, data_lower)

        
