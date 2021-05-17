
def encode(text):
    abc = list("abcdefgh7ijklm46nop2qrstu99vwxy5z)(-_=+!@#%^%-&*~`?8/$.>,<何🧓;:]}[{|31")
    hasil = ""
    c = int()
    for char in text:
        for b in abc:
            if char == b:
                hasil = hasil + abc[len(abc) - (c + 1)]
            elif char == b.upper():
                hasil = hasil + "七" + abc[len(abc) - (c + 1)]
            c += 1
        c = 0
    return hasil


print(" ")
print("\n" + encode("helo?? r u der?") + "\n")

