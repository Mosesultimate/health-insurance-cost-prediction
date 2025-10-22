# 🏥 Health Insurance Cost Prediction

Predicting medical insurance charges using **data science and machine learning** — this project explores how lifestyle, demographic, and health factors drive insurance pricing, enabling smarter cost estimation and fairer coverage strategies.

---

## 📘 Project Overview

In modern healthcare systems, understanding what drives **insurance costs** is vital for both providers and policyholders.  
This project analyzes a structured dataset of patient records and builds a **predictive model** that estimates individual insurance charges based on characteristics such as **age**, **BMI**, **smoking habits**, **gender**, and **region**.

By combining exploratory data analysis, visualization, and machine learning, the project delivers insights into **how personal health indicators influence financial risk** — and demonstrates how data can inform smarter pricing models.

---

## 🎯 Project Objectives

This project was designed with the following key objectives:

1. **Data Understanding & Preparation**
   - Import and explore the dataset to understand its structure, size, and variables.  
   - Handle missing data, identify outliers, and correct inconsistencies.  
   - Encode categorical variables (`sex`, `smoker`, `region`) for model readiness.

2. **Exploratory Data Analysis (EDA)**
   - Visualize relationships between demographic features and insurance cost.  
   - Identify correlations using heatmaps and pairplots.  
   - Detect key cost-driving variables (e.g., `age`, `BMI`, `smoker`).

3. **Feature Engineering**
   - Create derived features (e.g., BMI categories, smoker-age interaction).  
   - Scale and normalize numerical attributes for balanced model training.

4. **Model Building & Evaluation**
   - Split data into training and test sets using `train_test_split()`.  
   - Train baseline models (Linear Regression, Decision Tree, Random Forest).  
   - Evaluate performance using **R²**, **MAE**, and **RMSE** metrics.

5. **Model Optimization**
   - Tune hyperparameters using GridSearchCV.  
   - Compare performance across models to select the best predictor.  
   - Analyze feature importance and interpret model outputs.

6. **Results & Insights**
   - Present data-driven insights into which factors most influence insurance costs.  
   - Provide recommendations for both insurers and policyholders.  
   - Visualize the final model’s predictions vs. actual values.

---

## 🧠 Technologies Used

| Category | Tools & Libraries |
|-----------|------------------|
| Programming | Python 3.13|
| Data Handling | NumPy, Pandas |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Development Environment | Jupyter Notebook |

---

## ⚙️ How to Run the Project

1. **Clone this repository**
   ```bash
   git clone https://github.com/Mosesultimate/health-insurance-cost-prediction.git
Navigate to the project folder

bash
Copy code
cd health-insurance-cost-prediction
Install required dependencies

bash
Copy code
pip install -r requirements.txt
(You can generate this file later using pip freeze > requirements.txt.)

Launch Jupyter Notebook

bash
Copy code
python -m notebook
Open and run

pgsql
Copy code
Health-insurance-cost-prediction.ipynb
📈 Key Insights
Smokers consistently exhibit higher charges across all age groups.

BMI and Age show strong positive correlation with medical costs.

Gender and Region have minor but noticeable influence.

The Random Forest Regressor achieved the best performance (lowest RMSE).

Predictive analytics can help insurers price plans more accurately and fairly.

🚀 Future Enhancements
Add advanced models like XGBoost, LightGBM, or Neural Networks.

Deploy the model via a Flask or Streamlit web app.

Integrate real-time data or external health metrics (e.g., wearable data).

Build a dashboard for interactive cost simulation.

🧩 Folder Structure
bash
Copy code
health-insurance-cost-prediction/
│
├── data/                          # Dataset (if applicable)
├── Health-insurance-cost-prediction.ipynb  # Main notebook
├── README.md                      # Project documentation
├── requirements.txt               # Dependencies (optional)
└── .gitignore                     # Ignored files for clean commits
📚 Data Dictionary
Column	Description
age	Age of the insured individual
sex	Gender (male/female)
bmi	Body Mass Index — a measure of body fat based on height and weight
children	Number of children/dependents covered by the insurance
smoker	Whether the individual is a smoker (yes/no)
region	Residential area in the U.S. (northeast, northwest, southeast, southwest)
charges	Medical insurance cost billed by the insurance company

👤 Author
Moses Matola
📍 Data Analyst & Python Developer
💻 GitHub | LinkedIn
📧 [mosesmatola548@gmail.com]

"Data doesn’t just reveal patterns — it tells the story of human behavior.
Understanding it is the first step toward smarter systems and fairer outcomes."

⭐ If you find this project useful, please give it a star — it fuels continued learning and innovation.

 
