"""
This file contains the various messages that are used across the application.
"""

correctCommand = "\npython3 TelnetServer.py <portNumber>\n"

incorrectRuntCommand = "\nInvalid run command. Correct run command structure:\n" + correctCommand

incorrectPortNumber = "\nInvalid port number. Please enter a postive integer as the port number.\n"

incorrectCommand = "\nThe command you entered is either invalid or not currently supported.\n" \
                                "Make sure you are doing the following:\n" \
                                "1)Only use assigned variables.\n" \
                                "2)Only use supported operators for mathematical expressions.\n" \
                                "3)Input a valid mathematical expression.\n" \
                                "4)Input a valid assignmnet expression.\n" \
                                "You can type Help to see more details.\n"

help = "\nFollowing are the commands supported by this server:\n\n" \
       "1) Author: Return the name of the code author (the candidate in this case).\n\n" \
       "2) Hello: Return the word \"World\".\n\n" \
       "3) Help: Prints out this message that you are reading right now.\n\n" \
       "4) Variable Assignment: These are commands of the type <variableName> = <variableValue>." \
       "Decimals and negative numbers are allowed for <variableValue>. <variableName> should an alphanumeric string without spaces in-between.\n\n" \
       "5) Mathematical Expressions: These are commands of the type <operand> <operator> <operand>. " \
       "The <operand>s in this case can either be constants or stored variables. The operations supported are +,-,*,/ and **." \
       "There can of course be any number of <operand>s and <operator>s, as long as, they create a valid mathematical expression.\n\n" \
       "6) Stop: This ends you connection with the server and exits the telnet client.\n\n"


