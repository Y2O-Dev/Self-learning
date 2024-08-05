# LOOPING THROUGH A LIST
#     # For loop allow working with each item in a list, one item @ a time
# states = ["Kwara", "Lagos", "Kogi"]
# for each_state in states:
#     print(f"I've been to {each_state}")

# for state in states[:-2]:
#      print(f"I have lived in {state}")

# SORTING LIST
vowels = ['a', 'e', 'i', 'o', 'u']
# >>> vowels.sort()
# >>> vowels
# ['a', 'e', 'i', 'o', 'u']
# >>> nums = [1, 3, 2, 5]
# >>> sorted(nums)
# [1, 2, 3, 5]

# REVERSE SORTING: Natural / non natural order
# Natural--> sorted fxn
# sorted(vowels, reverse=True)
#['u', 'o', 'i', 'e', 'a']
# vowels.reverse()
# The reverse argument to sort() or sorted() results in
# reverse natural order; the reverse() method reverses the
# original order of the list.

# NUMERICAL LIST
# The range() function generates a series of numbers.
# Giving range() one argument returns a series of
# numbers from 0 up to, not including, the number:

# nums = []
# for x in range(1,10,2):
#     nums.append(2**x)
# print(nums)

# #LIST COMPRREHENSION: a compact way of defining: a list in one line
# # It uses sq bracket
# nums = [2**x for x in range (1,10,2)]
# print(nums)

# age = 19
# if age >= 18:
#    print ("You're old enough to vote")

#TUPPLES: ()
# sec_sch = (1, 2, 3)
# print(sec_sch)
# element in a tupple are accesed using index
# print (f'Welcome to school {sec_sch[0]}')
# for sec in sec_sch:
#     print (f'Welcome to school {sec}')


# DICTONARY: Allows for the establishment of connection between individual pieces of informatioon
# e.g an Abbr. and its full meaning                     
# No limit to the amount of info that can be stored in a# dictionary

# dictionary methods: get() key() value() and item() methods

capitals = {'KW': 'Ilorin', 'LG': 'Ikeja', 'OG': 'Abeokuta', 'OY': 'Ibadan'}
cap = capitals.get("KW", 'LG')
print(f"Welcome to {cap}")

#  Looping through dict to access keys only
# for states in capitals:
#     print(f"The state code: {states}")

# Looping through dict to access values only 
# for states in capitals.values():
#     print(f"The capitals: {states}")

# To work with both keys and values, use .items()
for states, capitals in capitals.items():
    print(f"For {states}, {capitals}")

# Dictionary can be used to represent a collection of key-value pairs as in glossary
python_term= {
    'loop': 'repeated action',
    'list': 'ordered collection',
    'dictionary': 'keys and values',
}
for terms, meaning in python_term.items():
    print(f"The term {terms} in python: {meaning}")

c_berry = {
    'first' : 'Yusuf',
    'last' : 'YAKUB',
    'birth' : '21-7-95',
    'religion' : 'islam',
}
# Nesting a list of dictionaries

musicians = []

e_fitzgerald = {
    'first': 'Ella'
    --snip--
}
musicians.append(ella)

j_joplin = {
    'first': 'Janis',
    --snip--
}
musicians.append(janis)
--snip--

for musician in musicians:
    full_name = f"{musician['first']} "
    full_name += f"{musician['last']}"
    print(full_name)
