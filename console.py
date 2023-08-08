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

    def do_destroy(self, arg):
        """destroyy"""
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
                    del date_base[k]
                    storage.save()
                    break
            if b == 1:
                print("** no instance found **")

    def do_all(self, arg):
        """print Alll"""
        q = arg.split()
        date_base = storage.all()
        if arg and q[0] != "BaseModel":
            print ("** class doesn't exist **")
        elif arg and q[0] == "BaseModel":
            z = []
            for v in date_base.values():
                if v.__class__.__name__ == "BaseModel":
                    z.append(str(v))
            print(z)
        else:
            z = []
            for v in date_base.values():
                z.append(str(v))
            print(z)
    def do_update(self, arg):
        """Update"""
        q = arg.replace('"', ' ').replace("'", ' ').split()
        date_base = storage.all()
        b = 1
        if not arg:
            print("** class name missing **")
            return
        if q[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(q) == 1:
            print("** instance id missing **")
            return
        if len(q) > 1:
            for k, v in date_base.items():
                if v.id == q[1]:
                    b = 2
            if b == 1:
                print("** no instance found **")
                return
        if len(q) == 2:
            print("** attribute name missing **")
            return
        if len(q) == 3:
            print("** value missing **")
            return
        if len(q) > 3:
            p = 1
            v = str(q[3])
            print(v)
            if q[3].isdigit():
                v = int(q[3])
                p = 2
            if p == 1:
                try:
                    v = float(q[3])
                except ValueError:
                    pass
            for k in date_base.values():
                if k.id == q[1]:
                    k.__dict__[q[2]] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
