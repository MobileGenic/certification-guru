import anvil.server
import requests
import json

@anvil.server.callable
def send_prompt_to_ollama(prompt_text, model="llama3"):
  url = "http://localhost:11434/api/generate"
  payload = {
    "model": model,
    "prompt": prompt_text,
    "stream": False
  }

  headers = {
    "Content-Type": "application/json"
  }

  try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data.get("response", "No response found.")
  except requests.exceptions.RequestException as e:
    return f"Error contacting Ollama API: {str(e)}"
✨ Optional Front-End Additions
Want to support model switching from the UI? You could pass a second argument like this:

python
def button_1_click(self, **event_args):
    prompt = self.text_box_1.text
    model_choice = self.drop_down_1.selected_value  # Assuming dropdown for model selection
    result = anvil.server.call('send_prompt_to_ollama', prompt, model_choice)
    self.label_1.text = result
  