# from dest.actions import add_destination, print_destinations
# from dest.search import search_destinations


from dest.actions import add_destination, print_destinations
from dest.edit import edit_destinations
from dest.search import search_destinations
from icecream import ic


def menu(my_dests):
    while True:
        # print("1-add")
        ic("1-add")
        ic("2-list")
        ic("3-search")
        ic("4-edit")
        ic("5-exit")
        selection = input("your command?")
        if selection == "1":
            add_destination(my_dests)
        if selection == "2":
            print_destinations(my_dests)
        if selection == "3":
            search_dest = input("what do you want to search")
            print_array =search_destinations(my_dests,search_dest)
            for index,dest in enumerate(print_array):
                print (dest[0], dest[1])
        if selection == "4":
            edit_destinations(my_dests)
        if selection == "5":
            print("goodbye")

            break
