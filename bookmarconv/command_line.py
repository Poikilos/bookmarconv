#!/usr/bin/python

import os, sys
import json

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

def customDie(msg):
    print("")
    if msg is not None:
        print("ERROR:")
        print("'" + msg + "' is not an existing file.")
    else:
        print("Unknown error.")
    print("")
    print("")
    exit(1)

def usage():
    print("python bookmarconv.py existingfile.json newfile.json")
    print("* output format is always: xBrowserSync")

def checkFirefoxBookmarkTree(parent):
    title = parent.get('title')
    guid = parent.get('guid')
    if (title is None):
        print("guid "+guid+": Missing title")
    elif (len(title) == 0):
        print("guid "+guid+": Title is zero length")
    elif (len(title.strip()) == 0):
        print("guid "+guid+": Title contains only whitespace")
    children = parent.get('children')
    if children is not None:
        for child in children:
            checkFirefoxBookmarkTree(child)


def main(argv):
    if len(sys.argv) > 3:
        usage()
        customDie("Input '" + str(sys.argv) + "' has too many arguments.")
    # elif len(sys.argv) < 3:
        # usage()
        # customDie("Input '" + str(sys.argv) + "' has too few arguments.")
    inPath = sys.argv[1]
    if not os.path.isfile(inPath):
        usage()
        customDie("'" + inPath + "' is not an existing file.")
    print("Reading JSON from "+inPath+"...")
    # inputObj = None
    inFile = open(inPath)
    if inFile is None:
        customDie("Cannot read " + inPath)
    inputObj = json.load(inFile)
    inFile.close()
    # inputObj = json.loads(inPath)
    checkFirefoxBookmarkTree(inputObj)
    # print("Writing json...")
    # with open(sys.argv[2], "w") as write_file:
    #     json.dump(outputObj, write_file)

if __name__ == "__main__":
   main(sys.argv)  # sys.argv[1:]
