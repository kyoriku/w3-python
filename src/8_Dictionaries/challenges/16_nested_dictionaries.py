# Create a dictionary myfamily with a specific nested structure.

# The dictionary should contain information about three children: child1, child2, and child3. Each child should have a nested dictionary with keys name and year, storing the child's name and birth year, respectively.

# Requirements
# The `myfamily` variable should be a dictionary.
# The `child1` dictionary should have the keys `name` and `year`, with values `Emil` and `2004` respectively.
# The `child2` dictionary should have the keys `name` and `year`, with values `Tobias` and `2007` respectively.
# The `child3` dictionary should have the keys `name` and `year`, with values `Linus` and `2011` respectively.

# Create the nested dictionary `myfamily` here
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
