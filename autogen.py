from typing import List
import os
import shutil

from sqlalchemy import null
import api_builder
import sys
from sql_python_mappings import get_python_type, validate_python_name, column_mappings
from db import SqlManager
from dataclasses import dataclass, field

@dataclass
class Property:
    property_name : str
    data_type : str
    max_length: int
    precision: int
    nullable: int
    identity: int
    def serialize(self):
        try:
            msg = f'{validate_python_name(self.property_name)} : {get_python_type(self.data_type)}'
            if self.nullable == 1 or self.identity == 1:
                return msg + ' = None'
            else:
                return msg
        except ValueError:
            return None

@dataclass
class Model:
    schema_name : str
    model_name : str
    properties : List = field(default_factory=lambda: [])

    def add_property(self, property: Property):
        self.properties.append(property)

    def serialize(self):
        joinable = '\n\t'
        template = f'''
class {self.model_name}(BaseModel):
\t{joinable.join([s.serialize() for s in self.properties if s.serialize() is not None])}
'''
        return template

def generate():
    db = SqlManager()
    cols = db.get()

    models = {}
    for c in cols:
        key = f'{c["schema_name"]}.{c["table_name"]}'
        if key not in models:
            m = Model(schema_name=c["schema_name"], model_name=c["table_name"])
            models[key] = m

        p = Property(property_name=c["column_name"], data_type=c["data_type"], max_length=c["max_length"], precision=c["precision"], nullable=c["is_nullable"], identity=c["identity_column"])
        models[key].add_property(p)

    out = os.path.join(os.getenv("OUTPUT"))
    try:
        shutil.rmtree(out)
    except FileNotFoundError as e:
        print('Nothing to clean, continuing')
    except OSError:
        pass

    out = os.path.join(os.getenv("OUTPUT"), 'models')
    os.makedirs(out)

    # build models
    for m in models:
        outfile = os.path.join(out, f'{models[m].schema_name}.py')
        if os.path.isfile(outfile) == False:
            with open(outfile, 'a') as ofile:
                ofile.write('from pydantic import BaseModel\n')
                ofile.write(models[m].serialize())
        else:
             with open(outfile, 'a') as ofile:
                ofile.write(models[m].serialize())

    with open(os.path.join(os.getenv("OUTPUT"), "models", "__init__.py"), 'w') as initfile:
        schemas = ', '.join(set([f"'{models[m].schema_name}'" for m in models]))
        initfile.write(f"__all__ = [{schemas}]")

    # copy templates files
    input = os.path.join('./api')
    templates = os.listdir(input)
    output = os.path.join(os.getenv("OUTPUT"))

    for f in templates:
        shutil.copy(os.path.join(input, f), os.path.join(output, f))

    api_imports = '\n'.join(set([f'import models.{models[m].schema_name}' for m in models]))
    api_endpoints = '\n'.join([api_builder.build_api_endpoints(models[m]) for m in models])

    with open(os.path.join(output, 'main.py'), 'r') as mainfile:
        c = mainfile.read()
        c = c.replace('## ENDPOINTS ##', f"{api_imports}\n{api_endpoints}")
    with open(os.path.join(output, 'main.py'), 'w') as mainfile:
        mainfile.write(c)

    with open(os.path.join(output, 'utils.py'), 'r') as mainfile:
        c = mainfile.read()
        c = c.replace('## Columns ##', f"column_mappings = {column_mappings}")
    with open(os.path.join(output, 'utils.py'), 'w') as mainfile:
        mainfile.write(c)

if __name__ == "__main__":
    generate()