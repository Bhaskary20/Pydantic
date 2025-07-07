from pydantic import BaseModel

class Address(BaseModel):

    state: str
    city: str
    pin: int


class patient(BaseModel):

    name: str
    age: int
    gender: str
    address: Address


address_dict= {'state': 'Assam', 'city':'Nalbari', 'pin': 781341}

address1= Address(**address_dict)

patient_dict= {'name': 'qwerty', 'age':22, 'gender': 'Male', 'address': address1}

patient1= patient(**patient_dict)

#print(patient1)
#print(patient1.address.city)

#temp= patient1.model_dump

temp= patient1.model_dump_json(include=['name', 'gender'])
print(temp)
print(type(temp))    