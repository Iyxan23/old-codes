import os
import sys

# variabel
ver = "1.0"


def runner(cmd):
    elol = ""
    if cmd == "":
        pass
    else:
        cmd = cmd.split()
        if cmd[0] == "tulis":
            try:
                if cmd[1] == "dalan":
                    for a in sys.path: print(a)
                else:
                    elol = "Aku ramudeng, " + cmd[1] + " kui opo??"
            except IndexError:
                elol = "mass ngopo koe nulis 'tulis' THOK???"
        elif cmd[0] == "metu" and len(cmd) == 1:
            elol = "heh mas.. aku meh metu"
        elif cmd[0] == "koe":
            try:
                if cmd[1] == "elek":
                    elol = "._."
            except IndexError:
                elol = "mas.. kurang kata2 ne"
        elif cmd[0] == "jalanke":
            hasil = ""
            try:
                cmd.remove("jalanke")
                for a in cmd:
                    hasil = hasil + a + " "
            except FileNotFoundError:
                elol = "ranek file neng " + hasil
                return elol
            except IndexError:
                elol = "MASS!! nek nulis perintah yoo sik bener no mas... >_<"
                return elol
            else:
                fi = open("out.bat", "w")
                fi.write("""
REM           Digawe dengan sendirinya.. mohon jangan diedit.
title """ + hasil + """
cd python
python.exe ../compiler.py """ + hasil + """
echo RAMPUNG DIEKSEKUSI!
echo monggo metu.. XD
set /p agwedfjqhswgfj=Klik enter gen metu..
exit
""")
                fi.close()

        else:
            elol = "mass!! aku ramudeng '" + cmd[0] + "' kui opo??"

    return elol

