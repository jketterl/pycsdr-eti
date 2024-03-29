#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from setuptools import setup, Extension
from distutils.sysconfig import get_python_inc
from sys import version_info
from os import path


version = "0.1.0-dev"

# some distributions seem to have messed with the install locations of header files, so we need to improvise here...
additional_includes = [
    x for x in [
        get_python_inc(plat_specific=True),
        get_python_inc(prefix="/usr/local"),
        "/usr/local/include/python{major}.{minor}".format(major=version_info.major, minor=version_info.minor),
    ] if path.isdir(x)
]

setup(
    name="csdreti",
    version=version,
    packages=["csdreti"],

    package_data={
        "csdreti": ["**.pyi", "**.py"],
    },

    headers=[
    ],

    ext_modules=[
        Extension(
            name="csdreti.modules",
            sources=[
                "src/modules.cpp",
                "src/types.cpp",
                "src/etidecoder.cpp",
                "src/pickleserializer.cpp",
            ],
            language="c++",
            extra_compile_args=["-std=c++17"],
            include_dirs=["src"] + additional_includes,
            libraries=["csdr-eti", "fftw3"],
            define_macros=[("VERSION", '"{}"'.format(version))],
        )
    ],

    install_requires=["pycsdr"],
)
