# 🏥 Insurance Premium Category Predictor

A Machine Learning web application that predicts the **Insurance Premium Category (Low, Medium, or High)** based on a user's demographic, lifestyle, and financial information.

The project is built using **Python, Scikit-learn, FastAPI, and Streamlit**, with feature engineering, model deployment, and an interactive user interface.

---

## 🚀 Features

* Predicts Insurance Premium Category (Low, Medium, High)
* Feature Engineering for improved model performance
* Random Forest Classifier
* Scikit-learn Pipeline with preprocessing
* FastAPI REST API
* Interactive Streamlit frontend
* Automatic API documentation using Swagger UI
* Input validation using Pydantic
* Clean and modular code structure

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Random Forest Classifier
* FastAPI
* Streamlit
* Pydantic
* Pickle

---

## 📂 Project Structure

```text
insurance-premium-predictor/
│
├── app.py                 # FastAPI backend
├── frontend.py            # Streamlit frontend
├── model.py               # Model training script
├── model.pkl              # Trained ML pipeline
├── requirements.txt
├── README.md
│
└── data/
    └── Insurance_Data.csv
```

---

## 📊 Dataset

The dataset contains customer information such as:

* Age
* Height
* Weight
* Annual Income (LPA)
* City
* Occupation
* Smoking Status
* Insurance Premium Category (Target)

---

## ⚙️ Feature Engineering

The following features are generated before model training:

### ✅ Body Mass Index (BMI)

BMI is calculated using height and weight.

```text
BMI = Weight / ((Height in centimeters/100)^2)
```

### ✅ Age Group

Users are categorized into:

* Young
* Adult
* Middle-age
* Senior

### ✅ Lifestyle Risk

Calculated using BMI and smoking status.

* Low
* Medium
* High

### ✅ City Tier

Cities are grouped into:

* Tier 1
* Tier 2
* Tier 3

These engineered features improve prediction performance.

---

## 🤖 Machine Learning Model

The project uses a **Random Forest Classifier** for prediction.

### ML Workflow

* Data Loading
* Feature Engineering
* Data Preprocessing
* One-Hot Encoding
* Train-Test Split
* Random Forest Model Training
* Model Evaluation
* Model Serialization using Pickle

The preprocessing pipeline and model are combined using **Scikit-learn Pipeline**, making deployment simple and reliable.

---

## 📈 Model Evaluation

The model is evaluated using:

* Accuracy Score
* Classification Report

---

## 🌐 FastAPI Backend

The backend is developed using **FastAPI**.

### API Endpoint

**POST** `/predict`

Example Request

```json
{
    "age": 28,
    "weight": 70,
    "height": 172,
    "city": "Mumbai",
    "income_lpa": 12,
    "smoker": false,
    "occupation": "Software Engineer"
}
```

Example Response

```json
{
    "insurance_premium_category": "Medium"
}
```

Interactive API documentation is automatically available at:

```text
http://127.0.0.1:8000/docs
```

---

## 🖥️ Streamlit Frontend

The Streamlit application provides a simple and interactive interface where users can:

* Enter personal details
* Submit data to the FastAPI backend
* View the predicted insurance premium category instantly

---

