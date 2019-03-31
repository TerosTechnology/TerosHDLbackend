
# core: Development

## Introduction

Respository description. Module functions.

## Diagram

![functional core diagram](./images/core.png)

## core module description

Module description

## Module description 1

Module description 1

## Module description 2

Module description 2

### Documentation dependencies

- doxygen: Documentation generation
- texlive-full: LaTeX to pdf.

### Testbenchs dependencies

- VUnit
```
sudo pip install vunit_hdl
```
- GHDL gcc compiled.
- numpy
- lcov: code coverage.
```
sudo apt-get install lcov
```
- gtkwave: visualization.

## Testbench documentation

[README_TB](tb/README_TB.md)

### Documentation generation

```
cd lib/doc_gen/
doxygen Doxyfile
```
The generated documentation is in /doc/html

To generate documentation in .pdf

```
cd doc/gen/latex
make pdf
```

Generated in doc/latex
