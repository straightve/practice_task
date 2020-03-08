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
    price = row[1].strip()
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
    str_cost.set("Price: " + str(food.get_price()))
    the_stock = food.get_stock()
    if the_stock > 0:
        str_stock.set("Avalible: yes")
    else:
        str_stock.set("Avalible: no")


def get_food(the_title):
    """finds the comic in the list.

    Args:
         the_title (int): the title of the comic.
    returns:
        comic(MyComic) the comic that the user clicked on.
    """
    # finds the comic from the comic list.
    for comic in food_list:
        if comic.get_name() == the_title:
            return comic
    print("comic not found")


def add_to_order(food):
    food_name = food.get_name()
    food_list.append(food_name)
    food_list.set_items()


comic_selector = Listbox(root, height=10)
for a_comic in food_list:
    comic_selector.insert(END, a_comic.get_name())
comic_selector.grid(row=1, column=0, rowspan=11, padx=5)

add_to_order = Button(root, text="Add to order", bg="#4c69f6", fg="white", width=17, command=lambda: add_to_order(get_food(
    comic_selector.get(ACTIVE))))
add_to_order.grid(row=5, column=1, sticky=W + E)

remove_from_order = Button(root, text="Remove from order", bg="#4c94f6", fg="white")
remove_from_order.grid(row=6, column=1, sticky=W + E)

update_details = Button(root, text="Update Details", bg="#ee5454", fg="white", command=lambda: update(get_food(
    comic_selector.get(ACTIVE))))
update_details.grid(row=12, column=0, sticky=E + W, padx=5)

revew_order = Button(root, text="Revew order", bg="#ffc510", fg="white")
revew_order.grid(row=11, column=1, sticky=E + W)

finish = Button(root, text="Finish", bg="#f6db35", fg="white")
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

