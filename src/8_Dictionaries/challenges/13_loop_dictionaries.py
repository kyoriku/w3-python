# Use a for-loop to iterate over the dictionary and print each value on a separate line.

# Requirements
# Loop through the dictionary, printing 3 lines as the result: 'Ford', 'Mustang', and '1964'.
# Use a for-loop to go through the dictionary.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Loop through the dictionary to print the values
for x in thisdict.values():
  print(x)