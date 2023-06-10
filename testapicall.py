import openai
openai.api_key= "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"

prompt = "Hello ai"

prompt = "Hello"
response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1000)

print(response.choices[0]['text'])