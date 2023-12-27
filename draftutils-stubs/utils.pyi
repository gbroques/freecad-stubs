import Draft_rc as Draft_rc
import FreeCAD as App
import FreeCADGui as Gui
import PySide.QtCore as QtCore
from _typeshed import Incomplete
from draftutils.messages import _err as _err, _log as _log, _msg as _msg, _wrn as _wrn
from draftutils.translate import translate as translate

ARROW_TYPES: list
arrowtypes: list
param_draft: ParameterGrp
param_view: ParameterGrp
ANNOTATION_STYLE: dict
def string_encode_coin(ustr):
    """Encode a unicode object to be used as a string in coin.

        Parameters
        ----------
        ustr : str
            A string to be encoded

        Returns
        -------
        str
            Encoded string. If the coin version is >= 4
            it will encode the string to `'utf-8'`, otherwise
            it will encode it to `'latin-1'`.
    """
def stringencodecoin(ustr):
    """Encode a unicode object to be used as a string in coin.

        Parameters
        ----------
        ustr : str
            A string to be encoded

        Returns
        -------
        str
            Encoded string. If the coin version is >= 4
            it will encode the string to `'utf-8'`, otherwise
            it will encode it to `'latin-1'`.
    """
def type_check(args_and_types, name: str = ...):
    """Check that the arguments are instances of certain types.

        Parameters
        ----------
        args_and_types : list
            A list of tuples. The first element of a tuple is tested as being
            an instance of the second element.
            ::
                args_and_types = [(a, Type), (b, Type2), ...]

            Then
            ::
                isinstance(a, Type)
                isinstance(b, Type2)

            A `Type` can also be a tuple of many types, in which case
            the check is done for any of them.
            ::
                args_and_types = [(a, (Type3, int, float)), ...]

                isinstance(a, (Type3, int, float))

        name : str, optional
            Defaults to `'?'`. The name of the check.

        Raises
        ------
        TypeError
            If the first element in the tuple is not an instance of the second
            element, it raises `Draft.name`.
    """
def typecheck(args_and_types, name: str = ...):
    """Check that the arguments are instances of certain types.

        Parameters
        ----------
        args_and_types : list
            A list of tuples. The first element of a tuple is tested as being
            an instance of the second element.
            ::
                args_and_types = [(a, Type), (b, Type2), ...]

            Then
            ::
                isinstance(a, Type)
                isinstance(b, Type2)

            A `Type` can also be a tuple of many types, in which case
            the check is done for any of them.
            ::
                args_and_types = [(a, (Type3, int, float)), ...]

                isinstance(a, (Type3, int, float))

        name : str, optional
            Defaults to `'?'`. The name of the check.

        Raises
        ------
        TypeError
            If the first element in the tuple is not an instance of the second
            element, it raises `Draft.name`.
    """
def get_param_type(param):
    """Return the type of the parameter entered.

        Parameters
        ----------
        param : str
            A string that indicates a parameter in the parameter database.

        Returns
        -------
        str or None
            The returned string could be `'int'`, `'string'`, `'float'`,
            `'bool'`, `'unsigned'`, depending on the parameter.
            It returns `None` for unhandled situations.
    """
def getParamType(param):
    """Return the type of the parameter entered.

        Parameters
        ----------
        param : str
            A string that indicates a parameter in the parameter database.

        Returns
        -------
        str or None
            The returned string could be `'int'`, `'string'`, `'float'`,
            `'bool'`, `'unsigned'`, depending on the parameter.
            It returns `None` for unhandled situations.
    """
def get_param(param, default: Incomplete | None = ...):
    """Return a parameter value from the current parameter database.

        The parameter database is located in the tree
        ::
            'User parameter:BaseApp/Preferences/Mod/Draft'

        In the case that `param` is `'linewidth'` or `'color'` it will get
        the values from the View parameters
        ::
            'User parameter:BaseApp/Preferences/View/DefaultShapeLineWidth'
            'User parameter:BaseApp/Preferences/View/DefaultShapeLineColor'

        Parameters
        ----------
        param : str
            A string that indicates a parameter in the parameter database.

        default : optional
            It indicates the default value of the given parameter.
            It defaults to `None`, in which case it will use a specific
            value depending on the type of parameter determined
            with `get_param_type`.

        Returns
        -------
        int, or str, or float, or bool
            Depending on `param` and its type, by returning `ParameterGrp.GetInt`,
            `ParameterGrp.GetString`, `ParameterGrp.GetFloat`,
            `ParameterGrp.GetBool`, or `ParameterGrp.GetUnsinged`.
    """
