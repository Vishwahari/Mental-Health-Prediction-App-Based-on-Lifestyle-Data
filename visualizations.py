import plotly.express as px

def create_scatter_plot(data):
    """
    Create a scatter plot of Sleep Hours vs Stress Level.
    Returns a Plotly figure.
    """
    fig = px.scatter(data, x='Sleep_Hours_Per_Night', y='Self_Reported_Stress_Level',
                     color='Stress_Category', title='Sleep Hours vs Stress Level',
                     labels={'Sleep_Hours_Per_Night': 'Sleep Hours per Night',
                             'Self_Reported_Stress_Level': 'Stress Level',
                             'Stress_Category': 'Stress Category (0=Low, 1=High)'})
    return fig

def create_box_plot(data):
    """
    Create a box plot of Screen Time by Stress Category.
    Returns a Plotly figure.
    """
    fig = px.box(data, x='Stress_Category', y='Daily_Screen_Time_Hours',
                 title='Screen Time Distribution by Stress Category',
                 labels={'Stress_Category': 'Stress Category (0=Low, 1=High)',
                         'Daily_Screen_Time_Hours': 'Daily Screen Time (Hours)'})
    return fig

def create_bar_plot(data):
    """
    Create a bar plot of Average Stress Level by Exercise Frequency.
    Returns a Plotly figure.
    """
    exercise_stress = data.groupby('Exercise_Frequency')['Self_Reported_Stress_Level'].mean().reset_index()
    fig = px.bar(exercise_stress, x='Exercise_Frequency', y='Self_Reported_Stress_Level',
                 title='Average Stress Level by Exercise Frequency',
                 labels={'Exercise_Frequency': 'Exercise Frequency',
                         'Self_Reported_Stress_Level': 'Average Stress Level'})
    return fig

def get_interesting_fact(data):
    """
    Calculate and return an interesting fact about the dataset.
    Returns a string with the fact.
    """
    high_stress = data[data['Stress_Category'] == 1]
    low_sleep_high_stress = high_stress[high_stress['Sleep_Hours_Per_Night'] < 6].shape[0] / high_stress.shape[0]
    return f"**Did you know?** {low_sleep_high_stress:.2%} of individuals with high stress levels sleep less than 6 hours per night, suggesting a strong link between poor sleep and elevated stress."