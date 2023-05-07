import os
import openai

'''
Execution Runner
'''

if __init__ == 'main':
  
  openai.organization = "YOUR_ORG_ID"
  openai.api_key = os.getenv("OPENAI_API_KEY")
  openai.Model.list()

  
  print('Hello World')
