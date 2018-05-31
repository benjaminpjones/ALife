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
        subtree, idx = getTree(idx, split_txt)
        subtrees.append(subtree)
    try:
        aacid = aacid.format(*subtrees)
    except Exception as error:
        print error
        print "aacid:", aacid, "-- subtrees:", subtrees
        aacid = "# txt2src could not parse here.\n"
        
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
    f.close()
    tree = ast.parse(source)

    txt_tree = ast2txt(tree)
    print(txt_tree)

    # round-trip source
    rt_source = txt2src(txt_tree) 

    # Finally, run ast again.
    rt_tree = None
    try:
        rt_tree = ast.parse(rt_source)
    except Exception as error:
        print "Re-translated source had syntax errors:"
        print "    ", error
        failed_ast_name = filename[:-3] + '(failed).txt'
        f = open(failed_ast_name, 'w+')
        f.write(txt_tree)
        f.close()
        failed_src_name = filename[:-3] + '(failed).py'
        f = open(failed_src_name, 'w+')
        f.write(rt_source)
        f.close()
        print "Translations written to file:"
        print "    ", failed_src_name
        print "    ", failed_ast_name
        quit()

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
