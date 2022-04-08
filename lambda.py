people = [
    {"name": "Jose", "city": "Gorbea"},
    {"name": "Valentina", "city": "Labranza"}
]

#This function f1 is the same that the code below print(people), an explanation of how lambda expressions 
#works
def f1(person):
    return person["name"]

people.sort(key=f1)

print(people)

#This is an apliccation of lambda expressions

people.sort(key=lambda person: person["name"])