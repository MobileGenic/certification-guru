from ._anvil_designer import Form2Template
from anvil import *
import anvil.server


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.output_box.text = "Enter a prompt and click Run."

    # Any code you write here will run before the form opens.

  def run_button_click(self, **event_args):
    prompt = (self.prompt_box.text or "").strip()  
    if not prompt:
      self.output_box.text = "Please type a prompt first."
      return
    try:
      self.run_button.enabled = False
      self.run_button.text = "Running..."
    finally:
        self.run_button.enabled = True
        self.run_button.text = "Run"
