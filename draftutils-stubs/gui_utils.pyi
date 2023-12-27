import FreeCAD as App
import FreeCADGui as Gui
import PySide.QtGui as QtGui
import draftutils.utils as utils
from _typeshed import Incomplete
from draftutils.messages import _err as _err, _msg as _msg, _wrn as _wrn
from draftutils.translate import translate as translate

def get_3d_view():
    """Return the current 3D view.

        Returns
        -------
        Gui::View3DInventor
            Return the current `ActiveView` in the active document,
            or the first `Gui::View3DInventor` view found.

            Return `None` if the graphical interface is not available.
    """
def get3DView():
    """Return the current 3D view.

        Returns
        -------
        Gui::View3DInventor
            Return the current `ActiveView` in the active document,
            or the first `Gui::View3DInventor` view found.

            Return `None` if the graphical interface is not available.
    """
def autogroup(obj):
    """Add a given object to the defined Draft autogroup, if applicable.

        This function only works if the graphical interface is available.
        It checks that the `App.draftToolBar` class is available,
        which contains the group to use to automatically store
        new created objects.

        Originally, it worked with standard groups (`App::DocumentObjectGroup`),
        and Arch Workbench containers like `'Site'`, `'Building'`, `'Floor'`,
        and `'BuildingPart'`.

        Now it works with Draft Layers.

        Parameters
        ----------
        obj: App::DocumentObject
            Any type of object that will be stored in the group.
    """
def dim_symbol(symbol: Incomplete | None = ..., invert: bool = ...):
    '''Return the specified dimension symbol.

        Parameters
        ----------
        symbol: int, optional
            It defaults to `None`, in which it gets the value from the parameter
            database, `get_param("dimsymbol", 0)`.

            A numerical value defines different markers
             * 0, `SoSphere`
             * 1, `SoSeparator` with a `SoLineSet`, a circle (in fact a 24 sided polygon)
             * 2, `SoSeparator` with a `soCone`
             * 3, `SoSeparator` with a `SoFaceSet`
             * 4, `SoSeparator` with a `SoLineSet`, calling `dim_dash`
             * Otherwise, `SoSphere`

        invert: bool, optional
            It defaults to `False`.
            If it is `True` and `symbol=2`, the cone will be rotated
            -90 degrees around the Z axis, otherwise the rotation is positive,
            +90 degrees.

        Returns
        -------
        Coin.SoNode
            A `Coin.SoSphere`, or `Coin.SoSeparator` (circle, cone, face, line)
            that will be used as a dimension symbol.
    '''
def dimSymbol(symbol: Incomplete | None = ..., invert: bool = ...):
    '''Return the specified dimension symbol.

        Parameters
        ----------
        symbol: int, optional
            It defaults to `None`, in which it gets the value from the parameter
            database, `get_param("dimsymbol", 0)`.

            A numerical value defines different markers
             * 0, `SoSphere`
             * 1, `SoSeparator` with a `SoLineSet`, a circle (in fact a 24 sided polygon)
             * 2, `SoSeparator` with a `soCone`
             * 3, `SoSeparator` with a `SoFaceSet`
             * 4, `SoSeparator` with a `SoLineSet`, calling `dim_dash`
             * Otherwise, `SoSphere`

        invert: bool, optional
            It defaults to `False`.
            If it is `True` and `symbol=2`, the cone will be rotated
            -90 degrees around the Z axis, otherwise the rotation is positive,
            +90 degrees.

        Returns
        -------
        Coin.SoNode
            A `Coin.SoSphere`, or `Coin.SoSeparator` (circle, cone, face, line)
            that will be used as a dimension symbol.
    '''
def dim_dash(p1, p2):
    """Return a SoSeparator with a line used to make dimension dashes.

        It is used by `dim_symbol` to create line end symbols
        like `'Tick-2'`, `'DimOvershoot'`, and `'ExtOvershoot'` dashes.

        Parameters
        ----------
        p1: tuple of three floats or Base::Vector3
            A point to define a line vertex.

        p2: tuple of three floats or Base::Vector3
            A point to define a line vertex.

        Returns
        -------
        Coin.SoSeparator
            A Coin object with a `SoLineSet` created from `p1` and `p2`
            as vertices.
    """
