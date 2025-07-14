from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE
import pandas as pd
import numpy as np

def train_model(data):
    """
    Train a Random Forest Classifier with SMOTE and hyperparameter tuning.
    Returns the trained model, scaler, accuracy, feature columns, feature importances, and optimal threshold.
    """
    # Define features and target
    X = data[['Age', 'Gender', 'Occupation', 'Daily_Screen_Time_Hours', 
              'Sleep_Hours_Per_Night', 'Exercise_Frequency', 
              'Social_Interactions_Per_Week', 'Meditation_Practice', 
              'Caffeine_Intake_Daily', 'BMI_Category', 'Has_Chronic_Condition']]
    y = data['Stress_Category']
    
    # Check for data imbalance
    class_distribution = y.value_counts(normalize=True)
    print("Stress Category Distribution (before SMOTE):")
    print(class_distribution)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Apply SMOTE to balance classes
    smote = SMOTE(random_state=42)
    X_train_balanced, y_train_balanced = smote.fit_resample(X_train_scaled, y_train)
    
    # Check distribution after SMOTE
    print("Stress Category Distribution (after SMOTE):")
    print(pd.Series(y_train_balanced).value_counts(normalize=True))
    
    # Define hyperparameter grid for Random Forest
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [10, 20, None],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2]
    }
    
    # Train Random Forest with GridSearchCV
    model = RandomForestClassifier(random_state=42, class_weight='balanced')
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='f1_macro', n_jobs=-1)
    grid_search.fit(X_train_balanced, y_train_balanced)
    
    # Best model
    best_model = grid_search.best_estimator_
    print("Best Hyperparameters:", grid_search.best_params_)
    
    # Evaluate model
    y_pred = best_model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=['Low Stress', 'High Stress'])
    
    # Find optimal threshold
    y_prob = best_model.predict_proba(X_test_scaled)[:, 1]
    thresholds = np.arange(0.3, 0.7, 0.05)
    best_threshold = 0.5
    best_f1 = 0
    for threshold in thresholds:
        y_pred_threshold = (y_prob >= threshold).astype(int)
        f1 = classification_report(y_test, y_pred_threshold, output_dict=True)['macro avg']['f1-score']
        if f1 > best_f1:
            best_f1 = f1
            best_threshold = threshold
    
    print("Model Accuracy:", accuracy)
    print("Classification Report:\n", report)
    print("Optimal Threshold:", best_threshold)
    
    # Get feature importances
    feature_importances = pd.Series(best_model.feature_importances_, index=X.columns)
    
    return best_model, scaler, accuracy, X.columns, feature_importances, best_threshold