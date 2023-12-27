import FreeCAD as App
import draftutils.utils as utils
from _typeshed import Incomplete

view_group: ParameterGrp
def get_layer_container():
    """Return a group object to put layers in.

        Returns
        -------
        App::DocumentObjectGroupPython
            The existing group object named `'LayerContainer'`
            of type `LayerContainer`.
            If it doesn't exist it will create it with this default Name.
    """
def getLayerContainer():
    """Get the Layer container. DEPRECATED. Use 'get_layer_container'."""
def make_layer(name: Incomplete | None = ..., line_color: Incomplete | None = ..., shape_color: Incomplete | None = ..., line_width: float = ..., draw_style: str = ..., transparency: int = ...):
    """Create a Layer object in the active document.

        If a layer container named `'LayerContainer'` does not exist,
        it is created with this name.

        A layer controls the view properties of the objects inside the layer,
        so all parameters except for `name` only apply if the graphical interface
        is up.

        Parameters
        ----------
        name: str, optional
            It is used to set the layer's `Label` (user editable).
            It defaults to `None`, in which case the `Label`
            is set to `'Layer'` or to its translation in the current language.

        line_color: tuple, optional
            It defaults to `None`, in which case it uses the value of the parameter
            `User parameter:BaseApp/Preferences/View/DefaultShapeLineColor`.
            If it is given, it should be a tuple of three
            floating point values from 0.0 to 1.0.

        shape_color: tuple, optional
            It defaults to `None`, in which case it uses the value of the parameter
            `User parameter:BaseApp/Preferences/View/DefaultShapeColor`.
            If it is given, it should be a tuple of three
            floating point values from 0.0 to 1.0.

        line_width: float, optional
            It defaults to 2.0.
            It determines the width of the edges of the objects contained
            in the layer.

        draw_style: str, optional
            It defaults to `'Solid'`.
            It determines the style of the edges of the objects contained
            in the layer.
            If it is given, it should be 'Solid', 'Dashed', 'Dotted',
            or 'Dashdot'.

        transparency: int, optional
            It defaults to 0.
            It should be an integer value from 0 (completely opaque)
            to 100 (completely transparent).

        Return
        ------
        App::FeaturePython
            A scripted object of type `'Layer'`.
            This object does not have a `Shape` attribute.
            Modifying the view properties of this object will affect the objects
            inside of it.

        None
            If there is a problem it will return `None`.
    """
def makeLayer(name: Incomplete | None = ..., linecolor: Incomplete | None = ..., drawstyle: Incomplete | None = ..., shapecolor: Incomplete | None = ..., transparency: Incomplete | None = ...):
    """Create a Layer. DEPRECATED. Use 'make_layer'."""
