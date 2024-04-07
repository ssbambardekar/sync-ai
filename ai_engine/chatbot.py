from matcher import find_matches

# Load spaCy's English language model
nlp = spacy.load("en_core_web_lg")

# Initialize the conversational model
try:
    conversational_pipeline = pipeline("conversational", model="microsoft/DialoGPT-medium")
    set_seed(42)
except Exception as e:
    print(f"Failed to initialize conversational model: {e}")
    exit(1)

def extract_interests_skills(message):
    """
    Advanced extraction of interests and skills using spaCy's dependency parsing.
    """
    doc = nlp(message)
    interests = []
    skills = []

    # Iterate through sentences to better contextualize extraction
    for sent in doc.sents:
        root = sent.root
        # Depending on your observation, adjust the conditions to better suit the common expressions
        for token in sent:
            if token.dep_ in ['dobj', 'pobj', 'attr'] and token.head.lemma_ in ['interest', 'skill', 'good', 'experience', 'knowledge']:
                if token.pos_ in ['NOUN', 'PROPN']:
                    interests.append(token.text)
                elif token.pos_ == 'VERB':
                    skills.append(token.text)

    return list(set(interests)), list(set(skills))

def update_user_profile(profile, message):
    interests, skills = extract_interests_skills(message)
    profile['Interests'].extend(interests)
    profile['Skills'].extend(skills)
    if interests:
        print(f"I've added '{', '.join(interests)}' to your interests.")
    if skills:
        print(f"I've added '{', '.join(skills)}' to your skills.")

    # Other functions (get_recommendations, chat_with_user) remain unchanged

def get_recommendations(profile):
    """
    Generate recommendations based on the updated user profile.
    """
    if not profile['Interests'] and not profile['Skills']:
        return "Please tell me about your interests or skills so I can recommend opportunities."

    criteria = {
        'Description': ", ".join(profile['Interests']),
        'Skills Needed': ", ".join(profile['Skills'])
    }
    
    matches = find_matches(criteria)
    recommendations = ""

    for category, matched_df in matches.items():
        if not matched_df.empty:
            recommendations += f"\nCategory: {category}, Matches Found: {len(matched_df)}\n"
            recommendations += matched_df[['Title', 'Company', 'Location', 'Description']].to_string(index=False, header=True) + "\n"
        else:
            recommendations += f"\nCategory: {category}, No matches found.\n"
    
    return recommendations if recommendations else "I couldn't find a matching opportunity right now. Could you tell me more?"

def chat_with_user():
    """
    Main chat function for interacting with the user, integrating dynamic responses
    from the conversational model with the ability to execute basic commands.
    """
    print("Hello! I'm here to help you find opportunities. Tell me about what you're looking for, or ask for recommendations.")
    user_profile = {'Interests': [], 'Skills': []}
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Assistant: It was great helping you. Have a wonderful day!")
            break
        
        # Check for specific commands in user input
        if 'recommend' in user_input.lower():
            # User is explicitly asking for recommendations
            recommendation = get_recommendations(user_profile)
            print(f"Assistant: {recommendation}")
        else:
            # For other inputs, first try to update the user profile
            interests_before_update = len(user_profile['Interests'])
            skills_before_update = len(user_profile['Skills'])
            update_user_profile(user_profile, user_input)
            # Check if the profile was updated to decide if we should ask a general question
            if len(user_profile['Interests']) > interests_before_update or len(user_profile['Skills']) > skills_before_update:
                print("Assistant: Got it. Do you have more to tell me about your interests or skills?")
            else:
                # Use the conversational model for a dynamic response
                conversation = Conversation(user_input)
                response = conversational_pipeline(conversation)
                print(f"Assistant: {response.generated_responses[0]}")

if __name__ == "__main__":
    chat_with_user()
