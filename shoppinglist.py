shoppinglist = []
#create a shoppinglist shoppinglist.py
#we ask the user "please insert the article wich you want into the shoppinglist"
def add_item():
   item = input ("please {insert} the article into the shoppinglist")
   print(f"add your item") 
   shoppinglist.append (item)


#Check the shoppinglist is empty
def check_shoppinglist():
   if not shoppinglist:
      print("your shoppinglist is empty")
   else: 
      print("your shoppinglist")
      for item in shoppinglist:
         print (item)


add_item()
check_shoppinglist()