# Libraries Used

from llamaapi import LlamaAPI
from openai import OpenAI

user_review = input("Write your review: ")
client = OpenAI(
    api_key="Your-Api-Key", # Write ur API Key here
    base_url="https://api.llama-api.com"
)

response = client.chat.completions.create(
    model="llama-13b-chat",
    messages=[
        {"role": "system", "content": "translate to english then Mention positive as the first word if the next sentiment is positive otherwise write negative the first word if the sentiment is negative "},
        {"role": "user", "content": user_review }   
    ]
)

review = response.choices[0].message.content

# Determine sentiment based on the review
if "positive" in review.lower():
    sentiment = "Positive"
else:
    sentiment = "Negative"

# Print formatted output
print(f"Review: {user_review}")
print(f"Sentiment: {sentiment}")
