# 🧠 Mental Health Prediction App Based on Lifestyle Data

This is an interactive Streamlit web application that predicts a user's stress level (High or Low) based on their lifestyle habits, such as sleep, screen time, exercise, and more. The app uses a Random Forest Classifier with SMOTE for handling data imbalance and provides personalized mental wellness recommendations, interactive Plotly visualizations, and a feature importance plot to explain predictions.

---

## 🚀 Features

* ✅ **Stress Level Prediction**: Predicts stress level (High or Low) using a Random Forest model with an optimized classification threshold.
* ✅ **Interactive User Inputs**: Accepts lifestyle inputs via a sidebar for real-time predictions.
* ✅ **Personalized Recommendations**: Offers up to three tailored suggestions to improve mental wellness.
* ✅ **Interactive Visualizations**: Includes Plotly scatter, box, and bar plots to visualize lifestyle-stress relationships.
* ✅ **Feature Importance**: Displays a plot showing which factors most influence stress predictions.
* ✅ **Debugging Support**: Shows user inputs and model performance metrics (accuracy, classification report) in the UI and console.
* ✅ **Built with Streamlit, scikit-learn, and Plotly** for a seamless user experience.

---

## 🧠 Technologies Used

| Tool / Library   | Purpose                           |
| ---------------- | --------------------------------- |
| Python           | Core programming language         |
| Streamlit        | Web app framework                 |
| scikit-learn     | Machine learning model training   |
| pandas, numpy    | Data handling and preprocessing   |
| plotly           | Interactive visualizations        |
| imbalanced-learn | SMOTE for handling data imbalance |
| Git + GitHub     | Version control and collaboration |

---

## 📁 Project Structure

```
Mental-Health-Prediction-App-Based-on-Lifestyle-Data/
├── app.py
├── data_preprocessing.py
├── model_training.py
├── recommendations.py
├── visualizations.py
├── mental_health_lifestyle_survey_2024.csv
├── requirements.txt
├── README.md
```

* `app.py`: Main Streamlit app, integrates all modules, handles user inputs, and displays predictions, recommendations, and visualizations.
* `data_preprocessing.py`: Loads and preprocesses the dataset, encoding categorical variables.
* `model_training.py`: Trains a Random Forest Classifier with SMOTE and hyperparameter tuning, returns model, scaler, accuracy, feature importances, and optimal threshold.
* `recommendations.py`: Generates prioritized lifestyle recommendations based on user inputs.
* `visualizations.py`: Creates Plotly visualizations (scatter, box, bar plots) and an interesting fact about stress.
* `mental_health_lifestyle_survey_2024.csv`: Dataset file containing lifestyle and stress data (not included in repository; must be provided).
* `requirements.txt`: Lists Python dependencies for easy installation.

---

## 📥 How to Run the App Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Vishwahari/Mental-Health-Prediction-App-Based-on-Lifestyle-Data.git
cd Mental-Health-Prediction-App-Based-on-Lifestyle-Data
```

### 2️⃣ Install Dependencies

Create a `requirements.txt` file with the following content:

```txt
streamlit
pandas
numpy
scikit-learn
plotly
imbalanced-learn
```

Then install:

```bash
pip install -r requirements.txt
```

### 3️⃣ Ensure Dataset Availability

* Place the `mental_health_lifestyle_survey_2024.csv` file in the project directory.
* Verify it contains the required columns:

```text
Age, Gender, Occupation, Daily_Screen_Time_Hours, Sleep_Hours_Per_Night,
Exercise_Frequency, Social_Interactions_Per_Week, Meditation_Practice,
Caffeine_Intake_Daily, BMI_Category, Has_Chronic_Condition, Self_Reported_Stress_Level
```

### 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

---

## 🧪 Inputs Considered

* Age: 18–80 years
* Gender: Male, Female, Other
* Occupation: Various categories (e.g., Student, Professional)
* Daily Screen Time: 0–24 hours
* Sleep Hours: 3–12 hours per night
* Exercise Frequency: None, 1-2x/week, 3-5x/week, Daily
* Social Interactions: 0–20 per week
* Meditation Practice: Yes, No
* Caffeine Intake: None, 1-2 cups, 3-4 cups, 4+ cups
* BMI Category: Underweight, Normal, Overweight, Obese
* Chronic Conditions: Yes, No

---

## 📊 Sample Output

* 🌟 Stress Level: High / Low
* 📈 Probability of High Stress: e.g., 78.9%
* 🌟 Classification Threshold: e.g., 0.45
* 💡 Recommendations: e.g., "Aim for 7-8 hours of sleep per night to improve mental wellness."
* 📊 Visualizations: Scatter (Sleep vs. Stress), Box (Screen Time vs. Stress), Bar (Exercise vs. Stress), Feature Importance
* ℹ️ Interesting Fact: e.g., "XX% of individuals with high stress sleep less than 6 hours per night."

---

## ✅ Example Test Cases

### High Stress Inputs:

* Sleep: 4 hours
* Screen Time: 10 hours
* Exercise: None
* Meditation: No
* Caffeine: 4+ cups
* Chronic Condition: Yes
* Expected: High stress, probability > 50%

### Low Stress Inputs:

* Sleep: 8 hours
* Screen Time: 4 hours
* Exercise: 3-5x/week
* Meditation: Yes
* Caffeine: None
* Chronic Condition: No
* Expected: Low stress, probability < 40%

---

## 🌐 Live Deployment

> 📦 Coming soon via **Streamlit Cloud**! Check the repository for updates.

---

## 👨‍💼 Author

**Vishwahari R.**
Field: Artificial Intelligence & Machine Learning
Email: [vishwahari4164@gmail.com](mailto:vishwahari4164@gmail.com)
GitHub: [github.com/Vishwahari](https://github.com/Vishwahari)

---

## 💖 Support

If you like this project, please ⭐ star the repository and share it with others!

---

## 📤 Upload to GitHub

```bash
git add README.md
git commit -m "📝 Updated README.md"
git push origin main
```

---

## ⚠️ Troubleshooting

### ModuleNotFoundError:

* Ensure all dependencies are installed:

```bash
pip install -r requirements.txt
```

* Verify Python version:

```bash
python --version  # e.g., Python 3.12
```

### Dataset Not Found:

* Confirm `mental_health_lifestyle_survey_2024.csv` is in the project directory.

### Predictions Always Low:

* Check console for class distribution and classification report.
* Test with high-stress inputs (see Sample Output).
* Verify dataset has varied `Self_Reported_Stress_Level` values.

### Visualizations Not Rendering:

* Check browser console for JavaScript errors.
* Ensure Plotly is installed:

```bash
pip show plotly
```

### Low Model Accuracy:

* Review classification report in the console.
* Consider trying alternative models (e.g., SVM) in `model_training.py`.
