#!/usr/bin/python3
"""

This module contains the entry point of the command interpreter

"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This class defines the interpreter for the project
    """

    prompt = "(hbnb) "
    __CLASS_LIST = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_quit(self, line):

        return True

    def do_EOF(self, line):
        return True

    def help_quit(self):
        """
        Displays info for quit command
        """

        print('Quit command to exit the program\n')

    def help_EOF(self):
        """
        Displays info for EOF command
        """

        print("EOF character exits the program\n")

    def emptyline(self):
        """
        Overrides the BaseClass method emptyline
        """

        pass

    def do_create(self, class_name):
        if not class_name:
            print("** class name missing **")
        elif class_name not in HBNBCommand.__CLASS_LIST:
            print("** class doesn't exist **")
        else:
            exec("self.obj=" + class_name + "()")
            storage.new(self.obj)
            storage.save()
            print(self.obj.id)

    def help_create(self):
        """
        Displays info for create command
        """

        print("create [class name]\n")

    def do_show(self, line):
        if not line:
            print("** class name missing **")
        elif line.split()[0] not in HBNBCommand.__CLASS_LIST:
            print("** class doesn't exist **")
        elif len(line.split()) < 2:
            print("** instance id missing **")
        else:
            obj_id = line.split()[0] + "." + line.split()[1]
            if obj_id not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[obj_id])

    def help_show(self):
        """
        Displays info for show command
        """

        print("show [class name] [instance id]\n")

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
        elif line.split()[0] not in HBNBCommand.__CLASS_LIST:
            print("** class doesn't exist **")
        elif len(line.split()) < 2:
            print("** instance id missing **")
        else:
            obj_id = line.split()[0] + "." + line.split()[1]
            if obj_id not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[obj_id]
                storage.save()

    def help_destroy(self):
        """
        Displays info for destroy command
        """

        print("destroy [class name] [instance ID]\n")

    def do_all(self, line):
        if line not in HBNBCommand.__CLASS_LIST and line:
            print("** class doesn't exist **")
        else:
            all_inst = []
            for key, value in storage.all().items():
                if line in key:
                    all_inst.append(str(value))
            print(all_inst)

    def help_all(self):
        """
        Displays help for all command
        """

        print("all (class name)\n")

    def do_update(self, line):
        if not line:
            print("** class name missing **")
        elif line.split()[0] not in HBNBCommand.__CLASS_LIST:
            print("** class doesn't exist **")
        elif len(line.split()) < 2:
            print("** instance id missing **")
        elif len(line.split()) < 3:
            obj_id = line.split()[0] + "." + line.split()[1]
            if obj_id not in storage.all():
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(line.split()) < 4:
            print("** value missing **")
        else:
            obj_id = line.split()[0] + "." + line.split()[1]
            obj = storage.all()[obj_id]
            attrib = line.split()[2]
            value = line.split()[3].strip('"')
            exec("obj." + attrib + "=value")
            storage.save()

    def help_update(self):
        """
        Displays info for update command
        """

        print("update [class name] [instance ID] [attribute] [value]\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
