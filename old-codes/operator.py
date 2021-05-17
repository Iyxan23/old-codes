#arithmatic Operator
print(10+10)
print(10*6)
print(2**3) #pangkat , yg angka 2 itu akngka yg mau dipangkatkan
            #klo yg 3 itu pangkatnya,, jadi "2 Kubik"
print(10%6) #Modulus / sisa bagi
print(4//3) #pembulatan /pembagian yg tidak ada desimalnya
            #kayak = 1.33333333.... menjadi 1 klo pake floor

#comparison Operator
1 == 2 #apakah 1 itu sama dgn 2?
1 != 3 #apakah 1 itu tdk sama dengan 3?
2 > 5 #apakah 2 lebih besar dari 5?
6 < 10 #apakah 6 itu lebih kecil drpd 10?
20 >= 20 #apakah 20 itu lebih besar atau sama dengan 20?
30 <= 40 #apakah 30 itu lebih kecil atau sama dengan 40?

#Logical Operator
True and True #jadi true karna keduanya True
True and False #maka jadi False karna ada false disitu
bool1 = True
bool2 = True

bool1 and bool2

bool1 = False

bool1 and bool2

bool1 or bool2 # jika ada true disitu.. maka hasilnya true
bool2 = False
bool1 or bool2 #Jika nggak ada true, maka jadi False
bool1 = True
not bool1 #maka mejadikan bool1 kebalikanya
not bool2
#Python membership operators
angka = 30

if angka in [25, 26, 27, 27, 28, 29, 30]:
    print("angka tsb. ada di data kami.")
else:
    print("angka tsb. tidak tercantum di data kami")

angka = 20
if angka not in [25, 26, 27, 27, 28, 29, 30]: #akan true karena tidak ada di list tsb.
    print("angka tsb. ada di data kami.")
else:
    print("angka tsb. tidak tercantum di data kami")

#Python identy operators
nama = Ihsan
pembuat = Ihsan
nama is pembuat #Hasilnya True, karna variabel nama itu sama
                #dengan variabel pembuat
nama is not pembuat #Kebalikan dari is

#Bitwise operators
