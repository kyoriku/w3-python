# Python Install
# Many PCs and Macs will have python already installed.

# To check if you have python installed on a Windows PC, search in the start bar for Python or run the following on the Command Line (cmd.exe):

# C:\Users\Your Name>python --version

# To check if you have python installed on a Linux or Mac, then on linux open the command line or on Mac open the Terminal and type:

# python --version

# If you find that you do not have Python installed on your computer, then you can download it for free from the following website: https://www.python.org/

# --------------------------------

# Python Quickstart
# Python is an interpreted programming language, this means that as a developer you write Python (.py) files in a text editor and then put those files into the python interpreter to be executed.

# Let's write our first Python file, called hello.py, which can be done in any text editor:

# hello.py:

# print("Hello, World!")

# Simple as that. Save your file. Open your command line, navigate to the directory where you saved your file, and run:

# C:\Users\Your Name>python hello.py (Windows)
# or
# $ python3 hello.py (Linux or Mac)

# The output should be:

# Hello, World!

# --------------------------------

# Python Version
# To check the Python version of the editor, you can find it by importing the sys module.

# Check the Python version of the editor:
import sys

print(sys.version)