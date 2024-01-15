# create a box enclosed with a symbol & has a specific height and width.

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol must be a single string."')
    if width < 2 or height < 2:
        raise Exception('"width" & "height" must be greater than 1.')
    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


print(boxPrint('&&', 2, 2)) # Exception 1
print(boxPrint('&', 1, 1)) # Exception 2
