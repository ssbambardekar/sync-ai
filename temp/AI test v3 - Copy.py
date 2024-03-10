from transformers import pipeline, set_seed, Conversation
import csv

# Initialize the conversational model
conversational_pipeline = pipeline("conversational", model="microsoft/DialoGPT-medium")
set_seed(42)

# Load opportunities data (Placeholder function, adapt as needed)
def load_opportunities(csv_path):
    opportunities = []
    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            opportunities.append(row)
    return opportunities

# Sample opportunities data loading
internships = load_opportunities('internships.csv')  # Ensure this CSV exists with appropriate structure

# User profile update logic
def update_user_profile(profile, message):
    response = "I'm here to help. Could you tell me more about what you're looking for?"
    if 'interest' in message.lower():
        interest = message.split('interest')[-1].strip()
        profile['Interests'].append(interest)
        response = f"I've noted your interest in {interest}."
    # Extend with more sophisticated logic or NLU
    return response

# Recommendation logic (Placeholder function, adapt as needed)
def get_recommendations(profile, internships):
    for internship in internships:
        if any(interest in internship['Description'] for interest in profile['Interests']):
            return f"Based on your interest in {profile['Interests'][-1]}, I recommend checking out the internship at {internship['Company']}."
    return "I couldn't find a matching opportunity right now. Tell me more about your interests?"

# Main chat function
def chat_with_user():
    print("Hello! I'm here to help you find internships, volunteering, and other opportunities. How can I assist you today?")
    user_profile = {'Interests': [], 'Skills': []}  # Initialize a new user profile
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Assistant: It was great helping you. Have a wonderful day!")
            break
        
        # Handle general conversation
        if 'recommend' not in user_input.lower():
            conversation = Conversation(user_input)
            response = conversational_pipeline(conversation)
            print(f"Assistant: {response.generated_responses[0]}")
        else:
            # Update user profile or provide recommendations
            profile_update_response = update_user_profile(user_profile, user_input)
            print(f"Assistant: {profile_update_response}")
            
            # After updating the profile, directly ask for more info or provide recommendations
            if 'interest' in user_input.lower():
                continue  # Prompt the user again to gather more info
            else:
                recommendation = get_recommendations(user_profile, internships)
                print(f"Assistant: {recommendation}")

def chat_with_user():
    print("Hello! I'm here to help you find opportunities. Tell me about what you're looking for, or ask for recommendations based on your interests.")
    user_profile = {'Interests': [], 'Skills': []}  # Initialize a new user profile
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Assistant: It was great helping you. Have a wonderful day!")
            break
        
        # Directly handle recommendation requests
        if 'recommend' in user_input.lower():
            # Update user profile or provide recommendations based on previous updates
            if user_profile['Interests']:  # Assuming there are already some interests noted
                recommendation = get_recommendations(user_profile, internships)  # Use your actual logic for recommendations
                print(f"Assistant: {recommendation}")
            else:
                print("Assistant: Could you tell me more about your interests so I can provide personalized recommendations?")
        else:
            # Assume this is part of updating the user profile
            profile_update_response = update_user_profile(user_profile, user_input)
            print(f"Assistant: {profile_update_response}")
            # Optionally, follow up with a prompt for more specific information or next steps

if __name__ == "__main__":
    chat_with_user()
