#!/usr/bin/python3
"""
commands
"""
import cmd
from models import storage
from models.engine.file_storage import class_dict
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    """
    HBNB comands
    """
    prompt = "(hbnb) "

    def default(self, arg):
        """
        Default
        """
        p = arg.split(".")
        if len(p) > 1:
            q = p[1].split("(")
            if len(q) > 1:
                if q[0] == 'all':
                    self.do_all(p[0])
                elif q[0] == 'count':
                    self.do_count(p[0])
                elif q[0] == 'show':
                    a = ""
                    a = a + p[0]
                    a = a + " "
                    b = q[1].split('"')
                    if len(b) > 1:
                        a = a + str(b[1])
                    self.do_show(a)
                elif q[0] == 'destroy':
                    a = ""
                    a = a + p[0]
                    a = a + " "
                    b = q[1].split('"')
                    if len(b) > 1:
                        a = a + str(b[1])
                    self.do_destroy(a)
                elif q[0] == 'update':
                    a = ""
                    a = a + p[0]
                    a = a + " "
                    b = p[1].replace(':', ',').replace('(', '"').replace(')', '"').split(",")
                    b = str(b).replace(',', '"').replace("'", '"').replace('}', '"').replace('{', '"').replace(' ', '"').replace('[', '"').replace(']', '"').replace('update', '"').split('"')
                    x = 0
                    for i in b:
                        if len(i) > 0:
                            x += 1
                    if x <= 3:
                        for i in b:
                            if len(i) > 0:
                                a = a + i
                                a = a + " "
                        self.do_update(a)
                    else:
                        l = []
                        for s in b:
                            if len(s) > 0:
                                l.append(s)
                        a = a + l[0]
                        x = x / 2
                        w = 1
                        a = a + " "
                        for i in range(int(x)):
                            n = a
                            r = 2
                            while r > 0:
                                n = n + l[w]
                                n = n + " "
                                r -= 1
                                w += 1
                            self.do_update(n)
                else:
                    print("*** Unknown syntax: {}".format(arg))
            else:
                print("*** Unknown syntax: {}".format(arg))
        else:
            print("*** Unknown syntax: {}".format(arg))

    def do_count(self, arg):
        """
        Count instances of class
        """
        q = arg.split()
        c = 0
        for v in storage.all().values():
            if q[0] == v.__class__.__name__:
                c += 1
        print(c)

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print("")
        return True

    def emptyline(self):
        """
        empty line
        """
        pass

    def do_create(self, arg):
        """
        create new instance
        """
        if not arg:
            print("** class name missing **")
        elif arg not in class_dict.keys():
            print("** class doesn't exist **")
        else:
            for key, value in class_dict.items():
                if arg == key:
                    s = value()
            s.save()
            print(s.id)

    def do_show(self, arg):
        """
        Show obj
        """
        q = arg.split()
        date_base = storage.all()
        b = 1
        if not arg:
            print("** class name missing **")
        elif q[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif len(q) == 1:
            print("** instance id missing **")
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
        elif q[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif len(q) == 1:
            print("** instance id missing **")
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
        if arg and q[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif arg and q[0] in class_dict.keys():
            z = []
            for v in date_base.values():
                if v.__class__.__name__ == q[0]:
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
        if q[0] not in class_dict.keys():
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
