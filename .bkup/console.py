#!/usr/bin/python3
''' Implements a console for the project.
'''
# from classes import cls_of
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    ''' The command interpreter class definition.
    '''

    prompt = "(hbnb) "
    args = [
            "email", "password", "first_name", "last_name", "name",
            "state_id", "city_id", "user_id", "description", "number_rooms",
            "number_bathrooms", "max_guest", "price_by_night", "longitude",
            "latitude", "amenity_ids", "place_id", "text", "BaseModel", "User",
            "Place", "State", "City", "Amenity", "Review"]

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

    def completedefault(self, text, line, begidx, endidx):
        ''' Auto argument completion implementation.'''
        completions = []
        if not text:
            # No prefix text to match yet
            completions.extend(self.args)  # return full list
        else:
            # There is some prefix text
            for name in self.args:
                if name.startswith(text):
                    completions.append(name)
        return completions

    def precmd(self, line):
        line_list = line.split()
        left_split = line_list[0].split('(')[0]
        pattern = left_split + '('  # pattern should look like `User.show(`

        match pattern:
            case "User.all(":
                line = "all User"
                return line
            case "BaseModel.all(":
                line = "all BaseModel"
                return line
            case "Place.all(":
                line = "all Place"
                return line
            case "State.all(":
                line = "all State"
                return line
            case "City.all(":
                line = "all City"
                return line
            case "Amenity.all(":
                line = "all Amenity"
                return line
            case "Review.all(":
                line = "all Review"
                return line
# ------------------------------------------
            case "User.count(":
                line = "count User"
                return line
            case "BaseModel.count(":
                line = "count BaseModel"
                return line
            case "Place.count(":
                line = "count Place"
                return line
            case "State.count(":
                line = "count State"
                return line
            case "City.count(":
                line = "count City"
                return line
            case "Amenity.count(":
                line = "count Amenity"
                return line
            case "Review.count(":
                line = "count Review"
                return line
# -------------------------------------------
            case "User.show(":
                idd = get_id(line)
                line = f"show User {idd}"
                return line
            case "BaseModel.show(":
                idd = get_id(line)
                line = f"show BaseModel {idd}"
                return line
            case "Place.show(":
                idd = get_id(line)
                line = f"show Place {idd}"
                return line
            case "State.show(":
                idd = get_id(line)
                line = f"show State {idd}"
                return line
            case "City.show(":
                idd = get_id(line)
                line = f"show City {idd}"
                return line
            case "Amenity.show(":
                idd = get_id(line)
                line = f"show Amenity {idd}"
                return line
            case "Review.show(":
                idd = get_id(line)
                line = f"show Review {idd}"
                return line
# -------------------------------------------
            case "User.destroy(":
                idd = get_id(line)
                line = f"destroy User {idd}"
                return line
            case "BaseModel.destroy(":
                idd = get_id(line)
                line = f"destroy BaseModel {idd}"
                return line
            case "Place.destroy(":
                idd = get_id(line)
                line = f"destroy Place {idd}"
                return line
            case "State.destroy(":
                idd = get_id(line)
                line = f"destroy State {idd}"
                return line
            case "City.destroy(":
                idd = get_id(line)
                line = f"destroy City {idd}"
                return line
            case "Amenity.destroy(":
                idd = get_id(line)
                line = f"destroy Amenity {idd}"
                return line
            case "Review.destroy(":
                idd = get_id(line)
                line = f"destroy Review {idd}"
                return line
# -------------------------------------------
            case "User.update(":
                cmd, idd, name, val = get_updAttrs(line)
                line = f"{cmd} User {idd} {name} {val}"
                return line
            case "BaseModel.update(":
                cmd, idd, name, val = get_updAttrs(line)
                line = f"{cmd} BaseModel {idd} {name} {val}"
                return line
            case "Place.update(":
                cmd, idd, name, val = get_updAttrs(line)
                line = f"{cmd} Place {idd} {name} {val}"
                return line
            case "State.update(":
                cmd, idd, name, val = get_updAttrs(line)
                line = f"{cmd} State {idd} {name} {val}"
                return line
            case "City.update(":
                cmd, idd, name, val = get_updAttrs(line)
                line = f"{cmd} City {idd} {name} {val}"
                return line
            case "Amenity.update(":
                cmd, idd, name, val = get_updAttrs(line)
                line = f"{cmd} Amenity {idd} {name} {val}"
                return line
            case "Review.update(":
                cmd, idd, name, val = get_updAttrs(line)
                line = f"{cmd} Review {idd} {name} {val}"
                return line
            case _:
                if line.startswith(' '):
                    first_word = line.split()[1]
                else:
                    first_word = line.split()[0]

                if '(' in first_word:
                    # `clsName.cmd()` command without any, or valid, clsName
                    cmd = first_word.split('(')[0]
                    return cmd  # command without class name
                return line
