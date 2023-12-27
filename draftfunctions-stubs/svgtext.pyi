import FreeCAD as App
import draftutils.utils as utils

def _get_text_techdraw(text, tcolor, fontsize, anchor, align, fontname, angle, base, linespacing):
    """Return the SVG representation of text for TechDraw display.

        `text` is a list of textual elements; they are iterated, styled,
        and added around a `<text>` tag.
        ::
            <text ...> text[0] </text>
            <text ...> text[1] </text>
    """
def _get_text_header(tcolor, fontsize, anchor, align, fontname, angle, base, flip):
    """Return the initial <text> tag with style options.

        The text must be added after this tag, and then must be closed.
        ::
            <text ...>
            ...
            </text>
    """
def get_text(plane, techdraw, tcolor, fontsize, fontname, angle, base, text, linespacing: float = ..., align: str = ..., flip: bool = ...):
    """Get the SVG representation of a textual element."""
def getText(plane, techdraw, tcolor, fontsize, fontname, angle, base, text, linespacing: float = ..., align: str = ..., flip: bool = ...):
    """Get the SVG representation of a textual element. DEPRECATED."""
