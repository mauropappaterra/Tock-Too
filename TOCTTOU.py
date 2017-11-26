# Tock Too 
# TOCTTOU.py
# Created by Mauro J. Pappaterra on 20 of November 2017.
import sys

path = "new.txt"
mode = "a" # append mode

try:
    with open (path, mode) as file:
        print("\nFile " + path + " opened for writing. You can now start writing on this file."
              "\nTo finish editing write <done> on a new line, then press enter.\n")
        text = ""
        line = ""

        while (line != "<done>"):
            line = input()
            text += line + "\n"

        file.write(text[:-7])
        print("\nAll changes saved into " + path)

except IOError as e:
    print("\nError could not write into file " + path +
          "\nI/O error({0}): {1}".format(e.errno, e.strerror))
except:
    print ("\nError could not write into file " + path +
           "\nUnexpected error:", sys.exc_info()[0])
    raise