import keyboard
import os
import json

if __name__ == "__main__":
    print("\n   Welcome to Im a Hacker (Game)")
    print(" -Made By Ihsan")
    print("1. Play")
    print("2. Settings")
    print("3. Exit\n")
    
    inp = input("Enter Number: ")
    if inp == 1:
        play()
    elif inp == 2:
        settings()
    elif inp == 3:
        exit(0)

