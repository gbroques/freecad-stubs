import App
import FreeCADGui as Gui
from typing import Any

ActiveDocument: App.Document
GuiUp: int
__ModDirs__: list
__cmake__: list
__unit_test__: list

def ConfigDump(*args, **kwargs):
    """Dump the configuration to the output."""
def ConfigGet(string) -> Any:
    """ConfigGet(string) -- Get the value for the given key."""
def ConfigSet(*args, **kwargs):
    """ConfigSet(string, string) -- Set the given key to the given value."""
def ParamGet(*args, **kwargs):
    """Get parameters by path"""
def Version(*args, **kwargs):
    """Print the version to the output."""
def activeDocument() -> objectorNone:
    """activeDocument() -> object or None

    Return the active document or None if there is no one."""
def addDocumentObserver() -> None:
    """addDocumentObserver() -> None

    Add an observer to get notified about changes on documents."""
def addExportType(*args, **kwargs):
    """Register filetype for export"""
def addImportType(*args, **kwargs):
    """Register filetype for import"""
def changeExportModule(*args, **kwargs):
    """Change the export module name of a registered filetype"""
def changeImportModule(*args, **kwargs):
    """Change the import module name of a registered filetype"""
def checkAbort() -> Any:
    """checkAbort() -- check for user abort in length operation.

    This only works if there is an active sequencer (or ProgressIndicator in Python).
    There is an active sequencer during document restore and recomputation. User may
    abort the operation by pressing the ESC key. Once detected, this function will
    trigger a Base.FreeCADAbort exception."""
def checkLinkDepth(depth) -> Any:
    """checkLinkDepth(depth) -- check link recursion depth"""
def closeActiveTransaction(abort=...) -> Any:
    """closeActiveTransaction(abort=False) -- commit or abort current active transaction"""
def closeDocument(string) -> None:
    """closeDocument(string) -> None

    Close the document with a given name."""
def getActiveTransaction(*args, **kwargs):
    """getActiveTransaction() -> (name,id) return the current active transaction name and ID"""
def getDependentObjects(*args, **kwargs):
    """getDependentObjects(obj|[obj,...], options=0)
    Return a list of dependent objects including the given objects.

    options: can have the following bit flags,
             1: to sort the list in topological order.
             2: to exclude dependency of Link type object."""
def getDocument(string) -> object:
    """getDocument(string) -> object

    Get a document by its name or raise an exception
    if there is no document with the given name."""
def getExportType(*args, **kwargs):
    """Get the name of the module that can export the filetype"""
def getHelpDir(*args, **kwargs):
    """Get the directory of the documentation"""
def getHomePath(*args, **kwargs):
    """Get the home path, i.e. the parent directory of the executable"""
def getImportType(*args, **kwargs):
    """Get the name of the module that can import the filetype"""
def getLibraryDir(*args, **kwargs):
    """Get the directory of all extension modules"""
def getLinksTo(obj, options=..., maxCount=...) -> Any:
    """getLinksTo(obj,options=0,maxCount=0) -- return the objects linked to 'obj'

    options: 1: recursive, 2: check link array. Options can combine.
    maxCount: to limit the number of links returned
    """
def getLogLevel(tag) -> Any:
    """getLogLevel(tag) -- Get the log level of a string tag"""
def getResourceDir(*args, **kwargs):
    """Get the root directory of all resources"""
def getTempPath(*args, **kwargs):
    """Get the root directory of cached files"""
def getUserAppDataDir(*args, **kwargs):
    """Get the root directory of application data"""
def getUserCachePath(*args, **kwargs):
    """Get the root path of cached files"""
def getUserConfigDir(*args, **kwargs):
    """Get the root path of user config files"""
def getUserMacroDir(*args, **kwargs):
    """getUserMacroDir(bool=False) -> stringGet the directory of the user's macro directory
    If parameter is False (the default) it returns the standard path in theuser's home directory, otherwise it returns the user-defined path."""
def isRestoring(*args, **kwargs):
    """isRestoring() -> Bool -- Test if the application is opening some document"""
def listDocuments(sort=...) -> list:
    """listDocuments(sort=False) -> list

    Return a list of names of all documents, optionally sort in dependency order."""
def loadFile(*args, **kwargs):
    """loadFile(string=filename,[string=module]) -> None

    Loads an arbitrary file by delegating to the given Python module:
    * If no module is given it will be determined by the file extension.
    * If more than one module can load a file the first one will be taken.
    * If no module exists to load the file an exception will be raised."""
def newDocument(name, label=..., hidden=..., temp=...) -> object:
    """newDocument(name, label=None, hidden=False, temp=False) -> object
    Create a new document with a given name.

    name: unique document name which is checked automatically.
    label: optional user changeable label for the document.
    hidden: whether to hide document 3D view.
    temp: mark the document as temporary so that it will not be saved"""
def open(*args, **kwargs):
    """See openDocument(string)"""
def openDocument(filepath, hidden=...) -> object:
    """openDocument(filepath,hidden=False) -> object
    Create a document and load the project file into the document.

    filepath: file path to an existing file. If the file doesn't exist
              or the file cannot be loaded an I/O exception is thrown.
              In this case the document is kept alive.
    hidden: whether to hide document 3D view."""
def removeDocumentObserver() -> None:
    """removeDocumentObserver() -> None

    Remove an added document observer."""
def saveParameter(config=...) -> None:
    """saveParameter(config='User parameter') -> None
    Save parameter set to file. The default set is 'User parameter'"""
def setActiveDocument(*args, **kwargs):
    """setActiveDocement(string) -> None

    Set the active document by its name."""
def setActiveTransaction(name, persist=...) -> Any:
    """setActiveTransaction(name, persist=False) -- setup active transaction with the given name

    name: the transaction name
    persist(False): by default, if the calling code is inside any invocation of a command, it
                    will be auto closed once all commands within the current stack exists. To
                    disable auto closing, set persist=True
    Returns the transaction ID for the active transaction. An application-wide
    active transaction causes any document changes to open a transaction with
    the given name and ID."""
def setLogLevel(tag, level) -> Any:
    """setLogLevel(tag, level) -- Set the log level for a string tag.
    'level' can either be string 'Log', 'Msg', 'Wrn', 'Error', or an integer value"""
