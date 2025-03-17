#type: ignore
from litellm import completion
import os

def call_gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",  
        messages=[
            {"role": "user", "content": "Hello, how are you?"}
        ],
        api_key=os.environ.get("GOOGLE_API_KEY")
    )

    response = response.choices[0].message.content

    print(response)
    return response
