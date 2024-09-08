# from openai import OpenAI
import os

import openai
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)


# Route to analyze sentiment using OpenAI GPT
@app.route("/sentiment", methods=["POST"])
def analyze_sentiment():
    try:
        # Extract the OpenAI API key and the text to analyze from the POST request

        text = request.json.get("text")

        # Set the OpenAI API key
        openai.api_key = os.getenv("OPENAI_API_KEY")

        # Make a request to the OpenAI GPT-3.5 API
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            # prompt
            {"role": "system", "content": "Analyze the text and showing random food or food how they want:"},
            {"role": "user", "content": text}
            ]
        )
                
        # Extract the response text
        response_text = response['choices'][0]['message']['content'].strip()
        
        print("Response from GPT-3.5:", response_text)

        # Extract the sentiment from the response
        sentiment_response = response["choices"][0]["message"]["content"].strip()
        # print(sentiment_response)

        # Assuming that sentiment_response contains the sentiment in neg, neu, or pos format
        

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
