import FreeCAD as App
import Part as Part
import lazy_loader.lazy_loader as lz

def print_places(places, title: str = ...):
    """Print a vector with a title."""
def get_init_values(path, count: int = ...):
    """Set values needed to create the array."""
def get_n_params(edge, number, step, norm):
    """Get the parameters needed in each iteration."""
def get_twisted_placements(path, count: int = ..., rot_factor: float = ...):
    """Get the placements of the twisted array elements."""
def get_twisted_array_shape(base, path, count: int = ..., rot_factor: float = ...):
    """Get the twisted array shape as a compound."""
def get_twisted_bridge_shape(base, path, count: int = ..., rot_factor: float = ..., width: int = ..., thickness: int = ...):
    """Get the twisted bridge array shape as a compound."""
def create_frames(obj, places):
    """Create the frames from the placements."""
def make_tunnel(path, profiles):
    """Create the tunnel shape."""
def make_walkway(path, width: int = ..., thickness: int = ...):
    """Construct the walkway of the twisted bridge array."""
