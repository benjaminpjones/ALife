global translation
global genome
translation = {'098': 'open', '099': 'w', '126': '######################tryToMove', '090': 'locationID', '091': 'uniqueID', '092': '8', '093': 'alphanumeric', '094': 'offspringName', '095': '_', '096': '.py', '097': 'offspring', '133': 'getAllOrganisms', '132': '###############################getAllOrganisms', '012': 'selfName', '013': 'world', '137': 'os.listdir({})', '015': '.5', '016': '3', '134': 'organisms', '018': '{}.split({})', '019': 'sys.argv', '139': 'findNearbyOrganisms', '138': '##############################findNearbyOrganisms', '025': '/', '121': 'organismName', '027': 'os.getcwd', '123': 'random.random', '124': 'newName', '020': '0', '023': '-{}', '127': 'tryToMove', '128': 'random.random()', '129': 'sys.argv[0]', '029': '#################################GetTree', '028': 'dedent', '010': 'metabolism', '011': 'codonLength', '131': '100', '130': 'random.uniform({},{})', '014': '{} = {}', '136': 'organism', '135': '[{}]', '017': '{}[{}]', '144': '{} or {}', '115': 'direction', '114': 'getNewPosition', '038': 'translation', '039': '{} += {}', '111': 'str({})', '110': 'num', '113': '#################################getNewPosition', '112': '{} - {}', '032': 'container', '033': 'codon', '030': 'getTree', '031': 'position', '119': '################################move', '037': 'aacid', '034': 'genome', '035': '{}:{}', '052': '{}.format(*{})', '108': '##################################intToString', '109': 'intToString', '148': 'organisms.remove("genomeGenerator.py")', '049': '{}.count({})', '048': 'range({})', '102': 'str', '103': '"', '045': '{}', '044': "'{}'", '043': '{} != {}', '042': 'if {}:', '041': '[]', '105': '##################################splitName', '077': 'getRandomString', '047': 'i', '058': 'codeList', '059': 'while {}:', '046': 'for {} in {}:', '054': '#####################################Translate', '055': 'translate', '056': 'output', '057': "''", '050': 'value', '051': '{}.append({})', '088': '#####################makeOffspring', '053': 'return {}', '101': 'write', '106': 'splitName', '107': 'name', '104': 'close', '040': 'newContainer', '061': 'len({})', '060': '{} < {}', '063': 'line', '062': 'indent', '065': '-1', '064': '{} == {}', '067': '\\n', '066': ':', '069': "' '", '068': '{}*{}', '022': '\\\\', '117': 'int({})', '116': '{} % {}', '076': '#######################getRandomString', '150': 'print organisms', '074': '{} -= {}', '075': 'else:', '072': '5', '073': 'elif {}:', '070': '{}+{}', '071': '({})', '078': 'length', '079': 'kind', '100': '{}.{}({})', '149': '200', '036': '{} + {}', '118': '1000', '146': '{} > {}', '147': '########################main', '089': 'makeOffspring', '145': 'abs({})', '142': 'nearby', '143': 'organismLocation', '140': 'self', '141': 'location', '083': 'numbers', '082': 'abcdefghijklmnopqrstuvwxyz', '081': 'chars', '080': 'letters', '087': 'random.choice({})', '086': 'string', '085': '0123456789abcdefghijklmnopqrstuvwxyz', '084': '0123456789', '003': 'random', '002': 'sys', '001': '{},{}', '000': 'import {}', '007': 'getTraits', '006': 'def {}({}):', '005': '#################################getTraits', '004': 'os', '009': 'global {}', '008': '', '120': 'move', '024': '1', '122': 'distance', '026': '{}({})', '021': '"{}"', '125': 'os.rename({},{})'}
genome = '000001002001003004005006007008009010009011009012009013014010015014011016014012017018017018017019020021022023024021025023024014013026027008028029006030001031032014033017034035031036031011014037017038033039031011014040041042043037044045046047048049037044045014001050031026030001031040051040050028014037052037040028053001037031028054006055008014056057014058041014031020059060031061034014001050031026030001031058051058050028014062020046063058042064017063065044066039056036044067068069070071068072062063039062024028073064063044028074062024028075039056036044067068069070071068072062063028028053056028076006077001078079042064079044080014081044082028073064079044083014081044084028075014081044085028014086057046047048078039086087081028053086028088006089008014090026077001016044083014091026077001092044093014094036090036044095036091044096014097026098001094044099100097101036044014038008026102038100097101036044067036044014034103036034044103100097101026055008100097104008028105006106107053018107021095028108006109001110078014110111110046047048112078061110014110036021020110028053110028113006114001031115053116071036117031115118028119006120001121122014001031091018121021095042060123015014115024028075014115023024028046047048122014031026109001026114001031115016014124036031036021095091125121124014121124028053121028126006127008042060128010014012017018017018129021022065021025065014122117068010130024131026053120001012122028028132006133013014134135008046136137013042064017136035023016008021096051134136028028053134028138006139001134001140122014141117017026106140020014142135008046136134042043136140014143117017026106136020042144060145112143141122146145112143141071112118122051142136028028028053142028147026007008026127008014134026133013148014142026139001134001012149150026089008'
import sys,random,os
#################################getTraits
def getTraits():
     global metabolism
     global codonLength
     global selfName
     global world
     metabolism = .5
     codonLength = 3
     selfName = sys.argv[0].split("\\")[-1].split("/")[-1]
     world = os.getcwd()
