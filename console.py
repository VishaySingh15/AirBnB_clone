#!/usr/bin/python3
"""

This module contains the entry point of the command interpreter

"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    This class defines the interpreter for the project
    """

    prompt = "(hbnb) "

    def do_quit(self, line):

        return True

    def do_EOF(self, line):
        return True

    def help_quit(self):
        """
        Displays info for quit command
        """

        print('Quit command to exit the program\n')

    def help_EOF(self):
        """
        Displays info for EOF command
        """

        print("EOF character exits the program\n")

    def emptyline(self):
        """
        Overrides the BaseClass method emptyline
        """

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
