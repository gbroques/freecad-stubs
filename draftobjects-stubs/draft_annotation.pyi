class DraftAnnotation:
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored.

                Check if new properties are present after the object is restored
                in order to migrate older objects.
        """
    def add_missing_properties_0v19(self, obj, vobj):
        """Provide missing annotation properties."""
    def dumps(self): ...
    def loads(self, state): ...
