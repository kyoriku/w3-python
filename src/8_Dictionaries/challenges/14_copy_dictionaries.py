# Write Python code that creates an actual copy of the given dictionary (not just a reference) and assign it to a new variable 'mydict'.

# Requirements
# Define the variable 'mydict' and assign it a copy of 'thisdict' using either the copy() or the dict() method.
# Ensure 'mydict' is a copy of 'thisdict', and a different object.

# Define the dictionary and copy it
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Copy the dictionary into mydict
mydict = thisdict.copy()