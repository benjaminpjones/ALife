translation = {'076': 'open', '077': 'w', '074': '.py', '075': 'offspring', '072': 'offspringName', '005': 'def {}({}):', '070': 'uniqueID', '071': '8', '022': '{} != {}', '004': '#################################GetTree', '078': '{}.{}({})', '079': 'write', '010': 'container', '054': '5', '012': '{} = {}', '039': 'codeList', '058': 'else:', '015': '{}:{}', '016': '{} + {}', '019': 'newContainer', '018': '{} += {}', '055': '1', '030': '{}({})', '057': '{} -= {}', '036': 'translate', '037': 'output', '001': '{},{}', '035': '#####################################Translate', '049': '\\n', '056': 'elif {}:', '044': 'indent', '029': 'value', '073': '_', '051': "' '", '083': 'close', '011': 'translation', '000': 'import {}', '052': '{}+{}', '082': '"', '032': 'dedent', '053': '({})', '061': 'length', '060': 'getRandomString', '063': 'abcdefghijklmnopqrstuvwxyz', '062': 'chars', '065': 'random.choice({})', '064': 'string', '067': 'makeOffspring', '066': '#####################makeOffspring', '069': 'locationID', '068': '3', '081': 'str', '080': '', '047': '-1', '009': 'position', '050': '{}*{}', '003': 'random', '024': '{}', '027': 'range({})', '026': 'i', '021': 'if {}:', '020': '[]', '023': "'{}'", '048': ':', '033': '{}.format(*{})', '046': '{} == {}', '045': 'line', '008': 'codonLength', '043': 'len({})', '028': '{}.count({})', '041': 'while {}:', '040': '0', '025': 'for {} in {}:', '042': '{} < {}', '031': '{}.append({})', '002': 'sys', '059': '#######################getRandomString', '038': "''", '034': 'return {}', '013': 'codon', '014': '{}[{}]', '017': 'aacid', '007': 'genome', '006': 'getTree'}
genome = '000001002003004005006001007001008001009001010011012013014007015009016009008012017014011013018009008012019020021022017023024025026027028017023024012001029009030006001007001008001009001019011031019029032012017033017019032034001017009032035005036001007001008011012037038012039020012009040041042009043007012001029009030006001007001008001009001039011031039029032012044040025045039021046014045047023048018037016023049050051052053050054044045018044055032056046045023032057044055032058018037016023049050051052053050054044045032032034037032059005060061012062023063012064038025026027061018064065062032034064032066005067001007011012008068012069030060068012070030060071012072016069016023073016070023074012075030076001072023077078075079016023012011080030081011078075079016023049016023012007082016007023082078075079030036001007001008011078075083080032030067001007011'
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
def getRandomString(length):
     chars = "abcdefghijklmnopqrstuvwxyz"
     string = ""
     for i in range(length):
          string += random.choice(chars)
     return string
def makeOffspring(genome,translation):
     codonLength = 3
     locationID = getRandomString(3)
     uniqueID = getRandomString(8)
     offspringName = locationID + "_" + uniqueID + ".py"
     offspring=open(offspringName,"w")
     offspring.write("translation = "+str(translation))
     offspring.write("\n"+"genome = '"+genome+"'")
     offspring.write(translate(genome,codonLength,translation))
     offspring.close()


makeOffspring(genome,translation)


