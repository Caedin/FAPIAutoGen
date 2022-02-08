import re

def validate_python_name(sqlname):
    sqlname = re.sub(r'[^a-zA-Z0-9]', '', sqlname)
    if sqlname.isupper() == False:
        sqlname = re.sub('([A-Z]{1})', r'_\1', sqlname).lower()
        if sqlname[0] == '_':
            sqlname = sqlname[1:]
    matches = re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*', sqlname)
    if matches is None or matches[0] != sqlname:
        print(f"Invalid or unsupported sqlname: {sqlname}")
        raise ValueError(f"Invalid or unsupported sqlname: {sqlname}") 
    return sqlname

def auto_mapper(type_reference, data, columns):
    columns = list(columns)
    def create_object(row):
        init_vals = {}
        for col, val in  zip(list(columns), row):
            col = validate_python_name(col)
            init_vals[col] = val
        return type_reference(**init_vals)
    
    results = list(map(create_object, data))
    return results

## Columns ##