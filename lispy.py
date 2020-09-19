import log
# all public variables
variables = {
    'SELF': __file__
}

def tokenize(s):
    return s.replace('(', '( ').replace(')', ' )').split()

# no error tracing !!!
def read_from_token(tokenized):

    stack = [[]]
    for i in range(len(tokenized)):
        token = tokenized[i]
        if token == '(':
            stack.append([])
        elif token == ')':
            stack[-2].append(stack[-1])
            stack.pop()
        else:
            stack[-1].append(token)
    return stack[0]

def isFloat(x):
    try: 
        float(x)
        return True 
    except:
        return False

def evaluate(parsed):

    if type(parsed) == type([]): # isList ?
        operator = parsed[0]
    elif not isFloat(parsed): # is operand
        operator = parsed
    else:
        return float(parsed) # real value

    if operator == '+':
        return evaluate(parsed[1]) + evaluate(parsed[2])

    if operator == '-':
        return evaluate(parsed[1]) - evaluate(parsed[2])

    if operator == '*':
        return evaluate(parsed[1]) * evaluate(parsed[2])

    if operator == '/':
        return evaluate(parsed[1]) / evaluate(parsed[2])

    if operator == '<-':
        variables[ parsed[1] ] = evaluate(parsed[2])
        return variables[parsed[1]]

    if operator == 'log':
        for param in parsed[1:]:
            x = evaluate(param)
            print(x, end=' ')
        print()
        return
    
    value = variables.get(operator, None) 
    if value != None:
        return value

def exec(s):
    evaluate(read_from_token(tokenize(s)))  

exec('<- x 102.0')
exec('log x')
exec('log ( + x 5 )')
exec('log SELF')