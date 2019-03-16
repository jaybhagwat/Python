#WAP to accpet a foldername from user and create a zip file out of it.(hint= import shutil)

from shutil import make_archive
import os

input=eval(input("Enter the file name"))
make_archive(input, 'gztar')

#make_archive is a method from shtuil library in which first argument is input file name with destination and 2nd argument is fromat of zip.
