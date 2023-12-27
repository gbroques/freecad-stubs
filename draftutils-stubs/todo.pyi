import FreeCAD as App
import FreeCADGui as Gui
import PySide.QtCore as QtCore
from draftutils.messages import _err as _err, _log as _log, _msg as _msg, _wrn as _wrn
from typing import ClassVar

__url__: list
_DEBUG: int
_DEBUG_inner: int

class ToDo:
    itinerary: ClassVar[list] = ...
    commitlist: ClassVar[list] = ...
    afteritinerary: ClassVar[list] = ...
    @staticmethod
    def doTasks():
        """Execute the commands stored in the lists.

                The lists are `itinerary`, `commitlist` and `afteritinerary`.
        """
    @staticmethod
    def delay(f, arg):
        """Add the function and argument to the itinerary list.

                Schedule geometry manipulation that would crash Coin if done
                in the event callback.

                If the `itinerary` list is empty, it will call
                `QtCore.QTimer.singleShot(0, ToDo.doTasks)`
                to execute the commands in the other lists.

                Finally, it will build the tuple `(f, arg)`
                and append it to the `itinerary` list.

                Parameters
                ----------
                f: function reference
                    A reference (pointer) to a Python command
                    which can be executed directly.
                    ::
                        f()

                arg: argument reference
                    A reference (pointer) to the argument to the `f` function.
                    ::
                        f(arg)
        """
    @staticmethod
    def delayCommit(cl):
        """Execute the other lists, and add to the commit list.

                Schedule geometry manipulation that would crash Coin if done
                in the event callback.

                First it calls
                `QtCore.QTimer.singleShot(0, ToDo.doTasks)`
                to execute the commands in all lists.

                Then the `cl` list is assigned as the new commit list.

                Parameters
                ----------
                cl: list of tuples
                    Each tuple is of the form `(name, command_list)`.
                    The `name` is a string identifier or description of the commands
                    that will be run, and `command_list` is a list of strings
                    that indicate the Python instructions that will be executed.

                    See the attributes of the `ToDo` class for more information.
        """
    @staticmethod
    def delayAfter(f, arg):
        """Add the function and argument to the afteritinerary list.

                Schedule geometry manipulation that would crash Coin if done
                in the event callback.

                Works the same as `delay`.

                If the `afteritinerary` list is empty, it will call
                `QtCore.QTimer.singleShot(0, ToDo.doTasks)`
                to execute the commands in the other lists.

                Finally, it will build the tuple `(f, arg)`
                and append it to the `afteritinerary` list.
        """

class todo:
    itinerary: ClassVar[list] = ...
    commitlist: ClassVar[list] = ...
    afteritinerary: ClassVar[list] = ...
    @staticmethod
    def doTasks():
        """Execute the commands stored in the lists.

                The lists are `itinerary`, `commitlist` and `afteritinerary`.
        """
    @staticmethod
    def delay(f, arg):
        """Add the function and argument to the itinerary list.

                Schedule geometry manipulation that would crash Coin if done
                in the event callback.

                If the `itinerary` list is empty, it will call
                `QtCore.QTimer.singleShot(0, ToDo.doTasks)`
                to execute the commands in the other lists.

                Finally, it will build the tuple `(f, arg)`
                and append it to the `itinerary` list.

                Parameters
                ----------
                f: function reference
                    A reference (pointer) to a Python command
                    which can be executed directly.
                    ::
                        f()

                arg: argument reference
                    A reference (pointer) to the argument to the `f` function.
                    ::
                        f(arg)
        """
    @staticmethod
    def delayCommit(cl):
        """Execute the other lists, and add to the commit list.

                Schedule geometry manipulation that would crash Coin if done
                in the event callback.

                First it calls
                `QtCore.QTimer.singleShot(0, ToDo.doTasks)`
                to execute the commands in all lists.

                Then the `cl` list is assigned as the new commit list.

                Parameters
                ----------
                cl: list of tuples
                    Each tuple is of the form `(name, command_list)`.
                    The `name` is a string identifier or description of the commands
                    that will be run, and `command_list` is a list of strings
                    that indicate the Python instructions that will be executed.

                    See the attributes of the `ToDo` class for more information.
        """
    @staticmethod
    def delayAfter(f, arg):
        """Add the function and argument to the afteritinerary list.

                Schedule geometry manipulation that would crash Coin if done
                in the event callback.

                Works the same as `delay`.

                If the `afteritinerary` list is empty, it will call
                `QtCore.QTimer.singleShot(0, ToDo.doTasks)`
                to execute the commands in the other lists.

                Finally, it will build the tuple `(f, arg)`
                and append it to the `afteritinerary` list.
        """
