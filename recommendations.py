def generate_recommendations(stress_prob, inputs):
    """
    Generate prioritized recommendations based on user inputs and predicted stress probability.
    Returns up to 3 recommendations, sorted by impact.
    """
    recommendations = []
    
    # Assign scores to recommendations for prioritization
    recs_with_scores = []
    
    if inputs['Sleep_Hours_Per_Night'] < 7:
        recs_with_scores.append((2.0, "Aim for 7-8 hours of sleep per night to improve mental wellness."))
    if inputs['Daily_Screen_Time_Hours'] > 7:
        recs_with_scores.append((1.5, "Reduce screen time to under 7 hours daily to lower stress."))
    if inputs['Exercise_Frequency'] in [0, 1]:  # None=0, 1-2x/week=1
        recs_with_scores.append((1.8, "Increase exercise to 3-5 times per week to reduce stress."))
    if inputs['Meditation_Practice'] == 0:  # No=0
        recs_with_scores.append((1.2, "Try meditation or mindfulness practices to improve mental health."))
    if inputs['Caffeine_Intake_Daily'] == 2:  # 4+ cups=2
        recs_with_scores.append((1.0, "Limit caffeine to 1-2 cups daily to help manage stress."))
    
    # Sort by score and take top 3
    recs_with_scores.sort(reverse=True, key=lambda x: x[0])
    recommendations = [rec for _, rec in recs_with_scores[:3]]
    
    if not recommendations:
        recommendations.append("Your lifestyle habits are well-balanced! Keep it up.")
    
    return recommendations