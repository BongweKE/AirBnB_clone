#!/usr/bin/python3
''' Implements file storage for serialization
and deserialozation of BaseModel instances.
'''
import json
import datetime

try:
    from models.base_model import BaseModel
except ImportError:
    pass


class FileStorage:
    ''' A class that provides the necessary file storage methods and attributes
    '''

    __file_path = "objects.json"
    __objects = {}

    def all(self):
        ''' Returns the private attribute, __objects.
        '''
        return FileStorage.__objects

    def new(self, obj):
        ''' Adds obj to the storage dictionary.
        '''
        FileStorage.__objects.update(
                {f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        ''' Serializes __objects to a JSON file.
        '''
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fout:
            srlzd_objs = {}  # the serialized form of __objects
            for key in FileStorage.__objects:
                # Convert each object in __objects to serializable forms
                obj = FileStorage.__objects[key]  # object for each key
                obj_dict = obj.to_dict()  # serializable form of obj
                srlzd_objs.update({key: obj_dict})  # update with serializables
            json.dump(srlzd_objs, fout)  # serialize __objects

    def reload(self):
        ''' Deserializes the JSON file into __objects dict.
        '''
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as fin:
                # from models.base_model import BaseModel
                from classes import cls_of
                objects = json.load(fin)  # collect all saved objects
                for key in objects:
                    # Recursively create objects from the collection
                    cls_name = key.split('.')[0]  # get class name from key
                    cls = cls_of(cls_name)  # get class reference
                    obj = cls(**(objects[key]))  # create a BaseModel instance
                    FileStorage.__objects.update({key: obj})  # upd __objects
        except FileNotFoundError:
            pass
