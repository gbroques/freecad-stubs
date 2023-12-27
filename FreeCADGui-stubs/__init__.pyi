import App
import Gui
from __main__ import Workbench
from typing import Any, overload

ActiveDocument: None
Control: Control

def SendMsgToActiveView(name, suppress=...) -> strorNone:
    """SendMsgToActiveView(name, suppress=False) -> str or None

    Send message to the active view. Deprecated, use class View.

    name : str
        Name of the view command.
    suppress : bool
        If the sent message fail, suppress warning message."""
def activateView(typeName, create=...) -> None:
    """activateView(typeName, create=False) -> None

    Activate a view of the given type in the active document.
    If a view of this type doesn't exist and create is True, a
    new view of this type is created.

    type : str
        Type name.
    create : bool"""
def activateWorkbench(name) -> bool:
    """activateWorkbench(name) -> bool

    Activate workbench by its name. Return False if the workbench is
    already active.

    name : str
        Name of the workbench to activate."""
def activeDocument() -> Gui.DocumentorNone:
    """activeDocument() -> Gui.Document or None

    Return the active document. If no one exists, return None."""
def activeView(typeName) -> objectorNone:
    """activeView(typeName) -> object or None

    Return the active view of the active document. If no one
    exists, return None.

    typeName : str
        Type name."""
def activeWorkbench() -> Workbench:
    """activeWorkbench() -> Workbench

    Return the active workbench object."""
def addCommand(name, cmd, activation) -> None:
    """addCommand(name, cmd, activation) -> None

    Add a command object.

    name : str
        Name of the command.
    cmd : object
        Command instance.
    activation : str
        Activation sequence. Optional."""
def addDocumentObserver(obj) -> None:
    """addDocumentObserver(obj) -> None

    Add an observer to get notifications about changes on documents.

    obj : object"""
def addIcon(name, content, format=...) -> None:
    """addIcon(name, content, format='XPM') -> None

    Add an icon to the system.

    name : str
        Name of the icon.
    content : str, bytes-like
        Content of the icon.
    format : str
        Format of the icon."""
def addIconPath(path) -> None:
    """addIconPath(path) -> None

    Add a new path to the system where to find icon files.

    path : str, bytes, bytearray
        Path to icon files."""
def addLanguagePath(path) -> None:
    """addLanguagePath(path) -> None

    Add a new path to the system where to find language files.

    path : str, bytes, bytearray
        Path to language files."""
def addModule(mod) -> None:
    """addModule(mod) -> None

    Prints the given module import only once in the macro recording.

    mod : str"""
@overload
def addPreferencePage(path, group) -> None:
    """addPreferencePage(path, group) -> None
    addPreferencePage(dialog, group) -> None

    Add a UI form to the preferences dialog in the specified group.

    path : str
        UI file path.
    group : str
        Group name.
    dialog : type
        Preference page."""
@overload
def addPreferencePage(dialog, group) -> None:
    """addPreferencePage(path, group) -> None
    addPreferencePage(dialog, group) -> None

    Add a UI form to the preferences dialog in the specified group.

    path : str
        UI file path.
    group : str
        Group name.
    dialog : type
        Preference page."""
def addResourcePath(path) -> None:
    """addResourcePath(path) -> None

    Add a new path to the system where to find resource files
    like icons or localization files.

    path : str, bytes, bytearray
        Path to resource files."""
def addWorkbench(workbench) -> None:
    """addWorkbench(workbench) -> None

    Add a workbench.

    workbench : Workbench, Workbench type
        Instance of a Workbench subclass or subclass of the
        Workbench class."""
def coinRemoveAllChildren(node) -> None:
    """coinRemoveAllChildren(node) -> None

    Remove all children from a group node.

    node : object"""
def createDialog(path) -> PyResource:
    """createDialog(path) -> PyResource

    Open a UI file.

    path : str
        UI file path."""
def createViewer(views=..., name) -> View3DInventorPyorAbstractSplitViewPy:
    """createViewer(views=1, name) -> View3DInventorPy or AbstractSplitViewPy

    Show and returns a viewer.

    views : int
        If > 1 a `AbstractSplitViewPy` object is returned.
    name : str
        Viewer title."""
def doCommand(cmd) -> None:
    """doCommand(cmd) -> None

    Prints the given string in the python console and runs it.

    cmd : str"""
def doCommandGui(cmd) -> None:
    """doCommandGui(cmd) -> None

    Prints the given string in the python console and runs it
    but doesn't record it in macros.

    cmd : str"""
def editDocument() -> Gui.DocumentorNone:
    """editDocument() -> Gui.Document or None

    Return the current editing document. If no one exists,
    return None."""
def embedToWindow() -> Any:
    """embedToWindow() -- Embeds the main window into another window"""
def exec_loop() -> Any:
    """exec_loop() -- Starts the event loop
    Note: this will block the call until the event loop has terminated"""
def export(objs, fileName) -> None:
    """export(objs, fileName) -> None

    Save scene to Inventor or VRML file.

    objs : sequence of App.DocumentObject
        Sequence of objects to save.
    fileName : str, bytes, bytearray
        File name."""
def exportSubgraph(*args, **kwargs):
    """exportSubgraph(Node, File or Buffer, [Format='VRML']) -> None

    Exports the sub-graph in the requested formatThe format string can be VRML or IV"""
