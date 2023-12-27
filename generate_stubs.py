import inspect
import os
import sys
from pathlib import Path
from typing import List

import FreeCAD
import FreeCADGui
import Part
import PartDesign
from mypy import stubgen
from mypy.stubgen import Options


def generate_freecad_modules() -> List[str]:
    result = []
    for module_name, module in sys.modules.items():
        path = ''
        try:
            path = inspect.getfile(module)
        except TypeError:
            path = 'python'
        except (NameError, AttributeError):
            pass
        if 'python' in path:
            continue
        
        conda_prefix = os.environ['CONDA_PREFIX']
        # Needed to filter out signature_bootstrap.py
        if path.startswith(conda_prefix):
            result.append(module_name)
    return result


def create_options(output_path: Path) -> Options:    
    return Options(
        pyversion=sys.version_info[:2],
        no_import=False,
        inspect=True,
        doc_dir="",
        search_path=[],
        interpreter="",
        ignore_errors=True,
        parse_only=False,
        include_private=True,
        output_dir=str(output_path),
        modules=generate_freecad_modules(),
        packages=[],
        files=[],
        verbose=False,
        quiet=True,
        export_less=False,
        include_docstrings=True
    )


def main() -> None:
    FreeCAD.newDocument()
    FreeCADGui.showMainWindow()  # Generate better stubs when Gui is up

    output_path = Path(__file__).resolve().parent
    output_path.mkdir(exist_ok=True)    
    options = create_options(output_path)
    stubgen.generate_stubs(options)

    for child in output_path.iterdir():
        if child.is_file() and child.suffix == '.pyi':
            package = output_path.joinpath(child.stem + '-stubs')
            package.mkdir(exist_ok=True)
            child.rename(package.joinpath('__init__.pyi'))
        elif child.is_dir() and not child.name.startswith('.'):
            child.rename(child.name + '-stubs')

if __name__ == "__main__":
    main()
