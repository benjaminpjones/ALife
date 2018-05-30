import ast

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
        elif char == ' ':
            pass
        elif char == '=':
            dump_list.append(': ')
        else:
            dump_list.append(char)
            did_return = False
    return "".join(dump_list)

tree = ast.parse("while 1 < 5:\n    print 'Hi'\n    print 'World'")
print pdumpAST(tree)
