import os
import platform
import runner


def main():
    print("+=============================+")
    print("| JowoLanguage Compiler       |")
    print("| Digawe pas 21 Agustus 2018  |")
    print("| Digawe oleh Ihsan           |")
    print("| neng " + platform.system())
    print("+=============================+")
    print("\n")
    os.system("title JowoLanguage File Compiler By Ihsan")
    while True:
        eror = runner.runner(input("jwlg-" + runner.ver + "#> "))
        if eror == "heh mas.. aku meh metu":
            break
        elif eror != "":
            print("Heh.. mas... enek sek salah neng kene...")
            print("Jare compilere : " + eror)
        print("")
    print("Rampung, klik enter gen metu")


if __name__ == "__main__":
    main()
    input()
