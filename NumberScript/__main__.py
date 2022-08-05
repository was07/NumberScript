from interpreter import Interpreter
import argparse
import os
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", help="file to interpret")

args = parser.parse_args()
run = True

help = """
0 <- start
1 <- end
2 <- print
3 <- var
4 <- Compare
% <- comment
^ <- Math-Operation-Start
"""

space = ""
for j in range(0, 16):
    space += " "

for k in range(0, len(os.name)):
    space = space.replace(" ", "", 1)

if args.file:
    with open(args.file, "r") as file:
        code = file.read()
        code = code.replace("\n", " ")
        Interpreter.interpret(code)
else:
    print(f"""
        +------------------------------------------+
        | NumberScript Shell: Type 'exit' to exit. |
        | Version: 1.6.1 Machine: {os.name} {space}|
        | Type 'help' for more information.        |
        | {current_time}                                 |
        +------------------------------------------+
    """)
    while run:
        code = input(">")
        if code == "exit":
            run = False
        elif code == "help":
            print(help)
        else:
            Interpreter.interpret(Interpreter, code)