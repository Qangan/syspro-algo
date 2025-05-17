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

def to_postfix(expression: str) -> list[str]:
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

    return output

def test_to_postfix_complex_expressions():
    assert to_postfix("3 + 4 * 2 ^ 3 - 6 / 2") == ["3", "4", "2", "3", "^", "*", "+", "6", "2", "/", "-"]
    assert to_postfix("2 ^ 3 ^ 2 ^ 1 + 5") == ["2", "3", "2", "1", "^", "^", "^", "5", "+"]
    assert to_postfix("( ( 2 + 3 ) * 4 ) ^ ( 5 - 1 )") == ["2", "3", "+", "4", "*", "5", "1", "-", "^"]
    assert to_postfix("1 + 2 * 3 - 4 ^ 5 / 6 + 7 * 8 - 9") == \
           ["1", "2", "3", "*", "+", "4", "5", "^", "6", "/", "-", "7", "8", "*", "+", "9", "-"]
    assert to_postfix("( 1 + 2 ^ 3 ) * ( 4 - 5 / 6 )") == \
           ["1", "2", "3", "^", "+", "4", "5", "6", "/", "-", "*"]
    assert to_postfix("2 ^ ( 3 ^ ( 4 ^ ( 5 + 1 ) ) )") == ["2", "3", "4", "5", "1", "+", "^", "^", "^"]
    assert to_postfix("2 * 3 ^ 4 * 5 ^ 6 * 7") == ["2", "3", "4", "^", "*", "5", "6", "^", "*", "7", "*"]
    assert to_postfix("1 + 2 ^ 3 * 4 + 5 ^ 6 / 7 - 8 * 9") == \
           ["1", "2", "3", "^", "4", "*", "+", "5", "6", "^", "7", "/", "+", "8", "9", "*", "-"]
    assert to_postfix("( 1 + ( 2 * ( 3 ^ ( 4 + 5 ) ) ) ) - ( 6 / ( 7 - 8 ) )") == \
           ["1", "2", "3", "4", "5", "+", "^", "*", "+", "6", "7", "8", "-", "/", "-"]
    assert to_postfix("1 + 2 - 3 * 4 / 5 ^ 6 + 7 - 8 * 9") == \
           ["1", "2", "+", "3", "4", "*", "5", "6", "^", "/", "-", "7", "+", "8", "9", "*", "-"]
    assert to_postfix("( 2 ^ ( 3 + 4 ) ) ^ ( 5 * ( 6 - 1 ) )") == \
           ["2", "3", "4", "+", "^", "5", "6", "1", "-", "*", "^"]
    assert to_postfix("1 * 2 + 3 * 4 - 5 * 6 + 7 * 8 - 9 * 10") == \
           ["1", "2", "*", "3", "4", "*", "+", "5", "6", "*", "-", "7", "8", "*", "+", "9", "10", "*", "-"]
    assert to_postfix("( ( 1 + 2 ) * 3 ) ^ ( ( 4 - 5 ) * 6 ) + ( 7 * ( 8 + 9 ) )") == \
           ["1", "2", "+", "3", "*", "4", "5", "-", "6", "*", "^", "7", "8", "9", "+", "*", "+"]
    assert to_postfix("1 + 2 * 3 ^ 4 + 5 * 6 ^ 7 - 8 / 9 + 10 * 11") == \
           ["1", "2", "3", "4", "^", "*", "+", "5", "6", "7", "^", "*", "+", "8", "9", "/", "-", "10", "11", "*", "+"]
    assert to_postfix("( 1 + ( 2 * ( 3 + ( 4 ^ ( 5 * ( 6 - ( 7 / 8 ) ) ) ) ) ) ) - ( ( 9 + 10 ) * ( 11 ^ 12 ) )") == \
           ["1", "2", "3", "4", "5", "6", "7", "8", "/", "-", "*", "^", "+", "*", "+", "9", "10", "+", "11", "12", "^", "*", "-"]

test_to_postfix_complex_expressions()
strs = 'a'
while strs:
    strs = input()
    expression = re.sub(r'([\^+*-])', r' \1 ', strs)
    print(' '.join(to_postfix(expression)))
