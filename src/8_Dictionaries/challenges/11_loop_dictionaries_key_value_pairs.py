# Loop through the dictionary, printing all key-value pairs, each pair on a new line.

# Requirements
# The program should print the key-value pairs from the dictionary.
# Use a for-loop to go through the dictionary.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Write your loop here to print each key-value pair
for x, y in thisdict.items():
  print(x, y)