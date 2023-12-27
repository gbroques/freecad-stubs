import FreeCAD as FreeCAD

def make_hatch(baseobject, filename, pattern, scale, rotation):
    """make_hatch(baseobject, filename, pattern, scale, rotation): Creates and returns a
        hatch object made by applying the given pattern of the given PAT file to the faces of
        the given base object. Given scale and rotation factors are applied to the hatch object.
        The result is a Part-based object created in the active document."""
