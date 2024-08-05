# Define individual dictionaries
python_term = [
    {
    'loop': 'repeated action',
    'list': 'ordered collection',
    'dictionary': 'keys and values',
    },

    {
    'function': 'reusable block of code',
    'variable': 'storage location',
    'class': 'blueprint for objects',
    },

    {
    'module': 'file containing Python definitions and statements',
    'package': 'collection of modules',
    'exception': 'error handling mechanism',
    }
]

# first_item = python_term[0]
# print(first_item)

# for key, value in first_item.items():
#      print(f"The term {key} in python: {value}")

# second_item = python_term[1]
# print(second_item["function"])

# for key, value in second_item.items():
#      print(f"The term {key} in python: {value}")

# # Print the list of dictionaries
# for term_dict in python_terms_list:
#     print(term_dict)



# for key, value in python_term1.items():
#     print(f"The term {key} in python: {value}")


# python_term= {
#     'loop': 'repeated action',
#     'list': 'ordered collection',
#     'dictionary': 'keys and values',
# }

import requests as r

url = f"https://api.github.com/repos/kubernetes/kubernetes/pulls"
reply = r.get(url)
pull = reply.json()

for i in pull:
     print(i["user"]["login"])