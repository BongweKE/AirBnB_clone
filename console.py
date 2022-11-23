#!/usr/bin/env python3
"""a program called `console.py` that contains the entry point
of the command interpreter
You must use the module cmd
Your class definition must be: class HBNBCommand(cmd.Cmd):
Your command interpreter should implement:
quit and EOF to exit the program
help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
a custom prompt: (hbnb)
an empty line + ENTER shouldn’t execute anything
***Your code should not be executed when imported
"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_quit(self, arg):
        """Exit the console using quit command"""
        return True
    def do_EOF(self, arg):
        """Exit console using Ctrl+d"""
        return True
    def emptyline(self):
        """Ensure when enter is pressed in an empty prompt
        all it does is show another prompt"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
