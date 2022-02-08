from fastapi import Request, FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from db import SqlManager
import os
import auth
import uvicorn
from pydantic import BaseModel, ValidationError
from utils import auto_mapper
from typing import List

db = SqlManager()
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

import models.Ref
import models.Site
import models.Device
import models.Report

## Device.Parameter ##
@app.get("/api/Device/Parameter/{id}", response_model=List[models.Device.Parameter])
async def Device_Parameter_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Device', 'Parameter', id, params=request_args)
        return auto_mapper(models.Device.Parameter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Device/Parameter", response_model=List[models.Device.Parameter])
async def Device_Parameter_post(data: models.Device.Parameter, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Device', 'Parameter', data)
        return auto_mapper(models.Device.Parameter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Device/Parameter/{id}", response_model=List[models.Device.Parameter])
async def Device_Parameter_put(id, data: models.Device.Parameter, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Device', 'Parameter', id, data)
        return auto_mapper(models.Device.Parameter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Device/Parameter/{id}", response_model=List[models.Device.Parameter])
async def Device_Parameter_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Device', 'Parameter', id)
        return auto_mapper(models.Device.Parameter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Device.Model ##
@app.get("/api/Device/Model/{id}", response_model=List[models.Device.Model])
async def Device_Model_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Device', 'Model', id, params=request_args)
        return auto_mapper(models.Device.Model, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Device/Model", response_model=List[models.Device.Model])
async def Device_Model_post(data: models.Device.Model, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Device', 'Model', data)
        return auto_mapper(models.Device.Model, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Device/Model/{id}", response_model=List[models.Device.Model])
async def Device_Model_put(id, data: models.Device.Model, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Device', 'Model', id, data)
        return auto_mapper(models.Device.Model, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Device/Model/{id}", response_model=List[models.Device.Model])
async def Device_Model_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Device', 'Model', id)
        return auto_mapper(models.Device.Model, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Device.DeviceTag ##
@app.get("/api/Device/DeviceTag/{id}", response_model=List[models.Device.DeviceTag])
async def Device_DeviceTag_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Device', 'DeviceTag', id, params=request_args)
        return auto_mapper(models.Device.DeviceTag, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Device/DeviceTag", response_model=List[models.Device.DeviceTag])
async def Device_DeviceTag_post(data: models.Device.DeviceTag, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Device', 'DeviceTag', data)
        return auto_mapper(models.Device.DeviceTag, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Device/DeviceTag/{id}", response_model=List[models.Device.DeviceTag])
async def Device_DeviceTag_put(id, data: models.Device.DeviceTag, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Device', 'DeviceTag', id, data)
        return auto_mapper(models.Device.DeviceTag, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Device/DeviceTag/{id}", response_model=List[models.Device.DeviceTag])
async def Device_DeviceTag_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Device', 'DeviceTag', id)
        return auto_mapper(models.Device.DeviceTag, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Device.Type ##
@app.get("/api/Device/Type/{id}", response_model=List[models.Device.Type])
async def Device_Type_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Device', 'Type', id, params=request_args)
        return auto_mapper(models.Device.Type, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Device/Type", response_model=List[models.Device.Type])
async def Device_Type_post(data: models.Device.Type, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Device', 'Type', data)
        return auto_mapper(models.Device.Type, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Device/Type/{id}", response_model=List[models.Device.Type])
async def Device_Type_put(id, data: models.Device.Type, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Device', 'Type', id, data)
        return auto_mapper(models.Device.Type, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Device/Type/{id}", response_model=List[models.Device.Type])
async def Device_Type_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Device', 'Type', id)
        return auto_mapper(models.Device.Type, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Device.DeviceParameter ##
@app.get("/api/Device/DeviceParameter/{id}", response_model=List[models.Device.DeviceParameter])
async def Device_DeviceParameter_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Device', 'DeviceParameter', id, params=request_args)
        return auto_mapper(models.Device.DeviceParameter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Device/DeviceParameter", response_model=List[models.Device.DeviceParameter])
async def Device_DeviceParameter_post(data: models.Device.DeviceParameter, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Device', 'DeviceParameter', data)
        return auto_mapper(models.Device.DeviceParameter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Device/DeviceParameter/{id}", response_model=List[models.Device.DeviceParameter])
async def Device_DeviceParameter_put(id, data: models.Device.DeviceParameter, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Device', 'DeviceParameter', id, data)
        return auto_mapper(models.Device.DeviceParameter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Device/DeviceParameter/{id}", response_model=List[models.Device.DeviceParameter])
async def Device_DeviceParameter_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Device', 'DeviceParameter', id)
        return auto_mapper(models.Device.DeviceParameter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Ref.Country ##
@app.get("/api/Ref/Country/{id}", response_model=List[models.Ref.Country])
async def Ref_Country_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Ref', 'Country', id, params=request_args)
        return auto_mapper(models.Ref.Country, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Ref/Country", response_model=List[models.Ref.Country])
async def Ref_Country_post(data: models.Ref.Country, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Ref', 'Country', data)
        return auto_mapper(models.Ref.Country, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Ref/Country/{id}", response_model=List[models.Ref.Country])
async def Ref_Country_put(id, data: models.Ref.Country, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Ref', 'Country', id, data)
        return auto_mapper(models.Ref.Country, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Ref/Country/{id}", response_model=List[models.Ref.Country])
async def Ref_Country_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Ref', 'Country', id)
        return auto_mapper(models.Ref.Country, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Site.Site ##
@app.get("/api/Site/Site/{id}", response_model=List[models.Site.Site])
async def Site_Site_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Site', 'Site', id, params=request_args)
        return auto_mapper(models.Site.Site, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Site/Site", response_model=List[models.Site.Site])
async def Site_Site_post(data: models.Site.Site, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Site', 'Site', data)
        return auto_mapper(models.Site.Site, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Site/Site/{id}", response_model=List[models.Site.Site])
async def Site_Site_put(id, data: models.Site.Site, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Site', 'Site', id, data)
        return auto_mapper(models.Site.Site, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Site/Site/{id}", response_model=List[models.Site.Site])
async def Site_Site_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Site', 'Site', id)
        return auto_mapper(models.Site.Site, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Site.Type ##
@app.get("/api/Site/Type/{id}", response_model=List[models.Site.Type])
async def Site_Type_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Site', 'Type', id, params=request_args)
        return auto_mapper(models.Site.Type, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Site/Type", response_model=List[models.Site.Type])
async def Site_Type_post(data: models.Site.Type, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Site', 'Type', data)
        return auto_mapper(models.Site.Type, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Site/Type/{id}", response_model=List[models.Site.Type])
async def Site_Type_put(id, data: models.Site.Type, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Site', 'Type', id, data)
        return auto_mapper(models.Site.Type, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Site/Type/{id}", response_model=List[models.Site.Type])
async def Site_Type_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Site', 'Type', id)
        return auto_mapper(models.Site.Type, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Site.SiteParameter ##
@app.get("/api/Site/SiteParameter/{id}", response_model=List[models.Site.SiteParameter])
async def Site_SiteParameter_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Site', 'SiteParameter', id, params=request_args)
        return auto_mapper(models.Site.SiteParameter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Site/SiteParameter", response_model=List[models.Site.SiteParameter])
async def Site_SiteParameter_post(data: models.Site.SiteParameter, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Site', 'SiteParameter', data)
        return auto_mapper(models.Site.SiteParameter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Site/SiteParameter/{id}", response_model=List[models.Site.SiteParameter])
async def Site_SiteParameter_put(id, data: models.Site.SiteParameter, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Site', 'SiteParameter', id, data)
        return auto_mapper(models.Site.SiteParameter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Site/SiteParameter/{id}", response_model=List[models.Site.SiteParameter])
async def Site_SiteParameter_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Site', 'SiteParameter', id)
        return auto_mapper(models.Site.SiteParameter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Site.Parameter ##
@app.get("/api/Site/Parameter/{id}", response_model=List[models.Site.Parameter])
async def Site_Parameter_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Site', 'Parameter', id, params=request_args)
        return auto_mapper(models.Site.Parameter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Site/Parameter", response_model=List[models.Site.Parameter])
async def Site_Parameter_post(data: models.Site.Parameter, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Site', 'Parameter', data)
        return auto_mapper(models.Site.Parameter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Site/Parameter/{id}", response_model=List[models.Site.Parameter])
async def Site_Parameter_put(id, data: models.Site.Parameter, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Site', 'Parameter', id, data)
        return auto_mapper(models.Site.Parameter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Site/Parameter/{id}", response_model=List[models.Site.Parameter])
async def Site_Parameter_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Site', 'Parameter', id)
        return auto_mapper(models.Site.Parameter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Report.TrackerDailyJournal ##
@app.get("/api/Report/TrackerDailyJournal/{id}", response_model=List[models.Report.TrackerDailyJournal])
async def Report_TrackerDailyJournal_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Report', 'TrackerDailyJournal', id, params=request_args)
        return auto_mapper(models.Report.TrackerDailyJournal, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Report/TrackerDailyJournal", response_model=List[models.Report.TrackerDailyJournal])
async def Report_TrackerDailyJournal_post(data: models.Report.TrackerDailyJournal, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Report', 'TrackerDailyJournal', data)
        return auto_mapper(models.Report.TrackerDailyJournal, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Report/TrackerDailyJournal/{id}", response_model=List[models.Report.TrackerDailyJournal])
async def Report_TrackerDailyJournal_put(id, data: models.Report.TrackerDailyJournal, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Report', 'TrackerDailyJournal', id, data)
        return auto_mapper(models.Report.TrackerDailyJournal, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Report/TrackerDailyJournal/{id}", response_model=List[models.Report.TrackerDailyJournal])
async def Report_TrackerDailyJournal_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Report', 'TrackerDailyJournal', id)
        return auto_mapper(models.Report.TrackerDailyJournal, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Report.Inverter ##
@app.get("/api/Report/Inverter/{id}", response_model=List[models.Report.Inverter])
async def Report_Inverter_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Report', 'Inverter', id, params=request_args)
        return auto_mapper(models.Report.Inverter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Report/Inverter", response_model=List[models.Report.Inverter])
async def Report_Inverter_post(data: models.Report.Inverter, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Report', 'Inverter', data)
        return auto_mapper(models.Report.Inverter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Report/Inverter/{id}", response_model=List[models.Report.Inverter])
async def Report_Inverter_put(id, data: models.Report.Inverter, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Report', 'Inverter', id, data)
        return auto_mapper(models.Report.Inverter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Report/Inverter/{id}", response_model=List[models.Report.Inverter])
async def Report_Inverter_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Report', 'Inverter', id)
        return auto_mapper(models.Report.Inverter, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Report.TrackerDailySummaryByIts ##
@app.get("/api/Report/TrackerDailySummaryByIts/{id}", response_model=List[models.Report.TrackerDailySummaryByIts])
async def Report_TrackerDailySummaryByIts_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Report', 'TrackerDailySummaryByIts', id, params=request_args)
        return auto_mapper(models.Report.TrackerDailySummaryByIts, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Report/TrackerDailySummaryByIts", response_model=List[models.Report.TrackerDailySummaryByIts])
async def Report_TrackerDailySummaryByIts_post(data: models.Report.TrackerDailySummaryByIts, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Report', 'TrackerDailySummaryByIts', data)
        return auto_mapper(models.Report.TrackerDailySummaryByIts, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Report/TrackerDailySummaryByIts/{id}", response_model=List[models.Report.TrackerDailySummaryByIts])
async def Report_TrackerDailySummaryByIts_put(id, data: models.Report.TrackerDailySummaryByIts, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Report', 'TrackerDailySummaryByIts', id, data)
        return auto_mapper(models.Report.TrackerDailySummaryByIts, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Report/TrackerDailySummaryByIts/{id}", response_model=List[models.Report.TrackerDailySummaryByIts])
async def Report_TrackerDailySummaryByIts_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Report', 'TrackerDailySummaryByIts', id)
        return auto_mapper(models.Report.TrackerDailySummaryByIts, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Report.Comment ##
@app.get("/api/Report/Comment/{id}", response_model=List[models.Report.Comment])
async def Report_Comment_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Report', 'Comment', id, params=request_args)
        return auto_mapper(models.Report.Comment, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Report/Comment", response_model=List[models.Report.Comment])
async def Report_Comment_post(data: models.Report.Comment, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Report', 'Comment', data)
        return auto_mapper(models.Report.Comment, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Report/Comment/{id}", response_model=List[models.Report.Comment])
async def Report_Comment_put(id, data: models.Report.Comment, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Report', 'Comment', id, data)
        return auto_mapper(models.Report.Comment, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Report/Comment/{id}", response_model=List[models.Report.Comment])
async def Report_Comment_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Report', 'Comment', id)
        return auto_mapper(models.Report.Comment, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Report.InverterFault ##
@app.get("/api/Report/InverterFault/{id}", response_model=List[models.Report.InverterFault])
async def Report_InverterFault_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Report', 'InverterFault', id, params=request_args)
        return auto_mapper(models.Report.InverterFault, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Report/InverterFault", response_model=List[models.Report.InverterFault])
async def Report_InverterFault_post(data: models.Report.InverterFault, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Report', 'InverterFault', data)
        return auto_mapper(models.Report.InverterFault, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Report/InverterFault/{id}", response_model=List[models.Report.InverterFault])
async def Report_InverterFault_put(id, data: models.Report.InverterFault, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Report', 'InverterFault', id, data)
        return auto_mapper(models.Report.InverterFault, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Report/InverterFault/{id}", response_model=List[models.Report.InverterFault])
async def Report_InverterFault_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Report', 'InverterFault', id)
        return auto_mapper(models.Report.InverterFault, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Report.Plant ##
@app.get("/api/Report/Plant/{id}", response_model=List[models.Report.Plant])
async def Report_Plant_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Report', 'Plant', id, params=request_args)
        return auto_mapper(models.Report.Plant, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Report/Plant", response_model=List[models.Report.Plant])
async def Report_Plant_post(data: models.Report.Plant, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Report', 'Plant', data)
        return auto_mapper(models.Report.Plant, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Report/Plant/{id}", response_model=List[models.Report.Plant])
async def Report_Plant_put(id, data: models.Report.Plant, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Report', 'Plant', id, data)
        return auto_mapper(models.Report.Plant, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Report/Plant/{id}", response_model=List[models.Report.Plant])
async def Report_Plant_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Report', 'Plant', id)
        return auto_mapper(models.Report.Plant, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Device.Device ##
@app.get("/api/Device/Device/{id}", response_model=List[models.Device.Device])
async def Device_Device_get(id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    try:
        data, cols = db.get('Device', 'Device', id, params=request_args)
        return auto_mapper(models.Device.Device, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/Device/Device", response_model=List[models.Device.Device])
async def Device_Device_post(data: models.Device.Device, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.post('Device', 'Device', data)
        return auto_mapper(models.Device.Device, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/Device/Device/{id}", response_model=List[models.Device.Device])
async def Device_Device_put(id, data: models.Device.Device, tkn = Depends(auth.validate_token)):
    try:
        data, cols = db.put('Device', 'Device', id, data)
        return auto_mapper(models.Device.Device, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/Device/Device/{id}", response_model=List[models.Device.Device])
async def Device_Device_delete(id, tkn = Depends(auth.validate_token)):
    try:    
        data, cols = db.delete('Device', 'Device', id)
        return auto_mapper(models.Device.Device, data, cols)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("API_PORT")),
        reload=True,
        ssl_keyfile="./server.key",
        ssl_certfile="./server.crt"
    )