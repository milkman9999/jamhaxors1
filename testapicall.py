import openai
openai.api_key= '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'

prompt = "Say this is a test"

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=10)

print(response)