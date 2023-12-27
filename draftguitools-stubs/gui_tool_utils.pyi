import FreeCAD as App
import FreeCADGui as Gui
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
from _typeshed import Incomplete

MODS: list
MODCONSTRAIN: str
MODSNAP: str
MODALT: str
def format_unit(exp, unit: str = ...):
    """Return a formatting string to set a number to the correct unit."""
def formatUnit(exp, unit: str = ...):
    """Return a formatting string to set a number to the correct unit."""
def select_object(arg):
    '''Handle the selection of objects depending on buttons pressed.

        This is a scene event handler, to be called from the Draft tools
        when they need to select an object.
        ::
            self.call = self.view.addEventCallback("SoEvent", select_object)

        Parameters
        ----------
        arg: Coin event
            The Coin event received from the 3D view.

            If it is of type Keyboard and the `ESCAPE` key, it runs the `finish`
            method of the active command.

            If Ctrl key is pressed, multiple selection is enabled until the
            button is released.
            Then it runs the `proceed` method of the active command
            to continue with the command\'s logic.
    '''
def selectObject(arg):
    '''Handle the selection of objects depending on buttons pressed.

        This is a scene event handler, to be called from the Draft tools
        when they need to select an object.
        ::
            self.call = self.view.addEventCallback("SoEvent", select_object)

        Parameters
        ----------
        arg: Coin event
            The Coin event received from the 3D view.

            If it is of type Keyboard and the `ESCAPE` key, it runs the `finish`
            method of the active command.

            If Ctrl key is pressed, multiple selection is enabled until the
            button is released.
            Then it runs the `proceed` method of the active command
            to continue with the command\'s logic.
    '''
def has_mod(args, mod):
    '''Check if args has a specific modifier.

        Parameters
        ----------
        args: Coin event
            The Coin event received from the 3D view.

        mod: str
            A string indicating the modifier, either `\'shift\'`, `\'ctrl\'`,
            or `\'alt\'`.

        Returns
        -------
        bool
            It returns `args["ShiftDown"]`, `args["CtrlDown"]`,
            or `args["AltDown"]`, depending on the passed value of `mod`.
    '''
def hasMod(args, mod):
    '''Check if args has a specific modifier.

        Parameters
        ----------
        args: Coin event
            The Coin event received from the 3D view.

        mod: str
            A string indicating the modifier, either `\'shift\'`, `\'ctrl\'`,
            or `\'alt\'`.

        Returns
        -------
        bool
            It returns `args["ShiftDown"]`, `args["CtrlDown"]`,
            or `args["AltDown"]`, depending on the passed value of `mod`.
    '''
def set_mod(args, mod, state):
    '''Set a specific modifier state in args.

        Parameters
        ----------
        args: Coin event
            The Coin event received from the 3D view.

        mod: str
            A string indicating the modifier, either `\'shift\'`, `\'ctrl\'`,
            or `\'alt\'`.

        state: bool
            The boolean value of `state` is assigned to `args["ShiftDown"]`,
            `args["CtrlDown"]`, or `args["AltDown"]`
            depending on `mod`.
    '''
def setMod(args, mod, state):
    '''Set a specific modifier state in args.

        Parameters
        ----------
        args: Coin event
            The Coin event received from the 3D view.

        mod: str
            A string indicating the modifier, either `\'shift\'`, `\'ctrl\'`,
            or `\'alt\'`.

        state: bool
            The boolean value of `state` is assigned to `args["ShiftDown"]`,
            `args["CtrlDown"]`, or `args["AltDown"]`
            depending on `mod`.
    '''
def get_point(target, args, mobile: bool = ..., sym: bool = ..., workingplane: bool = ..., noTracker: bool = ...):
    """Return a constrained 3D point and its original point.

        It is used by the Draft tools.

        Parameters
        ----------
        target: object (class)
            The target object with a `node` attribute. If this is present,
            return the last node, otherwise return `None`.

            In the Draft tools, `target` is essentially the same class
            of the Gui command, that is, `self`. Therefore, this method
            probably makes more sense as a class method.

        args: Coin event
            The Coin event received from the 3D view.

        mobile: bool, optional
            It defaults to `False`.
            If it is `True` the constraining occurs from the location of
            the mouse cursor when `Shift` is pressed; otherwise from the last
            entered point.

        sym: bool, optional
            It defaults to `False`.
            If it is `True`, the x and y values always stay equal.

        workingplane: bool, optional
            It defaults to `True`.
            If it is `False`, the point won't be projected on the currently
            active working plane.

        noTracker: bool, optional
            It defaults to `False`.
            If it is `True`, the tracking line will not be displayed.

        Returns
        -------
        CoinPoint, Base::Vector3, str
            It returns a tuple with some information.

            The first is the Coin point returned by `Snapper.snap`
            or by the `ActiveView`; the second is that same point
            turned into an `App.Vector`,
            and the third is some information of the point
            returned by the `Snapper` or by the `ActiveView`.
    """
