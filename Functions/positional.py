def para_func(pet,name):
    print("I have a", pet,)
    print("My", pet, "name is", name)

def my_func(name,/): #positional only argument
    print("Hello", name)

para_func("dog", "Buddy")
para_func("Buddy", "dog")
my_func("Yuva")
    