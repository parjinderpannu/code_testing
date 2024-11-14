import random

a = []
num_of_element = 10
min_element=1
max_element=100
a = random.sample(range(min_element,max_element+1),num_of_element)
print(f"Output of Array = {a}")