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
import json
from models import storage
from models.base_model import BaseModel

expected = ["BaseModel"]

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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

        if arg == "BaseModel":
            b = BaseModel()
            b.save()
            print(b.id)
        elif arg is "":
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

        if args is "":
            print("** class name missing **")
        else:
            args = args.split(' ')

            if args[0] not in expected:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                all_objs = storage.all()

                try:
                    my = all_objs["{}.{}".format(
                        args[0], args[1])]
                    
                    print(BaseModel(my))
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

        if args is "":
            # There were no args only destroy command
            print("** class name missing **")
        else:
            # There were args analyze how they were used
            args = args.split(' ')
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
                    my = all_objs["{}.{}".format(
                        args[0], args[1])]
                    del all_objs["{}.{}".format(args[0], args[1])]
                    # should the file name be a dynamic variable from __file_path?
                    # to change back to dynamoc mode search for all open() calls
                    with open("file.json", 'w') as f:
                        json.dump(all_objs, f)
                except KeyError:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name.
        (hbnb) all
        [BaseModel] (1ed39e47-8274-4ce5-a178-864247175f99) {'id': '1ed39e47.., ...)}
        ...
        ...
        Ex: $ all BaseModel or $ all
        """
        if arg is "":
            try:
                with open("file.json", 'r') as f:
                    all_objs = json.loads(f.read())
                for obj in all_objs:
                    print(BaseModel(obj))
            except FileNotFoundError:
                #file has not yet been created
                pass
        else:
            if arg not in expected:
                print("")
            try:
                with open("file.json", 'r') as f:
                    all_objs = json.loads(f.read())
                for obj_key in all_objs.keys():
                    obj = all_objs[obj_key]
                    if obj['__class__'] == "{}".format(arg):
                        print(BaseModel(obj))
            except FileNotFoundError:
                #file has not yet been created
                pass
                
        
    def emptyline(self):
        """Ensure when enter is pressed in an empty prompt
        all it does is show another prompt"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
