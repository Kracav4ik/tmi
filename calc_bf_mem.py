#!/usr/bin/env python3
import sys


def skip_brackets(s, op, from_i=0):
    idx = from_i + op
    count = op
    while count != 0 and 0 <= idx < len(s):
        if s[idx] == '[':
            count += 1
        elif s[idx] == ']':
            count -= 1
        idx += op
    return idx


def parse_bf(s):
    mem = [0]
    bf_i = 0
    cell_i = 0

    while bf_i < len(s):
        if s[bf_i] == '>':
            cell_i += 1
            if len(mem) == cell_i:
                mem.append(0)
        elif s[bf_i] == '<':
            cell_i -= 1
            if cell_i < 0:
                sys.stderr.write('< for 0th cell\n')
                cell_i = 0
        elif s[bf_i] == '.':
            sys.stdout.write(chr(mem[cell_i]))
            sys.stdout.flush()
        elif s[bf_i] == '+':
            mem[cell_i] += 1
            mem[cell_i] %= 256
        elif s[bf_i] == '-':
            mem[cell_i] += 255
            mem[cell_i] %= 256
        elif s[bf_i] == '[':
            if mem[cell_i] == 0:
                bf_i = skip_brackets(s, 1, bf_i) - 1
        elif s[bf_i] == ']':
            bf_i = skip_brackets(s, -1, bf_i)
        bf_i += 1

    return len(mem)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Not enough arguments. It should be used like "%s input_file"' % sys.argv[0])
        exit(0)

    with open(sys.argv[1], 'r') as input:
        print(parse_bf(input.read()))
