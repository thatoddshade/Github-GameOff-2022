import random

my_dict = {
    "first_thing": "one",
    "second_thing": "two"
}

my_array = [
    "something",
    "another_thing"
]

my_random_thing = random.choice(list(my_dict.keys()))
print(my_random_thing)
