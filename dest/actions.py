def print_destinations(my_dests):
    print(my_dests)
    if len(my_dests) == 0:
        print("there are no destinations")


def add_destination(my_dests):
    new_dest = input("destinations's name?")
    my_dests.append(new_dest)
    print_destinations(my_dests)
