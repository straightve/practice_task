from Food_Items import FoodItems
from Order import Order
from tkinter import *
import csv
from tkinter import messagebox

root = Tk()
# creates the main window.
root.title("Takeaway Shop")
root.geometry("600x480")
root.option_add("*font", "LucidaGrande 20")

order_list = []
input_file = open("food_items.csv", "r")
file_data = csv.reader(input_file)
# the list of comics.
food_list = []
for row in file_data:
    name = row[0].strip()
    price = int(row[1].strip())
    stock = int(row[2].strip())

    food_list.append(FoodItems(name, price, stock))
input_file.close()


def update(food):
    """update the details displayed of a given comic.

        Args:
            food(FoodItems): the food that you want to update the detail of.
        """
    # checks that there is a comic in the list.
    try:
        str_name.set("Name: " + food.get_name())
    except AttributeError:
        messagebox.showerror("Error", "There are no comics")
        return

    # puts the current cost in the label.
    str_cost.set("Price: $" + str(food.get_price()))
    # checks if there is more than 0 and then displays the availability.
    the_stock = food.get_stock()
    if the_stock > 0:
        str_stock.set("Available: yes")
    else:
        str_stock.set("Available: no")


def get_food(the_title):
    """finds the food in the list.

    Args:
         the_title (int): the title of the food.
    returns:
        food(FoodItems) the food that the user clicked on.
    """
    # finds the food from the food list.
    for food in food_list:
        if food.get_name() == the_title:
            return food
    print("food not found")


def add_to_order(food):
    """adds the name of the food to the order list and makes a confirmation window.

        Args:
            food(FoodItems): the food that is being added.
        """
    # checks if there is more than 0 stock and creates an error message.
    the_stock = food.get_stock()
    if the_stock <= 0:
        food_name = food.get_name()
        print("there are no {} avalible".format(food_name))
        error_window = Toplevel(root)
        error_window.title("confirmation")
        error_window.geometry("320x94")
        error_window.option_add("*Font", "LucidaGrande 20")
        Label(error_window, text="there are no {} avalible".format(food_name))

    # decreases the stock.
    new_stock = the_stock - 1
    food.set_stock(new_stock)
    print(new_stock)

    # adds chosen food to a order list.
    food_name = food.get_name()
    order_list.append(food_name)

    # makes a confirmation message.
    add_order_window = Toplevel(root)
    add_order_window.title("confomation")
    add_order_window.geometry("320x94")
    add_order_window.option_add("*Font", "LucidaGrande 20")

    Label(add_order_window, text=food_name + " added to order.").grid(row=0, column=0, columnspan=2, sticky=W)
    Button(add_order_window, text="Ok", bg="#4c69f6", fg="white", command=lambda: close_window(add_order_window)).grid(
        row=2,
        column=0,
        padx=40)


def close_window(window):
    """closes a window.

    Args:
         window (): the window that is to be closed.
    """
    # closes the current window.
    window.destroy()


def remove_from_order(food):
    """removes the name of the food from the order list and makes a confirmation window.

            Args:
                food(FoodItems): the food that is being added.

            """
    # finds food in order list and removes it.
    food_name = food.get_name()
    for the_food in order_list:
        if the_food == food_name:
            order_list.remove(the_food)
            # increases the stock.
            the_stock = food.get_stock()
            new_stock = the_stock + 1
            food.set_stock(new_stock)
    # creates confirmation message with a label and a button.
    remove_order_window = Toplevel(root)
    remove_order_window.title("confomation")
    remove_order_window.geometry("360x94")
    remove_order_window.option_add("*Font", "LucidaGrande 20")

    Label(remove_order_window, text=food_name + " removed from order.").grid(row=0, column=0, columnspan=2, sticky=W)
    # closes the window.
    Button(remove_order_window, text="Ok", bg="#4c69f6", fg="white",
           command=lambda: close_window(remove_order_window)).grid(row=2, column=0, padx=40)