def dimDash(p1, p2):
    """Return a SoSeparator with a line used to make dimension dashes.

        It is used by `dim_symbol` to create line end symbols
        like `'Tick-2'`, `'DimOvershoot'`, and `'ExtOvershoot'` dashes.

        Parameters
        ----------
        p1: tuple of three floats or Base::Vector3
            A point to define a line vertex.

        p2: tuple of three floats or Base::Vector3
            A point to define a line vertex.

        Returns
        -------
        Coin.SoSeparator
            A Coin object with a `SoLineSet` created from `p1` and `p2`
            as vertices.
    """
def remove_hidden(objectslist):
    """Return only the visible objects in the list.

        This function only works if the graphical interface is available
        as the `Visibility` attribute is a property of the view provider
        (`obj.ViewObject`).

        Parameters
        ----------
        objectslist: list of App::DocumentObject
            List of any type of object.

        Returns
        -------
        list
            Return a copy of the input list without those objects
            for which `obj.ViewObject.Visibility` is `False`.

            If the graphical interface is not loaded
            the returned list is just a copy of the input list.
    """
def removeHidden(objectslist):
    """Return only the visible objects in the list.

        This function only works if the graphical interface is available
        as the `Visibility` attribute is a property of the view provider
        (`obj.ViewObject`).

        Parameters
        ----------
        objectslist: list of App::DocumentObject
            List of any type of object.

        Returns
        -------
        list
            Return a copy of the input list without those objects
            for which `obj.ViewObject.Visibility` is `False`.

            If the graphical interface is not loaded
            the returned list is just a copy of the input list.
    """
def get_diffuse_color(objs):
    """Get a (cumulative) diffuse color from one or more objects.

        If all tuples in the result are identical a list with a single tuple is
        returned. In theory all faces of an object can be set to the same diffuse
        color that is different from its shape color, but that seems rare. The
        function does not take that into account.

        Parameters
        ----------
        objs: a single object or an iterable with objects.

        Returns
        -------
        list of tuples
            The list will be empty if no valid object is found.
    """
def format_object(target, origin: Incomplete | None = ...):
    """Apply visual properties from the Draft toolbar or another object.

        This function only works if the graphical interface is available
        as the visual properties are attributes of the view provider
        (`obj.ViewObject`).

        Parameters
        ----------
        target: App::DocumentObject
            Any type of scripted object.

            This object will adopt the applicable visual properties,
            `FontSize`, `TextColor`, `LineWidth`, `PointColor`, `LineColor`,
            and `ShapeColor`, defined in the Draft toolbar
            (`Gui.draftToolBar`) or will adopt
            the properties from the `origin` object.

            The `target` is also placed in the construction group
            if the construction mode in the Draft toolbar is active.

        origin: App::DocumentObject, optional
            It defaults to `None`.
            If it exists, it will provide the visual properties to assign
            to `target`, with the exception of `BoundingBox`, `Proxy`,
            `RootNode` and `Visibility`.
    """
def formatObject(target, origin: Incomplete | None = ...):
    """Apply visual properties from the Draft toolbar or another object.

        This function only works if the graphical interface is available
        as the visual properties are attributes of the view provider
        (`obj.ViewObject`).

        Parameters
        ----------
        target: App::DocumentObject
            Any type of scripted object.

            This object will adopt the applicable visual properties,
            `FontSize`, `TextColor`, `LineWidth`, `PointColor`, `LineColor`,
            and `ShapeColor`, defined in the Draft toolbar
            (`Gui.draftToolBar`) or will adopt
            the properties from the `origin` object.

            The `target` is also placed in the construction group
            if the construction mode in the Draft toolbar is active.

        origin: App::DocumentObject, optional
            It defaults to `None`.
            If it exists, it will provide the visual properties to assign
            to `target`, with the exception of `BoundingBox`, `Proxy`,
            `RootNode` and `Visibility`.
    """
