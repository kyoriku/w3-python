# Loop through the nested 'myfamily' dictionary to print its content.

# Requirements
# The first, outer, loop should print keys 'child1', 'child2', ...
# The second, inner, loop should print the children's names and birth years.

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

# Loop through the dictionary to print the content
for child, info in myfamily.items():
  # Print the child label
  print(child)

  for key, value in info.items():
    # Print each child's key-value pair
    print(key + ":", value)