from random import randint

LEFT = [[39, 51, 27, 33, 29, 57, 5, 17, 9, 23], [13, 25, 19, 61, 35, 49, 47, 59, 55, 11]]
RIGHT = [114, 102, 108, 66, 92, 78, 80, 68, 72, 116]
EO_TABLE = [63, 52, 50, 49, 44, 38, 35, 42, 41, 37]

bin2dec = lambda i: int(str(i), 2)

def barcode_reader(barcode):
    # Translate BarCode To Binary
    barcode = barcode.translate(str.maketrans(' _', '01'))

    # Slice Right hand and Left hand Values
    the_left = barcode[3:45]
    the_right = barcode[50:85]

    answer = []

    # Looking for the first digit
    fd_binary = ''

    # Format Left Characters
    my_digits = [the_left[7*i:7*(i+1)] for i in range(0, 6)]
    for i in my_digits:
        for j in LEFT:
            try:
                digit = j.index(bin2dec(i))
                # a is the Partial collection of the first digit
                if digit >= 0:
                    a = LEFT.index(j)
            except:
                pass
        fd_binary += str(a)
        answer.append(digit)
    answer.insert(0, EO_TABLE.index(bin2dec(fd_binary)))

    # Format Right Characters
    my_digits = [the_right[7*i:7*(i+1)] for i in range(0, 5)]
    for i in my_digits:
        answer.append(RIGHT.index(bin2dec(i)))

    # Looking for the Checksum [Check digit]
    cd = 10 - sum(a*(1, 3)[i % 2] for i, a in enumerate(answer)) % 10
    cd = cd if cd < 10 else 0
    answer.append(cd)

    # Backward
    backward = bool(randint(0, 1));
    if backward:
        barcode = barcode[::-1]
    
    return ''.join(map(str, answer))

print(barcode_reader('_ _   _ __ _  ___ __  __  _  __ ____ _  ___ _ _ _ __  __ __ __  _    _ _ ___  _  ___ _   _  _ _'))
print(barcode_reader('_ _ ___ __  __  _  _  __ ____ _ _   __ __   _ _ _ _ _    _   _  _  _   ___ _  __  __ __ __  _ _'))
