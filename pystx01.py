i = 1
print("i:", type(i))
l = 2L
print("l:", type(l))
a = 0.1
print("a", type(a))
#b = 2e - 1
#print("b:", type(b))
#c = a + b
#print("c val:", c)
d = complex(2, 3)
print("d:", type(d))
print("d val:", d)
["example"] * 2
#['example', 'example']
my_list = [1, 2, 3]
my_list + ["example"]
#[1, 2, 3, 'example']
# znaki utf-8 w dict w py2 z przedrostkiem u (dla klucza i wartości)
#d[u"x"] = u"y"

set_a = set([1, 2, 3])
set_a_alt = {1, 2, 3}

set_b = frozenset([2, 3, 4])

set_a.discard(1)
# co robi?
#set_a.remove()

# sprawdzanie podzbioru
set_a >= set_b

import math
dir(math)
callable(math)
a = "ble"
getattr(a, "__doc__")
