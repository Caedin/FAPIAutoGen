from pydantic import BaseModel

class Country(BaseModel):
	id : int = None
	name : str
	ISO : str
	ISO3 : str = None
	num_code : int = None
	phone_code : int
