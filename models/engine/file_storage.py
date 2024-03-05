#!/usr/bin/python3
"""class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances"""

import datetime
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """Class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = type(obj).__name__
        keyid = str(obj.id)
        FileStorage.__objects[key + "." + keyid] = obj
        

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dic = {}
        for k,v in FileStorage.__objects.items():
            dic[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(dic, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                json_load = json.load(file)
            for k, v in json_load.items():
                FileStorage.__objects[k] = BaseModel(**v)
        except:
            pass
