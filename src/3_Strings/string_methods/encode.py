# The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.

# UTF-8 encode the string:
txt = "My name is Ståle"
x = txt.encode()
print(x)

# These examples uses ascii encoding, and a character that cannot be encoded, showing the result with different errors:
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))