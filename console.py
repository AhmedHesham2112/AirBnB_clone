#!/usr/bin/python3
"""class HBNBCommand"""

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass

    def do_create(self,line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        """
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            model = BaseModel()
            print(model.id)
            model.save()

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id.
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints the string representation of an instance based on the class name and id.
        """
        if not line:
            instances = []
            for k in storage.all():
                instances.append(str(storage.all()[k]))
            print(instances)
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            instances = []
            for k in storage.all():
                instances.append(str(storage.all()[k]))
            print(instances)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    if args[3][0] == '"':
                        args[3] = args[3].replace('"', '')
                    elif "." in args[3]:
                        args[3] = float(args[3])
                    else:
                        args[3] = int(args[3])
                    storage.all()[key].__dict__[args[2]] = args[3]
                    storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
