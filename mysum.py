def mysum(*number):
    output = 0
    for number in number:
        output += number
    return output
print(mysum(10,20,30,40))