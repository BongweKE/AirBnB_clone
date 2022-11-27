#!/usr/bin/env python3
"""a module to handle the flow of serialization-deserialization
which will be:
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump
-> <class 'str'> -> FILE
FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
"""
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all instances of objects managed using the
        FileStorage class
        """
        self.reload()
        return type(self).__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Assumption is that the value to go with the key will be result
        of obj.to_dict()
        """
        type(self).__objects[
            "{:s}.{:s}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        all_objs = type(self).__objects
        all_good = {}
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            all_good[obj_id] = obj.to_dict()

        with open(type(self).__file_path, "w") as f:
            json.dump(all_good, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        from models.get_class import get_class
        # file access using json:
        filename = type(self).__file_path
        # ensure file exists
        isExists = os.path.exists(filename)
        # and is not empty
        isEmpty = isExists and os.stat(filename).st_size == 0
        # for it to be useful with json
        isUseful = isExists and not isEmpty

        if isUseful:
            with open(filename, 'r') as f:
                all_objs = json.loads(f.read())

                for obj_key in all_objs.keys():
                    ze_cls = get_class(all_objs[obj_key])
                    type(self).__objects[obj_key] = ze_cls(
                        **all_objs[obj_key])
                self.save()
