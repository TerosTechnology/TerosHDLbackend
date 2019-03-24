# Copyright 2018
#
# Ismael Pérez Rojo (ismaelprojo@gmail.com)
# Carlos Alberto Ruiz Naranjo (carlosruiznaranjo@gmail.com)
#
# This file is part of TerosHDL.
#
# TerosHDL is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TerosHDL is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TerosHDL.  If not, see <https://www.gnu.org/licenses/>.


#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
from argparse import ArgumentParser
import os.path
import hdlRunClass

def main():

  parser = ArgumentParser(description='Automated creation of VUnit run.py')
  parser.add_argument('--outPath', nargs='?', default="./", help='Run.py output path.',required=False)
  parser.add_argument('--src' , nargs='*', help='.vhd sources path.',required=True)
  parser.add_argument('--tb'  , nargs='*', help='.vhd testbenches path.',required=True)
  parser.add_argument('--name', nargs=1, help='IP core name.',required=True)
  parser.add_argument('--filename', nargs='?', default="", help='Run.py file name.',required=False)
  parser.add_argument('--lang', nargs='?', default="vhdl", help='Test language. Default: vhdl',required=False, choices=['vhdl', 'verilog'])
  parser.add_argument('--complex', nargs='?', const=True, default=False, help='Create a complex test.',required=False)
  parser.add_argument('--uvvm', nargs='?', const=True, default=False, help='Add UVVM libraries.',required=False)
  parser.add_argument('--precheck', nargs='?', const=True, default=False, help='Add precheck.',required=False)
  parser.add_argument('--poscheck', nargs='?', const=True, default=False, help='Add poscheck.',required=False)
  parser.add_argument('--xilib', nargs='?', const=True, default=False, help='Add Xilinx libraries.',required=False)
  parser.add_argument('--uvvmGhdlPath', nargs='?', default="", help='UVVM ghdl library path.',required=False)
  parser.add_argument('--uvvmModelsimPath', nargs='?', default="", help='UVVM Modelsim library path.',required=False)
  parser.add_argument('--xilibIseGhdlPath', nargs='?', default="", help='Xilinx ISE GHDL library path.',required=False)
  parser.add_argument('--xilibVivadoGhdlPath', nargs='?', default="", help='Xilinx Vivado GHDL library path.',required=False)
  parser.add_argument('--xilibVivadoModelsimPath', nargs='?', default="", help='Xilinx Vivado Modelsim library path.',required=False)
  parser.add_argument('--coverageReport', nargs='?', default="html", help='Folder to save code coverage report. Default: html',required=False)
  args = parser.parse_args()

  #Variable para la ruta al directorio
  outPath     = args.outPath
  lstFilesPathsrc = args.src
  lstFilesPathtb  = args.tb
  name        = args.name[0]
  filename    = args.filename+'_run.py'
  lang        = args.lang
  complex     = args.complex
  uvvm        = args.uvvm
  precheck    = args.precheck
  poscheck    = args.poscheck
  xilib       = args.xilib
  uvvmGhdlPath            = args.uvvmGhdlPath
  uvvmModelsimPath        = args.uvvmModelsimPath
  xilibIseGhdlPath        = args.xilibIseGhdlPath
  xilibVivadoGhdlPath     = args.xilibVivadoGhdlPath
  xilibVivadoModelsimPath = args.xilibVivadoModelsimPath
  coverageReport          = args.coverageReport

  #Lista vacia para incluir los ficheros
  lstFilesSrc = []
  lstFilesTb  = []

  #Crea una lista de los ficheros que existen en el directorio y los incluye a la lista.
  for i in range(0,len(lstFilesPathsrc)):
      (nombreFichero, extension) = os.path.splitext(lstFilesPathsrc[i])
      fileStr = nombreFichero+extension
      lstFilesSrc.append(fileStr)

  #Crea una lista de los ficheros vhd que existen en el directorio y los incluye a la lista.
  for i in range(0,len(lstFilesPathtb)):
      (nombreFichero, extension) = os.path.splitext(lstFilesPathtb[i])
      fileStr = nombreFichero+extension
      lstFilesTb.append(fileStr)

  runPy = hdlRunClass.RunPy(outPath+"/"+filename ,name,lstFilesSrc,lstFilesTb,complex,outPath,lang,uvvm,precheck,poscheck,xilib,uvvmGhdlPath,uvvmModelsimPath,xilibIseGhdlPath,xilibVivadoGhdlPath,xilibVivadoModelsimPath,coverageReport)
  runPy.generate()

if __name__ == '__main__':
  main()
