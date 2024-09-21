from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import webbrowser
import anvil.js.window
import anvil.js
from anvil.js.window import navigator
import time
















class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
     
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""

    w =anvil.js.window.open("https://www.bing.com/chat", "_blank")
    w.document.title='title'
    return_value=anvil.server.call('sayhello','james')
    print(f"the return value was {return_value}")
    time.sleep(60)
    print("after sleep")
    navigator.clipboard.writeText('Boom')
    
    
    

    