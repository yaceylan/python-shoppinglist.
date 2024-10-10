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

# Activate foreign key
cursor.execute("PRAGMA foreign_keys = ON;")

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

def show_shoppinglist():
    choice = input("Do you want all(1), a chosen(2) Items under a specific category(3) ? 1/2/3: ")
    try:
        if choice == '1':
            cursor.execute("SELECT * FROM groceries")
            list = cursor.fetchall()
            print(list)
        elif choice == '2':
            second_choice = input("Are you looking for ID(1) or name(2) ? 1/2: ")
            try:
                if second_choice == '1':
                    id = input("Please enter the ID: ")
                    cursor.execute("SELECT * FROM groceries WHERE id = ?", (id,))
                    item = cursor.fetchone()
                    print(item)
                elif second_choice == '2':
                    name = input("Please enter the name: ")
                    cursor.execute("SELECT * FROM groceries WHERE name = ?", (name,))
                    name_item = cursor.fetchone()
                    print(name_item)
                elif choice == '3':
                    category = input("Please enter the category: ")
                    cursor.execute('''SELECT groceries.* FROM groceries
                                        JOIN categories ON groceries.category_id = categories.id
                                        WHERE categories.name = ?
                                        ''', (category,))
                    output = cursor.fetchall()
                    for row in output:
                        print(f"ID: {row[0]}, name: {row[1]}")

            except ValueError:
                print("Are you sure?")
    except ValueError:
        print("1 or 2...")

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

def categories():
    id = input("Please enter the ID: ")
    category_name = input("Enter the category: ")
    cursor.execute("INSERT INTO categories (name) VALUES (?)", (category_name,))
    con.commit()
    print(f "{name} added successfully!")

def main_menu():
    while True:
        print("Welcome!\n1. Add\n2. Show\n3. Update\n4. Delete\n5. Category\n6. Finish")
        choice = input("Enter a number: ")
        try:
            if choice == '1':
                add_item()
            elif choice == '2':
                show_shoppinglist()
            elif choice == '3':
                update_list()
            elif choice == '4':
                delete_item()
            elif choice == '5':
                categories()
            elif choice == '6':
                quit()
        except ValueError:
            print("1, 2, 3, 4 or 5!")

if __name__ == '__main__':
    main_menu()


