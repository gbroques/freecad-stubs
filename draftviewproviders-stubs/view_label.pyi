import FreeCAD as App
import FreeCADGui as Gui
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
import draftviewproviders.view_draft_annotation
from draftviewproviders.view_draft_annotation import ViewProviderDraftAnnotation as ViewProviderDraftAnnotation

param: ParameterGrp

class ViewProviderLabel(draftviewproviders.view_draft_annotation.ViewProviderDraftAnnotation):
    def set_text_properties(self, vobj, properties):
        """Set text properties only if they don't already exist."""
    def set_graphics_properties(self, vobj, properties):
        """Set graphics properties only if they don't already exist."""
    def getIcon(self):
        """Return the path to the icon used by the viewprovider."""
    def attach(self, vobj):
        """Set up the scene sub-graph of the viewprovider."""
    def updateData(self, obj, prop):
        """Execute when a property from the Proxy class is changed."""
    def onChanged(self, vobj, prop):
        """Execute when a view property is changed."""
    def get_text_size(self, vobj):
        """Return the bounding box of the text element."""
    def update_label(self, obj, vobj):
        """Update the label including text size and multiplier."""
    def update_arrow(self, obj, vobj):
        """Update the arrow tip of the line."""
    def update_frame(self, obj, vobj):
        """Update the frame around the text."""

class ViewProviderDraftLabel(draftviewproviders.view_draft_annotation.ViewProviderDraftAnnotation):
    def set_text_properties(self, vobj, properties):
        """Set text properties only if they don't already exist."""
    def set_graphics_properties(self, vobj, properties):
        """Set graphics properties only if they don't already exist."""
    def getIcon(self):
        """Return the path to the icon used by the viewprovider."""
    def attach(self, vobj):
        """Set up the scene sub-graph of the viewprovider."""
    def updateData(self, obj, prop):
        """Execute when a property from the Proxy class is changed."""
    def onChanged(self, vobj, prop):
        """Execute when a view property is changed."""
    def get_text_size(self, vobj):
        """Return the bounding box of the text element."""
    def update_label(self, obj, vobj):
        """Update the label including text size and multiplier."""
    def update_arrow(self, obj, vobj):
        """Update the arrow tip of the line."""
    def update_frame(self, obj, vobj):
        """Update the frame around the text."""
