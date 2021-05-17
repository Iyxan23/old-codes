code = [
    [" "],
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j", "k", "l"],
    ["m", "n", "o"],
    ["p", "q", "r", "s"],
    ["t", "u", "v"],
    ["w", "x", "y", "z"],
    [" "]
]

txt = input("Enter to decode : ")

result = str()
r = str()
num = 0
numCl = 0
numCh = 0
for char in txt:
    r = ""
    numCl += 1
    if txt[numCl] == char:
        numCh += 1
        continue
    else:
        r = code[numCl-1][numCh-1]
        numCh = 0
    result += r

print("Decoded!\n" + result)
