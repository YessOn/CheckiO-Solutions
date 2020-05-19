
def chess_knight(start, count):
    delta = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

    def moves(c):
        def subfunc(_a):
            i,j = chr(ord(c[0]) + _a[0]), int(c[1]) + int(_a[1])
            if ('a' <= i and i <= 'h' and 0 < j and j < 9) : return f"{i}{j}"
        return list(filter(lambda x: x, map(subfunc, delta)))
    result = []
    tempo = [start]
    i = 0
    while i < count:
        i += 1
        new_res = []
        for x in tempo:
            for y in moves(x): new_res.append(y)
        tempo = new_res
        for x in new_res:
              if x not in result: result.append(x)
    return sorted(result)

if __name__ == '__main__':
    print("Example:")
    print(chess_knight('a1', 1))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert chess_knight('a1', 1) == ['b3', 'c2']
    assert chess_knight('h8', 2) == ['d6', 'd8', 'e5', 'e7', 'f4', 'f7', 'f8', 'g5', 'g6', 'h4', 'h6', 'h8']
    print("Coding complete? Click 'Check' to earn cool rewards!")
