global translation
global genome
translation = {'098': '_', '099': '.py', '023': '"{}"', '090': 'random.choice({})', '091': '#####################makeOffspring', '092': 'makeOffspring', '093': 'locationID', '094': 'uniqueID', '095': '8', '096': 'alphanumeric', '097': 'offspringName', '133': '100', '132': 'random.uniform({},{})', '131': 'random.random()', '130': 'tryToMove', '014': 'world', '136': 'organisms', '135': 'getAllOrganisms', '134': '###############################getAllOrganisms', '018': '3', '019': '{}[{}]', '139': 'os.listdir({})', '138': 'organism', '025': '-{}', '121': '1000', '122': '################################move', '123': 'move', '124': 'organismName', '125': 'distance', '126': 'random.random', '127': 'newName', '128': 'os.rename({},{})', '129': '######################tryToMove', '029': 'os.getcwd', '028': '{}({})', '010': 'global {}', '011': 'metabolism', '012': 'codonLength', '013': 'selfName', '137': '[{}]', '015': 'sightDistance', '016': '{} = {}', '084': 'chars', '017': '.5', '144': 'organismLocation', '115': '{} - {}', '114': 'str({})', '038': '{}:{}', '039': '{} + {}', '111': '##################################intToString', '110': 'name', '113': 'num', '112': 'intToString', '032': '#################################GetTree', '033': 'getTree', '030': '30', '031': 'dedent', '036': 'codon', '118': 'direction', '034': 'position', '035': 'container', '053': 'value', '108': '##################################splitName', '109': 'splitName', '148': '########################main', '049': 'for {} in {}:', '048': '{}', '102': 'w', '046': '{} != {}', '045': 'if {}:', '044': '[]', '106': '"', '107': 'close', '041': 'translation', '040': 'aacid', '076': 'elif {}:', '150': 'raw_input({})', '153': 'except:', '047': "'{}'", '075': '5', '058': 'translate', '059': 'output', '103': '{}.{}({})', '054': '{}.append({})', '055': '{}.format(*{})', '056': 'return {}', '057': '#####################################Translate', '050': 'i', '051': 'range({})', '052': '{}.count({})', '073': '{}+{}', '101': 'open', '157': '{}.get({})', '043': 'newContainer', '156': 'dict', '145': '{} or {}', '042': '{} += {}', '104': 'write', '105': 'str', '061': 'codeList', '060': "''", '063': '{} < {}', '062': 'while {}:', '065': 'indent', '064': 'len({})', '067': '{} == {}', '066': 'line', '069': ':', '068': '-1', '160': 'organisms.remove("genomeGenerator.py")', '022': '0', '117': 'getNewPosition', '116': '#################################getNewPosition', '151': 'try:', '077': '{} -= {}', '074': '({})', '152': 'json.loads({})', '155': 'type({})', '154': 'dict({})', '070': '\\n', '071': '{}*{}', '159': 'None', '158': 'acting_program', '078': 'else:', '079': '#######################getRandomString', '100': 'offspring', '119': '{} % {}', '072': "' '", '037': 'genome', '146': 'abs({})', '147': '{} > {}', '089': 'string', '088': '0123456789abcdefghijklmnopqrstuvwxyz', '142': 'location', '143': 'nearby', '140': '##############################findNearbyOrganisms', '141': 'findNearbyOrganisms', '083': 'letters', '082': 'kind', '081': 'length', '080': 'getRandomString', '087': '0123456789', '086': 'numbers', '085': 'abcdefghijklmnopqrstuvwxyz', '149': 'startConditions', '003': 'random', '002': 'sys', '001': '{},{}', '000': 'import {}', '007': 'def {}({}):', '006': '#################################getTraits', '005': 'json', '004': 'os', '009': '', '008': 'getTraits', '120': 'int({})', '024': '\\\\', '027': '/', '026': '1', '021': 'sys.argv', '020': '{}.split({})'}
genome = '000001002001003001004005006007008009010011010012010013010014010015016011017016012018016013019020019020019021022023024025026023027025026016014028029009016015030031032007033001034035016036019037038034039034012016040019041036042034012016043044045046040047048049050051052040047048016001053034028033001034043054043053031016040055040043031056001040034031057007058009016059060016061044016034022062063034064037016001053034028033001034061054061053031016065022049066061045067019066068047069042059039047070071072073074071075065066042065026031076067066047031077065026031078042059039047070071072073074071075065066031031056059031079007080001081082045067082047083016084047085031076067082047086016084047087031078016084047088031016089060049050051081042089090084031056089031091007092009016093028080001018047086016094028080001095047096016097039093039047098039094047099016100028101001097047102103100104039047016041009028105041103100104039047070039047016037106039037047106103100104028058009103100107009031108007109110056020110023098031111007112001113081016113114113049050051115081064113016113039023022113031056113031116007117001034118056119074039120034118121031122007123001124125016001034094020124023098045063126017016118026031078016118025026031049050051125016034028112001028117001034118018016127039034039023098094128124127016124127031056124031129007130009010013045063131011016125120071011132026133028123001013125031031134007135014016136137009049138139014045067019138038025018009023099054136138031031056136031140007141136016142120019028109013022016143137009049138136045046138013016144120019028109138022045145063146115144142015147146115144142074115121015054143138031031031056143031148016149150009151016149152149031153016149154009031045046155149156016149154009031045067157149023158159028008009028130009016136028135014160016143028141136028092009'
import sys,random,os,json
#################################getTraits
def getTraits():
     global metabolism
     global codonLength
     global selfName
     global world
     global sightDistance
     metabolism = .5
     codonLength = 3
     selfName = sys.argv[0].split("\\")[-1].split("/")[-1]
     world = os.getcwd()
     sightDistance = 30
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
     global selfName
     if random.random() < metabolism:
          distance = int(metabolism*random.uniform(1,100))
          move(selfName,distance)
###############################getAllOrganisms
def getAllOrganisms(world):
     organisms = []
     for organism in os.listdir(world):
          if organism[-3:] == ".py":
               organisms.append(organism)
     return organisms
##############################findNearbyOrganisms
def findNearbyOrganisms(organisms):
     location = int(splitName(selfName)[0])
     nearby = []
     for organism in organisms:
          if organism != selfName:
               organismLocation = int(splitName(organism)[0])
               if abs(organismLocation - location) < sightDistance or abs(organismLocation - location) > (1000 - sightDistance):
                    nearby.append(organism)
     return nearby
########################main
startConditions = raw_input()
try:
     startConditions = json.loads(startConditions)
except:
     startConditions = dict()
if type(startConditions) != dict:
     startConditions = dict()
if startConditions.get("acting_program") == None:
     getTraits()
     tryToMove()
     organisms = getAllOrganisms(world)
     organisms.remove("genomeGenerator.py")
     nearby = findNearbyOrganisms(organisms)
     makeOffspring()