menu = {"one": "1", "two": "2", "three": 3}

print menu["one"]
print menu["two"]
print menu
print menu.keys()
print menu.__contains__("one")
print menu.__sizeof__()
print len(menu)
print menu(1)
#print menu.fromkeys ("")
menu.clear()

print menu