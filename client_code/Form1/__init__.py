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
     
    # Any code you write here will run before the form opens'

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    #navigator.clipboard.writeText("Hello World!")

    w =anvil.js.window.open("https://www.bing.com/chat", "_blank")
    w.document.title='titletest'
    #w.document.title.innerText
    w.document.execCommand('copy')
    print("after copy")
    
    return_value=anvil.server.call('sayhello','james')
    print(f"the return value was {return_value}")
    print("after sleep")
    self.text_box_1.text='What is a cow'
    self.text_box_1.select()
    #print(w.document.title)

    
    #navigator.clipboard.writeText('Boom')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_1.select()
    
    
    

    