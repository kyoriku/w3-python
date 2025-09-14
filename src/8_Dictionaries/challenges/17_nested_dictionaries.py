# Write a program that looks up and prints the name of 'child2' in the nested 'myfamily' dictionary.

# Requirements
# The print of child2's name should be 'Tobias'.

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

# Use the dictionary to print the name of child2
print(myfamily["child2"]["name"])