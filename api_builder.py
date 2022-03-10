
from autogen import Model


def build_api_endpoints(model: Model):
    schema = model.schema_name
    table = model.model_name

    template = f'''
## {schema}.{table} ##
@app.get("/api/{schema}/{table}/{{id}}", response_model=List[models.{schema}.{table}])
async def {schema}_{table}_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    data, cols = db.get('{schema}', '{table}', id, params=request_args)
    return auto_mapper(models.{schema}.{table}, data, cols)

@app.post("/api/{schema}/{table}", response_model=List[models.{schema}.{table}])
async def {schema}_{table}_post(data: models.{schema}.{table}, tkn = Depends(auth.validate_token)):
    data, cols = db.post('{schema}', '{table}', data)
    return auto_mapper(models.{schema}.{table}, data, cols)

@app.put("/api/{schema}/{table}/{{id}}", response_model=List[models.{schema}.{table}])
async def {schema}_{table}_put(id, data: models.{schema}.{table}, tkn = Depends(auth.validate_token)):
    data, cols = db.put('{schema}', '{table}', id, data)
    return auto_mapper(models.{schema}.{table}, data, cols)

@app.delete("/api/{schema}/{table}/{{id}}", response_model=List[models.{schema}.{table}])
async def {schema}_{table}_delete(id, tkn = Depends(auth.validate_token)):  
    data, cols = db.delete('{schema}', '{table}', id)
    return auto_mapper(models.{schema}.{table}, data, cols)
    '''
    return template