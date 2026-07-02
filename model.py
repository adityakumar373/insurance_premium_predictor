import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, classification_report
import pickle

df=pd.read_csv('data/Insurance_Data.csv')
df.sample(5)
df_feat=df.copy()

#feature 1: bmi
df_feat['bmi']=df_feat['weight']/((df_feat['height']/100)**2)

#feature 2: age group
def age_group(age):
    if age < 25:
        return 'young'
    elif age<45:
        return 'adult'
    elif age<60:
        return 'middle-age'
    else:
        return 'senior'

df_feat['age_group']=df_feat["age"].apply(age_group)

#feature 3: lifestyle risk
def lifestyle_risk(row):
    if row['smoker'] and row['bmi'] > 30:
        return 'high'
    elif row['smoker'] or row['bmi'] > 27:
        return 'medium'
    else:
        return 'low'

df_feat["lifestyle_risk"]=df_feat.apply(lifestyle_risk, axis=1)

tier_1_cities=["Bangalore","Chennai","Delhi","Hyderabad","Kolkata","Mumbai","Pune","Ahmedabad"]
tier_2_cities=["Agra","Allahabad","Amritsar","Bhopal","Faridabad","Ghaziabad","Indore","Jaipur","Kanpur","Lucknow","Ludhiana","Meerut","Nagpur","Nashik","Patna","Rajkot","Ranchi","Srinagar","Surat","Vadodara","Varanasi","Visakhapatnam"]

#feature 4: city tier
def city_tier(city):
    if city in tier_1_cities:
        return 1
    elif city in tier_2_cities:
        return 2
    else:
        return 3
df_feat['city_tier']=df_feat['city'].apply(city_tier)

df_feat.drop(columns=['height','weight','age','city','smoker'])[['income_lpa', 'occupation', 'bmi', 'age_group', 'lifestyle_risk', 'city_tier', 'insurance_premium_category']].sample(5)

# Select features and target
x=df_feat[["bmi", "age_group", "lifestyle_risk", "city_tier", "income_lpa", "occupation"]]
y=df_feat["insurance_premium_category"]

# Define categorical and numeric features
categorical_features = ["age_group", "lifestyle_risk", "occupation", "city_tier"]
numeric_features = ["bmi", "income_lpa"]

# Create column transformer for OHE
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features),
        ("num", "passthrough", numeric_features)
    ]
)


# Create a pipeline with preprocessing and random forest classifier
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])


# Split data and train model
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
pipeline.fit(x_train, y_train)

Pipeline(steps=[('preprocessor',ColumnTransformer
                 (transformers=[('cat', OneHotEncoder(),['age_group','lifestyle_risk','occupation', 'city_tier']),('num', 'passthrough', ['bmi', 'income_lpa'])])),
                 ('classifier', RandomForestClassifier(random_state=42))])


# Predict and evaluate
y_pred = pipeline.predict(x_test)
accuracy_score(y_test, y_pred)

# Save the trained pipeline using pickle
pickle_model_path = "model.pkl"
with open(pickle_model_path, "wb") as f:
    pickle.dump(pipeline, f)