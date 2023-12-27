import DraftGeomUtils as DraftGeomUtils
import FreeCAD as App
import Part as Part
import draftobjects.base
import lazy_loader.lazy_loader as lz
from draftobjects.base import DraftObject as DraftObject

class DraftLink(draftobjects.base.DraftObject):
    def __init__(self, obj, tp) -> None: ...
    def dumps(self):
        """Return a tuple of all serializable objects or None."""
    def loads(self, state):
        """Set some internal properties for all restored objects."""
    def attach(self, obj):
        """Set up the properties when the object is attached."""
    def canLinkProperties(self, _obj):
        """Link properties.

                TODO: add more explanation. Overrides a C++ method?
        """
    def linkSetup(self, obj):
        """Set up the link properties on attachment."""
    def getViewProviderName(self, _obj):
        """Override the view provider name."""
    def migrate_attributes(self, obj):
        """Migrate old attribute names to new names if they exist.

                This is done to comply with Python guidelines or fix small issues
                in older code.
        """
    def onDocumentRestored(self, obj):
        """Execute code when the document in restored."""
    def buildShape(self, obj, pl, pls):
        """Build the shape of the link object."""
    def onChanged(self, obj, prop):
        """Execute when a property changes."""

class _DraftLink(draftobjects.base.DraftObject):
    def __init__(self, obj, tp) -> None: ...
    def dumps(self):
        """Return a tuple of all serializable objects or None."""
    def loads(self, state):
        """Set some internal properties for all restored objects."""
    def attach(self, obj):
        """Set up the properties when the object is attached."""
    def canLinkProperties(self, _obj):
        """Link properties.

                TODO: add more explanation. Overrides a C++ method?
        """
    def linkSetup(self, obj):
        """Set up the link properties on attachment."""
    def getViewProviderName(self, _obj):
        """Override the view provider name."""
    def migrate_attributes(self, obj):
        """Migrate old attribute names to new names if they exist.

                This is done to comply with Python guidelines or fix small issues
                in older code.
        """
    def onDocumentRestored(self, obj):
        """Execute code when the document in restored."""
    def buildShape(self, obj, pl, pls):
        """Build the shape of the link object."""
    def onChanged(self, obj, prop):
        """Execute when a property changes."""
