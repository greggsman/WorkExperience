import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-ada-001",
  prompt="Write a headline for an article about pythagoras",
  temperature=0,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)