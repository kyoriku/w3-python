# Create the Python update_key_if_exists_value function which accepts the parameters input_dict, keyand new_value that does the following:
# Check if key exists in input_dict and only update the value for that key to value if the key exists
# Return the dictionary

# Requirements
# Should update the value of key "name" to "Jane" in my_dict
# Should add new key "surname" with value "Doe" to my_dict

my_dict = {
    'name': 'John',
    'age': 25
}

# Update the key "name" with the value "Jane" in my_dict
my_dict['name'] = 'Jane'  
# Add a key "surname" with the value "Doe" to my_dict
my_dict['surname'] = 'Doe'