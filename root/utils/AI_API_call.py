import os
import openai
openai.organization =  os.getenv("OPENAI_ORG_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()