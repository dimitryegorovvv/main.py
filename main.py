import os
import subprocess
file = open('Logpass.in')
for line in file:
    a = line
login_file = (a.split(':')[0])
password_file = (a.split(':')[1])
login_inp = input("Введите логин: ")
password_inp = input("Введите пароль: ")
if login_file == login_inp and password_file == password_inp:
    command = input("Введите команду для запуска приложения: \n -word \n -txt \n -calc \n -power \n")
    if command == "-word":
        os.system('word.docx')
    elif command == "-txt":
        os.system('text.txt')
    elif command == "-calc":
        subprocess.run(["calc.exe"])
    elif command == "-power":
        os.system('power.pptx')
    else:
        print("Вы ввели неверную команду")
else:
    print("Вы ввели неверный логин и/или пароль")