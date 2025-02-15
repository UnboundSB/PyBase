from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "pybase_cpp",
        ["pybase_cpp/pybase_module.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++",
    ),
]

setup(
    name="pybase_cpp",
    ext_modules=ext_modules,
)
