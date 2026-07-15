# 🏥 Insurance Premium Predictor

A Machine Learning web application that predicts the **Insurance Premium Category (Low, Medium, or High)** based on a user's demographic, lifestyle, and financial information.

The project demonstrates an **end-to-end Machine Learning workflow**, from feature engineering and model training to REST API development, an interactive web interface, containerization with Docker, and deployment on AWS EC2.

---

# 🚀 Features

* Predicts Insurance Premium Category (**Low**, **Medium**, or **High**)
* Feature engineering for improved model performance
* Random Forest Classifier
* Scikit-learn Pipeline with preprocessing
* FastAPI REST API
* Interactive Streamlit frontend
* Dockerized multi-service application
* AWS EC2 deployment
* Automatic API documentation using Swagger UI
* Health Check API endpoint
* Input validation using Pydantic
* Modular and maintainable project structure

---

# 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Random Forest Classifier
* FastAPI
* Streamlit
* Docker
* AWS EC2
* Pydantic
* Pickle

---

# 📂 Project Structure

```text
insurance-premium-predictor/
│
├── app.py                     # FastAPI backend
├── frontend.py                # Streamlit frontend
├── Dockerfile
├── start.sh                   # Starts FastAPI & Streamlit
├── requirements.txt
├── README.md
│
├── config/
│   └── city_tier.py
│
├── data/
│   └── Insurance_Data.csv
│
├── model/
│   ├── predict.py
│   ├── model.pkl
│   └── __init__.py
│
├── schema/
│   ├── user_input.py
│   ├── prediction_response.py
│   └── __init__.py
│
├── .dockerignore
└── .gitignore
```

---

# 📊 Dataset

The dataset contains customer information including:

* Age
* Height
* Weight
* Annual Income (LPA)
* City
* Occupation
* Smoking Status
* Insurance Premium Category (Target)

---

# ⚙️ Feature Engineering

To improve prediction performance, additional features are generated before model training.

## ✅ Body Mass Index (BMI)

```text
BMI = Weight / ((Height in centimeters / 100)^2)
```

---

## ✅ Age Group

Customers are categorized into:

* Young
* Adult
* Middle-age
* Senior

---

## ✅ Lifestyle Risk

Calculated using BMI and smoking status.

* Low
* Medium
* High

---

## ✅ City Tier

Cities are grouped into:

* Tier 1
* Tier 2
* Tier 3

These engineered features help the model learn customer risk patterns more effectively.

---

# 🤖 Machine Learning Model

The project uses a **Random Forest Classifier** for prediction.

## Machine Learning Workflow

* Data Loading
* Feature Engineering
* Data Preprocessing
* One-Hot Encoding
* Train-Test Split
* Random Forest Model Training
* Model Evaluation
* Model Serialization using Pickle

The preprocessing steps and classifier are combined into a **Scikit-learn Pipeline**, ensuring consistent preprocessing during both training and inference.

---

# 📈 Model Evaluation

The model is evaluated using:

* Accuracy Score
* Classification Report

---

# 🌐 FastAPI Backend

The backend is built using **FastAPI**.

## Prediction Endpoint

**POST** `/predict`

### Example Request

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

### Example Response

```json
{
  "insurance_premium_category": "Medium"
}
```

---

## Health Check

**GET** `/health`

Example Response

```json
{
  "status": "Healthy"
}
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

```text
http://localhost:8000/docs
```

---

# 🖥️ Streamlit Frontend

The Streamlit application provides a simple and user-friendly interface where users can:

* Enter personal information
* Submit data to the FastAPI backend
* Instantly view the predicted insurance premium category

---

# 🐳 Docker

The application is fully containerized using **Docker**.

A startup script (`start.sh`) launches both services simultaneously.

### Services

| Service            | Port |
| ------------------ | ---- |
| FastAPI Backend    | 8000 |
| Streamlit Frontend | 8501 |

## Build Docker Image

```bash
docker build -t insurance-premium-predictor .
```

## Run Docker Container

```bash
docker run -p 8000:8000 -p 8501:8501 insurance-premium-predictor
```

## Access the Application

| Service               | URL                          |
| --------------------- | ---------------------------- |
| Streamlit Frontend    | http://localhost:8501        |
| FastAPI Backend       | http://localhost:8000        |
| Swagger Documentation | http://localhost:8000/docs   |
| Health Check          | http://localhost:8000/health |

---

# ☁️ Deployment

The application has been successfully deployed on **AWS EC2** using Docker.

The EC2 instance runs both the FastAPI backend and Streamlit frontend concurrently inside a Docker container, providing a consistent and portable deployment environment.

The same Docker image can also be deployed on cloud platforms such as:

* Oracle Cloud Infrastructure (OCI)
* Microsoft Azure
* Google Cloud Platform (GCP)

---

# 🏗️ Application Architecture

```text
                    User
                      │
                      ▼
         Streamlit Frontend (8501)
                      │
               HTTP Request
                      │
                      ▼
          FastAPI Backend (8000)
                      │
              Feature Engineering
                      │
                      ▼
         Scikit-learn Pipeline
                      │
                      ▼
      Random Forest Classifier
                      │
                      ▼
 Insurance Premium Category
      (Low / Medium / High)
```

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/adityakumar373/insurance_premium_predictor.git
```

```bash
cd insurance_premium_predictor
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run FastAPI

```bash
uvicorn app:app --reload
```

## Run Streamlit

```bash
streamlit run frontend.py
```


# 👨‍💻 Author

**Aditya Kumar**
