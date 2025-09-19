

# Student Stress Prediction

A Machine Learning + Streamlit web app that predicts the **stress levels of students** based on survey responses.  
This project uses a trained ML model to analyze patterns in student behavior, lifestyle, and academics to classify stress levels.  

---

## Project Structure

student_stress_prediction/
├── main.py                        # Streamlit app entry point
├── model_utils.py                  # Helper functions for ML model
├── training.ipynb                  # Jupyter Notebook for training the model
├── model.pkl                       # Saved trained ML model
├── scaler.pkl                      # Preprocessing scaler
├── StressLevelDataset.csv          # Dataset used for training
├── top_10_mental_health_hospitals_india.csv  # Reference dataset
├── questions.txt                   # Survey questions
├── requirements.txt                # Python dependencies
├── pages/                          # Additional Streamlit pages
└── .streamlit/                     # Streamlit configuration


---

## Installation

1. **Clone this repo**
   git clone [https://github.com/karthik132007/student_stress_prediction.git](https://github.com/karthik132007/student_stress_prediction)
   cd student_stress_prediction


2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Linux/Mac
   venv\Scripts\activate         # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the Streamlit app:

```bash
streamlit run main.py
```

Then open the link in your browser (usually `http://localhost:8501/`).

---

## Dataset

* **StressLevelDataset.csv** → Contains survey responses about student lifestyle, academics, and stress indicators.
* **questions.txt** → Survey questions used to collect responses.
* **top\_10\_mental\_health\_hospitals\_india.csv** → Extra dataset listing hospitals/resources in India.

---

## Model Training

* The training pipeline is inside `traning.ipynb`.
* The model is trained using classical ML techniques (check the notebook for details).
* Saved model: `model.pkl`
* Preprocessing scaler: `scaler.pkl`

---

## Features

* Predicts **stress levels** based on student survey inputs.
* Interactive **Streamlit UI**.
* Includes dataset + notebook for transparency.
* Provides **mental health resources** (top hospitals in India).

---


