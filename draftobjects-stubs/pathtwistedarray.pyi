import draftgeoutils.geo_arrays as geo
import draftobjects.draftlink
from draftobjects.draftlink import DraftLink as DraftLink

def QT_TRANSLATE_NOOP(ctx, txt): ...

class PathTwistedArray(draftobjects.draftlink.DraftLink):
    def __init__(self, obj) -> None: ...
    def attach(self, obj):
        """Set up the properties when the object is attached."""
    def set_properties(self, obj):
        """Set properties only if they don't exist."""
    def linkSetup(self, obj):
        """Set up the object as a link object."""
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored.

                Add properties that don't exist.
        """
    def execute(self, obj):
        """Execute when the object is created or recomputed."""
