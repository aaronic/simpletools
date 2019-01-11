import os, re
import argparse

'''
add_argument
read arguments from command line
add_argument(name or flag...[,action][,nargs][,const][,default][,type],[choices][,required][,help][,metaver][,dest])
nargs: arguments after option
nargs='?' -> only accept one or no arguments
nargs='*' -> multiple arguments
nargs='+' -> multiple arguments but not accept no argument
default -> when there is no arguments, will get from default
const -> option appear but no arguments for this option, it will get from const
metavar -> use for the help info, but can't be used when action is used
required -> this option have to be exist

'''

finder = argparse.ArgumentParser(description='find string in the files')
finder.add_argument('-r', dest='regex', action='store', help='regular expression')
finder.add_argument('-o', dest='output', action='store', help='output file')
finder.add_argument('-f', dest='filein', action='store', help='input file')
args = finder.parse_args()
print('regular expression: {}'.format(args.regex))
print('output filename: {}'.format(args.output))
print('input filename: {}'.format(args.filein))

def check_file(filein, fo, regex):
    with open(filein) as fi:
        for line in fi:
            data = line.strip()
            if re.match(args.regex, data):
                if fo is None:
                    print('{}: {}'.format(filein, data))
                else:
                    fo.write('{}: {}\n'.format(filein,data))

fo = None
if args.output:
    fo = open(args.output, mode='w')
if args.filein:
    try:
        check_file(args.filein, fo, args.regex)
    except Exception as err:
        print(str(err))    
else: 
    for dir_, folder_, files_ in os.walk(os.getcwd()):
        for file_ in files_:
            if file_ != args.output:
                file_path = os.path.join(dir_, file_)
                print(file_path)
                try:
                    check_file(file_path, fo, args.regex)
                except Exception as err:
                    print(str(err))
if fo:
    fo.close()
