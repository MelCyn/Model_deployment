# Model_deployment
ml_model deployment on Heroku
# ML Model Deployment - Toy Data Project

This project demonstrates how to train a simple machine learning model on toy data and deploy it using Flask on **Heroku**. It includes both a **web interface** and an **API endpoint**, making the model accessible through a browser and via HTTP requests.

## 📁 Contents

- `app.py` – Main Flask application
- `model.pkl` – Saved machine learning model
- `requirements.txt` – List of required Python libraries
- `Procfile` – Instructions for Heroku on how to run the app
- `templates/index.html` – HTML template for the web UI
- `deployment-report.pdf` – Step-by-step deployment documentation with screenshots
- `runtime.txt` – (Optional) Python version for Heroku

## 📊 Dataset Used

The project uses the **Iris dataset**, the toy dataset from **Week 4**, as allowed by the instructions.

## 🧠 Model Description

The model was trained using Random Forest Classifier on the toy dataset. It predicts the species of flowers based on three categories
- 0 for Iris setosa, 
- 1 for Iris versicolor, and 
- 2 for Iris virginica.

## 🌐 Deployment

The model is deployed to Heroku and includes:
- A web interface where users can input data and get predictions.
- A RESTful API endpoint that accepts POST requests and returns predictions.

**Live App Link:** https://iris-predictor-2025-5e5668f3f89b.herokuapp.com/
**GitHub Repo:** https://github.com/MelCyn/Model_deployment

## 📄 Report

The `deployment-report.pdf` document contains:
- Brief description of the deployment process
- Screenshots of each deployment step

