from ._anvil_designer import Form1Template
from anvil import *
import anvil.http
import anvil.server

import webbrowser
import anvil.js.window
import anvil.js
from anvil.js.window import navigator
import time
















class Form1(Form1Template):
  tx='this is the sentence to show word by word'
  ndx = 0
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
     
    # Any code you write here will run before the form opens'

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    #navigator.clipboard.writeText("Hello World!")
    alert("When the new tab appears press and hold the ctrl and 'v' keys. Then press the enter key for the answer.")
    alert("After receiving the response close the new browser tab to return here.")
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
    self.text_box_1.text='how old is the star trek tv series'
    #alert("press ok then press and hold the control and C keys at the same time, then click the ask question button")
    
    self.text_box_1.select()
    self.label_1.text = "now hold the control + c keys at the same time, then click the 'ask question' button"

    #alert("1press and hold the ctrl and 'c' keys")

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    if self.label_1.text == 'flash':
     self.label_1.text = 'clear'
    else:
      self.label_1.text = 'flash'
    ndx=1
    if ndx==10:
      ndx = 0

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
  
result = anvil.server.call('query_ollama', "What's the weather like in Tokyo?")
      
      
      
    
      
      
  
    
    
    

    