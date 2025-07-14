import streamlit as st
import pandas as pd
import plotly.express as px
from data_preprocessing import load_and_preprocess_data
from model_training import train_model
from recommendations import generate_recommendations
from visualizations import create_scatter_plot, create_box_plot, create_bar_plot, get_interesting_fact

# Set page configuration
st.set_page_config(page_title="Mental Health Prediction App", layout="wide")

@st.cache_data
def load_data():
    return load_and_preprocess_data()

@st.cache_resource
def get_model(data):
    return train_model(data)

def main():
    st.title("🧠 Mental Health Prediction App")
    st.markdown("Enter your daily habits to predict your stress level and receive personalized recommendations.")
    
    # Load data and model
    try:
        data, encoders = load_data()
    except FileNotFoundError:
        st.error("Dataset file 'mental_health_lifestyle_survey_2024.csv' not found. Please ensure it is in the project directory.")
        return
    
    model, scaler, accuracy, feature_columns, feature_importances, threshold = get_model(data)
    
    # Sidebar for user inputs
    st.sidebar.header("Input Your Daily Habits")
    age = st.sidebar.slider("Age", 18, 80, 30)
    gender = st.sidebar.selectbox("Gender", encoders['gender'].classes_)
    occupation = st.sidebar.selectbox("Occupation", encoders['occupation'].classes_)
    screen_time = st.sidebar.slider("Daily Screen Time (hours)", 0.0, 24.0, 5.0)
    sleep_hours = st.sidebar.slider("Sleep Hours per Night", 3.0, 12.0, 7.0)
    exercise = st.sidebar.selectbox("Exercise Frequency", encoders['exercise'].classes_)
    social_interactions = st.sidebar.slider("Social Interactions per Week", 0, 20, 5)
    meditation = st.sidebar.selectbox("Meditation Practice", encoders['meditation'].classes_)
    caffeine = st.sidebar.selectbox("Daily Caffeine Intake", encoders['caffeine'].classes_)
    bmi = st.sidebar.selectbox("BMI Category", encoders['bmi'].classes_)
    chronic_condition = st.sidebar.selectbox("Has Chronic Condition", encoders['chronic'].classes_)
    
    # Input validation
    if screen_time > 24:
        st.error("Daily Screen Time cannot exceed 24 hours.")
        return
    if sleep_hours > 12:
        st.error("Sleep Hours per Night cannot exceed 12 hours.")
        return
    
    # Encode user inputs
    user_input = {
        'Age': age,
        'Gender': encoders['gender'].transform([gender])[0],
        'Occupation': encoders['occupation'].transform([occupation])[0],
        'Daily_Screen_Time_Hours': screen_time,
        'Sleep_Hours_Per_Night': sleep_hours,
        'Exercise_Frequency': encoders['exercise'].transform([exercise])[0],
        'Social_Interactions_Per_Week': social_interactions,
        'Meditation_Practice': encoders['meditation'].transform([meditation])[0],
        'Caffeine_Intake_Daily': encoders['caffeine'].transform([caffeine])[0],
        'BMI_Category': encoders['bmi'].transform([bmi])[0],
        'Has_Chronic_Condition': encoders['chronic'].transform([chronic_condition])[0]
    }
    
    # Debug: Display user inputs
    # st.subheader("Debug: Your Inputs")
    # st.write(user_input)
    
    # Convert input to DataFrame
    user_df = pd.DataFrame([user_input], columns=feature_columns)
    user_scaled = scaler.transform(user_df)
    
    # Predict stress level with optimal threshold
    stress_prob = model.predict_proba(user_scaled)[0][1]
    stress_level = "High" if stress_prob >= threshold else "Low"
    
    # Display prediction
    st.subheader("Stress Level Prediction")
    st.write(f"Predicted Stress Level: **{stress_level}**")
    st.write(f"Probability of High Stress: **{stress_prob:.2%}**")
    st.write(f"Classification Threshold: **{threshold:.2f}**")
    if abs(stress_prob - threshold) <= 0.1:
        st.warning("This prediction is close to the decision boundary, so results may be less certain.")
    st.write(f"Model Accuracy: **{accuracy:.2%}**")
    
    # Display recommendations
    st.subheader("Personalized Recommendations")
    recommendations = generate_recommendations(stress_prob, user_input)
    for rec in recommendations:
        st.write(f"- {rec}")
    
    # Display visualizations
    st.subheader("Lifestyle vs Stress Level Visualizations")
    st.plotly_chart(create_scatter_plot(data), use_container_width=True)
    st.plotly_chart(create_box_plot(data), use_container_width=True)
    st.plotly_chart(create_bar_plot(data), use_container_width=True)
    
    # Feature importance plot
    st.subheader("Feature Importance")
    fig_importance = px.bar(x=feature_importances.values, y=feature_importances.index,
                           orientation='h', title='Feature Importance in Stress Prediction',
                           labels={'x': 'Importance', 'y': 'Feature'})
    st.plotly_chart(fig_importance, use_container_width=True)
    
    # Display interesting fact
    st.subheader("Interesting Fact")
    st.write(get_interesting_fact(data))

if __name__ == "__main__":
    main()