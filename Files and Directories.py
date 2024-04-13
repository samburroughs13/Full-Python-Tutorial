from pathlib import Path

# Absolute path
# C:\Program Files\Microsoft
# Relative path

# Return True or False depending on whether or not the file/directory exists
# path = Path("ecommerce")
# print(path.exists())

# Make a directory
# path = Path("emails")
# print(path.mkdir())

# Delete a directory
# path = Path("emails")
# print(path.rmdir())

path = Path()
# all files
# print(path.glob('*'))
# all files within current directory
# print(path.glob('*.*'))
for file in path.glob('*.py'):
    print(file)