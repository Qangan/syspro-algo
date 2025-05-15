import re
class Operator:
    # 1 - левая ассоциативность, 0 - правая
    def __init__(self, symbol: str, prio: int, assoc: 1 | 0 = 1):
        self.symbol = symbol
        self.prio = prio
        self.assoc = assoc


operators = {
    '+': Operator('+', 3),
    '-': Operator('-', 3),
    '*': Operator('*', 2),
    '/': Operator('/', 2),
    '^': Operator('^', 1, 0)
}

def to_postfix(expression: str) -> str:
    stack, output = [], []
    tokens = expression.split()

    for token in tokens:
        if token.isnumeric():
            output.append(token)
        elif token in operators:
            while stack and (stack[-1] != '(' and (operators[stack[-1]].prio < operators[token].prio or (operators[stack[-1]].prio == operators[token].prio and operators[token].assoc))):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    return ' '.join(output)

strs = 'a'
while strs:
    strs = input()
    expression = re.sub(r'([\^+*-])', r' \1 ', strs)
    print(to_postfix(expression))