def review_order():
    """creates a window that shows the order."""
    # finds the total price.
    total_price = total_cost()
    # creates order window with a list box two labels and a button.
    review_order_window = Toplevel(root)
    review_order_window.title("Order")
    review_order_window.geometry("320x580")
    review_order_window.option_add("*Font", "LucidaGrande 20")

    order_items = Listbox(review_order_window, height=10)
    for food in order_list:
        order_items.insert(END, food)
    order_items.grid(row=1, column=0, rowspan=10, padx=5)
    Label(review_order_window, text="Order", font=("LucidaGrande", 35, "bold"), fg="#ee5454").grid(row=0, column=0)
    Label(review_order_window, text="total price: ${}".format(total_price)).grid(row=11, column=0, columnspan=2,
                                                                                 pady=10)
    Label(review_order_window, text="cost for delevery: $5").grid(row=12, column=0, columnspan=2, pady=10)
    # closes window.
    Button(review_order_window, text="Close", bg="#4c69f6", fg="white",
           command=lambda: close_window(review_order_window)).grid(
        row=13,
        column=0,
        padx=40)


def total_cost():
    """finds the total cost of the things in the order list.
            returns:
                total_price(int) the total price of the things ordered.
            """
    total_price = 0
    # for each food in order list it finds the price and adds it to total_price.
    for the_food in order_list:
        food = get_food(the_food)
        the_price = food.get_price()
        total_price = total_price + the_price
    return total_price


def finish_order():
    """a window that has buttons that lead to the delivery and takeaway windows"""
    # creates a window with two buttons.
    takeaway_delivery_window = Toplevel(root)
    takeaway_delivery_window.title("takeaway or delivery")
    takeaway_delivery_window.geometry("440x208")
    takeaway_delivery_window.option_add("*Font", "LucidaGrande 20")
    # takes you to delivery window.
    Button(takeaway_delivery_window, text="delivery", bg="#4c69f6", fg="white",
           command=lambda: delivery(takeaway_delivery_window)).grid(row=0, column=0)
    # takes you to takeaway window.
    Button(takeaway_delivery_window, text="takeaway", bg="#4c69f6", fg="white",
           command=lambda: takeaway(takeaway_delivery_window)).grid(row=0, column=1)


def delivery(window):
    """creates a window where you can enter details """
    close_window(window)
    # creates a window with 4 labels 2 buttons and 3 entries.
    delivery_window = Toplevel(root)
    delivery_window.title("delivery")
    delivery_window.geometry("440x208")
    delivery_window.option_add("*Font", "LucidaGrande 20")

    Label(delivery_window, text="name:").grid(row=0, column=0, sticky=E)
    Label(delivery_window, text="address:").grid(row=1, column=0, sticky=E)
    Label(delivery_window, text="phone:").grid(row=2, column=0, sticky=E)

    str_person_name = StringVar("")
    str_address = StringVar("")
    str_phone = StringVar("")
    str_error_msg = StringVar("")

    Entry(delivery_window, textvariable=str_person_name).grid(row=0, column=1, sticky=E + W)
    Entry(delivery_window, textvariable=str_address).grid(row=1, column=1, sticky=E + W)
    Entry(delivery_window, textvariable=str_phone).grid(row=2, column=1, sticky=E + W)

    Label(delivery_window, textvariable=str_error_msg, fg="red").grid(row=4,
                                                                      column=0,
                                                                      columnspan=2,
                                                                      sticky=N + E + S + W)
    # closes the window
    Button(delivery_window, text="Cancel", bg="#ffc510", fg="white",
           command=lambda: close_window(delivery_window)).grid(row=5,
                                                               column=0,
                                                               sticky=E)
    # creates the comic and closes the window.
    Button(delivery_window, text="Finish", bg="#f6db35", fg="white",
           command=lambda: finish_delivery(str_person_name.get(),
                                           str_address.get(),
                                           str_phone.get(),
                                           delivery_window,
                                           str_error_msg)).grid(row=5, column=1, sticky=W)


def finish_delivery(person_name, address, phone, window, error_massage):
    """removes the name of the food from the order list and makes a confirmation window.

                Args:
                    person_name(str): the name put in in the delivery window.
                    phone(str): the phone put in in the delivery window.
                    address(str): the address put in in the delivery window.
                    window(): the delivery window.
                    error_massage(): the error message label from the delivery window

                """
    # checks if person_name, address, phone  dont have a value and shows error message.
    if "" in [person_name, address, phone]:
        error_massage.set("No field can be blank.")
        return
    # checks if phone is not a num and shows error message.
    try:
        new_price = int(phone)
    except ValueError:
        error_massage.set("phone number must be a number.")
        return
    else:
        # finds total price and creates a list with "delivery", person_name, address, phone in it.
        total_price = total_cost() + 5
        row_list = ["delivery", person_name, address, phone]

        # adds the items in order list to row_list.
        for item in order_list:
            row_list.append(item)
        row_list.append(total_price)
        # writes order_ list to a csv file.
        output_file = open("orders.csv", "w")
        writer = csv.writer(output_file)
        writer.writerow(row_list)

        # closes file, the window and clears the order list.
        output_file.close()
        close_window(window)
        order_list.clear()


