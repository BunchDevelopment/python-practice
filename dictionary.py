import requests

r = requests.get('https://swapi.dev/api/people/')

results = r.json()["results"][0]

# for key in results:
#     print("The key of the value:", key, "matches up with this value!", results[key])

sorted_results = {}

for i in sorted (results) :
    sorted_results[i] = results[i]

# print(sorted_results)

my_keys = ['color', 'number', 'name']
my_values = ['purple', 3, 'Brandon']
my_dict = {}

for i in range(len(my_keys)):
    my_dict[my_keys[i]] = my_values[i]

my_new_dictionary = dict(zip(my_keys, my_values))
print(my_dict)
print(my_new_dictionary)