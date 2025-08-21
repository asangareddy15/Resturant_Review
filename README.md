The Restaurant Review Sentiment Analyzer is a Python-based command-line interface (CLI) tool designed to analyze the sentiment of restaurant reviews using the advanced capabilities of the Gemini AI model from Google. Developed as a personal project using PyCharm on a Windows PC, this tool leverages the google-generativeai library to provide detailed insights into customer feedback, making it a valuable resource for restaurant owners, managers, or anyone interested in understanding dining experiences.
Features

Manual Review Input: Users can enter a restaurant review directly into the CLI, receiving an instant sentiment analysis.
File-Based Review Analysis: Supports loading multiple reviews from a text file (e.g., reviews.txt), separated by ---, for batch processing.
Sentiment Classification: Classifies the overall sentiment as Positive, Negative, or Neutral, with a confidence score (0-100%).
Detailed Breakdown: Provides a comprehensive analysis including:

Key positive aspects (e.g., food quality, service, ambiance).
Key negative aspects (e.g., wait time, pricing).
Practical suggestions for improvement.


Local Execution: Runs entirely on your local machine, with the Gemini API key securely stored in a .env file, ensuring privacy and security.
Open-Source: Hosted on GitHub as a public repository, encouraging community contributions and feedback.

Technical Details

Language: Python 3.x
Dependencies:

python-dotenv for environment variable management.
google-generativeai for AI-powered sentiment analysis.
