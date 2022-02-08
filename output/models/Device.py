from pydantic import BaseModel

class Parameter(BaseModel):
	parameter_id : int = None
	parameter_name : str
	device_type_id : int = None
	is_required : bool

class Model(BaseModel):
	model_id : int = None
	model : str

class DeviceTag(BaseModel):
	device_id : int
	tag_name : str
	tag_value : str

class Type(BaseModel):
	type_id : int = None
	type : str

class DeviceParameter(BaseModel):
	device_id : int
	parameter_id : int = None
	parameter_value : str

class Device(BaseModel):
	device_id : int = None
	UID : str
	device_type_id : int = None
	device_model_id : int = None
	site_id : int = None
	interval_in_seconds : int
	is_active : bool = None