def getParam(param, default: Incomplete | None = ...):
    """Return a parameter value from the current parameter database.

        The parameter database is located in the tree
        ::
            'User parameter:BaseApp/Preferences/Mod/Draft'

        In the case that `param` is `'linewidth'` or `'color'` it will get
        the values from the View parameters
        ::
            'User parameter:BaseApp/Preferences/View/DefaultShapeLineWidth'
            'User parameter:BaseApp/Preferences/View/DefaultShapeLineColor'

        Parameters
        ----------
        param : str
            A string that indicates a parameter in the parameter database.

        default : optional
            It indicates the default value of the given parameter.
            It defaults to `None`, in which case it will use a specific
            value depending on the type of parameter determined
            with `get_param_type`.

        Returns
        -------
        int, or str, or float, or bool
            Depending on `param` and its type, by returning `ParameterGrp.GetInt`,
            `ParameterGrp.GetString`, `ParameterGrp.GetFloat`,
            `ParameterGrp.GetBool`, or `ParameterGrp.GetUnsinged`.
    """
def set_param(param, value):
    """Set a Draft parameter with the given value.

        The parameter database is located in the tree
        ::
            'User parameter:BaseApp/Preferences/Mod/Draft'

        In the case that `param` is `'linewidth'` or `'color'` it will set
        the View parameters
        ::
            'User parameter:BaseApp/Preferences/View/DefaultShapeLineWidth'
            'User parameter:BaseApp/Preferences/View/DefaultShapeLineColor'

        Parameters
        ----------
        param : str
            A string that indicates a parameter in the parameter database.

        value : int, or str, or float, or bool
            The appropriate value of the parameter.
            Depending on `param` and its type, determined with `get_param_type`,
            it sets the appropriate value by calling `ParameterGrp.SetInt`,
            `ParameterGrp.SetString`, `ParameterGrp.SetFloat`,
            `ParameterGrp.SetBool`, or `ParameterGrp.SetUnsinged`.
    """
def setParam(param, value):
    """Set a Draft parameter with the given value.

        The parameter database is located in the tree
        ::
            'User parameter:BaseApp/Preferences/Mod/Draft'

        In the case that `param` is `'linewidth'` or `'color'` it will set
        the View parameters
        ::
            'User parameter:BaseApp/Preferences/View/DefaultShapeLineWidth'
            'User parameter:BaseApp/Preferences/View/DefaultShapeLineColor'

        Parameters
        ----------
        param : str
            A string that indicates a parameter in the parameter database.

        value : int, or str, or float, or bool
            The appropriate value of the parameter.
            Depending on `param` and its type, determined with `get_param_type`,
            it sets the appropriate value by calling `ParameterGrp.SetInt`,
            `ParameterGrp.SetString`, `ParameterGrp.SetFloat`,
            `ParameterGrp.SetBool`, or `ParameterGrp.SetUnsinged`.
    """
def precision():
    '''Return the precision value from the parameter database.

        It is the number of decimal places that a float will have.
        Example
        ::
            precision=6, 0.123456
            precision=5, 0.12345
            precision=4, 0.1234

        Due to floating point operations there may be rounding errors.
        Therefore, this precision number is used to round up values
        so that all operations are consistent.
        By default the precision is 6 decimal places.

        Returns
        -------
        int
            get_param("precision", 6)
    '''
def tolerance():
    '''Return the tolerance value from the parameter database.

        This specifies a tolerance around a quantity.
        ::
            value + tolerance
            value - tolerance

        By default the tolerance is 0.05.

        Returns
        -------
        float
            get_param("tolerance", 0.05)
    '''
