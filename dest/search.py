from dest.actions import print_destinations


def search_destinations(my_dests):
    print_destinations(my_dests)
    found = False
    search_dest = input("what do you want to search")
    search_index = -1
    for index, dest in enumerate(my_dests):
        if search_dest.lower() in dest.lower():
            print(index, dest)
            found = True
            if search_dest.lower == dest.lower():
                search_index = index
                return search_index
    if not found:
        print("no destinaions found")
