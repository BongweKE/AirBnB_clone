#!/usr/bin/env python3
"""a module to handle the flow of serialization-deserialization
which will be:
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump
-> <class 'str'> -> FILE
FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
"""
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all instances of objects managed using the
        FileStorage class
        """
        return type(self).__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Assumption is that the value to go with the key will be result
        of obj.to_dict()
        """
        type(self).__objects[
            f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        with open(type(self).__file_path, "w") as f:
            json.dump(type(self).__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(type(self).__file_path, 'r') as f:
                type(self).__objects = json.loads(f.read())
        except FileNotFoundError:
            pass
        except ValueError:
            pass
