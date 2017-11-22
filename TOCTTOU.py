# Tock Too 
# TOCTTOU.py
# Created by Mauro J. Pappaterra on 20 of November 2017.

from pathlib import Path # import Path module from library

path = "file.txt"
mode = "w" # write mode

with open (path, mode) as file:

    print("File open for writing. You can start writing the document below. Write <done> to finish editing")
    text = ""
    line = ""

    while (line != "<done>"):
        line = input()
        text += line + "\n"

    file.write(text[:-8])






