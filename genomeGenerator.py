"""

takes lines of text and converts them into a genome and translation table,
which are then converted into code.
{} indicates that the next line should be inserted into the current code block.

For instance:

for {} in {}:
x
range({})
10
print {}
{},{}
"{}"
Num:
x

would translate to (with codon length 3):
translation = {'001':'for {} in {}', '002':'x', '003':'range({})', '004':'10',
    '005':'print {}', '006':'{},{}', '007':'"{}"', '008':'Num:', '009':'x'}

genome = '001002003004005006007008009'

The reproduction framework would then translate the genome to:

for x in range(10):
    print "Num:",x

When converting a genome into code, the indentation level is automatically
increased whenever a line ends with a colon, but dedentation must be
manually specified by a line 'dedent'

"""

inputDict = {}

outputDict = {}

dictCount = 0
textFile = open("genomeAST.txt", "r")
aacids = textFile.readlines()
for i in range(len(aacids)):
    aacids[i] = aacids[i].strip()
    if aacids[i] not in inputDict:
        value = str(dictCount)
        value = (3-len(value))*"0"+value
        inputDict[aacids[i]] = value
        dictCount += 1
for item in inputDict:
    outputDict[inputDict[item]] = item

print "translation =",outputDict

genome = ""
for aacid in aacids:
    genome += inputDict[aacid]

print "genome = '"+genome+"'"
