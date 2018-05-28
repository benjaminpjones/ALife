import ast

def comma_separated(args):
    if not args:
        return ""
    ast_str = ""
    for arg in args[:-1]:
        ast_str += '{},{}\n'
        ast_str += arg
    ast_str += args[-1]
    return ast_str

# Appends tree's string representation to ast+string
def ast2txt(tree, ast_str=""):
    # module object (exists for every program)
    if isinstance(tree, ast.Module):
        for node in tree.body:
            ast_str += ast2txt(node)
        return ast_str

    # function definitions
    if isinstance(tree, ast.FunctionDef):
        for decorator in tree.decorator_list:
            ast_str += '@{}\n' + decorator.id + '\n'
        ast_str += "def {}({}):\n"
        ast_str += tree.name + '\n'
        ast_str += ast2txt(tree.args)
        for node in tree.body:
            ast_str += ast2txt(node)
        ast_str += 'dedent\n'
        return ast_str

    # function arguments
    if isinstance(tree, ast.arguments):
        args_len = len(tree.args)
        defaults_len = len(tree.defaults)
        defaults_start = args_len - defaults_len
        args_list = [ast2txt(arg) for arg in tree.args]
        for i in xrange(defaults_len):
            args_list[defaults_start + i] = ( '{}={}\n'
                                            + args_list[defaults_start + i]
                                            + ast2txt(tree.defaults[i]) )
        if tree.vararg:
            args_list.append('*{}\n' + tree.vararg + '\n')
        if tree.kwarg:
            args_list.append('**{}\n' + tree.kwarg + '\n')
        ast_str += comma_separated(args_list)
        return ast_str

    # names
    if isinstance(tree, ast.Name):
        ast_str += tree.id + '\n'
        return ast_str

    # numbers
    if isinstance(tree, ast.Num):
        ast_str += str(tree.n) + '\n'
        return ast_str
    
    # assignments
    if isinstance(tree, ast.Assign):
        for target in tree.targets:
            ast_str += '{}={}\n'
            ast_str += ast2txt(target)
        ast_str += ast2txt(tree.value)
        return ast_str

    # for loops
    if isinstance(tree, ast.For):
        ast_str += 'for {} in {}:\n'
        ast_str += ast2txt(tree.target)
        ast_str += ast2txt(tree.iter)
        for node in tree.body:
            ast_str += ast2txt(node)
        ast_str += 'dedent\n'
        if tree.orelse:
            ast_str += 'else:\n'
            for node in tree.orelse:
                ast_str += ast2txt(node)
            ast_str += 'dedent\n'
        return ast_str

    # function calls
    if isinstance(tree, ast.Call):
        ast_str += '{}({})\n'
        ast_str += ast2txt(tree.func)
        args_list = [ast2txt(arg) for arg in tree.args]
        args_list += [ast2txt(arg) for arg in tree.keywords]
        if tree.starargs:
            args_list += '*{}\n' + ast2txt(tree.starargs)
        if tree.kwargs:
            args_list += '**{}\n' + ast2txt(tree.kwargs)
        ast_str += comma_separated(args_list)
        return ast_str

    if isinstance(tree, ast.Pass):
        ast_str += 'pass\n'
        return ast_str

    if isinstance(tree, ast.Expr):
        ast_str += ast2txt(tree.value)
        return ast_str

    if isinstance(tree, ast.BinOp):
        op_txt = str()
        if isinstance(tree.op, ast.Add):
            op_txt = '+'
        if isinstance(tree.op, ast.Sub):
            op_txt = '-'
        if isinstance(tree.op, ast.Mult):
            op_txt = '*'
        if isinstance(tree.op, ast.Div):
            op_txt = '/'
        if isinstance(tree.op, ast.Mod):
            op_txt = '%'
        if isinstance(tree.op, ast.Pow):
            op_txt = '**'
        if isinstance(tree.op, ast.LShift):
            op_txt = '<<'
        if isinstance(tree.op, ast.RShift):
            op_txt = '>>'
        if isinstance(tree.op, ast.BitOr):
            op_txt = '|'
        if isinstance(tree.op, ast.BitXor):
            op_txt = '^'
        if isinstance(tree.op, ast.BitAnd):
            op_txt = '&'
        if isinstance(tree.op, ast.FloorDiv):
            op_txt = '//'
        ast_str += '{}' + op_txt + '{}\n'
        ast_str += ast2txt(tree.left)
        ast_str += ast2txt(tree.right)
        return ast_str

    if isinstance(tree, ast.Print):
        ast_str += 'print {}'
        if tree.nl:
            ast_str += '\n'
        else:
            # a comma at the end of a print statement indicates suppression
            # of a new line
            ast_str += ',\n'
        args_list = []
        if tree.dest:
            # the >> operator indicates a destination other than stdout
            args_list += '>>' + ast2txt(tree.dest)
        args_list += [ast2txt(arg) for arg in tree.values]
        ast_str += comma_separated(args_list)
        return ast_str

    print "Did not know what to do with",
    print type(tree)
    return ast_str
