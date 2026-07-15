# SmartLender - Loan Eligibility Prediction System Using Machine Learning

## 📌 Project Summary

SmartLender is a Machine Learning-based loan eligibility prediction system developed to automate the preliminary loan screening process. Instead of manually reviewing every loan application, the system analyzes applicant information such as gender, marital status, education, self-employment status, applicant income, co-applicant income, loan amount, loan amount term, credit history, and property area using trained machine learning models, and predicts whether the applicant is eligible for a loan.

Rather than replacing loan officers, SmartLender acts as an intelligent decision-support tool that enables faster, more consistent, and transparent lending decisions.

---

## ✨ Key Features

- Instant loan eligibility prediction
- Machine Learning-based loan approval system
- User-friendly web interface
- Data preprocessing and feature engineering
- Comparison across multiple machine learning algorithms
- Random Forest based prediction model
- Responsive HTML & CSS interface
- Fast and accurate loan prediction

---

## 🏗️ Technical Architecture

The project follows a modular three-layer architecture:

### 1. Machine Learning Layer
Handles data preprocessing, missing value handling, feature encoding, model training, model evaluation, and model selection.

**Algorithms Used:**
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- XGBoost

Random Forest is selected as the final prediction model based on its higher accuracy.

### 2. Backend Layer
Implemented using **Flask**. Handles:
- HTTP requests
- User input processing
- Machine learning model loading
- Loan prediction
- Result generation

### 3. Presentation Layer
Built using:
- HTML5
- CSS3
- Jinja2 templates

Provides a clean and responsive web interface for users to enter loan details and receive prediction results.

---

## 👥 Project Submitted By

**pavani Vallepu**
📧 vallepupavani2005@gmail.com

---

## 🚀 How to Run the Application

### Prerequisites
- Python 3.10 or higher installed
- pip package manager
- Visual Studio Code (recommended)

### Step 1: Navigate to the Project Folder
The complete source code of the application is located inside the `SmartLender_Project_codes` directory.

```bash
cd SmartLender_Project_codes
```

### Step 2: Install Project Dependencies
Install all required Python libraries.

```bash
pip install -r requirements.txt
```

### Step 3: Generate the Machine Learning Model
Execute the machine learning pipeline.

```bash
python model.py
```

This process loads the dataset, preprocesses the data, trains multiple machine learning models, compares their performance, selects the Random Forest model, and saves the trained model as `loan_model.pkl`.

### Step 4: Launch the Flask Web Application

```bash
python app.py
```

### Step 5: Open the Application
Visit the following URL in your web browser:

```
http://127.0.0.1:5000
```

---

## 🧪 Testing (Optional)

The application has been tested using multiple loan applicant records to verify prediction accuracy and functionality.

**Testing includes:**
- Functional testing
- User interface testing
- Prediction testing
- Input validation

---

## 📂 Project Structure

```
├── 1.Brainstorming and Ideation/ ... 8.Project Demonstration/   # Project lifecycle documentation
├── SmartLender_Project_codes/                                    # Complete project source code
│   ├── app.py               # Flask web application
│   ├── model.py              # Data preprocessing, model training, evaluation, and saving
│   ├── loan.csv               # Loan prediction dataset
│   ├── loan_model.pkl          # Trained Random Forest model
│   ├── requirements.txt        # Required Python libraries
│   ├── templates/               # HTML pages (index.html, result.html)
│   └── static/                   # CSS files (style.css)
```

---

## 📊 Machine Learning Performance

| Algorithm             | Accuracy |
|------------------------|----------|
| Decision Tree          | 70.73%   |
| Random Forest          | 76.42%   |
| K-Nearest Neighbors    | 57.72%   |
| XGBoost                | 76.42%   |

**Final Model:** Random Forest Classifier

---

## 🔮 Future Scope

- Improve prediction accuracy using Deep Learning
- Deploy the application on cloud platforms
- Add user authentication
- Develop mobile applications
- Integrate with banking APIs
- Improve user interface using modern frontend frameworks

---

## 📄 License

This project is developed for educational and academic purposes.