def getPoint(target, args, mobile: bool = ..., sym: bool = ..., workingplane: bool = ..., noTracker: bool = ...):
    """Return a constrained 3D point and its original point.

        It is used by the Draft tools.

        Parameters
        ----------
        target: object (class)
            The target object with a `node` attribute. If this is present,
            return the last node, otherwise return `None`.

            In the Draft tools, `target` is essentially the same class
            of the Gui command, that is, `self`. Therefore, this method
            probably makes more sense as a class method.

        args: Coin event
            The Coin event received from the 3D view.

        mobile: bool, optional
            It defaults to `False`.
            If it is `True` the constraining occurs from the location of
            the mouse cursor when `Shift` is pressed; otherwise from the last
            entered point.

        sym: bool, optional
            It defaults to `False`.
            If it is `True`, the x and y values always stay equal.

        workingplane: bool, optional
            It defaults to `True`.
            If it is `False`, the point won't be projected on the currently
            active working plane.

        noTracker: bool, optional
            It defaults to `False`.
            If it is `True`, the tracking line will not be displayed.

        Returns
        -------
        CoinPoint, Base::Vector3, str
            It returns a tuple with some information.

            The first is the Coin point returned by `Snapper.snap`
            or by the `ActiveView`; the second is that same point
            turned into an `App.Vector`,
            and the third is some information of the point
            returned by the `Snapper` or by the `ActiveView`.
    """
def set_working_plane_to_object_under_cursor(mouseEvent):
    """Set the working plane to the object under the cursor.

        It tests for an object under the cursor.
        If it is found, it checks whether a `'face'` or `'curve'` component
        is selected in the object's `Shape`.
        Then it tries to align the working plane to that face or curve.

        The working plane is only aligned to the face if
        the working plane is not `'weak'`.

        Parameters
        ----------
        mouseEvent: Coin event
            Coin event with the mouse, that is, a click.

        Returns
        -------
        None
            If no object was found in the 3D view under the cursor.
            Or if the working plane is not `weak`.
            Or if there was an exception with aligning the working plane
            to the component under the cursor.

        Coin info
            The `getObjectInfo` of the object under the cursor.
    """
def setWorkingPlaneToObjectUnderCursor(mouseEvent):
    """Set the working plane to the object under the cursor.

        It tests for an object under the cursor.
        If it is found, it checks whether a `'face'` or `'curve'` component
        is selected in the object's `Shape`.
        Then it tries to align the working plane to that face or curve.

        The working plane is only aligned to the face if
        the working plane is not `'weak'`.

        Parameters
        ----------
        mouseEvent: Coin event
            Coin event with the mouse, that is, a click.

        Returns
        -------
        None
            If no object was found in the 3D view under the cursor.
            Or if the working plane is not `weak`.
            Or if there was an exception with aligning the working plane
            to the component under the cursor.

        Coin info
            The `getObjectInfo` of the object under the cursor.
    """
def set_working_plane_to_selected_object():
    """Set the working plane to the selected object's face.

        The working plane is only aligned to the face if
        the working plane is `'weak'`.

        Returns
        -------
        None
            If more than one object was selected.
            Or if the selected object has many subelements.
            Or if the single subelement is not a `'Face'`.

        App::DocumentObject
            The single object that contains a single selected face.
    """
def setWorkingPlaneToSelectedObject():
    """Set the working plane to the selected object's face.

        The working plane is only aligned to the face if
        the working plane is `'weak'`.

        Returns
        -------
        None
            If more than one object was selected.
            Or if the selected object has many subelements.
            Or if the single subelement is not a `'Face'`.

        App::DocumentObject
            The single object that contains a single selected face.
    """
def get_support(mouseEvent: Incomplete | None = ...):
    """Return the supporting object and set the working plane.

        It saves the current working plane, then sets it to the selected object.

        Parameters
        ----------
        mouseEvent: Coin event, optional
            It defaults to `None`.
            Coin event with the mouse, that is, a click.

            If there is a mouse event it calls
            `set_working_plane_to_object_under_cursor`.
            Otherwise, it calls `set_working_plane_to_selected_object`.

        Returns
        -------
        None
            If there was a mouse event, but there was nothing under the cursor.
            Or if the working plane is not `weak`.
            Or if there was an exception with aligning the working plane
            to the component under the cursor.
            Or if more than one object was selected.
            Or if the selected object has many subelements.
            Or if the single subelement is not a `'Face'`.

        Coin info
            If there was a mouse event, the `getObjectInfo`
            of the object under the cursor.

        App::DocumentObject
            If there was no mouse event, the single selected object
            that contains the single selected face that was used
            to align the working plane.
    """
def getSupport(mouseEvent: Incomplete | None = ...):
    """Return the supporting object and set the working plane.

        It saves the current working plane, then sets it to the selected object.

        Parameters
        ----------
        mouseEvent: Coin event, optional
            It defaults to `None`.
            Coin event with the mouse, that is, a click.

            If there is a mouse event it calls
            `set_working_plane_to_object_under_cursor`.
            Otherwise, it calls `set_working_plane_to_selected_object`.

        Returns
        -------
        None
            If there was a mouse event, but there was nothing under the cursor.
            Or if the working plane is not `weak`.
            Or if there was an exception with aligning the working plane
            to the component under the cursor.
            Or if more than one object was selected.
            Or if the selected object has many subelements.
            Or if the single subelement is not a `'Face'`.

        Coin info
            If there was a mouse event, the `getObjectInfo`
            of the object under the cursor.

        App::DocumentObject
            If there was no mouse event, the single selected object
            that contains the single selected face that was used
            to align the working plane.
    """
def redraw_3d_view():
    """Force a redraw of 3D view or do nothing if it fails."""
def redraw3DView():
    """Force a redraw of 3D view or do nothing if it fails."""
