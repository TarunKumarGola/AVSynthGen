import os
from openai import OpenAI
from dotenv import load_dotenv

def CheckGPTConnection():
    print("checking")
    load_dotenv()
    client = OpenAI()
    api_key = os.getenv("OPENAI_API_KEY")

    if(not api_key):
       {"statusCode": 500, "body": "Unable to get API key"} 

    query = "Hello AI"

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "user",
        "content": query
        }
    ],
    temperature=1,
    max_tokens=511,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    json_data = response.choices[0].message.content
    return {"statusCode": 200, "body": "Hello, World!"} 
