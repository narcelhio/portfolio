def hex_output():
    decNum = 0
    # Hexadecimal numbers are represented by only 16 symbols. These symbols or values are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F.
    hexnum = input('Please enter a hex number to convert:  ')
    for power, digit in enumerate(reversed(hexnum)):
        decNum += int(digit, 16) * (16 ** power)
        print(decNum)


hex_output()
