
# all public variables
variables = {}

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

def evaluate(parsed):
    # print(parsed)
    operator = parsed[0]
    if parsed[0].isdigit():
        return float(parsed[0])

    if operator == '+':
        return evaluate(parsed[1]) + evaluate(parsed[2])

    if operator == '-':
        return evaluate(parsed[1]) - evaluate(parsed[2])

    if operator == '*':
        return evaluate(parsed[1]) * evaluate(parsed[2])

    if operator == '/':
        return evaluate(parsed[1]) / evaluate(parsed[2])

input = '- 3 ( + 1 ( * 5 ( + 2 7 ) ) )' # 3 - ( 1 +  5 * (2 + 7) ) = -43
parsed = read_from_token(tokenize(input))
evaluated = evaluate(parsed)

print(evaluated)
