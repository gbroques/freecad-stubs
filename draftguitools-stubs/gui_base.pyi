import App as App
import FreeCADGui as Gui
import draftutils.todo as todo

class GuiCommandSimplest:
    def __init__(self, name: str = ..., doc: App.Document = ...) -> None: ...
    def IsActive(self):
        """Return True when this command should be available.

                It is `True` when there is a document.
        """
    def Activated(self):
        """Execute when the command is called.

                Log the command name to the log file and console.
                Also update the `doc` attribute.
        """

class GuiCommandNeedsSelection(GuiCommandSimplest):
    def IsActive(self):
        """Return True when this command should be available.

                It is `True` when there is a selection.
        """

class GuiCommandBase:
    def __init__(self) -> None: ...
    def IsActive(self):
        """Return True when this command should be available."""
    def finish(self):
        """Terminate the active command by committing the list of commands.

                It also perform some other tasks like terminating
                the plane tracker and the snapper.
        """
    def commit(self, name, func):
        """Store actions to be committed to the document.

                Parameters
                ----------
                name : str
                    A string that indicates what is being committed.

                func : list of strings
                    Each element of the list should be a Python command
                    that will be executed.
        """
