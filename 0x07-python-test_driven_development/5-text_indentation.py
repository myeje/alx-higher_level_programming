#!/usr/bin/python3
"""Module function that indents texts from a txt file"""


def text_indentation(text):
    """
    text_indentation - function that indents texts
    @text: text to indent

    Raise error:
        TypeError: if text not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delim = ['.', '?', ':']
    result = ''
    text_lines = text.splitlines()

    for line in text_lines:
        line = line.strip()
        if line:
            result += line[0]

            for i in range(1, len(line)):
                if line[i-1] in delim:
                    result += '\n\n'
                elif line[i] == ' ' and line[i-1] != ' ':
                    result += ' '
                elif line[i] != ' ':
                    result += line[i]
            result += '\n\n'
    result = result.rstrip('\n')
    print(result, end='')
