import openai
from config import API_KEY
openai.api_key= API_KEY

prompt = "Say this is a test"

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=10)

print(response)