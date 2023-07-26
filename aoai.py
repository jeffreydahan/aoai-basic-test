import os
import openai

openai.api_key = ""   # enter key
openai.api_base = ""   # enter endpoint

openai.api_type = 'azure'
openai.api_version = '2023-05-15' # this may change in the future

response = openai.ChatCompletion.create(
    engine="",   # enter deployment name
    messages=[
        {"role": "system", "content": "You are a customer service representative helping a customer with a problem."},
        {"role": "user", "content": "How can you please help me troubleshoot my laptop that won't turn on?"},
    ],

)
print(response['choices'][0]['message']['content'])