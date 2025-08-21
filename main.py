from dotenv import load_dotenv
import os
import google.generativeai as genai



load_dotenv()
gemini_api_key = os.getenv("API_KEY")
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

def analyze_review_sentiment(review_text):
    """Uses Gemini to analyze the sentiment of a restaurant review with detailed breakdown."""
    if not review_text:
        return "Error: Review text cannot be empty."
    prompt = f"""
    Analyze the sentiment of the following restaurant review.
    Classify the overall sentiment as Positive, Negative, or Neutral.
    Provide a detailed breakdown including:
    - Key positive aspects (e.g., food, service, atmosphere)
    - Key negative aspects (e.g., food, service, atmosphere)
    - Confidence score (0-100%) for the classification

    Review: {review_text}
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}. Please check your API key or try again."


if __name__ == "__main__":
    print("Welcome to Restaurant Review Sentiment Analyzer!")
    while True:
        choice = input("Enter '1' for manual review input, '2' to load from file (or 'quit' to exit): ")
        if choice.lower() == 'quit':
            break
        reviews = []
        if choice == '1':
            review_text = input("Enter the restaurant review: ")
            reviews.append(review_text)
        elif choice == '2':
            try:
                file_path = input("Enter the file path (e.g., reviews.txt): ")
                with open(file_path, 'r') as file:
                    content = file.read().split('---')  # Assume reviews separated by '---'
                    for block in content:
                        if block.strip():
                            reviews.append(block.strip())
            except FileNotFoundError:
                print("Error: File not found. Please check the path.")
                continue
        else:
            print("Invalid choice. Please enter '1', '2', or 'quit'.")
            continue

        for review in reviews:
            if review:
                print("\nReview Preview:\n")
                print(review[:500])  # Show preview
                result = analyze_review_sentiment(review)
                print("\nSentiment Analysis Result:\n")
                print(result)
                print("\n---\n")