# -------------------------------------------

    def do_count(self, args_str):
        ''' Count the number of instances of the specified class.'''
        count = 0
        clsName = args_str.split()[0]  # retrieve class name from argument

        for key in storage.all():
            if key.startswith(clsName + '.'):
                count += 1
        print(count)

    def help_count(self):
        ''' Help for count command.'''
        print(
                "Count the number of instances of the specified class."
                "\n\tUsage: <class_name>.count()")

    def do_create(self, className):
        ''' Creates a new instance of BaseModel. '''
        from classes import cls_of

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
        from classes import cls_of

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
        from classes import cls_of

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
        from classes import cls_of

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
        from classes import cls_of

        className = ''
        idd = ''
        attr_name = ''
        attr_val = ''
        idx = 0

        if args_str:
            args_list = args_str.split()
            className = args_list[idx]
            idx += 1
            if len(args_list) > 1:
                idd = args_list[idx]
                idx += 1
            if len(args_list) > 2:
                attr_name = args_list[idx]
                idx += 1
            if len(args_list) > 3:
                attr_val, idx = get_quoted(args_list, idx)

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

        try:
            # Get type of attribute value
            attr_type = type(getattr(cls, attr_name))
        except AttributeError:
            print("** attribute name missing **")
            return

        try:
            # Attempt type-casting
            attr_val = attr_type(attr_val)  # typecast to class-defined type
        except (ValueError, TypeError):
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


def get_quoted(str_list, index):
    ''' Returns a quoted string from str_list, starting from index idx.

    Args:
        str_list (list): list of strings
        idx (int): the start index of the potentially quoted string in list

    Return:
        2-tuple: where the first item is the
        potentially quoted string, stripped of the double quotes,
        and the second item is end index of the string in the list.

    Note: there has to be a word in str_list that ends with the
    double quote character, otherwise the result is undefined.
    '''

    s = str_list[index]
    idx = index
    list_len = len(str_list)

    if s.startswith('"') and not s.endswith('"') and index != list_len - 1:
        # Find word with closing double quotes in str_list
        for i in range(index + 1, list_len):  # starts from idx of next word
            if str_list[i].endswith('"'):
                # Last word in quoted string found
                s += ' ' + str_list[i]
                idx = i
                break
            s += ' ' + str_list[i]  # original space striped off by splitting

    s = s.strip('"')
    return (s, idx)


def get_id(line):
    ''' Returns the id string from the cmd line `<cls_name>.show(<id>)`
    '''
    id_left_paren = line.split('(')[1]  # id + left parenthesis
    id = id_left_paren.split(')')[0]  # id with possible double quote char
    id = id.strip('"')  # strip possible left and right double quotes

    return id


def get_updAttrs(line):
    ''' Return a 4-tuple containing cmd, id, attr name, and value from the
    cmd line <class name>.update(<id>, <attribute name>, <attribute value>).

    Note: the three attributes in parentheses
    must be separated by a comma, optionally followed by a space character.
    '''

    strpd_attr_list = ['', '', '', '']
    if '{' in line and '}' in line:
        # A dictionary of attributes to update present
        strpd_attr_list[0] = 'update2'  # line to be dispatched to update2 cmd
    else:
        # A single attribute to update
        strpd_attr_list[0] = 'update'  # line to be dispatched to `update` cmd

    attrs_left_paren = line.split('(')[1]  # attributes + left parenthesis
    attrs = attrs_left_paren.split(')')[0]  # attrs with possible dbl quotes
    if '{' in attrs:
        # Get id stripped of comma, space, and double quote characters
        id = attrs.split('{')[0].strip(', "')
        # Get dictionary of attributes
        attr_dct = '{' + attrs.split('{')[1]  # '{' char was removed by split
        attr_dct = attr_dct.split('}')[0] + '}'  # ignore extra char after '}'
        strpd_attr_list[1:3] = [id, attr_dct]
        return strpd_attr_list

    # Parse attributes for the `update` command handler
    attr_list = attrs.split(',')  # get list of comma_separated args
    attr_list = [x.strip() for x in attr_list]  # strip whitespace

    for i in range(len(attr_list)):
        if i >= len(strpd_attr_list) - 1:
            # In case of more than 3 attributes in parentheses
            break
        attr = attr_list[i]
        if i == 2:
            # Do not strip argument value string; to be parsed by `update` cmd
            strpd_attr_list[i + 1] = attr
        else:
            strpd_attr_list[i + 1] = attr.strip('"')

    return strpd_attr_list


if __name__ == '__main__':
    HBNBCommand().cmdloop()
