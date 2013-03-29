#!/usr/bin/python
import sys, getopt, time

def follow(f):
    f.seek(0,2)
    try:
        while True:
             l = f.readline()
             if not l:
                 time.sleep(0.1)
                 continue
             yield l
    except:
        pass

def tail(file_path):
    input_file = open(file_path)
    lines = follow(input_file)
    for l in lines:
        print l

def main(argv):
    inputfile = None
    try:
        opts, args = getopt.getopt(argv, "hi:", ["inputfile="])
    except getopt.GetoptError:
        print 'error!'
        print 'pytail.py -i <inputfile>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print 'pytail.py -i <inputfile>'
            sys.exit()
        elif opt in ("i", "--inputfile"):
            inputfile = arg

    if inputfile == None:
        print 'pytail.py -i <inputfile>'
        sys.exit()

    tail(inputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
