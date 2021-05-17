f = open("test.ooo", "w+")
oo = input()
f.write(oo)
f.close()

fi = open("test.ooo", "r")
print(fi.read())
fi.close()

ff = open("test.ooo", "a")
ll = input()
ff.write(ll)
ff.close()

fi = open("test.ooo", "r")
print(fi.read())
fi.close()
