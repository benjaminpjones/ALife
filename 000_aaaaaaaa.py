global translation
global genome
translation = {'098': 'offspring', '099': 'open', '126': 'os.rename({},{})', '090': 'makeOffspring', '091': 'locationID', '092': 'uniqueID', '093': '8', '094': 'alphanumeric', '095': 'offspringName', '096': '_', '097': '.py', '133': 'getAllOrganisms', '132': '###############################getAllOrganisms', '131': '100', '013': 'selfName', '014': 'world', '015': '{} = {}', '135': '[{}]', '134': 'organisms', '018': '{}[{}]', '019': '{}.split({})', '139': 'findNearbyOrganisms', '138': '##############################findNearbyOrganisms', '120': '################################move', '121': 'move', '027': '{}({})', '026': '/', '021': '0', '125': 'newName', '023': '\\\\', '127': '######################tryToMove', '128': 'tryToMove', '129': 'random.random()', '029': 'dedent', '028': 'os.getcwd', '010': 'global {}', '011': 'metabolism', '012': 'codonLength', '130': 'random.uniform({},{})', '137': 'os.listdir({})', '136': 'organism', '016': '.5', '017': '3', '144': '{} or {}', '115': 'getNewPosition', '114': '#################################getNewPosition', '117': '{} % {}', '039': 'translation', '111': 'num', '110': 'intToString', '113': '{} - {}', '112': 'str({})', '032': 'position', '033': 'container', '030': '#################################GetTree', '031': 'getTree', '036': '{}:{}', '037': '{} + {}', '034': 'codon', '035': 'genome', '108': 'name', '109': '##################################intToString', '085': '0123456789', '049': 'range({})', '048': 'i', '047': 'for {} in {}:', '103': 'str', '100': 'w', '084': 'numbers', '043': 'if {}:', '042': '[]', '104': '"', '040': '{} += {}', '151': 'json.loads({})', '077': '#######################getRandomString', '074': 'elif {}:', '102': 'write', '152': 'except:', '058': "''", '059': 'codeList', '046': '{}', '054': 'return {}', '055': '#####################################Translate', '056': 'translate', '057': 'output', '050': '{}.count({})', '051': 'value', '052': '{}.append({})', '053': '{}.format(*{})', '044': '{} != {}', '070': "' '", '106': '##################################splitName', '073': '5', '156': '{}.get({})', '107': 'splitName', '159': 'organisms.remove("genomeGenerator.py")', '041': 'newContainer', '105': 'close', '061': '{} < {}', '060': 'while {}:', '063': 'indent', '062': 'len({})', '065': '{} == {}', '064': 'line', '067': ':', '066': '-1', '069': '{}*{}', '068': '\\n', '160': '30', '022': '"{}"', '038': 'aacid', '116': 'direction', '076': 'else:', '150': 'try:', '153': 'dict({})', '075': '{} -= {}', '155': 'dict', '154': 'type({})', '157': 'acting_program', '071': '{}+{}', '045': "'{}'", '158': 'None', '078': 'getRandomString', '079': 'length', '088': 'random.choice({})', '119': '1000', '072': '({})', '118': 'int({})', '101': '{}.{}({})', '146': '{} > {}', '147': '########################main', '089': '#####################makeOffspring', '145': 'abs({})', '142': 'nearby', '143': 'organismLocation', '140': 'self', '141': 'location', '083': 'abcdefghijklmnopqrstuvwxyz', '082': 'chars', '081': 'letters', '080': 'kind', '087': 'string', '086': '0123456789abcdefghijklmnopqrstuvwxyz', '148': 'startConditions', '149': 'raw_input({})', '003': 'random', '002': 'sys', '001': '{},{}', '000': 'import {}', '007': 'def {}({}):', '006': '#################################getTraits', '005': 'json', '004': 'os', '009': '', '008': 'getTraits', '025': '1', '024': '-{}', '122': 'organismName', '123': 'distance', '124': 'random.random', '020': 'sys.argv'}
genome = '000001002001003001004005006007008009010011010012010013010014015011016015012017015013018019018019018020021022023024025022026024025015014027028009029030007031001032033015034018035036032037032012015038018039034040032012015041042043044038045046047048049050038045046015001051032027031001032041052041051029015038053038041029054001038032029055007056009015057058015059042015032021060061032062035015001051032027031001032059052059051029015063021047064059043065018064066045067040057037045068069070071072069073063064040063025029074065064045029075063025029076040057037045068069070071072069073063064029029054057029077007078001079080043065080045081015082045083029074065080045084015082045085029076015082045086029015087058047048049079040087088082029054087029089007090009015091027078001017045084015092027078001093045094015095037091037045096037092045097015098027099001095045100101098102037045015039009027103039101098102037045068037045015035104037035045104101098102027056009101098105009029106007107108054019108022096029109007110001111079015111112111047048049113079062111015111037022021111029054111029114007115001032116054117072037118032116119029120007121001122123015001032092019122022096043061124016015116025029076015116024025029047048049123015032027110001027115001032116017015125037032037022096092126122125015122125029054122029127007128009010013043061129011015123118069011130025131027121001013123029029132007133014015134135009047136137014043065018136036024017009022097052134136029029054134029138007139001134001140123015141118018027107140021015142135009047136134043044136140015143118018027107136021043144061145113143141123146145113143141072113119123052142136029029029054142029147015148149009150015148151148029152015148153009029043044154148155015148153009029043065156148022157158027008009027128009015134027133014159015142027139001134001013160027090009'
import sys,random,os,json
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
     nearby = findNearbyOrganisms(organisms,selfName,30)
     makeOffspring()
