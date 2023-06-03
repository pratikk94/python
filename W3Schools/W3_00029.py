"""
     Write a Python program that prints out all colors from color_list_1 that are not present
        in color_list_2.

        Test Data :
            color_list_1 = set(["White", "Black", "Red"])
            color_list_2 = set(["Red", "Green"])
        Expected Output :
            {'Black', 'White'}

"""
color_list_1 = {"White", "Black", "Red"}
color_list_2 = {"Red", "Green"}
new_list = []
for item in color_list_1:
    if item not in color_list_2:
        new_list.append(item)
print(new_list)