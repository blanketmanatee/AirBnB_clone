#!/usr/bin/python3
""" import of a shell interpreter for PYTHON, customized for HBNB"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command Line for HBNBClone"""
    intro = ''
    prompt = '(hbnb) '
    file = None

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
        if arg is None:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            arg_obj = BaseModel()
            arg_obj.save()
            print(arg_obj.id)
    def do_show(self, readline):
        """ prints a dictionary representation of a given class.\n """
        args = readline.split(' ')
        if len(args) > 2:
            print("** too many arguments - (<class name, id> format only) **")
        else:
            if args[0] != "BaseModel":
                print("** class name doesn't exist **")
            elif args[0] is None:
                print("** class name missing **")
            elif len(args) > 1:
                if args[1] is not None:
                    key = args[0] + '.' + args[1]
                    arg_obj = storage.all()
                    if key in arg_obj:
                        print(arg_obj[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")

    def do_delete(self, readline):
        """ deletes an instance of a class.\n """
        args = readline.split(' ')
        if len(args) > 2:
            print("** too many arguments - (<class name, id> format only) **")
        else:
            if args[0] != "BaseModel":
                print("** class name doesn't exist **")
            elif args[0] is None:
                print("** class name missing **")
            elif len(args) > 1:
                if args[1] is not None:
                    key = args[0] + '.' + args[1]
                    arg_obj = storage.all()
                    if key in arg_obj:
                        del arg_obj[key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")

    def do_all(self, readline):
        """ prints string rep. of a given class.\n """
        new_l = []
        obj_args = storage.all()
        if readline == "BaseModel":
            for keys in obj_args.keys():
                if readline == obj_args[keys].__class__:
                    new_l.append(str(obj_args[keys]))
            print(new_l)
        elif len(readline) == 0:
            for keys in obj_args.keys():
                new_l.append(str(obj_args[keys]))
            print(new_l)
        else:
            print("** class doesn't exist **")

    def do_update(self, readline):
            """ updates a instance with a new attribute.\n """
            args = readline.split(' ')
            try:
                args[0]
            except IndexError:
                print("** class name missing **")
                return
            if args[0] == "BaseModel":
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
                    setattr(arg_obj[key], args[2], str(args[3]))
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