def epsilon():
    """Return a small number based on the tolerance for use in comparisons.

        The epsilon value is used in floating point comparisons. Use with caution.
        ::
            denom = 10**tolerance
            num = 1
            epsilon = num/denom

        Returns
        -------
        float
            1/(10**tolerance)
    """
def get_real_name(name):
    """Strip the trailing numbers from a string to get only the letters.

        Parameters
        ----------
        name : str
            A string that may have a number at the end, `Line001`.

        Returns
        -------
        str
            A string without the numbers at the end, `Line`.
            The returned string cannot be empty; it will have
            at least one letter.
    """
def getRealName(name):
    """Strip the trailing numbers from a string to get only the letters.

        Parameters
        ----------
        name : str
            A string that may have a number at the end, `Line001`.

        Returns
        -------
        str
            A string without the numbers at the end, `Line`.
            The returned string cannot be empty; it will have
            at least one letter.
    """
def get_type(obj):
    """Return a string indicating the type of the given object.

        Parameters
        ----------
        obj : App::DocumentObject
            Any type of scripted object created with Draft,
            or any other workbench.

        Returns
        -------
        str
            If `obj` has a `Proxy`, it will return the value of `obj.Proxy.Type`.

            * If `obj` is a `Part.Shape`, returns `'Shape'`

            * If `obj` has a `TypeId`, returns `obj.TypeId`

            In other cases, it will return `'Unknown'`,
            or `None` if `obj` is `None`.
    """
def getType(obj):
    """Return a string indicating the type of the given object.

        Parameters
        ----------
        obj : App::DocumentObject
            Any type of scripted object created with Draft,
            or any other workbench.

        Returns
        -------
        str
            If `obj` has a `Proxy`, it will return the value of `obj.Proxy.Type`.

            * If `obj` is a `Part.Shape`, returns `'Shape'`

            * If `obj` has a `TypeId`, returns `obj.TypeId`

            In other cases, it will return `'Unknown'`,
            or `None` if `obj` is `None`.
    """
def get_objects_of_type(objects, typ):
    """Return only the objects that match the type in the list of objects.

        Parameters
        ----------
        objects : list of App::DocumentObject
            A list of objects which will be tested.

        typ : str
            A string that indicates a type. This should be one of the types
            that can be returned by `get_type`.

        Returns
        -------
        list of objects
            Only the objects that match `typ` will be added to the output list.
    """
def getObjectsOfType(objects, typ):
    """Return only the objects that match the type in the list of objects.

        Parameters
        ----------
        objects : list of App::DocumentObject
            A list of objects which will be tested.

        typ : str
            A string that indicates a type. This should be one of the types
            that can be returned by `get_type`.

        Returns
        -------
        list of objects
            Only the objects that match `typ` will be added to the output list.
    """
def is_clone(obj, objtype: Incomplete | None = ..., recursive: bool = ...):
    """Return True if the given object is a clone of a certain type.

        A clone is of type `'Clone'`, and has a reference
        to the original object inside its `Objects` attribute,
        which is an `'App::PropertyLinkListGlobal'`.

        The `Objects` attribute can point to another `'Clone'` object.
        If `recursive` is `True`, the function will be called recursively
        to further test this clone, until the type of the original object
        can be compared to `objtype`.

        Parameters
        ----------
        obj : App::DocumentObject
            The clone object that will be tested for a certain type.

        objtype : str or list of str
            A type string such as one obtained from `get_type`.
            Or a list of such types.

        recursive : bool, optional
            It defaults to `False`.
            If it is `True`, this same function will be called recursively
            with `obj.Object[0]` as input.

            This option only works if `obj.Object[0]` is of type `'Clone'`,
            that is, if `obj` is a clone of a clone.

        Returns
        -------
        bool
            Returns `True` if `obj` is of type `'Clone'`,
            and `obj.Object[0]` is of type `objtype`.

            If `objtype` is a list, then `obj.Objects[0]`
            will be tested against each of the elements in the list,
            and it will return `True` if at least one element matches the type.

            If `obj` isn't of type `'Clone'` but has the `CloneOf` attribute,
            it will also return `True`.

            It returns `False` otherwise, for example,
            if `obj` is not even a clone.
    """
