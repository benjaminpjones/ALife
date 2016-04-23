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

## Creating the dictionary and genome from the text file
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

global genome
genome = ""
for aacid in aacids:
    genome += inputDict[aacid]

## Creating the first organism
global translation
translation = outputDict
global codonLength
codonLength = 3


def getTree(position,container):
     codon = genome[position:position + codonLength]
     aacid = translation[codon]
     position += codonLength
     newContainer = []
     if aacid != "{}":
          for i in range(aacid.count("{}")):
               value,position = getTree(position,newContainer)
               newContainer.append(value)
          aacid = aacid.format(*newContainer)
     return aacid,position
def translate():
     output = ""
     codeList = []
     position = 0
     while position < len(genome):
          value,position = getTree(position,codeList)
          codeList.append(value)
     indent = 0
     for line in codeList:
          if line[-1] == ":":
               output += "\n"+" "*(5*indent)+line
               indent += 1
          elif line == "dedent":
               indent -= 1
          else:
               output += "\n"+" "*(5*indent)+line
     return output
def makeOffspring():
     locationID = "000"
     uniqueID = "aaaaaaaa"
     offspringName = locationID + "_" + uniqueID + ".py"
     offspring=open(offspringName,"w")
     offspring.write("global translation"+"\n")
     offspring.write("global genome"+"\n")
     offspring.write("translation = "+str(translation))
     offspring.write("\n"+"genome = '"+genome+"'")
     offspring.write(translate())
     offspring.close()

makeOffspring()
