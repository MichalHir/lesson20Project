from dest.actions import print_destinations


def search_destinations(my_dests,search_str):
    print_destinations(my_dests)
    search_array = []
    found = False
    # search_dest = input("what do you want to search")
    # try:
    for index, dest in enumerate(my_dests):
        if search_str.lower() in dest.lower():
            #  thisdict = {"index_of" : str(index), "name" : dest}
                # thisdict = dict(index_of=index, name=dest)
            thisdest = (index, dest)
                # print (thisdest)
            search_array.append(thisdest)
            found = True
    if not found:
        print("no destinaions found")
    return search_array
    # except:
    #     for index, dest in enumerate(my_dests):
    #         if search_dest.lower() in dest.lower():
    #         #  thisdict = {"index_of" : str(index), "name" : dest}
    #             thisdest = index, dest
    #             # print (thisdest)
    #             search_array.append(thisdest)
    #             found = True
    #     if not found:
    #         print("no destinaions found")
    #     return search_array

