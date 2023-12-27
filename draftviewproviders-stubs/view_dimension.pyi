import DraftGeomUtils as DraftGeomUtils
import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import Part as Part
import draftutils.gui_utils as gui_utils
import draftutils.units as units
import draftutils.utils as utils
import draftviewproviders.view_draft_annotation
import lazy_loader.lazy_loader as lz
from draftviewproviders.view_draft_annotation import ViewProviderDraftAnnotation as ViewProviderDraftAnnotation

class ViewProviderDimensionBase(draftviewproviders.view_draft_annotation.ViewProviderDraftAnnotation):
    def set_text_properties(self, vobj, properties):
        """Set text properties only if they don't already exist."""
    def set_units_properties(self, vobj, properties):
        """Set unit properties only if they don't already exist."""
    def set_graphics_properties(self, vobj, properties):
        """Set graphics properties only if they don't already exist."""
    def getDefaultDisplayMode(self):
        """Return the default display mode."""
    def getIcon(self):
        """Return the path to the icon used by the viewprovider."""

class ViewProviderLinearDimension(ViewProviderDimensionBase):
    def attach(self, vobj):
        """Set up the scene sub-graph of the viewprovider."""
    def updateData(self, obj, prop):
        """Execute when a property from the Proxy class is changed.

                It only runs if `Start`, `End`, `Dimline`, or `Direction` changed.
        """
    def onChanged(self, vobj, prop):
        """Execute when a view property is changed."""
    def remove_dim_arrows(self):
        """Remove dimension arrows in the dimension lines.

                Remove the existing nodes.
        """
    def draw_dim_arrows(self, vobj):
        """Draw dimension arrows."""
    def remove_dim_overshoot(self):
        """Remove the dimension overshoot lines."""
    def draw_dim_overshoot(self, vobj):
        """Draw dimension overshoot lines."""
    def remove_ext_overshoot(self):
        """Remove dimension extension overshoot lines."""
    def draw_ext_overshoot(self, vobj):
        """Draw dimension extension overshoot lines."""
    def is_linked_to_circle(self):
        """Return true if the dimension measures a circular edge."""
    def getIcon(self):
        """Return the path to the icon used by the viewprovider."""

class _ViewProviderDimension(ViewProviderDimensionBase):
    def attach(self, vobj):
        """Set up the scene sub-graph of the viewprovider."""
    def updateData(self, obj, prop):
        """Execute when a property from the Proxy class is changed.

                It only runs if `Start`, `End`, `Dimline`, or `Direction` changed.
        """
    def onChanged(self, vobj, prop):
        """Execute when a view property is changed."""
    def remove_dim_arrows(self):
        """Remove dimension arrows in the dimension lines.

                Remove the existing nodes.
        """
    def draw_dim_arrows(self, vobj):
        """Draw dimension arrows."""
    def remove_dim_overshoot(self):
        """Remove the dimension overshoot lines."""
    def draw_dim_overshoot(self, vobj):
        """Draw dimension overshoot lines."""
    def remove_ext_overshoot(self):
        """Remove dimension extension overshoot lines."""
    def draw_ext_overshoot(self, vobj):
        """Draw dimension extension overshoot lines."""
    def is_linked_to_circle(self):
        """Return true if the dimension measures a circular edge."""
    def getIcon(self):
        """Return the path to the icon used by the viewprovider."""

class ViewProviderAngularDimension(ViewProviderDimensionBase):
    def attach(self, vobj):
        """Set up the scene sub-graph of the viewprovider."""
    def updateData(self, obj, prop):
        """Execute when a property from the Proxy class is changed."""
    def onChanged(self, vobj, prop):
        """Execute when a view property is changed."""
    def remove_dim_arrows(self):
        """Remove dimension arrows in the dimension lines.

                Remove the existing nodes.
        """
    def draw_dim_arrows(self, vobj):
        """Draw dimension arrows."""
    def getIcon(self):
        """Return the path to the icon used by the viewprovider."""

class _ViewProviderAngularDimension(ViewProviderDimensionBase):
    def attach(self, vobj):
        """Set up the scene sub-graph of the viewprovider."""
    def updateData(self, obj, prop):
        """Execute when a property from the Proxy class is changed."""
    def onChanged(self, vobj, prop):
        """Execute when a view property is changed."""
    def remove_dim_arrows(self):
        """Remove dimension arrows in the dimension lines.

                Remove the existing nodes.
        """
    def draw_dim_arrows(self, vobj):
        """Draw dimension arrows."""
    def getIcon(self):
        """Return the path to the icon used by the viewprovider."""