def getDocument(doc) -> Gui.Document:
    """getDocument(doc) -> Gui.Document

    Get a document.

    doc : str, App.Document
        `App.Document` name or `App.Document` object."""
def getIcon(name) -> QIconorNone:
    """getIcon(name) -> QIcon or None

    Get an icon in the system. If the pixmap is null, return None.

    name : str
        Name of the icon."""
def getLocale() -> str:
    """getLocale() -> str

    Returns the locale currently used by FreeCAD."""
def getMainWindow() -> QMainWindow:
    """getMainWindow() -> QMainWindow

    Return the main window instance."""
def getMarkerIndex(marker, size=...) -> int:
    """getMarkerIndex(marker, size=9) -> int

    Get marker index according to marker name and size.

    marker : str
        Marker style name.
    size : int
        Marker size."""
def getSoDBVersion() -> String:
    """getSoDBVersion() -> String

    Return a text string containing the name
    of the Coin library and version information"""
def getUserEditMode() -> str:
    """getUserEditMode() -> str

    Get current user edit mode."""
def getWorkbench(name) -> Workbench:
    """getWorkbench(name) -> Workbench

    Get the workbench by its name.

    name : str
        Name of the workbench to return."""
def hide(name) -> None:
    """hide(name) -> None

    Hide the given feature. Deprecated.

    name : str
        Feature name."""
def hideObject(obj) -> None:
    """hideObject(obj) -> None

    Hide the view provider of the given object.

    obj : App.DocumentObject"""
def insert(fileName, docName) -> None:
    """insert(fileName, docName) -> None

    Insert a macro, Inventor or VRML file. If no document name
    is given the active document is used.

    fileName : str, bytes, bytearray
        File name.
    docName : str
        Document name."""
def isIconCached(name) -> Bool:
    """isIconCached(name) -> Bool

    Check if an icon with the given name is cached.

    name : str
        Name of the icon."""
def listCommands(*args, **kwargs):
    """listAll() -> list of str

    Returns the name of all commands."""
def listUserEditModes() -> list:
    """listUserEditModes() -> list

    List available user edit modes."""
def listWorkbenches() -> dict:
    """listWorkbenches() -> dict

    Get a dictionary with all workbenches."""
def loadFile(fileName, module) -> None:
    """loadFile(fileName, module) -> None

    Loads an arbitrary file by delegating to the given Python module.
    If no module is given it will be determined by the file extension.
    If more than one module can load a file the first one will be taken.
    If no module exists to load the file an exception will be raised.

    fileName : str
    module : str"""
def open(fileName) -> None:
    """open(fileName) -> None

    Open a macro, Inventor or VRML file.

    fileName : str, bytes, bytearray
        File name."""
def reload(name) -> App.DocumentorNone:
    """reload(name) -> App.Document or None

    Reload a partial opened document. If the document is not open,
    return None.

    name : str
        `App.Document` name."""
def removeDocumentObserver(obj) -> None:
    """removeDocumentObserver(obj) -> None

    Remove an added document observer.

    obj : object"""
def removeWorkbench(name) -> None:
    """removeWorkbench(name) -> None

    Remove a workbench.

    name : str
        Name of the workbench to remove."""
def runCommand(name, index=...) -> None:
    """runCommand(name, index=0) -> None

    Run command by its name.

    name : str
        Name of the command.
    index : int
        Index of the child command."""
def sendMsgToFocusView(name, suppress=...) -> strorNone:
    """sendMsgToFocusView(name, suppress=False) -> str or None

    Send message to the focused view.

    name : str
        Name of the view command.
    suppress : bool
        If send message fail, suppress warning message."""
def setActiveDocument(doc) -> None:
    """setActiveDocument(doc) -> None

    Activate the specified document.

    doc : str, App.Document
        Document to activate."""
def setLocale(name) -> None:
    '''setLocale(name) -> None

    Sets the locale used by FreeCAD. Can be set by top-level
    domain (e.g. "de") or the language name (e.g. "German").

    name : str
        Locale name.'''
def setUserEditMode(mode) -> bool:
    """setUserEditMode(mode) -> bool

    Set user edit mode. Returns True if exists, False otherwise.

    mode : str"""
def setupWithoutGUI() -> Any:
    """setupWithoutGUI() -- Uses this module without starting
    an event loop or showing up any GUI
    """
def show(name) -> None:
    """show(name) -> None

    Show the given feature. Deprecated.

    name : str
        Feature name."""
def showDownloads() -> None:
    """showDownloads() -> None

    Show the downloads manager window."""
def showMainWindow() -> Any:
    """showMainWindow() -- Show the main window
    If no main window does exist one gets created"""
def showObject(obj) -> None:
    """showObject(obj) -> None

    Show the view provider of the given object.

    obj : App.DocumentObject"""
def showPreferences(grp, index=...) -> None:
    """showPreferences(grp, index=0) -> None

    Show the preferences window.

    grp: str
        Group to show.
    index : int
        Page index."""
def subgraphFromObject(object) -> Node:
    """subgraphFromObject(object) -> Node

    Return the Inventor subgraph to an object"""
def supportedLocales() -> dict:
    """supportedLocales() -> dict

    Returns a dict of all supported locales. The keys are the language
    names and the values the top-level domains."""
def updateGui() -> None:
    """updateGui() -> None

    Update the main window and all its windows."""
def updateLocale() -> None:
    """updateLocale() -> None

    Update the localization."""
