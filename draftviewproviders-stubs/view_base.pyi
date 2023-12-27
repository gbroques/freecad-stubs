import Draft_rc as Draft_rc
import FreeCAD as App
import FreeCADGui as Gui
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils

class ViewProviderDraft:
    def __init__(self, vobj) -> None: ...
    def _set_properties(self, vobj):
        """Set the properties of objects if they don't exist."""
    def dumps(self):
        """Return a tuple of all serializable objects or None.

                When saving the document this view provider object gets stored
                using Python's `json` module.

                Since we have some un-serializable objects (Coin objects) in here
                we must define this method to return a tuple of all serializable
                objects or `None`.

                Override this method to define the serializable objects to return.

                By default it returns `None`.

                Returns
                -------
                None
        """
    def loads(self, state):
        """Set some internal properties for all restored objects.

                When a document is restored this method is used to set some properties
                for the objects stored with `json`.

                Override this method to define the properties to change for the
                restored serialized objects.

                By default no objects were serialized with `dumps`,
                so nothing needs to be done here, and it returns `None`.

                Parameters
                ----------
                state : state
                    A serialized object.

                Returns
                -------
                None
        """
    def attach(self, vobj):
        """Set up the scene sub-graph of the view provider.

                This method should always be defined, even if it does nothing.

                Override this method to set up a custom scene.

                Parameters
                ----------
                vobj : the view provider of the scripted object.
                    This is `obj.ViewObject`.
        """
    def updateData(self, obj, prop):
        """Run when an object property is changed.

                Override this method to handle the behavior of the view provider
                depending on changes that occur to the real object's properties.

                By default, no property is tested, and it does nothing.

                Parameters
                ----------
                obj : the base C++ object
                    The scripted document object that is associated
                    with this view provider, which commonly may be of types
                    `Part::Part2DObjectPython`, `Part::FeaturePython`,
                    or `App::FeaturePython`.

                prop : str
                    Name of the property that was modified.
        """
    def getDisplayModes(self, vobj):
        """Return a list of display modes.

                Override this method to return a list of strings with
                display mode styles, such as `'Flat Lines'`, `'Shaded'`,
                `'Wireframe'`, `'Points'`.

                By default it returns an empty list.

                Parameters
                ----------
                vobj : the view provider of the scripted object.
                    This is `obj.ViewObject`.

                Returns
                -------
                list
                    Empty list `[ ]`
        """
    def getDefaultDisplayMode(self):
        """Return the default mode defined in getDisplayModes.

                Override this method to return a string with the default display mode.

                By default it returns `'Flat Lines'`.

                Returns
                -------
                str
                    `'Flat Lines'`

        """
    def setDisplayMode(self, mode):
        """Map the modes defined in attach with those in getDisplayModes.

                This method is optional.

                By default since they have the same names nothing needs to be done,
                and it just returns the input `mode`.

                Parameters
                ----------
                str
                    A string defining a display mode such as
                    `'Flat Lines'`, `'Shaded'`, `'Wireframe'`, `'Points'`.
        """
    def onChanged(self, vobj, prop):
        """Run when a view property is changed.

                Override this method to handle the behavior
                of the view provider depending on changes that occur to its properties
                such as line color, line width, point color, point size,
                draw style, shape color, transparency, and others.

                This method  updates the texture and pattern if
                the properties `TextureImage`, `Pattern`, `DiffuseColor`,
                and `PatternSize` change.

                Parameters
                ----------
                vobj : the view provider of the scripted object.
                    This is `obj.ViewObject`.

                prop : str
                    Name of the property that was modified.
        """
    def _update_pattern_size(self, vobj):
        """Update the pattern size. Helper method in onChanged."""
    def execute(self, vobj):
        """Run when the object is created or recomputed.

                Override this method to produce effects when the object
                is newly created, and whenever the document is recomputed.

                By default it does nothing.

                Parameters
                ----------
                vobj : the view provider of the scripted object.
                    This is `obj.ViewObject`.
        """
    def setEdit(self, vobj, mode):
        """Enter the edit mode of the object.

                Parameters
                ----------
                vobj : the view provider of the scripted object.
                    This is `obj.ViewObject`.

                mode : int
                    0, 1, 2 or 3. See the `Std_UserEditMode` command.

                Returns
                -------
                bool or None
                    `False`: NOT USED HERE.
                             Do not enter edit mode (unsetEdit is not called).
                    `True` : Handled edit mode.
                             Handled modes are 0 and 3, and only for certain objects.
                             The unsetEdit function should then also return `True`.
                    `None` : Unhandled edit mode.
                             Handling is left to Part::FeaturePython code.
                             The unsetEdit function should then also return `None`.
        """
    def unsetEdit(self, vobj, mode):
        """Terminate the edit mode of the object.

                See setEdit.
        """
    def setupContextMenu(self, vobj, menu): ...
    def edit(self): ...
    def transform(self): ...
    def getIcon(self):
        """Return the path to the icon used by the view provider.

                The path can be a full path in the system, or a relative path
                inside the compiled resource file.
                It can also be a string that defines the icon in XPM format.

                Override this method to provide a specific icon
                for the object in the tree view.

                By default it returns the path to the `Draft_Draft.svg` icon.

                Returns
                -------
                str
                    `':/icons/Draft_Draft.svg'`
        """
    def claimChildren(self):
        """Return objects that will be placed under it in the tree view.

                Override this method to return a list with objects
                that will appear under this object in the tree view.
                That is, this object becomes the `parent`,
                and all those under it are the `children`.

                By default the returned list is composed of objects from
                `Object.Base`, `Object.Objects`, `Object.Components`,
                and `Object.Group`, if they exist.

                Returns
                -------
                list
                    List of objects.
        """

