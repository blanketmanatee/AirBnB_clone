#!/usr/bin/python3
""" import of a shell interpreter for PYTHON, customized for HBNB"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """Command Line for HBNBClone"""
    prompt = '(hbnb)'
    file = None
    class_ctrs = {"User": User, "City": City, "Place": Place, "State": State,
                  "Review": Review, "BaseModel": BaseModel, "Amenity": Amenity}
    attr_flo = ["latitude", "longitude"]
    attr_int = ["number_rooms", "number_bathrooms", "max_guest",
                "price_by_night"]

    def do_quit(self, arg):
        """ Exits the shell.\n """
        return True

    def do_EOF(self, arg):
        """ Exits the shell by end of file. <Ctrl+D>\n """
        print()
        return True

    def emptyline(self):
        """ prevents ENTER from executing the previous command.\n """
        pass

    def do_create(self, arg):
        """ creates a new BaseModel class.\n """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.class_ctrs.keys():
            print("** class doesn't exist **")
        else:
            arg_obj = self.class_ctrs[arg]()
            arg_obj.save()
            print(arg_obj.id)

    def do_show(self, readline):
        """ prints a dictionary representation of a given class.\n """
        args = readline.split(' ')
        if len(args) > 2:
            print("** too many arguments - (<class name, id> format only) **")
        else:
            if len(args[0]) == 0:
                print("** class name missing **")
            elif args[0] not in self.class_ctrs.keys():
                print("** class name doesn't exist **")
            else:
                try:
                    args[1]
                except IndexError:
                    print("** instance id missing **")
                    return
                key = args[0] + '.' + args[1]
                arg_obj = storage.all()
                if key in arg_obj:
                    print(arg_obj[key])
                else:
                    print("** no instance found **")

    def do_delete(self, readline):
        """ deletes an instance of a class.\n """
        args = readline.split(' ')
        if len(args) > 2:
            print("** too many arguments - (<class name, id> format only) **")
        else:
            if len(args[0]) == 0:
                print("** class name missing **")
            elif args[0] not in self.class_ctrs.keys():
                print("** class name doesn't exist **")
            else:
                try:
                    args[1]
                except IndexError:
                    print("** instance id missing **")
                    return
                key = args[0] + '.' + args[1]
                arg_obj = storage.all()
                if key in arg_obj:
                    del arg_obj[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, readline):
        """ prints string rep. of a given class.\n """
        new_l = []
        obj_args = storage.all()
        args = readline.split(' ')
        if args[0] in self.class_ctrs.keys():
            for keys in obj_args.keys():
                if readline == obj_args[keys].__class__.__name__:
                    new_l.append(str(obj_args[keys]))
            print(new_l)
        elif len(args[0]) == 0:
            for keys in obj_args.keys():
                new_l.append(str(obj_args[keys]))
            print(new_l)
        else:
            print("** class doesn't exist **")

    def do_update(self, readline):
        """ updates a instance with a new attribute.\n """
        args = readline.split(' ')
        if args[0] in self.class_ctrs.keys():
            try:
                args[1]
            except IndexError:
                print("** instance id missing **")
                return
            key = args[0] + '.' + args[1]
            arg_obj = storage.all()
            if key in arg_obj:
                try:
                    args[2]
                except IndexError:
                    print("** attribute name missing **")
                    return
                try:
                    args[3]
                except IndexError:
                    print("** value missing **")
                    return
                if args[2] in self.attr_int:
                    setattr(arg_obj[key], args[2], int(args[3]))
                elif args[2] in self.attr_flo:
                    setattr(arg_obj[key], args[2], float(args[3]))
                else:
                    setattr(arg_obj[key], args[2], str(args[3]))
            else:
                print("** no instance found **")
        elif len(args[0]) == 0:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
