import FreeCAD as App
import draftutils.utils as utils
from _typeshed import Incomplete
from draftutils.messages import _err as _err, _msg as _msg
from draftutils.translate import translate as translate

def is_group(obj):
    """Return True if the given object is considered a group.

        Parameters
        ----------
        obj : App::DocumentObject
            The object to check.

        Returns
        -------
        bool
            Returns `True` if `obj` is considered a group:

            The object is derived from `App::DocumentObjectGroup` but not
            a `'LayerContainer'`.

            Or the object is of the type `'Project'`, `'Site'`, `'Building'`,
            `'Floor'`, `'BuildingPart'` or `'Space'` from the Arch Workbench.
            Note that `'Floor'` and `'Building'` are obsolete types.

            Otherwise returns `False`.
    """
def get_group_names(doc: Incomplete | None = ...):
    """Return a list of names of existing groups in the document.

        Parameters
        ----------
        doc: App::Document, optional
            It defaults to `None`.
            A document on which to search group names.
            It if is `None` it will search the current document.

        Returns
        -------
        list of str
            A list of names of objects that are considered groups.
            See the is_group function.

            Otherwise returns an empty list.
    """
def getGroupNames():
    """Return a list of group names. DEPRECATED."""
def ungroup(obj):
    '''Remove the object from any group to which it belongs.

        A "group" is any object returned by `get_group_names`.

        Parameters
        ----------
        obj: App::DocumentObject or str
            Any type of object.
            If it is a string, it must be the `Label` of that object.
            Since a label is not guaranteed to be unique in a document,
            it will use the first object found with this label.
    '''
def get_windows(obj):
    """Return the windows and rebars inside a host.

        Parameters
        ----------
        obj: App::DocumentObject
            A scripted object of type `'Wall'` or `'Structure'`
            (Arch Workbench).
            This will be searched for objects of type `'Window'` and `'Rebar'`,
            and clones of them, and the found elements will be added
            to the output list.

            The function will search recursively all elements under `obj.OutList`,
            in case the windows and rebars are nested under other walls
            and structures.

        Returns
        -------
        list
            A list of all found windows and rebars in `obj`.
            If `obj` is itself a `'Window'` or a `'Rebar'`, or a clone of them,
            it will return the same `obj` element.
    """
def get_group_contents(objectslist, walls: bool = ..., addgroups: bool = ..., spaces: bool = ..., noarchchild: bool = ...):
    '''Return a list of objects from expanding the input groups.

        The function accepts any type of object, although it is most useful
        with "groups", as it is meant to unpack the objects inside these groups.

        Parameters
        ----------
        objectslist: list
            If any object in the list is considered a group, see the `is_group`
            function, its contents (`obj.Group`) are extracted and added to the
            output list.

            Single items that aren\'t groups are added to the output list
            as is.

        walls: bool, optional
            It defaults to `False`.
            If it is `True`, Wall and Structure objects (Arch Workbench)
            are treated as groups; they are scanned for Window, Door,
            and Rebar objects, and these are added to the output list.

        addgroups: bool, optional
            It defaults to `False`.
            If it is `True`, the group itself is kept as part of the output list.

        spaces: bool, optional
            It defaults to `False`.
            If it is `True`, Arch Spaces are added to the output list even
            when addgroups is False (their contents are always added).

        noarchchild: bool, optional
            It defaults to `False`.
            If it is `True`, the objects inside Building and BuildingParts
            (Arch Workbench) aren\'t added to the output list.

        Returns
        -------
        list
            The list of objects from each group present in `objectslist`,
            plus any other individual object given in `objectslist`.
    '''
def getGroupContents(objectslist, walls: bool = ..., addgroups: bool = ..., spaces: bool = ..., noarchchild: bool = ...):
    """Return a list of objects from groups. DEPRECATED."""
def get_movable_children(objectslist, recursive: bool = ..., _donelist: list = ...):
    """Return a list of objects with child objects that move with a host.

        Builds a list of objects with all child objects (`obj.OutList`)
        that have their `MoveWithHost` attribute set to `True`.
        This function is mostly useful for Arch Workbench objects.

        Parameters
        ----------
        objectslist: list of App::DocumentObject
            A single scripted object or list of objects.

        recursive: bool, optional
            It defaults to `True`, in which case the function
            is called recursively to also extract the children of children
            objects.
            Otherwise, only direct children of the input objects
            are added to the output list.

        _donelist: list
            List of object names. Used internally to prevent an endless loop.

        Returns
        -------
        list
            List of children objects that have their `MoveWithHost` attribute
            set to `True`.
    """
def getMovableChildren(objectslist, recursive: bool = ...):
    """Return a list of objects with child objects. DEPRECATED."""
