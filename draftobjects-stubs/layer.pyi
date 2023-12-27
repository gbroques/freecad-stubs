class Layer:
    def __init__(self, obj) -> None: ...
    def set_properties(self, obj):
        """Set properties only if they don't exist."""
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored."""
    def add_missing_properties_0v19(self, obj, vobj):
        """Update view properties."""
    def dumps(self):
        """Return a tuple of objects to save or None."""
    def loads(self, state):
        """Set the internal properties from the restored state."""
    def execute(self, obj):
        """Execute when the object is created or recomputed. Do nothing."""
    def addObject(self, obj, child):
        """Add an object to this object if not in the Group property."""

class _VisGroup:
    def __init__(self, obj) -> None: ...
    def set_properties(self, obj):
        """Set properties only if they don't exist."""
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored."""
    def add_missing_properties_0v19(self, obj, vobj):
        """Update view properties."""
    def dumps(self):
        """Return a tuple of objects to save or None."""
    def loads(self, state):
        """Set the internal properties from the restored state."""
    def execute(self, obj):
        """Execute when the object is created or recomputed. Do nothing."""
    def addObject(self, obj, child):
        """Add an object to this object if not in the Group property."""

class LayerContainer:
    def __init__(self, obj) -> None: ...
    def execute(self, obj):
        """Execute when the object is created or recomputed.

                Update the value of `Group` by sorting the contained layers
                by `Label`.
        """
    def dumps(self):
        """Return a tuple of objects to save or None."""
    def loads(self, state):
        """Set the internal properties from the restored state."""
