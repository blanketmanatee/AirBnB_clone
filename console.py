#!/usr/bin/python3
""" import of a shell interpreter for PYTHON, customized for HBNB"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
