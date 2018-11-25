# Create a new Python file in this folder called cafe.py.
# Create a list called menu, which should contain at least 4 items in the cafe.
# Next, create a dictionary called stock, which should contain the stock value for each item on your menu.
# Create another dictionary called price, which should contain the prices for each item on your menu.
# Next, create a function which will calculate the total stock worth in the cafe. You will need to remember to loop through the appropriate dictionaries and lists to
# do this.
# Finally, print out the result of your function.

def print_bill(order):
    print("Orders thus far: ")
    print(enumerate("Item Ordered: " +  str(len(bill)) + " \tPrice: R" + str(sum(bill)) + ".00" )    )

def order(fb_menu, stock, price):
    order[fb_menu] = price
    order[stock] = quantity
    
stock = {"packets" : 100, "bags" : 100, "ham_cheese" : 100, "ice_cream" : 100}

fb_menu = {"coffee": 18, "tea": 15, "sandwich": 25, "waffle": 22}

def new_table(order, filename):
    in_table = open(filename, "w")
    for i in order.keys():
        in_table.write(i + " , " + orders[i] + "\n")
    in_table.close()

def idle_table(orders, filename):
    out_table = open(filename, "r")
    for line in out_table:
        line = line.rstrip("\n")
        stock, price = line.strip(" , ")
        order[stock] = price
    out_table.close()
        
def print_menu():
    print("1. Start a new table?")
    print("2. Place an order?")
    print("3. Call customer table?")
    print("4. Print Bill")
    print("5. Quit")
    print()
    
bill = {}
menu_choice = 0
print_menu()
while True:
    menu_choice = int(input("Welcome, please enter a number: "))
    if menu_choice == 1:
        filename = input("Customer name to save: ")
        new_table(bill, filename)
    elif menu_choice == 2:
        choice = int(input("Your options are: " + "\n1. Americano " + "\n2.Rooibos, " + "\n3.Sandwich, " + "\n4.Waffle" + "\n5.Enough ordered" + "\n"))
        if choice == 1:
            choice = "coffee"
            bill.append(choice)
            stock["packets"] -= 1
        elif choice == 2:
            choice = "tea"
            bill.append(choice)
            stock["bags"] -= 1
        elif choice == 3:
            choice = "sandwich"
            bill.append(choice)
            stock["ham_cheese"] -= 1
        elif choice == 4:
            choice = "waffle"
            bill.append(choice)
            stock["ice_cream"] -= 1
        elif choice == 5:
            break
    elif menu_choice == 3:
        filename = input("Customer name to load: ")
        idle_table(bill, filename)
    elif menu_choice == 4:
        print_bill(bill)
    elif menu_choice == 5:
        break
    else:
        print_menu()

print("Thank you for visiting, please come again.")



'''
1) To clarify the question and answer: the problem is that there are 2 dicts d, my_dict. each values is a tuple containing 2 items. what we want is to generate a new
   dict which has the keys and values of d but with the first item of the value tuple increased by 1 if the key exists in my_dict or set to 1 if it doesn't. we will
   achieve that like this:
{x: (y[0] + 1 if x in my_dict else 1, y[1]) for x, y in d.items()}          {x: (stock[packets] - 1 if x in stock else - 0) for x, packets in stock}

2) 
dlookup = {d['id'] : d['d'] for d in d_dicts}                               stock_lookup = {stock["packets"] : stock["stock"] for packets in bill}

for d in dicts:                                                             for item in stock:
    i = d['id']                                                                 i = item[stock]
    if i in dlookup:                                                            if i in stock_lookup:
        d['d'] = dlookup[i]                                                         item["packets"] = dlookup[i]
'''















































    
    
        


