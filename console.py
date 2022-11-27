#!/usr/bin/env python3
"""a program called `console.py` that contains the entry point
of the command interpreter
You must use the module cmd
Your class definition must be: class HBNBCommand(cmd.Cmd):
Your command interpreter should implement:
quit and EOF to exit the program
help (this action is provided by default by
cmd but you should keep it updated and documented as you work through tasks)
a custom prompt: (hbnb)
an empty line + ENTER shouldn’t execute anything
***Your code should not be executed when imported

__________________________
ASSUMPTIONS
__________________________
-You can assume arguments are always in the right order
-Each arguments are separated by a space
-A string argument with a space must be between double quote
-The error management starts from the first argument to the last one
"""
import cmd
import json
import os
from models import storage
from models.get_class import get_class
from models.get_class import expected


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    args = [
        "email", "password", "first_name", "last_name", "name",
        "state_id", "city_id", "user_id", "description", "number_rooms",
        "number_bathrooms", "max_guest", "price_by_night", "longitude",
        "latitude", "amenity_ids", "place_id", "text", "BaseModel", "User",
        "Place", "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """Exit the console using quit command
        (hbnb) quit"""
        return True

    def do_EOF(self, arg):
        """Exit console using Ctrl+d
        (hbnb) Ctrl+d"""
        return True

    def do_create(self, arg):
        """Create an instance of a model and
        save it to the Json file then print id
        of created instance
        _______________________________
        Examples
        _______________________________

        (hbnb) create BaseModel
        78dbc774-725e-4b86-982f-edf4e6cb186d
        ________________________
        Expected Errors:
        ________________________

        (hbnb) create
        ** class name missing **
        (hbnb) create NotListed
        ** class doesn't exist **
        """

        if arg in expected:
            my_model = expected[arg]()
            my_model.save()
            print(my_model.id)
            storage.save()
        elif arg == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        '''Prints the string representation of an
        instance based on the class name and id.
        _______________________________
        Examples
        _______________________________

        (hbnb) show BaseModel 1234-1234-1234
        78dbc774-725e-4b86-982f-edf4e6cb186d
        ________________________
        Expected Errors:
        ________________________

        (hbnb) show Unlisted
        ** class doesn't exist **
        (hbnb) show BaseModel
        ** instance id missing **
        (hbnb) show BaseModel Fake-ID
        ** no instance found **
        '''

        if args == "":
            print("** class name missing **")
        else:
            args = [s.strip('"') for s in args.split(' ')]

            if args[0] not in expected:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                all_objs = storage.all()

                try:
                    my = all_objs["{}.{}".format(
                        args[0], args[1])]
                    print(my)

                except KeyError:
                    print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the
        class name and id (save the change into the JSON file).
        _______________________________
        Examples
        _______________________________

        (hbnb) destroy BaseModel 78dbc774-725e-4b86-982f-edf4e6cb186d
        ________________________
        Expected Errors:
        ________________________
        (hbnb) destroy BaseModel
        ** instance id missing **
        (hbnb) destroy
        ** class name missing **
        (hbnb) destroy FakeClass REAL-ID/FakeID
        ** class doesn't exist **
        (hbnb) destroy BaseModel FakeID
        ** no instance found **
        """

        if args == "":
            # There were no args only destroy command
            print("** class name missing **")
        else:
            # There were args analyze how they were used
            args = [s.strip('"') for s in args.split(' ')]
            if args[0] not in expected:
                # Class name given is not in the list
                print("** class doesn't exist **")
            elif len(args) < 2:
                # No id of instance given
                print('** instance id missing **')
            else:
                # look for the instance
                all_objs = storage.all()

                try:
                    del all_objs["{}.{}".format(args[0], args[1])]
                    storage.save()

                except KeyError:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name.
        _______________________________
        Examples
        _______________________________

        (hbnb) all
        [BaseModel] (1ed39e47-8274-4ce5-a178-864247175f99)\
        {'id': '1ed39e47.., ...)}
        ...
        ...
        (hbnb) all BaseModel
        [BaseModel] (1ed39e47-8274-4ce5-a178-864247175f99)\
        {'id': '1ed39e47.., ...)}
        ...
        ...
        _______________________________
        Expected Error(s)
        _______________________________

        (hbnb) all FakeClass
        ** class doesn't exist **
        Ex: $ all BaseModel or $ all
        """
        storage.reload()

        if arg == "":
            # change back to read only once you shift back from temp fix
            all_objs = storage.all()
            temp = []
            for obj_key in all_objs.keys():
                temp.append(str(all_objs[obj_key]))

            print(temp)

        else:
            # user of the console supplied an argument for class to print all
            # instances of
            if arg not in expected:
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                temp = []
                for obj_key in all_objs.keys():
                    obj = all_objs[obj_key]
                    if obj.__class__.__name__ == "{}".format(arg):
                        temp.append(str(obj))
                print(temp)

    def do_update(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).

        -Only one attribute can be updated at the time
        -You can assume the attribute name is valid (exists for this model)
        -The attribute value must be casted to the attribute type

        id, created_at and updated_at can't  be updated.
        You can assume they won't be passed in the update command

        Usage: update <class name> <id> <attribute name> "<attribute value>"

        (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        _______________________________
        Examples
        _______________________________

        _______________________________
        Expected Error(s)
        _______________________________

        (hbnb) update
        ** class name missing **

        (hbnb) update FakeClass
        ** class doesn't exist **

        (hbnb) update BaseModel
        ** instance id missing **

        (hbnb) update BaseModel FakeID
        ** no instance found **

        (hbnb) update BaseModel RealID
        ** attribute name missing **

        (hbnb) update BaseModel RealID email
        ** value missing **

        """
        if args == "":
            print("** class name missing **")
        else:
            args = [s.strip('"') for s in args.split(' ')]
            la = len(args)
            if args[0] not in expected:
                print("** class doesn't exist **")
            elif la == 1:
                print("** instance id missing **")
            else:
                all_objs = storage.all()
                try:
                    my = all_objs["{}.{}".format(args[0], args[1])].to_dict()
                    if la <= 2:
                        print("** attribute name missing **")
                    elif la <= 3:
                        print("** value missing **")
                    else:
                        my[args[2]] = args[3]
                        # hot fix-ish
                        # (had to open json file)
                        with open("file.json", 'r') as f:
                            all_json = json.loads(f.read())
                        with open("file.json", 'w') as f:
                            all_json["{}.{}".format(args[0], args[1])] = my
                            json.dump(all_json, f)
                            storage.reload()
                except KeyError:
                    print("** no instance found **")

    def do_count(self, clsName):
        ''' Count the number of instances of the specified class.
        Usage: <class_name>.count()'''
        count = 0

        for key in storage.all().keys():
            if key.split('.')[0] == clsName:
                count += 1
        print(count)

    # ----------------------------------------------
    # CMD METHODS
    # ----------------------------------------------

    def precmd(self, line):
        """A function to handle expected console cmds
        which don't need to have a do_cmd fxn
        since they might cause redundancy.
        Solution is through str->array->str conversions
        using strip and split functions
        """
        try:
            simple_cmds = ["all", "count", "show"]
            s = line.split('.')
            s[1], temp = s[1].split('(')
            temp = f"({temp}"
            s.append(temp)
            # given User.all()
            # s = ['User', 'all', '()']

            if s[1] in simple_cmds:
                return f"{s[1]} {s[0]}"
            elif s[1] == "destroy":
                s[2].strip('"()')
                return f"{s[1]} {s[0]} {s[2]}"
            elif s[1] == "update":
                idd, name, val = [
                    i.strip('"') for i in s[2].strip("()").split(", ")]
                return f"{s[1]} {s[0]} {idd} {name} {val}"
            else:
                return line
        except IndexError:
            # to avoid EOF problems
            return line

    def emptyline(self):
        """Ensure when enter is pressed in an empty prompt
        all it does is show another prompt"""
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

    # -----------------------------------------------------------
    # SUPPORTING METHODS
    # -----------------------------------------------------------


if __name__ == '__main__':
    HBNBCommand().cmdloop()
