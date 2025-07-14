import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(file_path="mental_health_lifestyle_survey_2024.csv"):
    """
    Load and preprocess the mental health dataset.
    Returns the preprocessed DataFrame and a dictionary of label encoders.
    """
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Clean data (remove rows with missing values)
    data = data.dropna()
    
    # Initialize label encoders
    encoders = {
        'gender': LabelEncoder(),
        'occupation': LabelEncoder(),
        'exercise': LabelEncoder(),
        'meditation': LabelEncoder(),
        'caffeine': LabelEncoder(),
        'bmi': LabelEncoder(),
        'chronic': LabelEncoder()
    }
    
    # Encode categorical variables
    data['Gender'] = encoders['gender'].fit_transform(data['Gender'])
    data['Occupation'] = encoders['occupation'].fit_transform(data['Occupation'])
    data['Exercise_Frequency'] = encoders['exercise'].fit_transform(data['Exercise_Frequency'])
    data['Meditation_Practice'] = encoders['meditation'].fit_transform(data['Meditation_Practice'])
    data['Caffeine_Intake_Daily'] = encoders['caffeine'].fit_transform(data['Caffeine_Intake_Daily'])
    data['BMI_Category'] = encoders['bmi'].fit_transform(data['BMI_Category'])
    data['Has_Chronic_Condition'] = encoders['chronic'].fit_transform(data['Has_Chronic_Condition'])
    
    # Convert stress level to binary (0-5: Low, 6-10: High)
    data['Stress_Category'] = data['Self_Reported_Stress_Level'].apply(lambda x: 1 if x >= 6 else 0)
    
    return data, encoders