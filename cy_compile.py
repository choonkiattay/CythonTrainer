from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("init", ["matrix_operation/__init__.py"]),
    Extension("real_operation", ["realnumber_operation/real_operation.py"]),
    Extension("matrix_operation", ["matrix_operation/matrix_operation.py"]),
    Extension("feeling_lucky", ["feelinglucky_cy.py"]),


    #   ... all your modules that need be compiled ...

]

setup(
    name='CythonTrainer-bin',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)

# import os
# cwd = os.getcwd()
# files = os.listdir(cwd)
# for file in files:
#     if file.endswith(".c"):
#         os.remove(os.path.join(cwd,file))

# Cython required. Conda/Python environment still required.
# To compile, run "python compile.py build_ext --inplace"
