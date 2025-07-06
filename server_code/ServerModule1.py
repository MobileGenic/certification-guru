import anvil.server
import requests


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
@anvil.server.callable
def query_ollama(prompt):
  response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "llama3", "prompt": prompt}
  )
  return response.json()["response"]
  
  
  
  

