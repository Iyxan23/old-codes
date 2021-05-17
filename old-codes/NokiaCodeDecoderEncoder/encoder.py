import string

txt = str(input("Enter to encode : "))


def decode(txt, char):
    chNum = 0
    clNum = 0
    for codeList in code:
        for ch in codeList:
            if ch == char:
                return [chNum, clNum]
            chNum += 1
        clNum += 1
        chNum = 0


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

# Encoding the text using the code

resultL = list()
result = str()
l = list()
r = int()

for char in txt:
    if char == " ":
        result += " "
    elif char in string.ascii_lowercase:
        l = decode(txt, char)
        r = str(str(l[1]) * (int(l[0])+1))
        result += r
    else:
        result += char

for a in resultL:
    result += a

print("Encoded!\n" + str(result))
input()