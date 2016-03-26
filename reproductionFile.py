translation = {'010': 'container', '011': 'translation', '012': '{} = {}', '013': 'codon', '014': '{}[{}]', '015': '{}:{}', '016': '{} + {}', '017': 'aacid', '018': '{} += {}', '019': 'newContainer', '025': 'for {} in {}:', '024': '{}', '027': 'range({})', '026': 'i', '021': 'if {}:', '020': '[]', '023': "'{}'", '022': '{} != {}', '029': 'value', '028': '{}.count({})', '038': "''", '039': 'codeList', '032': 'dedent', '033': '{}.format(*{})', '030': '{}({})', '031': '{}.append({})', '036': 'translate', '037': 'output', '034': 'return {}', '035': '#####################################Translate', '049': '\\n', '048': ':', '047': '-1', '046': '{} == {}', '045': 'line', '044': 'indent', '043': 'len({})', '042': '{} < {}', '041': 'while {}:', '040': '0', '058': 'else:', '059': '#######################getRandomString', '054': '5', '055': '1', '056': 'elif {}:', '057': '{} -= {}', '050': '{}*{}', '051': "' '", '052': '{}+{}', '053': '({})', '061': 'length', '060': 'getRandomString', '063': 'letters', '062': 'kind', '065': 'abcdefghijklmnopqrstuvwxyz', '064': 'chars', '067': '0123456789', '066': 'numbers', '069': 'string', '068': '0123456789abcdefghijklmnopqrstuvwxyz', '076': '8', '077': 'alphanumeric', '074': 'locationID', '075': 'uniqueID', '072': 'makeOffspring', '073': '3', '070': 'random.choice({})', '071': '#####################makeOffspring', '078': 'offspringName', '079': '_', '089': 'close', '088': '"', '083': 'w', '082': 'open', '081': 'offspring', '080': '.py', '087': 'str', '086': '', '085': 'write', '084': '{}.{}({})', '003': 'random', '002': 'sys', '001': '{},{}', '000': 'import {}', '007': 'genome', '006': 'getTree', '005': 'def {}({}):', '004': '#################################GetTree', '009': 'position', '008': 'codonLength'}
genome = '000001002003004005006001007001008001009001010011012013014007015009016009008012017014011013018009008012019020021022017023024025026027028017023024012001029009030006001007001008001009001019011031019029032012017033017019032034001017009032035005036001007001008011012037038012039020012009040041042009043007012001029009030006001007001008001009001039011031039029032012044040025045039021046014045047023048018037016023049050051052053050054044045018044055032056046045023032057044055032058018037016023049050051052053050054044045032032034037032059005060001061062021046062023063012064023065032056046062023066012064023067032058012064023068032012069038025026027061018069070064032034069032071005072001007011012008073012074030060001073023066012075030060001076023077012078016074016023079016075023080012081030082001078023083084081085016023012011086030087011084081085016023049016023012007088016007023088084081085030036001007001008011084081089086032030072001007011'
import sys,random
def getTree(genome,codonLength,position,container,translation):
     codon = genome[position:position + codonLength]
     aacid = translation[codon]
     position += codonLength
     newContainer = []
     if aacid != "{}":
          for i in range(aacid.count("{}")):
               value,position = getTree(genome,codonLength,position,newContainer,translation)
               newContainer.append(value)
          aacid = aacid.format(*newContainer)
     return aacid,position
def translate(genome,codonLength,translation):
     output = ""
     codeList = []
     position = 0
     while position < len(genome):
          value,position = getTree(genome,codonLength,position,codeList,translation)
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
def getRandomString(length,kind):
     if kind == "letters":
          chars = "abcdefghijklmnopqrstuvwxyz"
     elif kind == "numbers":
          chars = "0123456789"
     else:
          chars = "0123456789abcdefghijklmnopqrstuvwxyz"
     string = ""
     for i in range(length):
          string += random.choice(chars)
     return string
def makeOffspring(genome,translation):
     codonLength = 3
     locationID = getRandomString(3,"numbers")
     uniqueID = getRandomString(8,"alphanumeric")
     offspringName = locationID + "_" + uniqueID + ".py"
     offspring=open(offspringName,"w")
     offspring.write("translation = "+str(translation))
     offspring.write("\n"+"genome = '"+genome+"'")
     offspring.write(translate(genome,codonLength,translation))
     offspring.close()


makeOffspring(genome,translation)


