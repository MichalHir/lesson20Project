from dest.actions import add_destination, print_destinations
from dest.search import search_destinations
from storage.load_save import load, save
from menu.main_menu import menu
from icecream import ic

# from dest.actions import print_destinations

my_destinations = []


# menu(my_destinations)
if __name__ == "__main__":
    load()
    ic()
    menu(my_destinations)
    save()
    # def foo(i):
    #     return i + 333

    # ic(foo(123))
# print(my_destinations)
