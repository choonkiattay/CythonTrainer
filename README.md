# Cython Trainer
This project is a Cython compilation tutorial

### Requirement
- Numpy
- Cython

```
pip install -r requirements.txt
```

## Steps
#### 1. Cython main file
Duplicate python main file into one copy. In this case,
`feelinglucky.py` copied to `feelinglucky_cy.py`. Turn the typical
Python main syntax into a normal function syntax.

**Typical python main**
```python 
if __name__ == '__main__':
    answer = some_function()
```


**Python normal function**
```python 
def main():
    answer = some_function()
```

#### 2. Prepare a compile script
The compile script is used for gather the classes and functions. Each
useful python file in each python package and main python file need to
be defined in `ext_modules`.

You may feel free to change the name in `setup` suits your project

Belows are the example of definition. Please refer `cy_compile.py` for
details. 

```python
ext_modules = [
    Extension("init", ["matrix_operation/__init__.py"]),
    Extension("real_operation", ["realnumber_operation/real_operation.py"]),
    Extension("matrix_operation", ["matrix_operation/matrix_operation.py"]),
    Extension("feeling_lucky", ["feelinglucky_cy.py"]),
]

setup(
    name='CythonTrainer-bin',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
...
```

#### 3. Start compilation
Use the command below to compile the python project. 

```
python cy_compile.py build_ext --inplace
```

It will generate the `.c`, `.o` and `.so` files of the defined python
file.

For deployment, you are encourage to use `.so` binary files for speed
and intellectual security. Therefore, make a new directory with same
tree level as the original python project. Place each `.so` files into
directories accordingly. 

**Make another python main file to call function on directory root** 
```python
from feelinglucky_cy import main
main()
```

#### 4. Run with Binary files
To run the binary file, just use the command

```
python main_feelinglucking.py --numbers --mode --type
```

#### Acknowledgement
Appreciate my friend Kin Yee Ho for passing Cython knowledge.

#### TODO
Tree Directory of binary run file