from matcher import find_matches

def gather_user_criteria():
    print("Let's find opportunities that match your interests and skills.")
    interests = input("What are you interested in? (e.g., environmental sustainability): ")
    skills = input("What skills do you have? (e.g., communication): ")
    return {'Description': interests, 'Skills Needed': skills}

def display_matches(matches):
    for category, matched_df in matches.items():
        if not matched_df.empty:
            print(f"\nCategory: {category}, Matches Found: {len(matched_df)}")
            print(matched_df[['Title', 'Company', 'Location', 'Skills', 'Description']], "\n")
        else:
            print(f"\nCategory: {category}, No matches found.")

def manage_chat_session():
    while True:
        criteria = gather_user_criteria()
        matches = find_matches(criteria)
        display_matches(matches)

        feedback = input("Are these recommendations helpful? (yes/no): ").lower()
        if feedback == 'no':
            print("Let's try adjusting your criteria.")
        else:
            print("Great! Let me know if you want to search for more opportunities.")
        
        cont = input("Do you want to continue? (yes/no): ").lower()
        if cont != 'yes':
            break

# Unit Tests 
# Test for the class
if __name__ == "__main__":
    manage_chat_session()
