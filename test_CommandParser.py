import unittest
from CommandParser import CommandParser
import Messages


class Test(unittest.TestCase):
    """
    This class runs unit tests for the commandParser class.

   ...

   Attributes
   ----------
   None

   Methods
   -------
    test_isValidVarName()
       Tests the isValidVarName method of the commandParser class.

    test_isValidNumber()
       Tests the isValidNumnber method of the commandParser class.

    test_isValidAssignmentExpression()
       Tests the isValidAssignmentExpression method of the commandParser class.

    test_parseCommand()
       Tests the parseCommand method of the commandParser class.

   """


    commandParser = CommandParser()

    def test_isValidVarName(self):
        """
        Tests the isValidVarName method of the commandParser class.

        :return:
            None
        """
        print("\nStart isValidVarName test.")
        self.assertEqual(self.commandParser.isValidVarName("x"), True)
        self.assertEqual(self.commandParser.isValidVarName("x1"), True)
        self.assertEqual(self.commandParser.isValidVarName("x1-12["), False)
        self.assertEqual(self.commandParser.isValidVarName("x_1"), True)
        self.assertEqual(self.commandParser.isValidVarName("x x y z"), False)
        self.assertEqual(self.commandParser.isValidVarName("xxyz"), True)
        self.assertEqual(self.commandParser.isValidVarName("x@z"), False)
        self.assertEqual(self.commandParser.isValidVarName("z1.1"), False)
        print("Finished isValidVarName test. All tests passed.\n")

    def test_isValidNumber(self):
        """
        Tests the isValidNumber method of the commandParser class.

        :return:
            None
        """
        print("\nStart isValidNumber test.")
        self.assertEqual(self.commandParser.isValidNumber("10"), True)
        self.assertEqual(self.commandParser.isValidNumber("-10"), True)
        self.assertEqual(self.commandParser.isValidNumber("1.2432"), True)
        self.assertEqual(self.commandParser.isValidNumber("-0.000121"), True)
        self.assertEqual(self.commandParser.isValidNumber("-121212341"), True)
        self.assertEqual(self.commandParser.isValidNumber("1.2.2.3.4"), False)
        self.assertEqual(self.commandParser.isValidNumber("112abcd"), False)
        self.assertEqual(self.commandParser.isValidNumber("1()1"), False)
        self.assertEqual(self.commandParser.isValidNumber("-+*2"), False)
        self.assertEqual(self.commandParser.isValidNumber("-----554.12"), False)
        print("Finished isValidNumber test. All tests passed.\n")

    def test_isValidAssignmentExpression(self):
        """
        Tests the isValidAssignmentExpression method of the commandParser class.

        :return:
            None
        """

        print("\nStart isValidAssignmentExp test.")
        self.assertEqual(self.commandParser.isValidAssignmentExp("x = 1"), True)
        self.assertEqual(self.commandParser.isValidAssignmentExp("x1 = 1"), True)
        self.assertEqual(self.commandParser.isValidAssignmentExp("x = = 1"), False)
        self.assertEqual(self.commandParser.isValidAssignmentExp("x"), False)
        self.assertEqual(self.commandParser.isValidAssignmentExp("x y z = 12"), False)
        self.assertEqual(self.commandParser.isValidAssignmentExp("x = y = z = 12"), False)
        self.assertEqual(self.commandParser.isValidAssignmentExp("x = y"), False)
        print("Finished isValidAssignmentExp test. All tests passed.\n")

    def test_parseCommand(self):
        """
        Tests the parseCommand method of the commandParser class.

        :return:
            None
        """

        print("\nStart parseCommand test.")
        self.assertEqual(self.commandParser.parseCommand("x = 5"), "x has been set to 5")  # simplest assignment test
        self.assertEqual(self.commandParser.parseCommand("y = 10"), "y has been set to 10")  # simplest assignment test
        self.assertEqual(self.commandParser.parseCommand("y1 = 6"),
                         "y1 has been set to 6")  # alphanumeric variable name test
        self.assertEqual(self.commandParser.parseCommand("z = 3.14"), "z has been set to 3.14")  # float assignment test
        self.assertEqual(self.commandParser.parseCommand("p = -0.9112"),
                         "p has been set to -0.9112")  # negative float assignment test
        self.assertEqual(self.commandParser.parseCommand("p = x = -0.9112"),
                         Messages.incorrectCommand)  # double assignment test
        self.assertEqual(self.commandParser.parseCommand("x"), 5)  # fetch variable test
        self.assertEqual(self.commandParser.parseCommand("x + y1"), 11)  # operation on stored variables
        self.assertEqual(self.commandParser.parseCommand("z ** p"),
                         0.35253131799965065)  # operation on stored variables
        self.assertEqual(self.commandParser.parseCommand("12 ** 3"), 1728)  # exponent operation test
        self.assertEqual(self.commandParser.parseCommand("(x+y)*2/6"), 5)  # operation on stored variables with
        # parentheses
        self.assertEqual(self.commandParser.parseCommand("k = -----2"), Messages.incorrectCommand)  # incorrect
        # variable value. There can only be 0 or 1 prefix negative signs.
        self.assertEqual(self.commandParser.parseCommand("k(12 = 2"), Messages.incorrectCommand)  # incorrect variable
        # name
        self.assertEqual(self.commandParser.parseCommand("k 12 34 abc = 2"), Messages.incorrectCommand)  # incorrect
        # assignment expression.
        self.assertEqual(self.commandParser.parseCommand("1/ 0"), Messages.incorrectCommand)  # division by zero error
        print("Finished parseCommand test. All tests passed.")


if __name__ == "__main__":
    unittest.main()