class _ViewProviderDraft:
    def __init__(self, vobj) -> None: ...
    def _set_properties(self, vobj):
        """Set the properties of objects if they don't exist."""
    def dumps(self):
        """Return a tuple of all serializable objects or None.

                When saving the document this view provider object gets stored
                using Python's `json` module.

                Since we have some un-serializable objects (Coin objects) in here
                we must define this method to return a tuple of all serializable
                objects or `None`.

                Override this method to define the serializable objects to return.

                By default it returns `None`.

                Returns
                -------
                None
        """
    def loads(self, state):
        """Set some internal properties for all restored objects.

                When a document is restored this method is used to set some properties
                for the objects stored with `json`.

                Override this method to define the properties to change for the
                restored serialized objects.

                By default no objects were serialized with `dumps`,
                so nothing needs to be done here, and it returns `None`.

                Parameters
                ----------
                state : state
                    A serialized object.

                Returns
                -------
                None
        """
    def attach(self, vobj):
        """Set up the scene sub-graph of the view provider.

                This method should always be defined, even if it does nothing.

                Override this method to set up a custom scene.

                Parameters
                ----------
                vobj : the view provider of the scripted object.
                    This is `obj.ViewObject`.
        """
    def updateData(self, obj, prop):
        """Run when an object property is changed.

                Override this method to handle the behavior of the view provider
                depending on changes that occur to the real object's properties.

                By default, no property is tested, and it does nothing.

                Parameters
                ----------
                obj : the base C++ object
                    The scripted document object that is associated
                    with this view provider, which commonly may be of types
                    `Part::Part2DObjectPython`, `Part::FeaturePython`,
                    or `App::FeaturePython`.

                prop : str
                    Name of the property that was modified.
        """
    def getDisplayModes(self, vobj):
        """Return a list of display modes.

                Override this method to return a list of strings with
                display mode styles, such as `'Flat Lines'`, `'Shaded'`,
                `'Wireframe'`, `'Points'`.

                By default it returns an empty list.

                Parameters
                ----------
                vobj : the view provider of the scripted object.
                    This is `obj.ViewObject`.

                Returns
                -------
                list
                    Empty list `[ ]`
        """
    def getDefaultDisplayMode(self):
        """Return the default mode defined in getDisplayModes.

                Override this method to return a string with the default display mode.

                By default it returns `'Flat Lines'`.

                Returns
                -------
                str
                    `'Flat Lines'`

        """
    def setDisplayMode(self, mode):
        """Map the modes defined in attach with those in getDisplayModes.

                This method is optional.

                By default since they have the same names nothing needs to be done,
                and it just returns the input `mode`.

                Parameters
                ----------
                str
                    A string defining a display mode such as
                    `'Flat Lines'`, `'Shaded'`, `'Wireframe'`, `'Points'`.
        """
    def onChanged(self, vobj, prop):
        """Run when a view property is changed.

                Override this method to handle the behavior
                of the view provider depending on changes that occur to its properties
                such as line color, line width, point color, point size,
                draw style, shape color, transparency, and others.

                This method  updates the texture and pattern if
                the properties `TextureImage`, `Pattern`, `DiffuseColor`,
                and `PatternSize` change.

                Parameters
                ----------
                vobj : the view provider of the scripted object.
                    This is `obj.ViewObject`.

                prop : str
                    Name of the property that was modified.
        """
    def _update_pattern_size(self, vobj):
        """Update the pattern size. Helper method in onChanged."""
    def execute(self, vobj):
        """Run when the object is created or recomputed.

                Override this method to produce effects when the object
                is newly created, and whenever the document is recomputed.

                By default it does nothing.

                Parameters
                ----------
                vobj : the view provider of the scripted object.
                    This is `obj.ViewObject`.
        """
    def setEdit(self, vobj, mode):
        """Enter the edit mode of the object.

                Parameters
                ----------
                vobj : the view provider of the scripted object.
                    This is `obj.ViewObject`.

                mode : int
                    0, 1, 2 or 3. See the `Std_UserEditMode` command.

                Returns
                -------
                bool or None
                    `False`: NOT USED HERE.
                             Do not enter edit mode (unsetEdit is not called).
                    `True` : Handled edit mode.
                             Handled modes are 0 and 3, and only for certain objects.
                             The unsetEdit function should then also return `True`.
                    `None` : Unhandled edit mode.
                             Handling is left to Part::FeaturePython code.
                             The unsetEdit function should then also return `None`.
        """
    def unsetEdit(self, vobj, mode):
        """Terminate the edit mode of the object.

                See setEdit.
        """
    def setupContextMenu(self, vobj, menu): ...
    def edit(self): ...
    def transform(self): ...
    def getIcon(self):
        """Return the path to the icon used by the view provider.

                The path can be a full path in the system, or a relative path
                inside the compiled resource file.
                It can also be a string that defines the icon in XPM format.

                Override this method to provide a specific icon
                for the object in the tree view.

                By default it returns the path to the `Draft_Draft.svg` icon.

                Returns
                -------
                str
                    `':/icons/Draft_Draft.svg'`
        """
    def claimChildren(self):
        """Return objects that will be placed under it in the tree view.

                Override this method to return a list with objects
                that will appear under this object in the tree view.
                That is, this object becomes the `parent`,
                and all those under it are the `children`.

                By default the returned list is composed of objects from
                `Object.Base`, `Object.Objects`, `Object.Components`,
                and `Object.Group`, if they exist.

                Returns
                -------
                list
                    List of objects.
        """

class ViewProviderDraftAlt(ViewProviderDraft):
    def __init__(self, vobj) -> None: ...
    def doubleClicked(self, vobj): ...
    def claimChildren(self): ...

class _ViewProviderDraftAlt(ViewProviderDraft):
    def __init__(self, vobj) -> None: ...
    def doubleClicked(self, vobj): ...
    def claimChildren(self): ...

class ViewProviderDraftPart(ViewProviderDraftAlt):
    def __init__(self, vobj) -> None: ...
    def getIcon(self): ...
    def setEdit(self, vobj, mode): ...
    def unsetEdit(self, vobj, mode): ...

class _ViewProviderDraftPart(ViewProviderDraftAlt):
    def __init__(self, vobj) -> None: ...
    def getIcon(self): ...
    def setEdit(self, vobj, mode): ...
    def unsetEdit(self, vobj, mode): ...
