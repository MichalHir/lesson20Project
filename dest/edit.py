from dest.actions import print_destinations
from dest.search import search_destinations


def edit_destinations(my_dests):
    print_destinations(my_dests)
    edit_dest = input("which destination do you want to edit")
    edit_arr=search_destinations(my_dests,edit_dest)
    if len(edit_arr)==1  and edit_arr[0][1].lower()==edit_dest.lower():
        new_name= input("what is the new name?")
        my_dests[edit_arr[0][0]]=new_name
        print_destinations(my_dests)
    elif len(edit_arr)!=0:
        print("the name is not a destination's full name")
        print("the possible destination are:")
        print_destinations(edit_arr)
    elif len(edit_arr)==0:
        print("the destination's list is:")
        print_destinations(my_dests)