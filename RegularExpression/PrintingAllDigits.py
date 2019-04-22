#Write a programa to accept a file name from user and print all digits from it.

#!/usr/bin/python
import re

def PrintDigits(file_name):
    fd = open(file_name)
    data = fd.read()
    regex_obj = re.compile(r"\d+")
    for match in regex_obj.finditer(data):
        print(match)

def main():
    file_name = input("enter filename:")
    PrintDigits(file_name)

if __name__ == '__main__':
    main()
