shoppinglist = []
#create a shoppinglist shoppinglist.py
#we ask the user "please insert the article wich you want into the shoppinglist"
def add_item():
   item = input ("please {insert} the article into the shoppinglist")
   print(f"add your item") 
   shoppinglist.append (item)

add_item()

def show_shoppinglist():
   