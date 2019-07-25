
ruamel.yaml.clib
================

``ruamel.yaml.clib`` is the C based reader/scanner and emitter for ruamel.yaml

:version:       0.1.0
:updated:       2019-07-25
:documentation: http://yaml.readthedocs.io
:repository:    https://bitbucket.org/ruamel/yaml.clib
:pypi:          https://pypi.org/project/ruamel.yaml.clib/

This package was split of from ruamel.yaml, so that ruamel.yaml can be build as  
a universal wheel. Apart from the C code seldom changing, and taking a long
time to compile for all platforms, this allows installation of the .so
on Linux systems under /usr/lib64/pythonX.Y (without a .pth file or a ruamel 
directory) and the Python code for ruamel.yaml under /usr/lib/pythonX.Y.


.. image:: https://bestpractices.coreinfrastructure.org/projects/1128/badge
   :target: https://bestpractices.coreinfrastructure.org/projects/1128

.. image:: https://bitbucket.org/ruamel/yaml/raw/default/_doc/_static/license.svg
   :target: https://opensource.org/licenses/MIT
 
