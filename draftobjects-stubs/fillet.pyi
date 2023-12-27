import FreeCAD as App
import draftobjects.base
import draftobjects.base as base

class Fillet(draftobjects.base.DraftObject):
    def __init__(self, obj) -> None: ...
    def _set_properties(self, obj):
        """Set the properties of objects if they don't exist."""
    def execute(self, obj):
        """Run when the object is created or recomputed."""
    def _update_radius(self, obj, radius): ...
    def onChanged(self, obj, prop):
        """Change the radius of fillet. NOT IMPLEMENTED.

                This should automatically recalculate the new fillet
                based on the new value of `FilletRadius`.
        """
