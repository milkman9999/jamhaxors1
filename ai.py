import openai
openai.api_key= "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"

completion = openai.Completion.create(engine="text-davinci-003", prompt="Is this a test?", max_tokens=1000)
print(completion.choices[0]['text'])