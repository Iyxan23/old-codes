import sys

variabelstr = dict()
variabelnom = dict()
rampung = bool()


def compilejwlg(file):
    isi = file.read()
    isi += "\n"
    file.close()
    # TODO : COMPILER!! PENTING!!
    # Variabel Sistem!!
    perintah = list(isi)
    tok = ""
    tokens = list()

    # Variabel untuk memisahkan tipe data
    nomor = str()
    vrnom = bool()
    varnom = str()
    string = ""
    vrstr = bool()
    varstr = str()

    # Semua variabel yg dibutuhkan command :
    itung = False
    statusn = False  # Status Nomor
    statuss = int()  # Status String

    # - Gawe command
    gawe = False
    jenengvar = False
    namaVarSimpenan = ""

    # - - Deklarasi Variabel
    # - - - String
    variabelOut = False
    namavariabel = ""

    # - - - Nomor
    variabelOutn = False
    namavariabeln = ""

    for char in perintah:
        tok += char
        if tok == " ":
            if statuss == 0:
                tok = ""
            else:
                tok = " "

        elif tok == "\n":
            if vrstr:
                tokens.append("variabelstr:"+varstr)
                varstr = ""
                vrstr = False

            if vrnom:
                tokens.append("variabelnom:"+varnom)
                varnom = ""
                vrnom = False

            if itung:
                itung = False
                tokens.append("nomor:" + nomor)
                nomor = ""

            if gawe:
                gawe = False
                if nomor != None:
                    tokens.append("nomor:" + nomor)
                    nomor = ""

                elif string != None:
                    tokens.append("string:" + string)
                    string = ""

            tok = ""

        # Semua Command yg ada disini

        elif tok == "tulis":            # Statement = tulis "string"
            tokens.append("tulis")
            tok = ""

        elif tok == "itung":            # Statement = itung nom [+/-/*//]
            tokens.append("itung")
            itung = True
            tok = ""

        elif tok == "gawe":             # Statement = gawe (jeneng vaiabel) = (isi variabel)
            tokens.append("gawe")
            gawe = True
            tok = ""

        elif tok == "rampung":
            tokens.append("rampung")
            tok = ""

        # Lain Lain

        elif tok in variabelstr:
            varstr += tok
            vrstr = True

        elif tok in variabelnom:
            varnom += tok
            vrnom = True

        elif tok == "0" or tok == "1" or tok == "2" or tok == "3" or tok == "4" or tok == "5" or tok == "6" or tok == \
                "7" or tok == "8" or tok == "9":
            nomor += tok
            tok = ""

        elif tok == "`":
            if itung:
                pass
            if not statusn:
                statusn = True
                nomor += tok
                tok = ""
            else:
                statusn = False
                tokens.append(nomor)
                nomor = ""

        if gawe:
            if tok == "=":
                print("IFF!!")
                if jenengvar:
                    jenengvar = False
                    tokens.append(namaVarSimpenan)
                    namaVarSimpenan = ""
                tokens.append("=")
                tok = ""
            else:
                print("Else")
                jenengvar = True
                if jenengvar:
                    namaVarSimpenan += tok
                tok = ""

        if itung:
            if tok == "+":
                tokens.append("nomor:" + nomor)
                nomor = ""
                tokens.append("+")
                tok = ""

            elif tok == "-":
                tokens.append("nomor:" + nomor)
                nomor = ""
                tokens.append("-")
                tok = ""

            elif tok == "*":
                tokens.append("nomor:" + nomor)
                nomor = ""
                tokens.append("*")
                tok = ""

            elif tok == "/":
                tokens.append("nomor:" + nomor)
                nomor = ""
                tokens.append("/")
                tok = ""

        elif tok == "\"":
            if statuss == 0:
                statuss = 1
                tok = ""
            elif statuss == 1:
                tokens.append("string:" + string)
                string = ""
                statuss = 0
                tok = ""

        elif tok == "#":
            tok = ""
            if variabelOut:
                namavariabel += tok
                tokens.append("varstr:" + namavariabel)
            variabelOut = True

        elif tok == "$":
            tok = ""
            if variabelOutn:
                namavariabeln += tok
                tokens.append("varnom:" + namavariabeln)
            variabelOutn = True

        elif statuss == 1:
            string += tok
            tok = ""

        print(tok)

    return tokens