def isClone(obj, objtype: Incomplete | None = ..., recursive: bool = ...):
    """Return True if the given object is a clone of a certain type.

        A clone is of type `'Clone'`, and has a reference
        to the original object inside its `Objects` attribute,
        which is an `'App::PropertyLinkListGlobal'`.

        The `Objects` attribute can point to another `'Clone'` object.
        If `recursive` is `True`, the function will be called recursively
        to further test this clone, until the type of the original object
        can be compared to `objtype`.

        Parameters
        ----------
        obj : App::DocumentObject
            The clone object that will be tested for a certain type.

        objtype : str or list of str
            A type string such as one obtained from `get_type`.
            Or a list of such types.

        recursive : bool, optional
            It defaults to `False`.
            If it is `True`, this same function will be called recursively
            with `obj.Object[0]` as input.

            This option only works if `obj.Object[0]` is of type `'Clone'`,
            that is, if `obj` is a clone of a clone.

        Returns
        -------
        bool
            Returns `True` if `obj` is of type `'Clone'`,
            and `obj.Object[0]` is of type `objtype`.

            If `objtype` is a list, then `obj.Objects[0]`
            will be tested against each of the elements in the list,
            and it will return `True` if at least one element matches the type.

            If `obj` isn't of type `'Clone'` but has the `CloneOf` attribute,
            it will also return `True`.

            It returns `False` otherwise, for example,
            if `obj` is not even a clone.
    """
def get_clone_base(obj, strict: bool = ..., recursive: bool = ...):
    """Return the object cloned by this object, if any.

        Parameters
        ----------
        obj: App::DocumentObject
            Any type of object.

        strict: bool, optional
            It defaults to `False`.
            If it is `True`, and this object is not a clone,
            this function will return `False`.

        recursive: bool, optional
            It defaults to `True`
            If it is `True`, it call recursively to itself to
            get base object and if it is `False` then it just
            return base object, not call recursively to find
            base object.

        Returns
        -------
        App::DocumentObject
            It `obj` is a `Draft Clone`, it will return the first object
            that is in its `Objects` property.

            If `obj` has a `CloneOf` property, it will search iteratively
            inside the object pointed to by this property.

        obj
            If `obj` is not a `Draft Clone`, nor it has a `CloneOf` property,
            it will return the same `obj`, as long as `strict` is `False`.

        False
            It will return `False` if `obj` is not a clone,
            and `strict` is `True`.
    """
def getCloneBase(obj, strict: bool = ..., recursive: bool = ...):
    """Return the object cloned by this object, if any.

        Parameters
        ----------
        obj: App::DocumentObject
            Any type of object.

        strict: bool, optional
            It defaults to `False`.
            If it is `True`, and this object is not a clone,
            this function will return `False`.

        recursive: bool, optional
            It defaults to `True`
            If it is `True`, it call recursively to itself to
            get base object and if it is `False` then it just
            return base object, not call recursively to find
            base object.

        Returns
        -------
        App::DocumentObject
            It `obj` is a `Draft Clone`, it will return the first object
            that is in its `Objects` property.

            If `obj` has a `CloneOf` property, it will search iteratively
            inside the object pointed to by this property.

        obj
            If `obj` is not a `Draft Clone`, nor it has a `CloneOf` property,
            it will return the same `obj`, as long as `strict` is `False`.

        False
            It will return `False` if `obj` is not a clone,
            and `strict` is `True`.
    """
def shapify(obj):
    """Transform a parametric object into a static, non-parametric shape.

        Parameters
        ----------
        obj : App::DocumentObject
            Any type of scripted object.

            This object will be removed, and a non-parametric object
            with the same topological shape (`Part::TopoShape`)
            will be created.

        Returns
        -------
        Part::Feature
            The new object that takes `obj.Shape` as its own.

            Depending on the contents of the Shape, the resulting object
            will be named `'Face'`, `'Solid'`, `'Compound'`,
            `'Shell'`, `'Wire'`, `'Line'`, `'Circle'`,
            or the name returned by `get_real_name(obj.Name)`.

            If there is a problem with `obj.Shape`, it will return `None`,
            and the original object will not be modified.
    """
