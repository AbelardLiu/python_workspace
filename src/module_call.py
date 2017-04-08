
import os
import sys
import pydoc
import argparse

parser = None

def usage(info):
    print (info)

    parser.print_help()

    exit()

def args_parse(argv):
    global parser

    parser = argparse.ArgumentParser()

    parser.add_argument("-module", action="store", default="", help="module name")
    parser.add_argument("-classname", action="store",  default="", help="class name")
    parser.add_argument("-classargs", action="store", default="", help="class init args, splited with \',\'")
    parser.add_argument("-function", action="store", default="", help="function name")
    parser.add_argument("-funcargs",action="store", default="", help="function call args, splited with \',\'")

    return parser.parse_args()

def object_help(obj):
    temp_file = "help.tmp"

    f = file(temp_file, "w")
    sys.stdout = f
    pydoc.help(obj)
    f.close()
    sys.stdout = sys.__stdout__

    f = file(temp_file)
    content = f.read()
    print(content)
    f.close()

    return

if __name__ == "__main__":
    args = args_parse(sys.argv[1:])

    # 1 import module
    try:
        module = __import__(args.module, fromlist=True)
    except:
        usage("Import module error!")
    else:
        pass

    if args.classname:
        # call class function
        if hasattr(module, args.classname):
            classtype = getattr(module, args.classname)

            # initial class instance with init args
            instance = None
            if args.classargs:
                # some args for class __init__
                try:
                    cargs = args.classargs.split(",")
                    instance - classtype(*cargs)
                except:
                    usage("Initial class[%s] error with args[%s]!" % (args.classname, args.classargs))
                else:
                    pass
            else:
                # empty args for class __init__
                instance = classtype()

            if hasattr(instance, args.function):
                func = getattr(instance, args.function)

                try:
                    if args.funcargs:
                        # some function args passed
                        fargs = args.funcargs.split(",")
                        func(*fargs)
                    else:
                        # empty function args passed
                        func()
                except:
                    usage("call function[%s.%s.%s] with args [%s] error!" % (args.module, args.classname, args.function, args.funcargs))
                else:
                    pass    
            else:
                usage("Not specify function!")
        else:
            # not find claas in module
            usage("Cannot find class[%s] in module[%s]!" % (args.classname, args.module))
    else:
        # call module function directly
        if hasattr(module, args.function):
            # find function in module
            func = getattr(module, args.function)

            try:
                if args.funcargs:
                    # some function args passed
                    fargs = args.funcargs.split(",")
                    func(*fargs)
                else:
                    # empty function args passwd
                    func()
            except:
                usage("call function[%s.%s] with args[%s] error!" % (args.module, args.function, args.funcargs))
            else:
                pass
        else:
            # not find function in module
            usage("Cannot find function[%s] in module[%s]!" % (args.function, args.module))
