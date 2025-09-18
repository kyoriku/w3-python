# The replace() method replaces a specified phrase with another specified phrase.

# Note: All occurrences of the specified phrase will be replaced, if nothing else is specified.

# Replace the word "bananas":
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

# Replace all occurrence of the word "one":
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)

# Replace the two first occurrence of the word "one":
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)