def print_shape(shape):
    """Print detailed information of a topological shape.

        Parameters
        ----------
        shape : Part::TopoShape
            Any topological shape in an object, usually obtained from `obj.Shape`.
    """
def printShape(shape):
    """Print detailed information of a topological shape.

        Parameters
        ----------
        shape : Part::TopoShape
            Any topological shape in an object, usually obtained from `obj.Shape`.
    """
def compare_objects(obj1, obj2):
    """Print the differences between 2 objects.

        The two objects are compared through their `TypeId` attribute,
        or by using the `get_type` function.

        If they are the same type their properties are compared
        looking for differences.

        Neither `Shape` nor `Label` attributes are compared.

        Parameters
        ----------
        obj1 : App::DocumentObject
            Any type of scripted object.
        obj2 : App::DocumentObject
            Any type of scripted object.
    """
def compareObjects(obj1, obj2):
    """Print the differences between 2 objects.

        The two objects are compared through their `TypeId` attribute,
        or by using the `get_type` function.

        If they are the same type their properties are compared
        looking for differences.

        Neither `Shape` nor `Label` attributes are compared.

        Parameters
        ----------
        obj1 : App::DocumentObject
            Any type of scripted object.
        obj2 : App::DocumentObject
            Any type of scripted object.
    """
def load_svg_patterns():
    """Load the default Draft SVG patterns and user defined patterns.

        The SVG patterns are added as a dictionary to the `App.svgpatterns`
        attribute.
    """
def loadSvgPatterns():
    """Load the default Draft SVG patterns and user defined patterns.

        The SVG patterns are added as a dictionary to the `App.svgpatterns`
        attribute.
    """
def svg_patterns():
    """Return a dictionary with installed SVG patterns.

        Returns
        -------
        dict
            Returns `App.svgpatterns` if it exists.
            Otherwise it calls `load_svg_patterns` to create it
            before returning it.
    """
def svgpatterns():
    """Return a dictionary with installed SVG patterns.

        Returns
        -------
        dict
            Returns `App.svgpatterns` if it exists.
            Otherwise it calls `load_svg_patterns` to create it
            before returning it.
    """
def get_rgb(color, testbw: bool = ...):
    """Return an RRGGBB value #000000 from a FreeCAD color.

        Parameters
        ----------
        color : list or tuple with RGB values
            The values must be in the 0.0-1.0 range.
        testwb : bool (default = True)
            Pure white will be converted into pure black.
    """
def getrgb(color, testbw: bool = ...):
    """Return an RRGGBB value #000000 from a FreeCAD color.

        Parameters
        ----------
        color : list or tuple with RGB values
            The values must be in the 0.0-1.0 range.
        testwb : bool (default = True)
            Pure white will be converted into pure black.
    """
def argb_to_rgba(color):
    '''Change byte order of a 4 byte color int from ARGB (Qt) to RGBA (FreeCAD).

        Alpha in both integers is always 255.
        Alpha in color properties, although ignored, is always zero however.

        Usage:

            qt_int = self.form.ShapeColor.property("color").rgba() # Note: returns ARGB int
            qt_int = self.form.ShapeColor.property("color").rgb()  # Note: returns ARGB int
            fc_int = argb_to_rgba(qt_int)

            FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View")            .SetUnsigned("DefaultShapeColor", fc_int)

            obj.ViewObject.ShapeColor = fc_int & 0xFFFFFF00

        Related:

            getRgbF() returns an RGBA tuple. 4 floats in the range 0.0 - 1.0. Alpha is always 1.
            Alpha should be set to zero or removed before using the tuple to change a color property:

            obj.ViewObject.ShapeColor = self.form.ShapeColor.property("color").getRgbF()[:3]
    '''
def rgba_to_argb(color):
    """Change byte order of a 4 byte color int from RGBA (FreeCAD) to ARGB (Qt).
    """