def takeaway(window):
    """removes the name of the food from the order list and makes a confirmation window.

                    Args:
                        window(): the takeaway_delivery_window.

                    """
    close_window(window)
    takaway_window = Toplevel(root)
    takaway_window.title("Add comic")
    takaway_window.geometry("440x208")
    takaway_window.option_add("*Font", "LucidaGrande 20")

    Label(takaway_window, text="name:").grid(row=2, column=0, sticky=E)

    str_person_name = StringVar("")
    str_error_msg = StringVar("")

    Entry(takaway_window, textvariable=str_person_name).grid(row=0, column=1, sticky=E + W)

    Label(takaway_window, textvariable=str_error_msg, fg="red").grid(row=4, column=0, columnspan=2,
                                                                     sticky=N + E + S + W)
    # closes the window
    Button(takaway_window, text="Cancel", bg="#ffc510", fg="white",
           command=lambda: close_window(takaway_window)).grid(row=5, column=0, sticky=E)
    # creates the comic and closes the window.
    Button(takaway_window, text="finish", bg="#f6db35", fg="white",
           command=lambda: finish_takeaway(str_person_name.get(),
                                           takaway_window,
                                           str_error_msg)).grid(row=5, column=1, sticky=W)


def finish_takeaway(person_name, window, error_massage):
    """removes the name of the food from the order list and makes a confirmation window.

                Args:
                    person_name(str): the name put in in the delivery window.
                    window(): the delivery window.
                    error_massage(): the error message label from the delivery window

                """
    # checks that there is something in person_name.
    if "" in [person_name]:
        error_massage.set("No field can be blank.")
        return
    else:
        # finds the total price and creates a list with "takeaway", person_name in it.
        total_price = total_cost()
        row_list = ["takeaway", person_name]

        # adda the items in order list to roe_list.
        for item in order_list:
            row_list.append(item)
        row_list.append(total_price)

        # writes it to a csv file.
        output_file = open("orders.csv", "w")
        writer = csv.writer(output_file)
        writer.writerow(row_list)

        # closes the file, clears the order list and closes the window.
        output_file.close()
        order_list.clear()
        close_window(window)


food_selector = Listbox(root, height=10)
for a_food in food_list:
    food_selector.insert(END, a_food.get_name())
food_selector.grid(row=1, column=0, rowspan=11, padx=5)

add_to_order_button = Button(root, text="Add to order", bg="#4c69f6", fg="white", width=17,
                             command=lambda: add_to_order(
                                 get_food(food_selector.get(ACTIVE))))
add_to_order_button.grid(row=5, column=1, sticky=W + E)

remove_from_order_button = Button(root, text="Remove from order", bg="#4c94f6", fg="white",
                                  command=lambda: remove_from_order(get_food(
                                      food_selector.get(ACTIVE))))
remove_from_order_button.grid(row=6, column=1, sticky=W + E)

update_details = Button(root, text="Update Details", bg="#ee5454", fg="white", command=lambda: update(get_food(
    food_selector.get(ACTIVE))))
update_details.grid(row=12, column=0, sticky=E + W, padx=5)

review_order_button = Button(root, text="Revew order", bg="#ffc510", fg="white", command=lambda: review_order())
review_order_button.grid(row=11, column=1, sticky=E + W)

finish = Button(root, text="Finish", bg="#f6db35", fg="white", command=lambda: finish_order())
finish.grid(row=12, column=1, sticky=E + W)

str_name = StringVar(value="Name: ")
str_cost = StringVar(value="Price: ")
str_stock = StringVar(value="Avaliblty: ")

heading = Label(root, text="Takeaway Shop", font=("LucidaGrande", 35, "bold"), fg="#ee5454").grid(row=0,
                                                                                                  column=0,
                                                                                                  columnspan=2,
                                                                                                  pady=10)
the_name = Label(root, textvariable=str_name).grid(row=1, column=1, sticky=W)
cost = Label(root, textvariable=str_cost).grid(row=2, column=1, sticky=W)
stock = Label(root, textvariable=str_stock).grid(row=3, column=1, sticky=W)

root.mainloop()
