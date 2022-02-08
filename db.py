import sqlalchemy
from urllib.parse import quote_plus
import os

class SqlManager():
    def __init__(self):
        server = os.getenv("MSSQL_SERVER")
        database = os.getenv("MSSQL_DATABASE")
        user = os.getenv("MSSQL_USER")
        password = os.getenv("MSSQL_PASSWORD")
        conn = quote_plus(f"DRIVER={{FreeTDS}};SERVER={server};DATABASE={database};UID={user};PWD={password};PORT=1433")
        self.engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % conn)

    def _execute_query(self, text, params = {}):
        conn = self.engine.connect()
        try:
            txn = conn.begin()
            result = conn.execute(text, **params)
            result = result.fetchall()
            txn.commit()
        finally:
            conn.close()
        return result

    def get(self):
        text = sqlalchemy.sql.text(f'''
            with columns AS
            (
                select schema_name(tab.schema_id) as schema_name,
                    tab.name as table_name, 
                    col.column_id,
                    col.name as column_name, 
                    t.name as data_type,    
                    col.max_length,
                    col.precision,
                    col.is_nullable
                from sys.tables as tab
                    inner join sys.columns as col
                        on tab.object_id = col.object_id
                    left join sys.types as t
                    on col.user_type_id = t.user_type_id
            ),
            id_cols as
            (
                select TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME
                from INFORMATION_SCHEMA.COLUMNS
                where COLUMNPROPERTY(object_id(TABLE_SCHEMA+'.'+TABLE_NAME), COLUMN_NAME, 'IsIdentity') = 1
            )
            SELECT
                c.*, case WHEN ic.column_name IS NULL THEN 0 ELSE 1 END AS 'identity_column'
            FROM
                columns c
            LEFT JOIN
                id_cols ic
            ON
                c.schema_name = ic.TABLE_SCHEMA
            AND
                c.table_name = ic.TABLE_NAME
            AND
                c.column_name = ic.COLUMN_NAME
            '''
        )
        return self._execute_query(text)
