#!/bin/sh
# ----------------------------------------------------------------------------------
# Must be executed when a desired conda environment is activated.
#
# By adding the $CONDA_PREFIX/lib directory to $PYTHONPATH, python is able to find
# FreeCAD, FreeCADGui, and other various FreeCAD-related modules during execution.
# ----------------------------------------------------------------------------------
cd $CONDA_PREFIX
mkdir -p ./etc/conda/activate.d
mkdir -p ./etc/conda/deactivate.d

touch ./etc/conda/activate.d/env_vars.sh
touch ./etc/conda/deactivate.d/env_vars.sh

echo '#!/bin/sh' > ./etc/conda/activate.d/env_vars.sh
echo 'export INITIAL_PYTHONPATH=${PYTHONPATH}' >> ./etc/conda/activate.d/env_vars.sh
echo "export PYTHONPATH=$CONDA_PREFIX/lib:\${PYTHONPATH}" >> ./etc/conda/activate.d/env_vars.sh

echo '#!/bin/sh' > ./etc/conda/deactivate.d/env_vars.sh
echo 'export PYTHONPATH=${INITIAL_PYTHONPATH}' >> ./etc/conda/deactivate.d/env_vars.sh
echo 'unset INITIAL_PYTHONPATH' >> ./etc/conda/deactivate.d/env_vars.sh

# https://github.com/conda/conda/issues/7993#issuecomment-459453605
touch ./etc/conda/activate.d/env_vars.fish
touch ./etc/conda/deactivate.d/env_vars.fish

echo '#!/usr/bin/env fish' > ./etc/conda/activate.d/env_vars.fish
echo 'set -gx INITIAL_PYTHONPATH $PYTHONPATH' > ./etc/conda/activate.d/env_vars.fish
echo "set -gx PYTHONPATH $CONDA_PREFIX/lib $PYTHONPATH" >> ./etc/conda/activate.d/env_vars.fish

echo '#!/usr/bin/env fish' > ./etc/conda/deactivate.d/env_vars.fish
echo 'set -gx PYTHONPATH $INITIAL_PYTHONPATH' >> ./etc/conda/deactivate.d/env_vars.fish
echo 'set -e INITIAL_PYTHONPATH' >> ./etc/conda/deactivate.d/env_vars.fish

