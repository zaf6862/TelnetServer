"""
This file is just a driver code for the server.
"""


import sys
from Server import Server
import Messages



def main(argv):
    if len(argv) == 1:
        if argv[0] == "-h":
            print(Messages.correctCommand)
        elif argv[0].isdigit():
            telnetServer = Server(int(argv[0]))
            telnetServer.listen()
        else:
            print(Messages.incorrectPortNumber)
    else:
        print(Messages.incorrectCommand)


if __name__ == "__main__":
    main(sys.argv[1:])
