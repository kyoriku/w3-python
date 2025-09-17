# Built-in Data Types
# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:

# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Type: bool
# Binary Types: bytes, bytearray, memoryview
# None Type: NoneType

# Getting the Data Type
# You can get the data type of any object by using the type() function:

# String
x = "Hello World"
print(x, type(x))

# Int
x = 20
print(x, type(x))

# Float
x = 20.5
print(x, type(x))

# Complex
x = 1j
print(x, type(x))

# List
x = ["apple", "banana", "cherry"]
print(x, type(x))

# Tuple
x = ("apple", "banana", "cherry")
print(x, type(x))

# Range
x = range(6)
print(x, type(x))

# Dictionary
x = {"name": "John", "age": 36}
print(x, type(x))

# Set
x = {"apple", "banana", "cherry"}
print(x, type(x))

# Frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x, type(x))

# Boolean
x = True
print(x, type(x))

# Bytes
x = b"Hello"
print(x, type(x))

# Bytearray
x = bytearray(5)
print(x, type(x))

# Memoryview
x = memoryview(bytes(5))
print(x, type(x))

# NoneType
x = None
print(x, type(x))

# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:
x = str(5)
print(x, type(x))

x = int(20)
print(x, type(x))

x = float(20.5)
print(x, type(x))

x = complex(1j)
print(x, type(x))

x = list(("apple", "banana", "cherry"))
print(x, type(x))

x = tuple(("apple", "banana", "cherry"))
print(x, type(x))

x = range(6)
print(x, type(x))

x = dict(name="John", age=36)
print(x, type(x))

x = set(("apple", "banana", "cherry"))
print(x, type(x))

x = frozenset(("apple", "banana", "cherry"))
print(x, type(x))

x = bool(5)
print(x, type(x))

x = bytes(8)
print(x, type(x))

x = bytearray(5)
print(x, type(x))

x = memoryview(bytes(5))
print(x, type(x))