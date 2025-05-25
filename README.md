# Real Estate Price Prediction

This is a simple web application built with **Streamlit** that predicts real estate prices based on user inputs such as number of bedrooms, bathrooms, and house size. The model uses a pre-trained machine learning model and scaler saved with `joblib`.

---

## Features

- Interactive UI to input house features
- Real-time prediction of house price
- Preprocessing with scaler for input normalization
- Easy deployment with Streamlit

---

## Dataset

The dataset used for training is downloaded dynamically using the `kagglehub` Python package from the [USA Real Estate Dataset](https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset).

---

## Project Structure
├── app.py # Main Streamlit app code
├── Scaler.pkl # Pre-trained scaler object
├── model.pkl # Trained machine learning model
├── requirements.txt # Python dependencies
└── README.md # This file


---

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Steps

1. Clone this repository:

```bash
git clone https://github.com/yourusername/RealEstate_Price_Predictor.git
cd RealEstate_Price_Predictor
```

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


pip install -r requirements.txt
streamlit
joblib
numpy
kagglehub


streamlit run app.py

## Live Demo

Try the live app here:  
[Real Estate Price Predictor](https://realestatepricepredictor-kburwgjiwt7obusquraxvg.streamlit.app/)

                              
