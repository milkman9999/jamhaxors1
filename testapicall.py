import openai

openai.api_key= "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"

prompt = "Hello"
response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1000)

print(response.choices[0]['text'])