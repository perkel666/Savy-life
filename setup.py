__author__ = 'Perkel'

import cx_Freeze

executables = [cx_Freeze.Executable("main.py", base="Win32GUI")]

buildOptions = dict(include_files=['data/'])
cx_Freeze.setup(
    name = "Savy_life",
    author = "perkel666",
    options = dict(build_exe = buildOptions),
    description = "test building",
    executables = executables
    )