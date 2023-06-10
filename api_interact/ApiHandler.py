import openai
import config
import api_interact.PromptHandler as PromptHandler

# set key from config
openai.api_key=config.API_KEY

def gen_from_prompt(privprompt, temperature, max_tokens):
    prompt = privprompt    
    response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=10)
    return response.choices[0]['text']

print(gen_from_prompt("hello ai"))