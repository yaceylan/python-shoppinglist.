shoppinglist = []
#create a shoppinglist shoppinglist.py
#we ask the user "please insert the article wich you want into the shoppinglist"
def add_item():
   item = input ("please {insert} the article into the shoppinglist ")
   print(f"add your item") 
   shoppinglist.append (item)


#Check the shoppinglist is empty
def check_shoppinglist():
   print("your shoppinglist:")
   if not shoppinglist:
      print("your shoppinglist is empty")
   else: 
      for item in shoppinglist:
         print (item)


#add_item()

while 2 == 2:
   print("-----Einkaufliste-----")
   print("1. Artikel zur Einkaufsliste hinzufügen")
   print("2. Artikel zur Einkaufsliste")
   print("3. Programm beenden")
   choice = input("Was möchten Sie tun?")
   if choice == "1": 
      add_item()
   elif choice == "2":
      check_shoppinglist()
   elif choice == "3":
      break 

   print("---Ende des Programm---")


