import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Sample DataFrame (replace with your actual dataset)
data = pd.read_csv("final_dataset.csv")

# Features used for performance calculation
features = ['Likes', 'Views', 'Views Per Day', 'Engagement', 'Days Since Upload']

# Normalize the features using MinMaxScaler
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data[features])

# Convert the normalized data back to a DataFrame for easier processing
normalized_df = pd.DataFrame(normalized_data, columns=features)

# Define weights for the features
weights = {
    'Likes': 0.25,
    'Views': 0.25,
    'Views Per Day': 0.2,
    'Engagement': 0.15,
    'Days Since Upload': 0.15
}

# Function to calculate performance score dynamically
def calculate_performance_score(row):
    # Calculate the weighted sum of normalized features
    weighted_sum = (
        weights['Likes'] * row['Likes'] + 
        weights['Views'] * row['Views'] + 
        weights['Views Per Day'] * row['Views Per Day'] + 
        weights['Engagement'] * row['Engagement'] + 
        weights['Days Since Upload'] * row['Days Since Upload']
    )
    
    # Scale the score between 50 and 100
    max_score = 100
    min_score = 50
    
    # Normalize the weighted sum to get a score between min_score and max_score
    performance_score = min_score + (weighted_sum * (max_score - min_score))
    
    # Ensure the score is between 50% and 100%
    return round(min(max(performance_score, 50), 100), 2)

# Add the performance score to the dataset
data['Performance Score'] = normalized_df.apply(calculate_performance_score, axis=1)

# Now you have the performance scores in the 'Performance Score' column of the dataset.
print(data[['Title', 'Performance Score']])
