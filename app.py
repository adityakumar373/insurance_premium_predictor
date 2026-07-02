from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd

#import the ml model
with open('model.pkl','rb') as f:
    model=pickle.load(f)

app=FastAPI()

tier_1_cities = ["Bangalore", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai", "Pune", "Ahmedabad"]
tier_2_cities = ["Agra", "Allahabad", "Amritsar", "Bhopal", "Faridabad", "Ghaziabad", "Indore", "Jaipur","Kanpur", "Lucknow", "Ludhiana", "Meerut", "Nagpur", "Nashik", "Patna", "Rajkot","Ranchi", "Srinagar", "Surat", "Vadodara", "Varanasi", "Visakhapatnam"]

#pydantic model to validate incoming data
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of user")]
    weight: Annotated[float, Field(..., gt=0, description="weight of the patient in kg")]
    height: Annotated[float, Field(..., gt=0, description="height of the patient in cm")]
    city: Annotated[str, Field(..., description="city of user")]
    income_lpa: Annotated[float, Field(..., gt=0, description="annual income in lakhs")]
    smoker: Annotated[bool, Field(..., description="whether the user smokes")]
    occupation: Annotated[Literal['Accountant', 'Architect', 'Banker', 'Businessman', 'Carpenter', 'Chef', 'Civil Servant', 'Consultant', 'Content Writer', 'Data Analyst', 'Doctor', 'Driver', 'Electrician', 'Engineer', 'Factory Worker', 'Government Employee', 'HR Manager', 'Insurance Agent', 'Lab Technician', 'Lawyer', 'Marketing Manager', 'Nurse', 'Pharmacist', 'Plumber', 'Real Estate Agent', 'Retail Manager', 'Sales Manager', 'Shop Owner', 'Software Engineer', 'Teacher'], Field(..., description="occupation of the user")]

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
        
@app.post("/predict")
def predict_premium(data: UserInput):
    input_df = pd.DataFrame([
        {
            'bmi':data.bmi,
            'age_group':data.age_group,
            'lifestyle_risk':data.lifestyle_risk,
            'city_tier':data.city_tier,
            'income_lpa':data.income_lpa,
            'occupation':data.occupation
        }
    ])

    prediction=model.predict(input_df)[0]

    return JSONResponse(status_code=200, content={"insurance_premium_category": prediction})

