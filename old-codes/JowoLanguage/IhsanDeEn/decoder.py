
def decode(text):
    abc = list("abcdefgh7ijklm46nop2qrstu99vwxy5z )(-_=+!@#%^%-&*~`?8/$.>,<何🧓;:]}[{|31")
    hasil = ""
    gede = False
    c = int()
    for char in text:
        for b in abc:
            if gede:
                hasil = hasil + abc[len(abc) - (c + 1)].upper
            else:
                if char == b:
                    hasil = hasil + abc[len(abc) - (c + 1)]
                elif char == b.upper():
                    hasil = hasil + abc[len(abc) - (c + 1)].upper()
                elif char == "七":
                    gede = True
                c += 1
        c = 0
    return hasil


print("\n" + decode(":[,8pp-*-%-{[*p"))
