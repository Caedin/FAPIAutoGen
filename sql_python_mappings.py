import re

mapping = {
    'text' : 'str',
    'uniqueidentifier' : 'str',
    'date' : 'str',
    'time' : 'str',
    'datetime2' : 'str',
    'tinyint' : 'int',
    'smallint' : 'int',
    'int' : 'int',
    'smalldatetime' : 'str',
    'real' : 'float',
    'datetime' : 'str',
    'float' : 'float',
    'ntext' : 'str',
    'bit' : 'bool',
    'decimal' : 'float',
    'numeric' : 'float',
    'smallmoney' : 'int',
    'bigint' : 'int',
    'varbinary' : 'str',
    'varchar' : 'str',
    'binary' : 'str',
    'char' : 'str',
    'timestamp' : 'str',
    'nvarchar' : 'str',
    'nchar' : 'str'
}

column_mappings = {}

def validate_python_name(sqlname):
    global column_mappings
    starting_val = sqlname
    leading_digits = re.match(r'^[0-9]*', sqlname)
    if leading_digits is not None and leading_digits[0] != '':
        sqlname = sqlname.replace(leading_digits[0], '') + '_' + leading_digits[0]
    sqlname = re.sub(r'[^a-zA-Z0-9]', '', sqlname)
    if sqlname.isupper() == False:
        sqlname = re.sub('([A-Z]{1})', r'_\1', sqlname).lower()
        if sqlname[0] == '_':
            sqlname = sqlname[1:]
    matches = re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*', sqlname)
    if matches is None or matches[0] != sqlname:
        print(f"Invalid or unsupported sqlname: {sqlname}")
        raise ValueError(f"Invalid or unsupported sqlname: {sqlname}") 
    column_mappings[sqlname] = starting_val
    return sqlname

def get_python_type(sqltype):
    if sqltype in mapping:
        return mapping[sqltype]
    else:
        raise ValueError(f"Invalid or unsupported sqltype: {sqltype}")