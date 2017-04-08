
import os
import sys
import argparse

parser = None

def args_parse(argv):
    global parser

    parser = argparse.ArgumentParser()

    parser.add_argument("-module", action="store", default="")
    parser.add_argument("-classname", action="store",  default="")
    parser.add_argument("-classargs", action="store", default="")
    parser.add_argument("-function", action="store", default="")
    parser.add_argument("-funcargs",action="store", default="")

    return parser.parse_args()

if __name__ == "__main__":
    args = args_parse(sys.argv[1:])

    print args
