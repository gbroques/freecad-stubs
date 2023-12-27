import Base
import FreeCAD as App
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
from _typeshed import Incomplete

def make_text(string, placement: Incomplete | None = ..., screen: bool = ...):
    """Create a Text object containing the given list of strings.

        The current color and text height and font specified in preferences
        are used.

        Parameters
        ----------
        string: str, or list of str
            String to display on screen.
            If it is a list, each element in the list represents a new text line.

        placement: Base::Placement, Base::Vector3, or Base::Rotation, optional
            It defaults to `None`.
            If it is provided, it is the placement of the new text.
            The input could be a full placement, just a vector indicating
            the translation, or just a rotation.

        screen: bool, optional
            It defaults to `False`, in which case the text is placed in 3D space
            oriented like any other object, on top of a given plane,
            by the default the XY plane.
            If it is `True`, the text will always face perpendicularly
            to the camera direction, that is, it will be flat on the screen.

        Returns
        -------
        App::FeaturePython
            A scripted object of type `'Text'`.
            This object does not have a `Shape` attribute, as the text is created
            on screen by Coin (pivy).

        None
            If there is a problem it will return `None`.
    """
def makeText(stringlist, point: Base.Vector = ..., screen: bool = ...):
    """Create Text. DEPRECATED. Use 'make_text'."""
def convert_draft_texts(textslist: Incomplete | None = ...):
    """Convert the given Annotation to a Draft text.

        In the past, the `Draft Text` object didn't exist; text objects
        were of type `App::Annotation`. This function was introduced
        to convert those older objects to a `Draft Text` scripted object.

        This function was already present at splitting time during v0.19.

        Parameters
        ----------
        textslist: list of objects, optional
            It defaults to `None`.
            A list containing `App::Annotation` objects or a single of these
            objects.
            If it is `None` it will convert all objects in the current document.
    """
def convertDraftTexts(textslist: list = ...):
    """Convert Text. DEPRECATED. Use 'convert_draft_texts'."""
