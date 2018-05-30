import ast
from makeAST import getValidFileFromUser
from ast2txt import ast2txt
from difflib import unified_diff

def pdumpAST(tree):
    ast_str = ast.dump(tree)
    dump_list = []
    indent = 0
    did_return = False
    for char in ast_str:
        if char == '(':
            indent += 4
            dump_list.append('()\n' + ' ' * indent)
            did_return = True
        elif char == ')':
            indent -= 4
            if not did_return:
                dump_list.append('\n' + ' ' * indent)
            did_return = True
        elif char == ',':
            if not did_return:
                dump_list.append('\n' + ' ' * indent)
            did_return = True
        elif char == '[' or char == ']':
            pass
        elif char == ' ' and did_return:
            pass
        elif char == '=':
            dump_list.append(': ')
        else:
            dump_list.append(char)
            did_return = False
    return "".join(dump_list)

def getTree(idx, split_txt):
    aacid = split_txt[idx]
    idx += 1
    subtrees = []
    num_subtrees = aacid.replace('{{', "").replace('}}', "").count('{}')
    for i in xrange(num_subtrees):
        try:
            subtree, idx = getTree(idx, split_txt)
        except:
            subtree, idx = "ERRORED subtree", idx + 1
        subtrees.append(subtree)
    aacid = aacid.format(*subtrees)
    return aacid, idx

def txt2src(txt_str):
    split_txt = txt_str.split('\n')
    code_list = []
    idx = 0
    while idx < len(split_txt):
        src, idx = getTree(idx, split_txt)
        code_list.append(src)
    indent = 0
    output = ""
    for line in code_list:
        if len(line) == 0:
            output += "\n"
        elif line[-1] == ":":
            output += "\n" + " " * (4 * indent) + line
            indent += 1
        elif line == "dedent":
            indent -= 1
        else:
            output += "\n" + " " * (4 * indent) + line
    return output
        
if __name__ == '__main__':
    f, filename = getValidFileFromUser()
    source = f.read()
    tree = ast.parse(source)

    txt_tree = ast2txt(tree)
    print(txt_tree)

    # round-trip source
    rt_source = txt2src(txt_tree) 

    # Finally, run ast again.
    rt_tree = ast.parse(rt_source)

    # diff
    num_lines = 0
    before = pdumpAST(tree).split('\n')
    after = pdumpAST(rt_tree).split('\n')
    for line in unified_diff(before, after, 'before', 'after'):
        num_lines += 1
        print line

    if not num_lines:
        print pdumpAST(rt_tree)
        print "TEST PASSED: ASTs are identical!"
