<img src="./doc/images/teros_logo.svg" align="right" width=30% height=30%>

# TerosHDLbackend

Tools to accelerate the FPGA development.

## Install from pip

```
pip install TerosHDL
```

## Install from source code

```
git clone
cd /terosHDLbackend
pip install .
```

## Tools

### hdlRepo

Create a repository structure for an HDL module.

```
usage: hdlRepo [-h] --core [CORE [CORE ...]]

create a repository structure for an HDL module.

optional arguments:
  -h, --help            show this help message and exit
  --core [CORE [CORE ...]]
                        Add IP to the repository. Run in git project. Example:
                        --core DDC block_RAM
```

### hdlRun

Automated creation of VUnit run.py

```
usage: terosHdlRunpy [-h] [--outPath [OUTPATH]] --src [SRC [SRC ...]] --tb
                     [TB [TB ...]] --name NAME [--filename [FILENAME]]
                     [--lang [{vhdl,verilog}]] [--complex [COMPLEX]]
                     [--uvvm [UVVM]] [--precheck [PRECHECK]]
                     [--poscheck [POSCHECK]]
                     [--disableIeeeWarnings [DISABLEIEEEWARNINGS]]
                     [--synopsysLibraries [SYNOPSYSLIBRARIES]]
                     [--xilib [XILIB]] [--pslSupport [PSLSUPPORT]]
                     [--uvvmGhdlPath [UVVMGHDLPATH]]
                     [--uvvmModelsimPath [UVVMMODELSIMPATH]]
                     [--xilibIseGhdlPath [XILIBISEGHDLPATH]]
                     [--xilibVivadoGhdlPath [XILIBVIVADOGHDLPATH]]
                     [--xilibVivadoModelsimPath [XILIBVIVADOMODELSIMPATH]]
                     [--coverageReport [COVERAGEREPORT]]

Automated creation of VUnit run.py

optional arguments:
  -h, --help            show this help message and exit
  --outPath [OUTPATH]   Run.py output path.
  --src [SRC [SRC ...]]
                        .vhd sources path.
  --tb [TB [TB ...]]    .vhd testbenches path.
  --name NAME           IP core name.
  --filename [FILENAME]
                        Run.py file name.
  --lang [{vhdl,verilog}]
                        Test language. Default: vhdl
  --complex [COMPLEX]   Create a complex test.
  --uvvm [UVVM]         Add UVVM libraries.
  --precheck [PRECHECK]
                        Add precheck.
  --poscheck [POSCHECK]
                        Add poscheck.
  --disableIeeeWarnings [DISABLEIEEEWARNINGS]
                        Disable IEEE warnings.
  --synopsysLibraries [SYNOPSYSLIBRARIES]
                        Add support for synopsys libraries.
  --xilib [XILIB]       Add Xilinx libraries.
  --pslSupport [PSLSUPPORT]
                        Add support for PSL.
  --uvvmGhdlPath [UVVMGHDLPATH]
                        UVVM ghdl library path.
  --uvvmModelsimPath [UVVMMODELSIMPATH]
                        UVVM Modelsim library path.
  --xilibIseGhdlPath [XILIBISEGHDLPATH]
                        Xilinx ISE GHDL library path.
  --xilibVivadoGhdlPath [XILIBVIVADOGHDLPATH]
                        Xilinx Vivado GHDL library path.
  --xilibVivadoModelsimPath [XILIBVIVADOMODELSIMPATH]
                        Xilinx Vivado Modelsim library path.
  --coverageReport [COVERAGEREPORT]
                        Folder to save code coverage report. Default: html
```

## Upload to pip

```
python setup.py sdist
twine upload dist/dist/TerosHDL.tar.gz
```
