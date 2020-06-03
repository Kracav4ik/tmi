#!/usr/bin/env python3
import sys


def cmd(x):
    cmds = {
        ']': '0',
        '[': '1',
        '<': '2',
        '>': '3',
        '.': '4',
        ',': '5',
        '+': '6',
        '-': '7',
    }

    if x in cmds:
        return cmds[x] + ' '

    return ''


if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print('Not enough arguments. It should be used like "%s input_file output_file"' % sys.argv[0])
        exit(0)

    with open(sys.argv[1], 'r') as input:
        with open(sys.argv[2], 'w') as output:
            output.write('v2.0 raw\n')
            s = input.read()
            s = ''.join(s.split())
            comm = 0
            start = s[0] != '['
            for c in s:
                if start:
                    output.write(cmd(c))
                if not start:
                    if c == '[':
                        comm += 1
                    if c == ']':
                        comm -= 1
                if comm == 0:
                    start = True
            output.write('8')
