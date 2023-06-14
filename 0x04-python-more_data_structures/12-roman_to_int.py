#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return(0)

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    digit = 0
    for roman in reversed(roman_string):
        result = roman_numerals.get(roman, 0)
        if total < digit:
            total -= result
        else:
            total += result
        digit = result
    return(total)
