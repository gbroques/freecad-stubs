import FreeCAD as App
import FreeCADGui as Gui
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import draftutils.utils as utils

class ViewProviderLayer:
    def __init__(self, vobj) -> None: ...
    def set_properties(self, vobj):
        """Set the properties only if they don't already exist."""
    def set_override_options(self, vobj, properties):
        """Set property options only if they don't already exist."""
    def set_visual_properties(self, vobj, properties):
        """Set visual properties only if they don't already exist."""
    def getIcon(self):
        """Return the path to the icon used by the viewprovider.

                Normally it returns the basic Layer icon, but if `icondata` exists
                it is the modified icon with the line and shape colors of the layer.
        """
    def attach(self, vobj):
        """Set up the scene sub-graph of the viewprovider."""
    def claimChildren(self):
        """Return objects that will be placed under it in the tree view.

                These are the elements of the `Group` property of the Proxy object.
        """
    def getDisplayModes(self, vobj):
        """Return the display modes that this viewprovider supports."""
    def getDefaultDisplayMode(self):
        """Return the default display mode."""
    def setDisplayMode(self, mode):
        """Return the saved display mode."""
    def dumps(self):
        """Return a tuple of objects to save or None."""
    def loads(self, state):
        """Set the internal properties from the restored state."""
    def updateData(self, obj, prop):
        """Execute when a property from the Proxy class is changed."""
    def change_view_properties(self, vobj, prop):
        """Iterate over the contents and change the properties."""
    def onChanged(self, vobj, prop):
        """Execute when a view property is changed."""
    def canDragObject(self, obj):
        """Return True to allow dragging one object from the Layer.

                Also store parent group data for update_groups_after_drag_drop and
                trigger that function.
        """
    def canDragObjects(self):
        """Return True to allow dragging many objects from the Layer."""
    def dragObject(self, vobj, otherobj):
        """Remove the object that was dragged from the layer."""
    def canDropObject(self, obj):
        """Return true to allow dropping one object.

                If the object being dropped is itself a `'Layer'`, return `False`
                to prevent dropping a layer inside a layer, at least for now.

                Also store parent group data for update_groups_after_drag_drop and
                trigger that function.
        """
    def canDropObjects(self):
        """Return true to allow dropping many objects."""
    def dropObject(self, vobj, otherobj):
        """Add object that was dropped into the Layer to the group.

                If the object being dropped is itself a `'Layer'`,
                return immediately to prevent dropping a layer inside a layer,
                at least for now.
        """
    def update_groups_after_drag_drop(self):
        """Workaround function to improve the drag and drop behavior of Layer
                objects.

                The function processes the parent group data stored in the
                old_parent_data dictionary by canDragObject and canDropObject.
        """
    def replaceObject(self, old_obj, new_obj):
        """Return immediately to prevent replacement of children."""
    def setupContextMenu(self, vobj, menu):
        """Set up actions to perform in the context menu."""
    def activate(self):
        """Activate the selected layer, it becomes the Autogroup."""
    def select_contents(self):
        """Select the contents of the layer."""

class ViewProviderLayerContainer:
    def __init__(self, vobj) -> None: ...
    def getIcon(self):
        """Return the path to the icon used by the viewprovider."""
    def attach(self, vobj):
        """Set up the scene sub-graph of the viewprovider."""
    def setupContextMenu(self, vobj, menu):
        """Set up actions to perform in the context menu."""
    def merge_by_name(self):
        """Merge the layers that have the same base label."""
    def add_layer(self):
        """Creates a new layer"""
    def dumps(self):
        """Return a tuple of objects to save or None."""
    def loads(self, state):
        """Set the internal properties from the restored state."""
    def replaceObject(self, old_obj, new_obj):
        """Return immediately to prevent replacement of children."""

class _ViewProviderVisGroup:
    def __init__(self, vobj) -> None: ...
    def set_properties(self, vobj):
        """Set the properties only if they don't already exist."""
    def set_override_options(self, vobj, properties):
        """Set property options only if they don't already exist."""
    def set_visual_properties(self, vobj, properties):
        """Set visual properties only if they don't already exist."""
    def getIcon(self):
        """Return the path to the icon used by the viewprovider.

                Normally it returns the basic Layer icon, but if `icondata` exists
                it is the modified icon with the line and shape colors of the layer.
        """
    def attach(self, vobj):
        """Set up the scene sub-graph of the viewprovider."""
    def claimChildren(self):
        """Return objects that will be placed under it in the tree view.

                These are the elements of the `Group` property of the Proxy object.
        """
    def getDisplayModes(self, vobj):
        """Return the display modes that this viewprovider supports."""
    def getDefaultDisplayMode(self):
        """Return the default display mode."""
    def setDisplayMode(self, mode):
        """Return the saved display mode."""
    def dumps(self):
        """Return a tuple of objects to save or None."""
    def loads(self, state):
        """Set the internal properties from the restored state."""
    def updateData(self, obj, prop):
        """Execute when a property from the Proxy class is changed."""
    def change_view_properties(self, vobj, prop):
        """Iterate over the contents and change the properties."""
    def onChanged(self, vobj, prop):
        """Execute when a view property is changed."""
    def canDragObject(self, obj):
        """Return True to allow dragging one object from the Layer.

                Also store parent group data for update_groups_after_drag_drop and
                trigger that function.
        """
    def canDragObjects(self):
        """Return True to allow dragging many objects from the Layer."""
    def dragObject(self, vobj, otherobj):
        """Remove the object that was dragged from the layer."""
    def canDropObject(self, obj):
        """Return true to allow dropping one object.

                If the object being dropped is itself a `'Layer'`, return `False`
                to prevent dropping a layer inside a layer, at least for now.

                Also store parent group data for update_groups_after_drag_drop and
                trigger that function.
        """
    def canDropObjects(self):
        """Return true to allow dropping many objects."""
    def dropObject(self, vobj, otherobj):
        """Add object that was dropped into the Layer to the group.

                If the object being dropped is itself a `'Layer'`,
                return immediately to prevent dropping a layer inside a layer,
                at least for now.
        """
    def update_groups_after_drag_drop(self):
        """Workaround function to improve the drag and drop behavior of Layer
                objects.

                The function processes the parent group data stored in the
                old_parent_data dictionary by canDragObject and canDropObject.
        """
    def replaceObject(self, old_obj, new_obj):
        """Return immediately to prevent replacement of children."""
    def setupContextMenu(self, vobj, menu):
        """Set up actions to perform in the context menu."""
    def activate(self):
        """Activate the selected layer, it becomes the Autogroup."""
    def select_contents(self):
        """Select the contents of the layer."""
