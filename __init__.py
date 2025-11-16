# coding: utf-8

from __future__ import print_function, absolute_import, division, unicode_literals

if False:  # MYPY
    from typing import Dict, Any  # NOQA

_package_data = dict(
    full_package_name='ruamel.yaml.clib',
    version_info=(0, 2, 15),
    __version__='0.2.15',
    version_timestamp='2025-09-22 18:47:49',
    author='Anthon van der Neut',
    author_email='a.van.der.neut@ruamel.eu',
    description='C version of reader, parser and emitter for ruamel.yaml derived from libyaml',
    license='MIT',
    entry_points=None,
    nested=True,  # not really nested as this should not have any files under ruamel
    binary_only=True,
    since=2019,
    ext_modules=[
        dict(
            name='_ruamel_yaml',
            src=[
                '_ruamel_yaml.c',
                'api.c',
                'writer.c',
                'dumper.c',
                'loader.c',
                'reader.c',
                'scanner.c',
                'parser.c',
                'emitter.c',
                # '_ruamel_yaml.h',
                # 'config.h',
                # 'yaml_private.h',
                # 'yaml.h',
            ],
            lib=[],
            test="""
            int main(int argc, char* argv[])
            {
              /* prevent warning */
              return 0;
            }
            """,
        ),
    ],
    # NOQA
    # test='#include "ext/yaml.h"\n\nint main(int argc, char* argv[])\n{\nyaml_parser_t parser;\nparser = parser;  /* prevent warning */\nreturn 0;\n}\n',  # NOQA
    classifiers=[
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='yaml 1.2 parser c-library config',
    wheels=dict(
        windows='appveyor',
        linux='libyaml-devel',
        macos='builder@macos',
    ),
    url_doc='https://yaml.dev/doc/{full_package_name}/',
    supported=[(3, 9)],  # minimum
    python_requires='>=3.9',
    tox=dict(
        env='*',
    ),
    manifest='include README.md LICENSE setup.py *.c *.h *.pxd *.pyx',
    # rtfd='yaml',
)  # type: Dict[Any, Any]


version_info = _package_data['version_info']
__version__ = _package_data['__version__']
