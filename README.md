# Heart Disease Prediction using Machine Learning

## Project Overview

This project predicts whether a patient is likely to have heart disease using a Machine Learning model trained on the Heart Disease dataset. A Random Forest Classifier is used for prediction, and the application is deployed using Flask and Render.

---

## Author Information

| Field | Details |
|-------|---------|
| **Name** | Abhishek Thakur |
| **Registration Number** | 23MIM10078 |
| **Application Number** | IN26011189 |
| **Batch** | 1A |
| **University** | VIT Bhopal University |

---

## Features

- Heart disease prediction using Machine Learning
- Random Forest Classifier
- Flask Web Application
- User-friendly interface
- REST API endpoint
- Cloud deployment using Render

---

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Gunicorn
- Render

---

## Project Structure

```
assignment-10/
│
├── app.py
├── train_model.py
├── heart.csv
├── model.pkl
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── .gitignore
```

---

## Installation

```bash
git clone https://github.com/Abthakur-hub/assignment-10.git

cd assignment-10

pip install -r requirements.txt

python app.py
```

---

## Deployment

### GitHub Repository

https://github.com/Abthakur-hub/assignment-10

### Render Deployment


https://assignment-10-gi4q.onrender.com

---

## Model

- Algorithm: Random Forest Classifier
- Evaluation Metric: Accuracy Score

---

## Conclusion

This project successfully demonstrates the end-to-end deployment of a machine learning application using Flask and Render. A Random Forest Classifier was trained on the Heart Disease dataset to predict the likelihood of heart disease based on patient health parameters. The project involved data preprocessing, model training, evaluation, model serialization using Joblib, and integration with a Flask web application. The trained model was deployed on the Render cloud platform, enabling real-time predictions through a user-friendly web interface. During deployment, challenges related to dependency management and server configuration were resolved, providing practical exposure to MLOps concepts. Overall, this project highlights the importance of combining machine learning with web technologies and cloud deployment to build scalable, reliable, and production-ready AI applications that can be accessed from anywhere.

---