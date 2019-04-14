
PROGRAM = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'



def brainfuck(code):
    def debugvm():
        print(' '+' | '.join('%3d' % x for x in tape))
        print(' '*6*caret+'-----')

    caret = 0
    tape = [0] * 25

    i = 0
    while i < len(code):
        # print('OPERATOR: '+code[i])

        op = code[i]
        if op == '>':
            caret += 1
        elif op == '<':
            caret -= 1
        elif op == '+':
            tape[caret] += 1
        elif op == '-':
            tape[caret] -= 1
        elif op == '.':
            print(chr(tape[caret]) if tape[caret] > 0 else ' ', end='')
        elif op == ',':
            tape[caret] = ord(input())
        elif op == '[' and tape[caret] == 0:
            j = i + 1
            k = 0
            while True:
                if code[j] == ']' and k == 0:
                    i = j
                    break
                elif code[j] == '[':
                    k += 1
                elif code[j] == ']':
                    k -= 1
                j += 1
        elif op == ']' and tape[caret] != 0:
            j = i - 1
            k = 0
            while True:
                if code[j] == '[' and k == 0:
                    i = j
                    break
                elif code[j] == ']':
                    k += 1
                elif code[j] == '[':
                    k -= 1
                j -= 1

        # debugvm()
        i += 1

    


brainfuck(PROGRAM)