def get_selection(gui: int = ...):
    """Return the current selected objects.

        This function only works if the graphical interface is available
        as the selection module only works on the 3D view.

        It wraps around `Gui.Selection.getSelection`

        Parameters
        ----------
        gui: bool, optional
            It defaults to the value of `App.GuiUp`, which is `True`
            when the interface exists, and `False` otherwise.

            This value can be set to `False` to simulate
            when the interface is not available.

        Returns
        -------
        list of App::DocumentObject
            Returns a list of objects in the current selection.
            It can be an empty list if no object is selected.

            If the interface is not available, it returns `None`.
    """
def getSelection(gui: int = ...):
    """Return the current selected objects.

        This function only works if the graphical interface is available
        as the selection module only works on the 3D view.

        It wraps around `Gui.Selection.getSelection`

        Parameters
        ----------
        gui: bool, optional
            It defaults to the value of `App.GuiUp`, which is `True`
            when the interface exists, and `False` otherwise.

            This value can be set to `False` to simulate
            when the interface is not available.

        Returns
        -------
        list of App::DocumentObject
            Returns a list of objects in the current selection.
            It can be an empty list if no object is selected.

            If the interface is not available, it returns `None`.
    """
def get_selection_ex(gui: int = ...):
    """Return the current selected objects together with their subelements.

        This function only works if the graphical interface is available
        as the selection module only works on the 3D view.

        It wraps around `Gui.Selection.getSelectionEx`

        Parameters
        ----------
        gui: bool, optional
            It defaults to the value of `App.GuiUp`, which is `True`
            when the interface exists, and `False` otherwise.

            This value can be set to `False` to simulate
            when the interface is not available.

        Returns
        -------
        list of Gui::SelectionObject
            Returns a list of `Gui::SelectionObject` in the current selection.
            It can be an empty list if no object is selected.

            If the interface is not available, it returns `None`.

        Selection objects
        -----------------
        One `Gui::SelectionObject` has attributes that indicate which specific
        subelements, that is, vertices, wires, and faces, were selected.
        This can be useful to operate on the subelements themselves.
        If `G` is a `Gui::SelectionObject`
         * `G.Object` is the selected object
         * `G.ObjectName` is the name of the selected object
         * `G.HasSubObjects` is `True` if there are subelements in the selection
         * `G.SubObjects` is a tuple of the subelements' shapes
         * `G.SubElementNames` is a tuple of the subelements' names

        `SubObjects` and `SubElementNames` should be empty tuples
        if `HasSubObjects` is `False`.
    """
def getSelectionEx(gui: int = ...):
    """Return the current selected objects together with their subelements.

        This function only works if the graphical interface is available
        as the selection module only works on the 3D view.

        It wraps around `Gui.Selection.getSelectionEx`

        Parameters
        ----------
        gui: bool, optional
            It defaults to the value of `App.GuiUp`, which is `True`
            when the interface exists, and `False` otherwise.

            This value can be set to `False` to simulate
            when the interface is not available.

        Returns
        -------
        list of Gui::SelectionObject
            Returns a list of `Gui::SelectionObject` in the current selection.
            It can be an empty list if no object is selected.

            If the interface is not available, it returns `None`.

        Selection objects
        -----------------
        One `Gui::SelectionObject` has attributes that indicate which specific
        subelements, that is, vertices, wires, and faces, were selected.
        This can be useful to operate on the subelements themselves.
        If `G` is a `Gui::SelectionObject`
         * `G.Object` is the selected object
         * `G.ObjectName` is the name of the selected object
         * `G.HasSubObjects` is `True` if there are subelements in the selection
         * `G.SubObjects` is a tuple of the subelements' shapes
         * `G.SubElementNames` is a tuple of the subelements' names

        `SubObjects` and `SubElementNames` should be empty tuples
        if `HasSubObjects` is `False`.
    """
