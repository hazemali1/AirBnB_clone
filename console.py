#!/usr/bin/python3
"""
commands
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNB comands
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        print("")
        return True

    def emptyline(self):
        """empty line
        """
        pass

    def do_create(self, arg):
        """create new instance
        """
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            s = BaseModel()
            s.save()
            print (s.id)

    def do_show(self, arg):
        """Show obj
        """
        q = arg.split()
        date_base = storage.all()
        b = 1
        if not arg:
            print("** class name missing **")
        elif q[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(q) == 1:
            print ("** instance id missing **")
        else:
            for k, v in date_base.items():
                if v.id == q[1]:
                    b = 2
                    print(v)
            if b == 1:
                print("** no instance found **")

    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
