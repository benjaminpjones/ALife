import sys
import ast
from ast2txt import ast2txt

def pyToTxt(filename):
    if filename[-3:] == '.py':
        filename = filename[:-3] + '.txt'
    return filename

# get a filename
filename = None
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = raw_input('Please enter the filename of a python script: ')

f = None
while (True):
    try:
        f = open(filename)
    except:
        print 'Error opening file', filename
        filename = raw_input('Please enter another filename: ')
    else:
        break

filetext = f.read()
tree = ast.parse(filetext)

astfilename = pyToTxt(filename)
astfile = open(astfilename, 'w')

ast_text = ast2txt(tree)
astfile.write(ast_text)
