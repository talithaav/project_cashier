# import library
from tabulate import tabulate

class Transaction:
    
    def __init__(self):
        self.item_dict = dict()
        
    def add_item(self):
        """Function to add items by inputting the name, quantity, and price for each item.
        """
        
        item_name = input("Input Item Name: ")
        item_qty = int(input("Input Item Quantity: "))
        price_per_item = float(input("Input Item Price: "))
        
        self.item_dict.update({item_name : [item_qty, price_per_item]})
        
        print("\nItem successfully added!\n")
        print(f"Item Name: {item_name} \nQuantity: {int(item_qty)}\nPrice: Rp {float(price_per_item)}\n")
        
    def print_item_list(self):
        """Function to show all items along with their quantity and price in tabulate.
        """
        
        index =[]
        table = []
        headers = ['No','Item Name', 'Item Qty', 'Item Price']
        
        for idx, _ in enumerate(self.item_dict, start=1):
            index.append(idx)
            
        for key, value in self.item_dict.items():
            table.append([key, value[0], value[1]])
            
        print("==================ORDER LIST==================")
        print(tabulate(table, headers=headers, tablefmt='fancy_grid', stralign="center", showindex=index))
    
    def print_receipt(self):
        """
        Function to show the receipt contains all items along with their quantity, price, 
        and total price for each item in tabulate
        """
        
        index =[]
        table = []
        headers = ['No','Item Name', 'Item Qty', 'Item Price', 'Total Price']
        
        for idx, _ in enumerate(self.item_dict, start=1):
            index.append(idx)
            
        for key, value in self.item_dict.items():
            total_price = value[0]*value[1]
            table.append([key, value[0], value[1], total_price])

        print("==================RECEIPT==================")
        print(tabulate(table, headers=headers, tablefmt='fancy_grid', stralign="center", showindex=index))
    
    def check_order(self):
        """
        Function to recheck items that have been added.
        The function will call the print_item_list() function to show all items with its detail.
        """
        
        self.print_item_list()
        
#         while True:
#             check = input("Is the order correct? (*yes/no)").lower()
#             if check in ['yes', 'no']:
#                 break
#             else:
#                 print("Please enter 'yes' or 'no'.")

#         if check == 'yes':
#             self.print_receipt()
#         else:
#             self.edit_order()
        # self.menu()

    def edit_order(self):
        """This function will guide user for several inputs regarding editing incorrect inputs.
        """
        
        while True:
            edit = input("Specify the column you want to edit (*name/quantity/price)"):.lower()
            if edit in ['name', 'quantity', 'price']:
                break
            else:
                print("Please enter 'name', 'quantity', or 'price'.")

        if edit == 'name':
            old_name = input("Write the wrong item name (*make sure the item name is correct):")
            new_name = input("Write the new item name:")
            self.update_item_name(old_name, new_name)
        elif edit == 'quantity':
            item_name = input("Which item do you want to change?")
            new_qty = float(input("Enter new quantity:"))
            if new_qty >= 0:
                self.update_item_quantity(item_name, new_qty)
            else:
                raise ValueError("Invalid quantity input! Quantity must be a positive number.")
        elif edit == 'price':
            item_name = input("Which item do you want to change?")
            new_price = float(input("Enter new price:"))
            if new_price >= 0:
                self.update_item_price(item_name, new_price)
            else:
                raise ValueError("Invalid price input! Price must be a positive number.")

    def update_item_name(self, old_name, new_name):
        """
        Function to correct item name.
        This function will be called from the edit_order() function if the user inputs "name" to 
        which column to be corrected.
        
        Parameters
        ----------
        old_name: string
            wrong item name
        new_name: string
            correct item name
        """
        
        if old_name in self.item_dict:
            item_list = self.item_dict.pop(old_name)
            self.item_dict[new_name] = item_list
            print("\nItem has been updated!")
            self.print_item_list()
        else:
            raise Exception("Item does not exist")

    def update_item_quantity(self, item_name, new_qty):
        """
        Function to correct item quantity.
        This function will be called from the edit_order() function if the user inputs "quantity" to 
        which column to be corrected.
        
        Parameters
        ----------
        item_name: string
            item with wrong quantity
        new_qty: int
            correct item quantity
        """
        
        if item_name in self.item_dict:
            self.item_dict[item_name][0] = int(new_qty)
            print("\nItem has been updated!")
            self.print_item_list()
        else:
            raise Exception("Item does not exist")

    def update_item_price(self, item_name, new_price):
        """
        Function to correct item price.
        This function will be called from the edit_order() function if the user inputs "price" to 
        which column to be corrected.
        
        Parameters
        ----------
        item_name: string
            item with wrong price
        new_price: float
            correct item price
        """
        
        if item_name in self.item_dict:
            self.item_dict[item_name][1] = float(new_price)
            print("\nItem has been updated!")
            self.print_item_list()
        else:
            raise Exception("Item does not exist")
    
    def delete_item(self, item_name):
        """
        Function to delete items.
        
        Parameters
        ----------
        item_name: string
            item to be deleted
        """
        
        if item_name in self.item_dict.keys():
            self.item_dict.pop(item_name)
            print("Item has successfully deleted!")
            self.print_item_list()

        else:
            raise Exception("Item does not exist")
            
        return self.item_dict
    
    def reset_transaction(self):
        """Function to delete all orders that have been added.
        """
        
        self.item_dict.clear()
        
        print("All items successfully deleted!")
            
    def total_price(self):
        """
        Function to calculate the final price for user's spending after discounts based on total price.
        
        Conditions:
        1. If total purchases are above Rp 200,000, user will get a 5% discount.
        2. If total purchases are above Rp 300,000, user will get a 8% discount.
        3. If total purchases are above Rp 500,000, user will get a 10% discount.
        """
        
        total = sum(value[0] * value[1] for value in self.item_dict.values())
    
        if total > 500_000:
            discount_rate, discount = 0.10, "10%"
        elif total > 300_000:
            discount_rate, discount = 0.08, "8%"
        elif total > 200_000:
            discount_rate, discount = 0.05, "5%"
        else:
            discount_rate, discount = 0, "0%"

        final_price = total * (1 - discount_rate)
        
        self.print_receipt()

        print(f"TOTAL PRICE: Rp {total:,.2f} \nDISCOUNT: {discount} \nFINAL PRICE: Rp {final_price:,.2f}")
        
    def menu(self):
        """Function to display menu list.
        """
        
        while True:
            print("-"*60)
            print("WELCOME TO PACMANN SUPERMARKET")
            print("-"*60)
            print("1. Add Items")
            print("2. Show list of Items")
            print("3. Update Items")
            print("4. Delete Items")
            print("5. Clear All Items")
            print("6. Print Receipt")
            print("7. Exit")
            print("-"*60)

            choice = input('\nEnter Task Number : ')

            try:
                if choice == '1':
                    self.add_item()
                elif choice == '2':
                    self.check_order()
                elif choice == '3':
                    self.edit_order()
                elif choice == '4':
                    item_name = input("Enter item name to delete: ")
                    self.delete_item(item_name)
                elif choice == '5':
                    self.reset_transaction()
                elif choice == '6':
                    self.total_price()
                elif choice == '7':
                    print("-"*60)
                    print("Thank you for visiting Pacmann Supermarket.")
                    print("-"*60)
                    break
                else:
                    print("Incorrect Input. Please try again.\n")
            except ValueError:
                print("Please enter a valid number.")
            except Exception as e:
                print(f"Ann error occurred: {e}")

# Usage
if __name__ == "__main__":
    transaction = Transaction()
    transaction.menu()