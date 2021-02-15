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
        'Exits the shell.\n'
        return True

    def do_EOF(self, arg):
        'Exits the shell by end of file. <Ctrl+D>\n'
        print()
        return True

    def emptyline(self):
        'prevents ENTER from executing the previous command.\n'
        pass

    def do_create(self, arg):
        'creates a new BaseModel class.\n'
        if arg is None:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            arg_obj = BaseModel()
            arg_obj.save()
            print(arg_obj.id)
    def do_show(self, readline):
        'prints a dictionary representation of '
        args = readline.split(' ')
        print(args)
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
        'deletes an instance of a class'
        args = readline.split(' ')
        print(args)
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
                    
    def do_obj(self, arg):
        'prints the current list of objects.'
        print(storage.all())

if __name__ == '__main__':
    HBNBCommand().cmdloop()
