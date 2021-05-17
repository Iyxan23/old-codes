nm = input()
f = open(nm, "w")
fl = open(nm, "r")
w = input()
f.write(w)
print(fl.read())
f.close
fl.close
