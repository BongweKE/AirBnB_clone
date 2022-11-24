#!/usr/bin/python3
''' Implements a console for the project.
'''
import cmd
from models import storage
from models.base_model import BaseModel


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

    def do_create(self, className):
        ''' Creates a new instance of BaseModel. '''
        if className == '':
            print("** class name missing **")
            return

        try:
            cls = cls_of(className)
            inst = cls()
            inst.save()
            print(inst.id)
        except NameError:
            print("** class doesn't exist **")

    def help_create(self):
        ''' Help for create command. '''
        print(
                "Creates a new instance of BaseModel."
                "\n\tUsage: create <class_name>")

    def do_show(self, className, idd=None):
        ''' Prints the string representation of
        an instance based on the class name and id.
        '''
        if className:
            args = className.split()
            className = args[0]
            if len(args) > 1:
                idd = args[1]

        if className == '':
            print("** class name missing **")
            return

        try:
            cls = cls_of(className)
        except NameError:
            print("** class doesn't exist **")
            return

        if idd is None:
            print("** instance id missing **")
            return

        key = className + "." + idd
        print(key)

        all_objs = storage.all()  # collect the dict of all current objects
        try:
            obj = all_objs[key]
            print(obj)  # instance found
        except KeyError:
            #  No instance with id, idd
            print("** no instance found **")

    def help_show(self):
        ''' Help for show command.'''
        print(
                "Prints the string representation ofan instance."
                "\n\tUsage: show <className> <instance_id>")


def cls_of(cls_name):
    ''' Returns the class object whose name is cls_name. '''

    match cls_name:
        case "BaseModel":
            return BaseModel
        case _:
            raise NameError


if __name__ == '__main__':
    HBNBCommand().cmdloop()
