import sqlite3

#Connect to SQLite database
con = sqlite3.connect('shoppinglist.db')
cursor = con.cursor()

# Create tables, if not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS groceries (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(32) NOT NULL,
               amount INTEGER NOT NULL,
               price INTEGER,
               category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
                )
            ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(32) NOT NULL)
               ''')



def add_item():
    name = input("Which item are you looking for?: ")
    amount = int(input("How much would you like to buy?: "))
    price = float(nput("Enter the price: "))

    cursor.execute('''INSERT INTO groceries (name, amount, price) VALUES (?, ?, ?)''', (name, amount, price))
    print(f"{name} added successfully!")
    con.commit()
    further_article = input("Would you like to enter another article? y/n: ").lower()
    if another_article == 'y':
        add_item()
    else:
        None

def update_list():
    id = input("Please enter the ID: ")
    name = input("new name: ")
    amount = input("new quantity: ")
    price = input("new price: ")
    cursor.execute('''UPDATE groceries SET name = ?, amount = ?, price = ? WHERE id = ?''', (name, amount, price, id))
    con.commit()
    print(f"{name} changed successfully!")
    choice = input("Would you like to enter another article? y/n: ").lower()
    if choice == 'y':
        update_list()
    else:
        main_menu()

def delete_item():
    id = input("Please enter the ID: ")
    cursor.execute("DELETE FROM groceries WHERE id = ?", (id,))
    print("deleted successfully!")

    main_menu()


