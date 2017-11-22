# Tock Too 
# TOCTTOU.py
# Created by Mauro J. Pappaterra on 20 of November 2017.
import sys

path = "file.txt"
mode = "a" # append mode

try:
    with open (path, mode) as file:
        print("\nFile open for writing. You can start writing the document below.\nWrite <done> in a new line to finish editing!\n")
        text = ""
        line = ""

        while (line != "<done>"):
            line = input()
            text += line + "\n"

        file.write(text[:-7])
        print("\nAll changes saved into " + path)
#except:
#    print ("\nError could not write into file " + path)
except IOError as e:
    print ("I/O error({0}): {1}".format(e.errno, e.strerror))
except:
    print ("Unexpected error:", sys.exc_info()[0])
    raise