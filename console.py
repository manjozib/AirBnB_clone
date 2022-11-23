#!/usr/bin/python3
"""Define a HBNBCommand class """
import cmd
from models.base_model import BaseModel
from models.user import User
import models


class HBNBCommand(cmd.Cmd):
    """customised console class"""
    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Ctrl + d to exit the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        return cmd.Cmd.intro

    def do_create(self, line):
        """Creates a new instance of given class saves it
        (to the JSON file) and prints the id"""
        classes = models.storage.return_class()
        if len(line) == 0:
            print("** class name missing **")
        elif classes.get(line) is None:
            print("** class doesn't exist **")
        else:
            print(classes)
            print(classes[line])
            new_model = classes[line]()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        classes = models.storage.return_class()
        lines = line.split(' ')
        if len(line) == 0:
            print("** class name missing **")
        elif classes.get(lines[0]) is None:
            print("** class doesn't exist **")
        elif len(lines) == 1:
            print("** instance id missing **")
        else:
            if not models.storage.all().get(lines[0] + "." + lines[1]):
                print("** no instance found **")
            else:
                print(models.storage.all()[lines[0] + "." + lines[1]])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id"""
        classes = models.storage.return_class()
        lines = line.split(' ')
        if len(line) == 0:
            print("** class name missing **")
        elif classes.get(lines[0]) is None:
            print("** class doesn't exist **")
        elif len(lines) == 1:
            print("** instance id missing **")
        else:
            if not models.storage.all().get(lines[0] + "." + lines[1]):
                print("** no instance found **")
            else:
                del models.storage.all()[lines[0] + "." + lines[1]]
                models.storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        a = 0
        new_list = []
        if len(line) == 0:
            print([str(v) for k, v in models.storage.all().items()])
        else:
            lines = line.split(' ')
            for k, v in models.storage.all().items():
                key = k.split('.')
                if key[0] == line:
                    a += 1
                    new_list.append(str(v))
                else:
                    continue
            if a == 0:
                print("** class doesn't exist **")
            else:
                print(new_list)
    def do_update(self, line):
        """ Updates an instance based on the class name and id by 
        adding or updating attribute"""
        classes = models.storage.return_class()
        lines = line.split(' ')
        if len(line) == 0:
            print("** class name missing **")
        elif classes.get(lines[0]) is None:
            print("** class doesn't exist **")
        elif len(lines) == 1:
            print("** instance id missing **")
        else:
            if not models.storage.all().get(lines[0] + "." + lines[1]):
                print("** no instance found **")
            elif len(lines) < 3:
                print("** attribute name missing **")
            elif len(lines) < 4:
                print("** value missing **")
            else:
                obj = models.storage.all()[lines[0] + "." + lines[1]]
                if lines[3].isdigit():
                    lines[3] = float(lines[3])
                    if lines[3].is_integer():
                        lines[3] = int(lines[3])
                else:
                    if lines[3].startswith('"'):
                       lines[3] = lines[3].removeprefix('"')
                       lines[3] = lines[3].removesuffix('"')
                setattr(obj, lines[2], lines[3])
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
