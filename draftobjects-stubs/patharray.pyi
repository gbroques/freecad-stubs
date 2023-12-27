import Base
import DraftGeomUtils as DraftGeomUtils
import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import Part as Part
import draftobjects.draftlink
import lazy_loader.lazy_loader as lz
from _typeshed import Incomplete
from draftobjects.base import DraftObject as DraftObject
from draftobjects.draftlink import DraftLink as DraftLink

def QT_TRANSLATE_NOOP(ctx, txt): ...

class PathArray(draftobjects.draftlink.DraftLink):
    def __init__(self, obj) -> None: ...
    def attach(self, obj):
        """Set up the properties when the object is attached.

                Note: we don't exactly know why the properties are added
                in the `attach` method. They should probably be added in the `__init__`
                method. Maybe this is related to the link behavior of this class.

                For PathLinkArray, DraftLink.attach creates the link to the Base.

                Realthunder: before the big merge, there was only the attach() method
                in the view object proxy, not the object proxy.
                I added that to allow the proxy to override the C++ view provider
                type. The view provider type is normally determined by object's
                C++ API getViewProviderName(), and cannot be overridden by the proxy.
                I introduced the attach() method in proxy to allow the core
                to attach the proxy before creating the C++ view provider.
        """
    def set_properties(self, obj):
        """Set properties only if they don't exist."""
    def set_general_properties(self, obj, properties):
        """Set general properties only if they don't exist."""
    def set_align_properties(self, obj, properties):
        """Set general properties only if they don't exist."""
    def linkSetup(self, obj):
        """Set up the object as a link object."""
    def execute(self, obj):
        """Execute when the object is created or recomputed."""
    def get_wires(self, path_object, subelements):
        """Get wires from the path object."""
    def get_wire_from_subelements(self, subelements):
        """Make a wire from the path object subelements."""
    def onChanged(self, obj, prop):
        """Execute when a property is changed."""
    def show_and_hide(self, obj, prop):
        """Show and hide the properties depending on the touched property.

                Note that when the array is created, some properties will change
                more than once in a seemingly random order.
        """
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored.

                Add properties that don't exist.
        """
    def migrate_properties_0v19(self, obj):
        """Migrate properties of this class, not from the parent class."""

class _PathArray(draftobjects.draftlink.DraftLink):
    def __init__(self, obj) -> None: ...
    def attach(self, obj):
        """Set up the properties when the object is attached.

                Note: we don't exactly know why the properties are added
                in the `attach` method. They should probably be added in the `__init__`
                method. Maybe this is related to the link behavior of this class.

                For PathLinkArray, DraftLink.attach creates the link to the Base.

                Realthunder: before the big merge, there was only the attach() method
                in the view object proxy, not the object proxy.
                I added that to allow the proxy to override the C++ view provider
                type. The view provider type is normally determined by object's
                C++ API getViewProviderName(), and cannot be overridden by the proxy.
                I introduced the attach() method in proxy to allow the core
                to attach the proxy before creating the C++ view provider.
        """
    def set_properties(self, obj):
        """Set properties only if they don't exist."""
    def set_general_properties(self, obj, properties):
        """Set general properties only if they don't exist."""
    def set_align_properties(self, obj, properties):
        """Set general properties only if they don't exist."""
    def linkSetup(self, obj):
        """Set up the object as a link object."""
    def execute(self, obj):
        """Execute when the object is created or recomputed."""
    def get_wires(self, path_object, subelements):
        """Get wires from the path object."""
    def get_wire_from_subelements(self, subelements):
        """Make a wire from the path object subelements."""
    def onChanged(self, obj, prop):
        """Execute when a property is changed."""
    def show_and_hide(self, obj, prop):
        """Show and hide the properties depending on the touched property.

                Note that when the array is created, some properties will change
                more than once in a seemingly random order.
        """
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored.

                Add properties that don't exist.
        """
    def migrate_properties_0v19(self, obj):
        """Migrate properties of this class, not from the parent class."""
def placements_on_path(shapeRotation, pathwire, count, xlate, align, mode: str = ..., forceNormal: bool = ..., normalOverride: Incomplete | None = ..., startOffset: float = ..., endOffset: float = ...):
    """Calculate the placements of a shape along a given path.

        Copies will be distributed evenly.
    """
def calculatePlacementsOnPath(shapeRotation, pathwire, count, xlate, align, mode: str = ..., forceNormal: bool = ..., normalOverride: Incomplete | None = ..., startOffset: float = ..., endOffset: float = ...):
    """Calculate the placements of a shape along a given path.

        Copies will be distributed evenly.
    """
def calculate_placement(globalRotation, edge, offset, RefPt, xlate, align, normal: Base.Vector = ..., mode: str = ..., overrideNormal: bool = ...):
    """Orient shape in the local coordinate system at parameter offset.

        http://en.wikipedia.org/wiki/Euler_angles (previous version)
        http://en.wikipedia.org/wiki/Quaternions
    """
def calculatePlacement(globalRotation, edge, offset, RefPt, xlate, align, normal: Base.Vector = ..., mode: str = ..., overrideNormal: bool = ...):
    """Orient shape in the local coordinate system at parameter offset.

        http://en.wikipedia.org/wiki/Euler_angles (previous version)
        http://en.wikipedia.org/wiki/Quaternions
    """
def get_parameter_from_v0(edge, offset):
    """Return parameter at distance offset from edge.Vertexes[0].

        sb method in Part.TopoShapeEdge???
    """
def getParameterFromV0(edge, offset):
    """Return parameter at distance offset from edge.Vertexes[0].

        sb method in Part.TopoShapeEdge???
    """
