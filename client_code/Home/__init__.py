from ._anvil_designer import HomeTemplate
from anvil import *
from ..About import About
from ..Cart import Cart
from ..Shop import Shop




class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.navigate(self.home_link, Home)

  def main_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    home = Home()
    open_form(home)

  def home_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    home = Home()
    open_form(home)
  

  def shop_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    shop = Shop()
    open_form(shop)

  def cart_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    cart = Cart()
    open_form(cart)

  def about_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    about = About()
    open_form(about)
  
    
    
