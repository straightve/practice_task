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
            food(MyComic): the comic that you want to update the detail of.
        """
    print("update details")
    # checks that there is a comic in the list.
    try:
        str_name.set("Name: " + food.get_name())
    except AttributeError:
        messagebox.showerror("Error", "There are no comics")
        return
    # puts the current cost, stock and title in the labels
    str_cost.set("Price: $" + str(food.get_price()))
    the_stock = food.get_stock()
    if the_stock > 0:
        str_stock.set("Avalible: yes")
    else:
        str_stock.set("Avalible: no")


def get_food(the_title):
    """finds the food in the list.

    Args:
         the_title (int): the title of the food.
    returns:
        food(MyComic) the food that the user clicked on.
    """
    # finds the food from the food list.
    for food in food_list:
        if food.get_name() == the_title:
            return food
    print("food not found")


def add_to_order(food):
    # checks if there is more than 0 stock and provid an error mesage
    stock = food.get_stock()
    if stock <= 0:
        food_name = food.get_name()
        print("there are no {} avalible".format(food_name))
        error_window = Toplevel(root)
        error_window.title("confomation")
        error_window.geometry("320x94")
        error_window.option_add("*Font", "LucidaGrande 20")
        Label(error_window, text="there are no {} avalible".format(food_name))
    # decreses the stock
    new_stock = stock - 1
    food.set_stock(new_stock)
    print(new_stock)
    # adds chosen food to a oredr list
    food_name = food.get_name()
    order_list.append(food_name)
    # makes a confomation mesage
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
    food_name = food.get_name()
    # finds food in order list and removes it
    for the_food in order_list:
        if the_food == food_name:
            order_list.remove(the_food)
            # increses the stock
            stock = food.get_stock()
            new_stock = stock + 1
            food.set_stock(new_stock)
    # creats comfamation mesage
    remove_order_window = Toplevel(root)
    remove_order_window.title("confomation")
    remove_order_window.geometry("360x94")
    remove_order_window.option_add("*Font", "LucidaGrande 20")

    Label(remove_order_window, text=food_name + " removed from order.").grid(row=0, column=0, columnspan=2, sticky=W)
    Button(remove_order_window, text="Ok", bg="#4c69f6", fg="white",
           command=lambda: close_window(remove_order_window)).grid(
        row=2,
        column=0,
        padx=40)
    return total_cost


def revew_order():
    # finds the total price
    total_price = total_cost()
    # creats order window
    revew_order_window = Toplevel(root)
    revew_order_window.title("Order")
    revew_order_window.geometry("320x510")
    revew_order_window.option_add("*Font", "LucidaGrande 20")

    order_items = Listbox(revew_order_window, height=10)
    for food in order_list:
        order_items.insert(END, food)
    order_items.grid(row=1, column=0, rowspan=10, padx=5)
    Label(revew_order_window, text="Order", font=("LucidaGrande", 35, "bold"), fg="#ee5454").grid(row=0, column=0)
    Label(revew_order_window, text="total price: ${}".format(total_price)).grid(row=11, column=0, columnspan=2, pady=10)
    Label(revew_order_window, text="cost for delevery: $5").grid(row=12, column=0, columnspan=2, pady=10)


def total_cost():
    total_price = 0
    # for each food in order list it finds the price and adds it to total_price
    for the_food in order_list:
        food = get_food(the_food)
        the_price = food.get_price()
        total_price = total_price + the_price
    return total_price


def finish_order():
    takeaway_deleviry_window = Toplevel(root)
    takeaway_deleviry_window.title("takeaway or deleviry")
    takeaway_deleviry_window.geometry("440x208")
    takeaway_deleviry_window.option_add("*Font", "LucidaGrande 20")
    Button(takeaway_deleviry_window, text="deleviry", bg="#4c69f6", fg="white").grid(row=0, column=0)
    Button(takeaway_deleviry_window, text="takeaway", bg="#4c69f6", fg="white", command=lambda: takeaway()).grid(row=0,
                                                                                                                 column=1)


def takeaway():
    takaway_window = Toplevel(root)
    takaway_window.title("Add comic")
    takaway_window.geometry("440x208")
    takaway_window.option_add("*Font", "LucidaGrande 20")

    Label(takaway_window, text="name:").grid(row=2, column=0, sticky=E)

    str_new_name = StringVar("")
    str_error_msg = StringVar("")

    Entry(takaway_window, textvariable=str_new_name).grid(row=0, column=1, sticky=E + W)

    Label(takaway_window, textvariable=str_error_msg, fg="red").grid(row=4, column=0, columnspan=2, sticky=N + E + S + W)
    # closes the window
    Button(takaway_window, text="Cancel", bg="#ffc510", fg="white",
           command=lambda: close_window(takaway_window)).grid(row=5, column=0, sticky=E)
    # creates the comic and closes the window.
    Button(takaway_window, text="finish", bg="#f6db35", fg="white",
           command=lambda: finish_and_close(str_new_name.get(),
                                            takaway_window,
                                            str_error_msg)).grid(row=5, column=1, sticky=W)
def finish_and_close(preson_name, window, error_massage):
    if "" in [preson_name]:
        error_massage.set("No field can be blank.")
        return

    total_price = total_cost()
    output_file = open("orders.csv", "w")
    writer = csv.writer(output_file)
    writer.writerow(preson_name, order_list, total_price)
    output_file.close()

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

revew_order_button = Button(root, text="Revew order", bg="#ffc510", fg="white", command=lambda: revew_order())
revew_order_button.grid(row=11, column=1, sticky=E + W)

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
