import ast

def comma_separated(args):
    if not args:
        return "\n"
    ast_str = ""
    for arg in args[:-1]:
        ast_str += '{},{}\n'
        ast_str += arg
    ast_str += args[-1]
    return ast_str

operators = { ast.Add: '+', ast.Sub: '-', ast.Mult: '*', ast.Div: '/',
              ast.Mod: '%', ast.Pow: '**', ast.LShift: '<<', ast.RShift: '>>',
              ast.BitOr: '|', ast.BitXor: '^', ast.BitAnd: '&',
              ast.FloorDiv: '//', ast.Lt: '<', ast.LtE: '<=', ast.Gt: '>',
              ast.GtE: '>=', ast.Eq: '=='}

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
        ast_str += 'def {}({}):\n'
        ast_str += ast2txt(tree.name)
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
        ast_str += ast2txt(tree.id)
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

    # pass statements
    if isinstance(tree, ast.Pass):
        ast_str += 'pass\n'
        return ast_str

    # expressions
    if isinstance(tree, ast.Expr):
        ast_str += ast2txt(tree.value)
        return ast_str

    # binary operations
    if isinstance(tree, ast.BinOp):
        ast_str += '({}' + operators[type(tree.op)] + '{})\n'
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
        if tree.values:
            args_list += [ast2txt(arg) for arg in tree.values]
            ast_str += comma_separated(args_list)
        return ast_str

    # dictionaries
    if isinstance(tree, ast.Dict):
        ast_str += '{{{}}}\n'
        kw_pairs = []
        for i in xrange(len(tree.keys)):
            kw_pairs.append('{}:{}\n')
            kw_pairs[-1] += ast2txt(tree.keys[i])
            kw_pairs[-1] += ast2txt(tree.values[i])
        ast_str += comma_separated(kw_pairs)
        return ast_str

    # strings
    if isinstance(tree, ast.Str):
        ast_str += '"{}"\n'
        ast_str += tree.s.replace('\\','\\\\').replace('"','\\"') + '\n'
        return ast_str

    # import statements
    if isinstance(tree, ast.Import):
        ast_str += 'import {}\n'
        modules = [ast2txt(m) for m in tree.names]
        ast_str += comma_separated(modules)
        return ast_str

    # aliases
    if isinstance(tree, ast.alias):
        if tree.asname:
            ast_str += '{} as {}\n'
        ast_str += ast2txt(tree.name)
        if tree.asname:
            ast_str += ast2txt(tree.asname)
        return ast_str

    # global variables
    if isinstance(tree, ast.Global):
        ast_str += 'global {}\n'
        ast_str += comma_separated([ast2txt(name) for name in tree.names]) + '\n'
        return ast_str

    # subscript operators (to get an element from a List)
    if isinstance(tree, ast.Subscript):
        ast_str += '{}[{}]\n'
        ast_str += ast2txt(tree.value)
        ast_str += ast2txt(tree.slice)
        return ast_str

    # indices
    if isinstance(tree, ast.Index):
        ast_str += ast2txt(tree.value)
        return ast_str

    # slices
    if isinstance(tree, ast.Slice):
        ast_str += '{}:{}'
        if tree.step:
            ast_str += ':{}'
        ast_str += '\n'
        ast_str += ast2txt(tree.lower)
        ast_str += ast2txt(tree.upper)
        if tree.step:
            ast_str += ast2txt(tree.step)
        return ast_str

    # plaintext string (usually an id for a Name object)
    if isinstance(tree, str):
        return ast_str + tree + '\n'

    # object attributes (i.e. class members)
    if isinstance(tree, ast.Attribute):
        ast_str += '{}.{}\n'
        ast_str += ast2txt(tree.value)
        ast_str += ast2txt(tree.attr)
        return ast_str

    # augment assignments
    if isinstance(tree, ast.AugAssign):
        ast_str += '{}' + operators[type(tree.op)] + '={}\n'
        ast_str += ast2txt(tree.target)
        ast_str += ast2txt(tree.value)
        return ast_str

    # return statement
    if isinstance(tree, ast.Return):
        ast_str += 'return {}\n'
        ast_str += ast2txt(tree.value)
        return ast_str

    # keyword
    if isinstance(tree, ast.keyword):
        ast_str += tree.arg+'\n'
        return ast_str

    if isinstance(tree, ast.List):
        ast_str += '[{}]\n'
        ast_str += comma_separated([ast2txt(element) for element in tree.elts])
        return ast_str

    if isinstance(tree, ast.Tuple):
        ast_str += '({})\n'
        ast_str += comma_separated([ast2txt(element) for element in tree.elts])
        return ast_str

    if isinstance(tree, ast.While):
        ast_str += 'while {}:\n'
        ast_str += ast2txt(tree.test)
        ast_str += ast2txt(tree.body)
        return ast_str

    if isinstance(tree, ast.Compare):
        operation = operators[type(tree.ops[0])]
        ast_str += '({} ' + operation + ' {})\n'
        ast_str += ast2txt(tree.left)
        ast_str += ast2txt(tree.comparators)
        return ast_str

    if isinstance(tree, list):
        ast_str += comma_separated([ast2txt(element) for element in tree])
        return ast_str

    print "Did not know what to do with",type(tree)
    return ast_str + 'NOT IMPLEMENTED\n'
