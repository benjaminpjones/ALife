translation = {'074': "'", '075': '{}.close()', '072': '{}.write({})', '073': '', '070': 'open({},{})', '071': '"w"', '022': '{} != {}', '004': '#################################GetTree', '010': 'container', '054': '5', '012': '{} = {}', '039': 'codeList', '058': 'else:', '015': '{}:{}', '016': '{} + {}', '019': 'newContainer', '018': '{} += {}', '055': '1', '030': '{}({})', '057': '{} -= {}', '036': 'translate', '037': 'output', '001': '{},{}', '035': '#####################################Translate', '049': '\\n', '056': 'elif {}:', '044': 'indent', '029': 'value', '051': '" "', '069': 'babyFile', '011': 'translation', '000': 'import {}', '052': '{}+{}', '032': 'dedent', '053': '({})', '061': '3', '060': 'makeOffspring', '063': 'random.randrange({},{})', '062': 'offspringNum', '065': 'babyName', '064': '40', '067': 'str({})', '066': 'baby', '005': 'def {}({}):', '068': '.py', '047': '-1', '009': 'position', '050': '{}*{}', '003': 'random', '024': '{}', '027': 'range({})', '026': 'i', '021': 'if {}:', '020': '[]', '023': '"{}"', '048': ':', '033': '{}.format(*{})', '046': '{} == {}', '045': 'line', '008': 'codonLength', '043': 'len({})', '028': '{}.count({})', '041': 'while {}:', '040': '0', '025': 'for {} in {}:', '042': '{} < {}', '031': '{}.append({})', '002': 'sys', '059': '#####################makeOffspring', '038': "''", '034': 'return {}', '013': 'codon', '014': '{}[{}]', '017': 'aacid', '007': 'genome', '006': 'getTree'}
genome = '000001002003004005006001007001008001009001010011012013014007015009016009008012017014011013018009008012019020021022017023024025026027028017023024012001029009030006001007001008001009001019011031019029032012017033017019032034001017009032035005036001007001008011012037038012039020012009040041042009043007012001029009030006001007001008001009001039011031039029032012044040025045039021046014045047023048018037016023049050051052053050054044045018044055032056046045023032057044055032058018037016023049050051052053050054044045032032034037032059005060001007011012008061012062063055064012065016023066016067062023068012069070065071072069016023012011073067011072069016023049016023012007074016007023074072069030036001007001008011075069032030060001007011'
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
def makeOffspring(genome,translation):
     codonLength = 3
     offspringNum = random.randrange(1,40)
     baby=open("baby"+str(offspringNum)+".py","w")
     baby.write("translation = "+str(translation))
     baby.write("\n"+"genome = '"+genome+"'")
     baby.write(translate(genome,codonLength,translation))
     baby.close()

makeOffspring(genome,translation)
