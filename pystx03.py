# coding: utf-8

from string import ascii_lowercase

def print_alphabet():
    for letter in ascii_lowercase:
        print letter

#print_alphabet()

def print_every_second_letter():
    list_even_letters = ascii_lowercase[::2]
    for letter in list_even_letters:
        print letter,

#print_every_second_letter()

def is_palindrome(word):
    print word, "is palindrome", word == word[::-1]

#is_palindrome("abcba")
#is_palindrome("kolejorz")

def is_in_alphabet(writing):
    new_writing = ""
    for letter in writing:
        if not(letter in ascii_lowercase):
            new_writing += letter

    print new_writing

#is_in_alphabet("abcdeąęózcv")

def long_words(words, nlength):
    print(filter(lambda x: len(x) > nlength, words))

#long_words(["raz", "dwa", "trzy", "cztery"], 3)
#long_words(["raz", "dwa", "trzy", "cztery"], 4)

#[i for i in range(101)]
#[i for i in range(101) if i%2==0]

#print([letter for letter in ascii_lowercase])
#print({ord(value): value for key, value in enumerate(ascii_lowercase)})

words_list = ["bla", "blabla", "blablabla", "blablablabla"]
length = 4
#print(filter(lambda word: len(word) >= length, words_list))
#print([word for word in words_list if len(word) >= length])

#print(map(lambda x: x ** 2, range(1, 51)))

def fib():
    n0 = 0
    n1 = 1
    n2 = 1
    yield n0
    yield n1
    while True:
        yield n2
        n0 = n1
        n1 = n2
        n2 = n0 + n1

fb = fib()
list_num = list()

for n2 in range(13):
    list_num.append(fb.next())

#print [num for num in list_num if num%2 != 0]
#print [num for num in list_num if num%2 == 0]

# wyświetla docstring dla metod (callable)
def obj_attr(obj):
    for attr in dir(obj):
        if callable(getattr(list_num, attr)):
            print getattr(list_num, attr).__doc__


obj_attr(list_num)