def initialize_variable(token, ln):
    i = 0
    try:
        while i < len(token):
            if token[i] == "gawe" and token[i+2] == "=":
                if token[i+3][:7] == "string:":
                    variabelstr["#" + token[i+1]] = token[i+3][7:]

                elif token[i+3][:6] == "nomor:":
                    variabelnom["$" + token[i+1]] = token[i+3][6:]

                i += 4
                ln += 1

            if token[i] in variabelstr:
                token[i] = "string:" + variabelstr[token[i]]

            elif token[i] in variabelnom:
                token[i] = "nomor:" + variabelnom[token[i]]

            i += 1
    except:
        pass
    return ln


def parse(toke, line):
    error = False
    i = 0
    line += 1
    rampung = False
    print(variabelstr)
    print(variabelnom)
    while i < len(toke):
        try:
            if toke[i] == "gawe":
                print("GAWEEE!")
                line += 1
                i += 4

            if toke[i] + " " + toke[i+1][:7] == "tulis string:" or toke[i] + " " + toke[i+1][:7] == "tulis nomor:":
                print(toke[i+1][7:])
                i += 2
                line += 1

            elif  toke[i] + " " + toke[i+1][:7] == "tulis variabelstr:" or toke[i] + " " + toke[i+1][:7] == "tulis variabelnom:":
                if toke[i+1][7:] == "varstr:":
                    try:
                        print(variabelstr["#" + toke[i+1][:12]])
                    except:
                        print("===============================")
                        print("Error ! ranek variabel string jenenge " + toke[i+1][:12])
                        print("===============================")
                        error = True
                elif toke[i+1][7:] == "varnom:":
                    try:
                        print(variabelstr["$" + toke[i+1][:12]])
                    except:
                        print("===============================")
                        print("Error ! ranek variabel nomor jenenge " + toke[i+1][:12])
                        print("===============================")
                        error = True

            elif toke[i] + " " + toke[i+1][:6] + " " + toke[i+3][:6] == "itung nomor: nomor:":
                if toke[i + 2] == "+":
                    print(int(toke[i + 1][6:]) + int(toke[i + 3][6:]))

                elif toke[i + 2] == "-":
                    print(int(toke[i + 1][6:]) - int(toke[i + 3][6:]))

                elif toke[i + 2] == "*":
                    print(int(toke[i + 1][6:]) * int(toke[i + 3][6:]))

                elif toke[i + 2] == "/":
                    print(int(toke[i + 1][6:]) / int(toke[i + 3][6:]))

                i += 4
                line += 1

            elif toke[i] + " " + toke[i+1][:12] + " " + toke[i+3][:12] == "itung variabelnom: variabelnom:":
                if toke[i+2] == "+":
                    print(int(variabelnom[toke[i+1][6:]]) + int(variabelnom[toke[i+3][6:]]))

                elif toke[i+2] == "-":
                    print(int(variabelnom[toke[i+1][6:]]) - int(variabelnom[toke[i+3][6:]]))

                elif toke[i+2] == "*":
                    print(int(variabelnom[toke[i+1][6:]]) * int(variabelnom[toke[i+3][6:]]))

                elif toke[i+2] == "/":
                    print(float(variabelnom[toke[i+1][6:]]) / float(variabelnom[toke[i+3][6:]]))

                i += 4
                line += 1

            elif toke[i] == "rampung":
                rampung = True

            else:
                break

        except Exception as e:
            print("Error " + e.__str__())
            # if error:
            #     break

    if not rampung:
        print("\n======================================")
        print("Error!, enek sik salah neng kene..")
        print("Neng baris " + str(line))
        print("======================================")

        # except IndexError as e:
        #     a = "Error saat Mem-Parsing Data"
        #     sys.stderr.write("\n==Error!==============\n")
        #     sys.stderr.write(a + "\n")
        #     sys.stderr.write("Error at line " + str(line) + "\n")
        #     sys.stderr.write("Python error : " + str(e) + "\n")
        #     sys.stderr.write("======================\n")
        #     break


# python compiler.py test.jowo


def mulai(fi):
    lin = 0
    toks = compilejwlg(fi)
    print(toks)
    line = initialize_variable(toks, lin)
    print("\n" + str(toks) + "\n")
    parse(toks, line)
    print("\nFile rampung di-compile! klik enter gen metu")
    input()


if __name__ == "__main__":
    arg = sys.argv
    try:
        f = open(arg[1], "r")
    except Exception:
        a = input("Nama file = ")
        try:
            f = open(a, "r")
        except:
            sys.exit(0)
        else:
            mulai(f)
    else:
        mulai(f)
