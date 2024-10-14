"""mydict = {}
names = ["Aybuke", "Melike", "Elif", "Sevgi", "İsmail"]
surname = "Eren"
full_name = mydict.fromkeys(names, surname)
print(full_name)"""

member_1 = {
    "name" : "Aybuke",
    "Job" : "student",
    "weigt" : "48"
}
member_2 = {
    "name" : "Melike",
    "Job" : "student",
    "weigt" : "56"
}
member_3 = {
    "name" : "Elif",
    "Job" : "student",
    "weigt" : "35"    
}
family_dict = {
    "child1" : member_1,
    "child2" : member_2,
    "child3" : member_3
}

for x, y in family_dict.items():
    print(x, y)
    
