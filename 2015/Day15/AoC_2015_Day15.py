import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')


ingredients = {}
for item in f:
	props = item.split()
	ingredients[props[0].replace(':','')] = [(props[2], props[4], props[6], props[8], props[10])]

# print(ingredients)

capacity = 100

for key in ingredients.keys():
	print(key)