#################################GetTree
def getTree(position,container):
     codon = genome[position:position + codonLength]
     aacid = translation[codon]
     position += codonLength
     newContainer = []
     if aacid != '{}':
          for i in range(aacid.count('{}')):
               value,position = getTree(position,newContainer)
               newContainer.append(value)
          aacid = aacid.format(*newContainer)
     return aacid,position
#####################################Translate
def translate():
     output = ''
     codeList = []
     position = 0
     while position < len(genome):
          value,position = getTree(position,codeList)
          codeList.append(value)
     indent = 0
     for line in codeList:
          if line[-1] == ':':
               output += '\n' + ' '*(5*indent)+line
               indent += 1
          elif line == 'dedent':
               indent -= 1
          else:
               output += '\n' + ' '*(5*indent)+line
     return output
#######################getRandomString
def getRandomString(length,kind):
     if kind == 'letters':
          chars = 'abcdefghijklmnopqrstuvwxyz'
     elif kind == 'numbers':
          chars = '0123456789'
     else:
          chars = '0123456789abcdefghijklmnopqrstuvwxyz'
     string = ''
     for i in range(length):
          string += random.choice(chars)
     return string
#####################makeOffspring
def makeOffspring():
     locationID = getRandomString(3,'numbers')
     uniqueID = getRandomString(8,'alphanumeric')
     offspringName = locationID + '_' + uniqueID + '.py'
     offspring = open(offspringName,'w')
     offspring.write('translation = ' + str(translation))
     offspring.write('\n' + 'genome = "' + genome + '"')
     offspring.write(translate())
     offspring.close()
##################################splitName
def splitName(name):
     return name.split("_")
##################################intToString
def intToString(num,length):
     num = str(num)
     for i in range(length - len(num)):
          num = "0" + num
     return num
#################################getNewPosition
def getNewPosition(position,direction):
     return (int(position) + direction) % 1000
################################move
def move(organismName,distance):
     position,uniqueID = organismName.split("_")
     if random.random < .5:
          direction = 1
     else:
          direction = -1
     for i in range(distance):
          position = intToString(getNewPosition(position,direction),3)
          newName = position + "_" + uniqueID
          os.rename(organismName,newName)
          organismName = newName
     return organismName
######################tryToMove
def tryToMove():
     if random.random() < metabolism:
          selfName = sys.argv[0].split("\\")[-1].split("/")[-1]
          distance = int(metabolism*random.uniform(1,100))
          return move(selfName,distance)
###############################getAllOrganisms
def getAllOrganisms(world):
     organisms = []
     for organism in os.listdir(world):
          if organism[-3:] == ".py":
               organisms.append(organism)
     return organisms
##############################findNearbyOrganisms
def findNearbyOrganisms(organisms,self,distance):
     location = int(splitName(self)[0])
     nearby = []
     for organism in organisms:
          if organism != self:
               organismLocation = int(splitName(organism)[0])
               if abs(organismLocation - location) < distance or abs(organismLocation - location) > (1000 - distance):
                    nearby.append(organism)
     return nearby
########################main
getTraits()
tryToMove()
organisms = getAllOrganisms(world)
organisms.remove("genomeGenerator.py")
nearby = findNearbyOrganisms(organisms,selfName,200)
print organisms
makeOffspring()