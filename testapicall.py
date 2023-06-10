import openai
openai.api_key= "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"

prompt = "Hello ai"

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=10)

print(response)