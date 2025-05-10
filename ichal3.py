#Challenge 3: Converting numbers to roman numbers

def int_to_roman(num):
    
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ''
    i = 0

    while num > 0:
        if values[i] <= num:
            roman += numerals[i]
            num -= values[i]
        else:
            i += 1
    
    return roman

if __name__ == "__main__":
    print(int_to_roman(int(input("Insert a number to convert (1 - 3999): "))))

#First solution before adding improved converter
"""
def convert_to_roman(num: int) -> str: #1 - 10
    
    roman = ""

    milli = num // 1000
    num %= 1000
    cent = num // 100
    num %= 100
    deci = num // 10
    num %= 10
    ones = num

    for i in range(milli):
        roman += "M"

    if cent == 9:
        roman += "CM"
    elif cent == 4:
        roman += "CD"
    else:
        roman += "D"*(cent//5) + "C"*(cent%5)

    if deci == 9:
        roman += "XC"
    elif deci == 4:
        roman += "XL"
    else:
        roman += "L"*(deci//5) + "X"*(deci%5)

    if ones == 9:
        roman += "IX"
    elif ones == 4:
        roman += "IV"
    else:
        roman += "V"*(ones//5) + "I"*(ones%5)

    return roman
"""