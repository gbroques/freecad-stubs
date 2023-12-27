import FreeCAD as App
import FreeCADGui as Gui
import draftutils.utils as utils
import draftviewproviders.view_draft_annotation
from draftviewproviders.view_draft_annotation import ViewProviderDraftAnnotation as ViewProviderDraftAnnotation

class ViewProviderText(draftviewproviders.view_draft_annotation.ViewProviderDraftAnnotation):
    def set_text_properties(self, vobj, properties):
        """Set text properties only if they don't already exist."""
    def getIcon(self):
        """Return the path to the icon used by the view provider."""
    def attach(self, vobj):
        """Set up the scene sub-graph of the view provider."""
    def updateData(self, obj, prop):
        """Execute when a property from the Proxy class is changed."""
    def onChanged(self, vobj, prop):
        """Execute when a view property is changed."""
    def edit(self): ...
    def createObject(self): ...
    def finish(self, cont: bool = ...): ...

class ViewProviderDraftText(draftviewproviders.view_draft_annotation.ViewProviderDraftAnnotation):
    def set_text_properties(self, vobj, properties):
        """Set text properties only if they don't already exist."""
    def getIcon(self):
        """Return the path to the icon used by the view provider."""
    def attach(self, vobj):
        """Set up the scene sub-graph of the view provider."""
    def updateData(self, obj, prop):
        """Execute when a property from the Proxy class is changed."""
    def onChanged(self, vobj, prop):
        """Execute when a view property is changed."""
    def edit(self): ...
    def createObject(self): ...
    def finish(self, cont: bool = ...): ...
