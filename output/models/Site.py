from pydantic import BaseModel

class Site(BaseModel):
	site_id : int = None
	site_type : str
	latitude : float
	longitude : float
	display_name : str
	country_id : int

class Type(BaseModel):
	type_id : int = None
	type : str

class SiteParameter(BaseModel):
	site_id : int
	parameter_id : int = None
	parameter_value : str

class Parameter(BaseModel):
	parameter_id : int = None
	parameter_name : str
	site_type_id : int = None
	is_required : bool
