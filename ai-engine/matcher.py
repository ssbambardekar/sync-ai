import pandas as pd
from fuzzywuzzy import process, fuzz

# Define paths for the CSV files
csv_files = {
    'internships': 'data/internship-opportunities.csv',
    'volunteering': 'data/volunteer-opportunities.csv',
    'other': 'data/other-opportunities.csv',
} 

# Load opportunities using pandas
def load_opportunities(file_type):
    return pd.read_csv(csv_files[file_type])

# Fuzzy match function to find close matches based on criteria
def fuzzy_match_opportunities(df, criteria):
    matched = pd.DataFrame()
    for key, value in criteria.items():
        if key in df.columns:
            # Apply fuzzy matching for each criterion
            top_matches = df.apply(lambda x: fuzz.partial_ratio(x[key], value), axis=1)
            matched = pd.concat([matched, df[top_matches > 70]])  # Threshold of 70
    return matched.drop_duplicates()

# Main function to find matches based on multiple criteria
def find_matches(criteria):
    all_matches = {}
    for file_type in csv_files.keys():
        opportunities = load_opportunities(file_type)
        matches = fuzzy_match_opportunities(opportunities, criteria)
        all_matches[file_type] = matches
    return all_matches

# Unit Tests 
# Test for the class
if __name__ == "__main__":
    criteria = {
        'Title': 'building',
        'Description': 'high school',        
        'Skills':'communication'
    }
    
    # Test for function find_matches() 
    matches = find_matches(criteria)
    for category, matched_df in matches.items():
        print(f"Category: {category}, Matches Found: {len(matched_df)}")
        print(matched_df[['Title', 'Company', 'Location', 'Description']], "\n")  # Customize output columns as needed
