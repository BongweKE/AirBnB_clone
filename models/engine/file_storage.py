#!/usr/bin/python3
''' Implements file storage for serialization
and deserialozation of BaseModel instances.
'''
import json
import datetime


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
                {f"{obj.__class__.__name__}.{obj.id}": obj.to_dict()})

    def save(self):
        ''' Serializes __objects to a JSON file.
        '''
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fout:
            for key in FileStorage.__objects:
                # Convert datetime objects to serializable string
                obj_dict = FileStorage.__objects[key]
                dtime_obj = obj_dict['created_at']
                if type(dtime_obj) is not str:
                    obj_dict['created_at'] = dtime_obj.isoformat()

                dtime_obj = obj_dict['updated_at']
                if type(dtime_obj) is not str:
                    obj_dict['updated_at'] = dtime_obj.isoformat()
            json.dump(FileStorage.__objects, fout)

    def reload(self):
        ''' Deserializes the JSON file into __objects dict.
        '''
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as fin:
                FileStorage.__objects = json.load(fin)
                # print(FileStorage.__objects)
                for key in FileStorage.__objects:
                    obj_dict = FileStorage.__objects[key]
                    obj_dict['created_at'] =\
                        datetime.datetime.fromisoformat(
                            obj_dict['created_at'])

                    obj_dict['updated_at'] =\
                        datetime.datetime.fromisoformat(
                            obj_dict['updated_at'])
        except FileNotFoundError:
            pass