def filter_objects_for_modifiers(objects, isCopied: bool = ...): ...
def filterObjectsForModifiers(objects, isCopied: bool = ...): ...
def is_closed_edge(edge_index, object): ...
def isClosedEdge(edge_index, object): ...
def utf8_decode(text):
    '''Decode the input string and return a unicode string.

        Python 2:
        ::
            str -> unicode
            unicode -> unicode

        Python 3:
        ::
            str -> str
            bytes -> str

        It runs
        ::
            try:
                return text.decode("utf-8")
            except AttributeError:
                return text

        Parameters
        ----------
        text : str, unicode or bytes
            A str, unicode, or bytes object that may have unicode characters
            like accented characters.

            In Python 2, a `bytes` object can include accented characters,
            but in Python 3 it must only contain ASCII literal characters.

        Returns
        -------
        unicode or str
            In Python 2 it will try decoding the `bytes` string
            and return a `\'utf-8\'` decoded string.

            >>> "Aá".decode("utf-8")
            >>> b"Aá".decode("utf-8")
            u\'A\\xe1\'

            In Python 2 the unicode string is prefixed with `u`,
            and unicode characters are replaced by their two-digit hexadecimal
            representation, or four digit unicode escape.

            >>> "AáBẃCñ".decode("utf-8")
            u\'A\\xe1B\\u1e83C\\xf1\'

            In Python 2 it will always return a `unicode` object.

            In Python 3 a regular string is already unicode encoded,
            so strings have no `decode` method. In this case, `text`
            will be returned as is.

            In Python 3, if `text` is a `bytes` object, then it will be converted
            to `str`; in this case, the `bytes` object cannot have accents,
            it must only contain ASCII literal characters.

            >>> b"ABC".decode("utf-8")
            \'ABC\'

            In Python 3 it will always return a `str` object, with no prefix.
    '''
def print_header(name, description, debug: bool = ...):
    """Print a line to the console when something is called, and log it.

        Parameters
        ----------
        name: str
            The name of the function or class that is being called.
            This `name` will be logged in the log file, so if there are problems
            the log file can be investigated for clues.

        description: str
            Arbitrary text that will be printed to the console
            when the function or class is called.

        debug: bool, optional
            It defaults to `True`.
            If it is `False` the `description` will not be printed
            to the console.
            On the other hand the `name` will always be logged.
    """
def find_doc(doc: Incomplete | None = ...):
    """Return the active document or find a document by name.

        Parameters
        ----------
        doc: App::Document or str, optional
            The document that will be searched in the session.
            It defaults to `None`, in which case it tries to find
            the active document.
            If `doc` is a string, it will try to get the document by `Name`.

        Returns
        -------
        bool, App::Document
            A tuple containing the information on whether the search
            was successful. In this case, the boolean is `True`,
            and the second value is the document instance.

        False, None
            If there is no active document, or the string in `doc`
            doesn't correspond to an open document in the session.
    """
def find_object(obj, doc: Incomplete | None = ...):
    """Find object in the document, inclusive by Label.

        Parameters
        ----------
        obj: App::DocumentObject or str
            The object to search in `doc`.
            Or if the `obj` is a string, it will search the object by `Label`.
            Since Labels are not guaranteed to be unique, it will get the first
            object with that label in the document.

        doc: App::Document or str, optional
            The document in which the object will be searched.
            It defaults to `None`, in which case it tries to search in the
            active document.
            If `doc` is a string, it will search the document by `Name`.

        Returns
        -------
        bool, App::DocumentObject
            A tuple containing the information on whether the search
            was successful. In this case, the boolean is `True`,
            and the second value is the object found.

        False, None
            If the object doesn't exist in the document.
    """
def use_instead(function, version: str = ...):
    """Print a deprecation message and suggest another function.

        This function must be used inside the definition of a function
        that has been considered for deprecation, so we must provide
        an alternative.
        ::
            def old_function():
                use_instead('new_function', 1.0)

            def someFunction():
                use_instead('some_function')

        Parameters
        ----------
        function: str
            The name of the function to use instead of the current one.

        version: float or str, optional
            It defaults to the empty string `''`.
            The version where this command is to be deprecated, if it is known.
            If we don't know when this command will be deprecated
            then we should not give a version.
    """
