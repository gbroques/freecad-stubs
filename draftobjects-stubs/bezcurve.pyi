import FreeCAD as App
import draftobjects.base
import draftutils.utils as utils
from draftobjects.base import DraftObject as DraftObject

class BezCurve(draftobjects.base.DraftObject):
    def __init__(self, obj) -> None: ...
    def execute(self, fp): ...
    def _segpoleslst(self, fp):
        """Split the points into segments."""
    def resetcontinuity(self, fp): ...
    def onChanged(self, fp, prop): ...
    def createGeometry(self, fp): ...
    @classmethod
    def symmetricpoles(cls, knot, p1, p2):
        """Make two poles symmetric respective to the knot."""
    @classmethod
    def tangentpoles(cls, knot, p1, p2, allowsameside: bool = ...):
        """Make two poles have the same tangent at knot."""
    @staticmethod
    def modifysymmetricpole(knot, p1):
        """calculate the coordinates of the opposite pole
                of a symmetric knot"""
    @staticmethod
    def modifytangentpole(knot, p1, oldp2):
        """calculate the coordinates of the opposite pole
                of a tangent knot"""

class _BezCurve(draftobjects.base.DraftObject):
    def __init__(self, obj) -> None: ...
    def execute(self, fp): ...
    def _segpoleslst(self, fp):
        """Split the points into segments."""
    def resetcontinuity(self, fp): ...
    def onChanged(self, fp, prop): ...
    def createGeometry(self, fp): ...
    @classmethod
    def symmetricpoles(cls, knot, p1, p2):
        """Make two poles symmetric respective to the knot."""
    @classmethod
    def tangentpoles(cls, knot, p1, p2, allowsameside: bool = ...):
        """Make two poles have the same tangent at knot."""
    @staticmethod
    def modifysymmetricpole(knot, p1):
        """calculate the coordinates of the opposite pole
                of a symmetric knot"""
    @staticmethod
    def modifytangentpole(knot, p1, oldp2):
        """calculate the coordinates of the opposite pole
                of a tangent knot"""
