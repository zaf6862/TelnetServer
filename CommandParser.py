import Messages


class CommandParser:
    """
    This class is the main logic of the application.
    It parses each of the commands that the user inputs
    and generates appropriate response.

   ...

   Attributes
   ----------
    variableDict : dict
        A dictionary that keeps track of all the variables that a client has initialized.

    validChars : str
        A string that contains all the valid characters that can be used in a variables name.


   Methods
   -------
    isValidNumber()
       This method checks if the given token is a valid number or not.

    isValidVarName()
        This method checks if the given variable name is valid or not.

    isValidAssignmentExp()
        This method checks if the assignment expression input by the user is valid or not.

    parseCommand()
        This method parses the command input by the user and generates appropriate response.

   """
    def __init__(self):
        """
        Initializes the class variables.
        """
        self.variableDict = {}
        self.validChars = "abcdefghijklmnopqrstuvwxyz0123456789_"

    def isValidNumber(self, token):
        """
        Check if the input token is a valid number or not.

        :param token: str

        :return:
            True : If the token is a valid number.
            False: If the token is not a valid number.
        """
        if token.count("-") > 1:
            return False
        return token.lstrip('-').replace('.', '', 1).isdigit()

    def isValidVarName(self, varName):
        """
        Check if varName is a valid name for a variable.

        :param varName: str
        :return:
            True: If varName is a valid variable name.
            False: If varName is not a valid variable name.

        """
        varName = varName.lower()
        for eachChar in varName:
            if not eachChar in self.validChars:
                return False
        return True

    def isValidAssignmentExp(self, command):
        """
        Checks if the command input by the user is a valid assignment expression.
        A valid assignment is of the form <variableName> = <variableValue>.
        This method does not currently support assignments of the type x = y = 1
        or just x = y. It only supports assignments of the form x = 1 or y = 2.

        :param command: str
        :return:
            True: If command is a valid assignment expression.
            False: If command is not a valid assignment expression.
        """
        if command.count("=") != 1:
            return False

        command = command.split("=")
        variableName = command[0]
        variableValue = command[1]
        if len(variableName.strip().split(" ")) != 1:
            return False

        if not self.isValidVarName(variableName.strip()):
            return False

        if not self.isValidNumber(variableValue.strip()):
            return False

        return True

    def parseCommand(self, command):
        """
        Parses the command input by the user and generates appropriate response to send back to the client.

        :param command: str
        :return:
            Various strings based on the type of the command.
        """
        command = command.strip()
        validAssignmentExp = self.isValidAssignmentExp(command)
        if command.lower() == "author":
            return "Zaid Ahmed Farooq"
        elif command.lower() == "hello":
            return "World"
        elif command.lower() == "help":
            return Messages.help
        elif command.lower() == "stop":
            return "Stop"
        elif validAssignmentExp: # if the command is a valid assignment expression.
            command = command.split("=")
            command[0] = command[0].strip()
            command[1] = command[1].strip()
            if "." in command[1]:
                self.variableDict[command[0]] = float(command[1])
            else:
                self.variableDict[command[0]] = int(command[1])

            return command[0] + " has been set to " + command[1]

        # if the command is fetching an already initialized variable
        elif len(command.split(" ")) == 1 and self.isValidVarName(command):
            if command in self.variableDict.keys():
                return self.variableDict[command]
            else:
                return "Variable \"" + command + "\" is not found."
        else:
            try:
                # This is currently unsafe. More details in the README file.
                result = eval(command, {'__builtins__': None}, self.variableDict)
                return result
            except:
                # If all else failed then the command must be either incorrect or unsupported.
                return Messages.incorrectCommand
