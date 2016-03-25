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
