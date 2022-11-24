#!/usr/bin/python3
''' Implements a console for the project.
'''
import cmd


class HBNBCommand(cmd.Cmd):
    ''' The command interpreter class definition.
    '''

    prompt = "(hbnb) "

    def do_quit(self, quitt):
        ''' Quits from the interpreter. '''
        return True

    def help_quit(self):
        ''' Help for quit command. '''
        print("Quits from the interpreter.\n\tUsage: quit")

    def do_EOF(self, eof):
        ''' Exits from the interpreter. '''
        print()
        return True

    def help_EOF(self):
        ''' Help for EOF command. '''
        print("Exits from the interpreter\n\tUsage: CTRL + D")

    def emptyline(self):
        ''' Defines actions for an empty command. '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