def select(objs: Incomplete | None = ..., gui: int = ...):
    """Unselects everything and selects only the given list of objects.

        This function only works if the graphical interface is available
        as the selection module only works on the 3D view.

        Parameters
        ----------
        objs: list of App::DocumentObject, optional
            It defaults to `None`.
            Any type of scripted object.
            It may be a list of objects or a single object.

        gui: bool, optional
            It defaults to the value of `App.GuiUp`, which is `True`
            when the interface exists, and `False` otherwise.

            This value can be set to `False` to simulate
            when the interface is not available.
    """
def load_texture(filename, size: Incomplete | None = ..., gui: int = ...):
    """Return a Coin.SoSFImage to use as a texture for a 2D plane.

        This function only works if the graphical interface is available
        as the visual properties that can be applied to a shape
        are attributes of the view provider (`obj.ViewObject`).

        Parameters
        ----------
        filename: str
            A path to a pixel image file (PNG) that can be used as a texture
            on the face of an object.

        size: tuple of two int, or a single int, optional
            It defaults to `None`.
            If a tuple is given, the two values define the width and height
            in pixels to which the loaded image will be scaled.
            If it is a single value, it is used for both dimensions.

            If it is `None`, the size will be determined from the `QImage`
            created from `filename`.

            CURRENTLY the input `size` parameter IS NOT USED.
            It always uses the `QImage` to determine this information.

        gui: bool, optional
            It defaults to the value of `App.GuiUp`, which is `True`
            when the interface exists, and `False` otherwise.

            This value can be set to `False` to simulate
            when the interface is not available.

        Returns
        -------
        coin.SoSFImage
            An image object with the appropriate size, number of components
            (grayscale, grayscale and transparency, color,
            color and transparency), and byte data.

            It returns `None` if the interface is not available,
            or if there is a problem creating the image.
    """
def loadTexture(filename, size: Incomplete | None = ..., gui: int = ...):
    """Return a Coin.SoSFImage to use as a texture for a 2D plane.

        This function only works if the graphical interface is available
        as the visual properties that can be applied to a shape
        are attributes of the view provider (`obj.ViewObject`).

        Parameters
        ----------
        filename: str
            A path to a pixel image file (PNG) that can be used as a texture
            on the face of an object.

        size: tuple of two int, or a single int, optional
            It defaults to `None`.
            If a tuple is given, the two values define the width and height
            in pixels to which the loaded image will be scaled.
            If it is a single value, it is used for both dimensions.

            If it is `None`, the size will be determined from the `QImage`
            created from `filename`.

            CURRENTLY the input `size` parameter IS NOT USED.
            It always uses the `QImage` to determine this information.

        gui: bool, optional
            It defaults to the value of `App.GuiUp`, which is `True`
            when the interface exists, and `False` otherwise.

            This value can be set to `False` to simulate
            when the interface is not available.

        Returns
        -------
        coin.SoSFImage
            An image object with the appropriate size, number of components
            (grayscale, grayscale and transparency, color,
            color and transparency), and byte data.

            It returns `None` if the interface is not available,
            or if there is a problem creating the image.
    """
def migrate_text_display_mode(obj_type: str = ..., mode: str = ..., doc: Incomplete | None = ...):
    """Migrate the display mode of objects of certain type."""
def get_bbox(obj, debug: bool = ...):
    """Return a BoundBox from any object that has a Coin RootNode.

        Normally the bounding box of an object can be taken
        from its `Part::TopoShape`.
        ::
            >>> print(obj.Shape.BoundBox)

        However, for objects without a `Shape`, such as those
        derived from `App::FeaturePython` like `Draft Text` and `Draft Dimension`,
        the bounding box can be calculated from the `RootNode` of the viewprovider.

        Parameters
        ----------
        obj: App::DocumentObject
            Any object that has a `ViewObject.RootNode`.

        Returns
        -------
        Base::BoundBox
            It returns a `BoundBox` object which has information like
            minimum and maximum values of X, Y, and Z, as well as bounding box
            center.

        None
            If there is a problem it will return `None`.
    """
