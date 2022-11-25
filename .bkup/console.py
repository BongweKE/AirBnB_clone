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

    def do_destroy(self, args_str):
        ''' Deletes an instance based on name and id.'''
        className = ''
        idd = ''

        if args_str:
            args_list = args_str.split()
            className = args_list[0]
            if len(args_list) > 1:
                idd = args_list[1]

        if className == '':
            print("** class name missing **")
            return

        try:
            cls = cls_of(className)
        except NameError:
            print("** class doesn't exist **")
            return

        if idd == '':
            print("** instance id missing **")
            return

        key = className + "." + idd

        all_objs = storage.all()  # collect the dict of all current objects

        try:
            del all_objs[key]
            storage.save()
        except KeyError:
            #  No instance with id, idd
            print("** no instance found **")

    def help_destroy(self):
        ''' Help for destroy command.'''
        print(
                "Deletes an instance from file storage."
                "\n\tUsage: destroy <class_name> <instance_id>")

    def do_all(self, args_str):
        ''' Prints the string representation of all instances.'''
        className = ''

        if args_str:
            args_list = args_str.split()
            className = args_list[0]

        all_objs = storage.all()  # collect the dict of all current objects
        obj_str_list = []

        if className == '':  # print all
            for key in all_objs:
                # Append each object's string representation to a list
                obj_str_list.append(str(all_objs[key]))
            print(obj_str_list)
            return

        # A potential class name was specified
        try:
            cls = cls_of(className)
            for key in all_objs:
                # Append each object's string representation to a list
                if key.startswith(className + '.'):
                    obj_str_list.append(str(all_objs[key]))
            print(obj_str_list)
        except NameError:
            print("** class doesn't exist **")
            return

    def help_all(self):
        ''' Help for all command.'''
        print(
                "Prints the string representation of all instances."
                "\n\tUsage: all [<class_name>]")

    def do_update(self, args_str):
        ''' Updates an instance based on name and id.'''
        className = ''
        idd = ''
        attr_name = ''
        attr_val = ''

        if args_str:
            args_list = args_str.split()
            className = args_list[0]
            if len(args_list) > 1:
                idd = args_list[1]
            if len(args_list) > 2:
                attr_name = args_list[2]
            if len(args_list) > 3:
                try:
                    attr_val = int(args_list[3])
                except ValueError:
                    try:
                        attr_val = float(args_list[3])
                    except ValueError:
                        attr_val = args_list[3]

        if className == '':
            print("** class name missing **")
            return

        try:
            cls = cls_of(className)
        except NameError:
            print("** class doesn't exist **")
            return

        if idd == '':
            print("** instance id missing **")
            return

        key = className + "." + idd

        all_objs = storage.all()  # collect the dict of all current objects

        try:
            obj = all_objs[key]
        except KeyError:
            #  No instance with id, idd
            print("** no instance found **")
            return

        if attr_name == '':
            print("** attribute name missing **")
            return
        if attr_val == '':
            print("** value missing **")
            return

        # Update the provided attributes
        setattr(obj, attr_name, attr_val)
        storage.save()

    def help_update(self):
        ''' Help for update command.'''
        print(
                'Updates instances with attributes.\n\tUsage: '
                'update <class name> <id> <attribute name> "<attribute val>"')


def cls_of(cls_name):
    ''' Returns the class object whose name is cls_name. '''

    match cls_name:
        case "BaseModel":
            return BaseModel
        case _:
            raise NameError


if __name__ == '__main__':
    HBNBCommand().cmdloop()
