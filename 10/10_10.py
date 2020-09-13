filename = '10\Highwayman of the Void.txt'
try:
    with open(filename) as file_object:
        content = file_object.read()
        num = content.lower().count('the')
    print('number of "the" in this book: ' + str(num))
except FileNotFoundError:
    print('file not found! ')
