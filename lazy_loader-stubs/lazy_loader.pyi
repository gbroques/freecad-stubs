from _typeshed import Incomplete

class LazyLoader(module):
    def __init__(self, local_name, parent_module_globals, name, warning: Incomplete | None = ...) -> None: ...
    def _load(self):
        """Load the module and insert it into the parent's globals."""
    def __getattr__(self, item): ...
    def __dir__(self): ...
