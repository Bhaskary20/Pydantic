from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):

    name: str= Annotated[str, Field(max_length=50, title='Name likh de bruv', description='less than 50 words', examples=['Hari om'] )]
    email: EmailStr
    linkedin: AnyUrl
    age: int= Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married:Annotated[bool, Field(default=None, description='yay or nay?')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]
    height: float


    @field_validator('email')
    @classmethod

    def email_validator(cls, value):
        valid_domain=['icici.com', 'hdfc.com']
        
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('Not a valid domain')
        
        return value
    


    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Must have')
        return model
    


    @computed_field
    @property

    def bmi(self) -> float:
        bmi= round(self.weight/(self.height**2), 2)
        return bmi

    

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('BMI:', patient.bmi)
    print(patient.linkedin)
    print('inserted')
    


patient_info={'name': 'qwerty', 'age':30, 'weight': 72.5, 'height':1.72, 'married': True, 'email': 'abc@icici.com', 'linkedin': 'http://linkedin.com/1132', 'allergies': ['dust', 'animal'], 'contact_details': {'phone': '23456'}}

patient1=Patient(**patient_info)


insert_patient_data(patient1)