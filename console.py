#!/usr/bin/env python3
"""
    Program that contains the entry point
    of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """ Definition for the class `HBNBCommand`

    Public Class attributes:
        prompt -- The string prompt that will be printed
        names -- List with the names of classes
    """
    prompt = "(hbnb) "
    names = ["BaseModel"]

    def do_quit(self, arg):
        """ Function that handles the quit command

            Returns: True (Always)
        """
        return True

    def do_EOF(self, arg):
        """ Function that handles End of file

            Returns: True (Always)
        """
        print()
        return True

    def emptyline(self):
        """ Function that handles an empty line input """
        pass

    def validate_input(self, args, min_args=0,
                       class_check=True, id_check=True):
        """ Validate input arguments and perform checks

        Args:
            self -- The object itsself
            args -- List of arguments
            min_args -- The minimum number of args to pass
            class_check -- Whether class should be checked or not
            id_check -- Whether id should be checked or not

        Returns:
            bool -- True if input is valid, False otherwise
        """
        if len(args) == 0:
            print("** class name missing **")
            return False
        if class_check:
            if args[0] not in type(self).names:
                print("** class doesn't exist **")
                return False
        if id_check:
            if len(args) < 2:
                print("** instance id missing **")
                return False
            if f"{args[0]}.{args[1]}" not in storage.all():
                print("** no instance found **")
                return False
        return True

    def do_create(self, arg):
        """ Function that handles the create command

            Args:
                self -- The object itself
                arg -- The argument passed to the command
            Returns: Nothing
        """
        args = arg.split()

        if self.validate_input(args, min_args=1, id_check=False):
            obj = eval(args[0] + "()")
            print(obj.id)
            obj.save()

    def do_show(self, arg):
        """ Function that handles the show command

            Args:
                self -- The object itself
                arg -- The argument passed to the command
            Returns: Nothing
        """
        args = arg.split()
        if self.validate_input(args, min_args=2):
            key = f"{args[0]}.{args[1]}"
            print(storage.all()[key])

    def do_destroy(self, arg):
        """ Function that handles the destroy command

            Args:
                self -- The object itself
                arg -- The argument passed to the command
            Returns: Nothing
        """
        args = arg.split()

        if self.validate_input(args, min_args=2):
            key = f"{args[0]}.{args[1]}"
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """ Function that handles the all command

            Args:
                self -- The object itself
                arg -- The argument passed to the command
            Returns: Nothing
        """
        args = arg.split()
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
        else:
            if self.validate_input(args, id_check=False):
                objs = []
                for key, obj in storage.all().items():
                    if key.startswith(args[0]):
                        objs.append(str(obj))
                print(objs)

    def do_update(self, arg):
        """ Function that handles the update command

            Args:
                self -- The object itself
                arg -- The argument passed to the command
            Returns: Nothing
        """
        args = arg.split()
        if self.validate_input(args, min_args=4):
            key = f"{args[0]}.{args[1]}"
            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attribute_name = args[2]
                attribute_value = args[3]
                obj = models.storage.all()[key]
                try:
                    setattr(obj, attribute_name, eval(attribute_value))
                except Exception as e:
                    print(e)
                    return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
