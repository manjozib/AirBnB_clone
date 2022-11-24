#!/usr/bin/python3
"""Define a HBNBCommand class """
import cmd
import re

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

    def default(self, line):
        """
        Method called on an input line when the command prefix is
        not recognized for example <class name>.all(), etc, where
        <class name> might be User, BaseModel etc

        So this method will take care of the following commands:
        <class name>.all()
        <class name>.count()
        <class name>.show(<id>)
        """

        known_classes = models.storage.return_class()
        if '.' in line:
            split = re.split(r'\.|\(|\)', line)
            class_name = split[0]
            method_name = split[1]
            id = split[2]
            id = id.removeprefix('"')
            id = id.removesuffix('"')
            output = [str(v) for k, v in models.storage.all().items()]

            if class_name == '':
                print("** class name missing **")
            elif class_name in known_classes:
                if method_name == 'all':
                    new_list = []
                    for i in range(len(output)):
                        if output.__getitem__(i).__contains__(class_name):
                            new_list.append(output.__getitem__(i))
                    print(new_list)

                elif method_name == "count":
                    count = 0
                    for i in range(len(output)):
                        if output.__getitem__(i).__contains__(class_name):
                            count += 1
                    print(count)
                elif method_name == "show":
                    id = split[2]
                    id = id.removeprefix('"')
                    id = id.removesuffix('"')
                    if id == '':
                        print("** instance id missing **")
                    elif not models.storage.all().get(class_name + "." + id):
                        print("** no instance found **")
                    else:
                        print(models.storage.all()[class_name + "." + id])
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
