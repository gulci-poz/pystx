def print_args(*args):
    for index, value in enumerate(args):
        print "{0}. {1}".format(index, value)

print_args("jeden", "dwa", "trzy")

def print_kwargs(**kwargs):
    for name, value in kwargs.items():
        print "{0} is {1}".format(name, value)

print_kwargs(fruit = "apple", vegetable = "carrot")

def print_default_value(fruit, vegetable = "carrot", **kwargs):
    print "Fruit is {}".format(fruit)
    print "Vegetable is {}".format(vegetable)

    for name, value in kwargs.items():
        print "{0} is {1}".format(name, value)

print_default_value("apple")
print_default_value(fruit = "apple")
print_default_value("apple", "carrot", meat = "sth")
print_default_value("apple", meat = "sth")
