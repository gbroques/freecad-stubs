from _typeshed import Incomplete

class DraftObject:
    def __init__(self, obj, tp: str = ...) -> None: ...
    def onDocumentRestored(self, obj): ...
    def dumps(self):
        """Return a tuple of all serializable objects or None.

                When saving the document this object gets stored
                using Python's `json` module.

                Override this method to define the serializable objects to return.

                By default it returns the `Type` attribute.

                Returns
                -------
                str
                    Returns the value of `Type`
        """
    def loads(self, state):
        """Set some internal properties for all restored objects.

                When a document is restored this method is used to set some properties
                for the objects stored with `json`.

                Override this method to define the properties to change for the
                restored serialized objects.

                By default the `Type` was serialized, so `state` holds this value,
                which is re-assigned to the `Type` attribute.
                ::
                    self.Type = state

                Parameters
                ----------
                state : state
                    A serialized object.
        """
    def execute(self, obj):
        """Run this method when the object is created or recomputed.

                Override this method to produce effects when the object
                is newly created, and whenever the document is recomputed.

                By default it does nothing.

                Parameters
                ----------
                obj : the scripted object.
                    This commonly may be of types `Part::Part2DObjectPython`,
                    `Part::FeaturePython`, or `App::FeaturePython`.
        """
    def onChanged(self, obj, prop):
        """Run this method when a property is changed.

                Override this method to handle the behavior
                of the object depending on changes that occur to its properties.

                By default it does nothing.

                Parameters
                ----------
                obj : the scripted object.
                    This commonly may be of types `Part::Part2DObjectPython`,
                    `Part::FeaturePython`, or `App::FeaturePython`.

                prop : str
                    Name of the property that was modified.
        """
    def props_changed_store(self, prop):
        """Store the name of the property that will be changed in the
                self.props_changed list.

                The function should be called at the start of onChanged or onBeforeChange.

                The list is used to detect Placement-only changes. In such cases the
                Shape of an object does not need to be updated. Not updating the Shape
                avoids Uno/Redo issues for the Windows version and is also more efficient.
        """
    def props_changed_clear(self):
        """Remove the self.props_changed attribute if it exists.

                The function should be called just before execute returns.
        """
    def props_changed_placement_only(self, obj: Incomplete | None = ...):
        """Return `True` if the self.props_changed list, after removing `Shape`
                and `_LinkTouched` items, only contains `Placement` items.

                Parameters
                ----------
                obj : the scripted object. Need only be supplied if the Shape of obj
                    is, or can be, derived from other objects.

        """

class _DraftObject:
    def __init__(self, obj, tp: str = ...) -> None: ...
    def onDocumentRestored(self, obj): ...
    def dumps(self):
        """Return a tuple of all serializable objects or None.

                When saving the document this object gets stored
                using Python's `json` module.

                Override this method to define the serializable objects to return.

                By default it returns the `Type` attribute.

                Returns
                -------
                str
                    Returns the value of `Type`
        """
    def loads(self, state):
        """Set some internal properties for all restored objects.

                When a document is restored this method is used to set some properties
                for the objects stored with `json`.

                Override this method to define the properties to change for the
                restored serialized objects.

                By default the `Type` was serialized, so `state` holds this value,
                which is re-assigned to the `Type` attribute.
                ::
                    self.Type = state

                Parameters
                ----------
                state : state
                    A serialized object.
        """
    def execute(self, obj):
        """Run this method when the object is created or recomputed.

                Override this method to produce effects when the object
                is newly created, and whenever the document is recomputed.

                By default it does nothing.

                Parameters
                ----------
                obj : the scripted object.
                    This commonly may be of types `Part::Part2DObjectPython`,
                    `Part::FeaturePython`, or `App::FeaturePython`.
        """
    def onChanged(self, obj, prop):
        """Run this method when a property is changed.

                Override this method to handle the behavior
                of the object depending on changes that occur to its properties.

                By default it does nothing.

                Parameters
                ----------
                obj : the scripted object.
                    This commonly may be of types `Part::Part2DObjectPython`,
                    `Part::FeaturePython`, or `App::FeaturePython`.

                prop : str
                    Name of the property that was modified.
        """
    def props_changed_store(self, prop):
        """Store the name of the property that will be changed in the
                self.props_changed list.

                The function should be called at the start of onChanged or onBeforeChange.

                The list is used to detect Placement-only changes. In such cases the
                Shape of an object does not need to be updated. Not updating the Shape
                avoids Uno/Redo issues for the Windows version and is also more efficient.
        """
    def props_changed_clear(self):
        """Remove the self.props_changed attribute if it exists.

                The function should be called just before execute returns.
        """
    def props_changed_placement_only(self, obj: Incomplete | None = ...):
        """Return `True` if the self.props_changed list, after removing `Shape`
                and `_LinkTouched` items, only contains `Placement` items.

                Parameters
                ----------
                obj : the scripted object. Need only be supplied if the Shape of obj
                    is, or can be, derived from other objects.

        """
