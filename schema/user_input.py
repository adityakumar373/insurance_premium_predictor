from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities

#pydantic model to validate incoming data
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of user")]
    weight: Annotated[float, Field(..., gt=0, description="weight of the patient in kg")]
    height: Annotated[float, Field(..., gt=0, description="height of the patient in cm")]
    city: Annotated[str, Field(..., description="city of user")]
    income_lpa: Annotated[float, Field(..., gt=0, description="annual income in lakhs")]
    smoker: Annotated[bool, Field(..., description="whether the user smokes")]
    occupation: Annotated[Literal['Accountant', 'Architect', 'Banker', 'Businessman', 'Carpenter', 'Chef', 'Civil Servant', 'Consultant', 'Content Writer', 'Data Analyst', 'Doctor', 'Driver', 'Electrician', 'Engineer', 'Factory Worker', 'Government Employee', 'HR Manager', 'Insurance Agent', 'Lab Technician', 'Lawyer', 'Marketing Manager', 'Nurse', 'Pharmacist', 'Plumber', 'Real Estate Agent', 'Retail Manager', 'Sales Manager', 'Shop Owner', 'Software Engineer', 'Teacher'], Field(..., description="occupation of the user")]

    @field_validator('city')
    @classmethod
    def validate_city(cls, v:str)->str:
        v=v.strip().title()
        return v

    @field_validator('occupation')
    @classmethod
    def validate_occupation(cls, v:str)->str:
        v=v.strip().title()
        return v    

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / ((self.height / 100) ** 2)

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle-age"
        else:
            return "senior"

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3         
