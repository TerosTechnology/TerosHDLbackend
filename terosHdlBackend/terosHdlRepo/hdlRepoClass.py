# Copyright 2019 Carlos Alberto Ruiz Naranjo, Ismael Pérez Rojo
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


# -*- coding: utf-8 -*-

import os
import subprocess
import sys
from argparse import ArgumentParser
import os.path
import shutil

PARENT_DIR = os.path.dirname(os.path.dirname(__file__))

class CreateRepo:
  def __init__(self,path,core):
    self.docPath = os.path.join(os.path.dirname(__file__),"resources","doc")
    self.docPathDest = os.path.join(path,"doc")
    self.SrcIPPath = os.path.join(path,"src","ip")
    self.SrcBDPath = os.path.join(path,"src","bd")
    self.SrcPath = os.path.join(os.path.dirname(__file__),"resources")
    self.TbPath = os.path.join(os.path.dirname(__file__),"resources")
    self.imagesPath = os.path.join(path,"doc","images")
    self.YmlPath = os.path.join(os.path.dirname(__file__),"resources")
    self.ConfTabPath = path
    self.ReadmePath = os.path.join(path)
    self.LibPath = os.path.join(os.path.dirname(__file__),"resources","lib")    #Lib folder origin
    self.LibPathDest = os.path.join(os.path.join(path,"lib"))    #Lib folder destination
    self.GitignorePath = os.path.join(os.path.dirname(__file__),"resources")
    self.GitignoreDest = path
    self.YmlFileDest = path
    self.JsonFileDest = path
    self.SrcDest = os.path.join(path,"src")
    self.TbDest = os.path.join(path,"tb")
    self.CopyfilesjsDest = os.path.join(path,".scripts")
    self.CopyfilesPath = os.path.join(os.path.dirname(__file__),"resources",".scripts")
    self.JsonPath = os.path.join(os.path.dirname(__file__),"resources")
    self.JsonFile = "package.json"
    self.scriptFile = "copy-files.js"
    self.SrcFile = "core_top.vhd"
    self.PkgFile = "core_top_pkg.vhd"
    self.core = core
    self.corePath = os.path.join(path)
    self.path = path
    self.TbFile = 'core_top_tb.vhd'
    self.YmlFile = ".gitlab-ci.yml"
    self.GitignoreFile = ".gitignore"
    self.ConfigTabFile = "ConfigTable.md"
    self.ReadmeFile = "README.md"
    self.ReadmeFileInt = "README_integration.md"
    self.ReadmeFileDev = "README_development.md"
    self.MainCoreFile = "main.core"
    self.MainCorePath = path
    self.FiltroFile = "filter.teros"
#########################
  def close(self):
    self.makefile.close()

  def addDoc(self, core):
    if not os.path.exists(self.docPathDest):
      shutil.copytree(self.docPath,self.docPathDest) #(doc folder origin, doc folder destination)
      with open(os.path.join(self.docPathDest,self.ReadmeFileInt), 'r') as file :
        filedata = file.read()
      filedata = filedata.replace('core', self.core)
      with open(os.path.join(self.docPathDest,self.ReadmeFileInt), 'w') as file:
        file.write(filedata)
      with open(os.path.join(self.docPathDest,self.ReadmeFileDev), 'r') as file :
        filedata = file.read()
      filedata = filedata.replace('core', self.core)
      with open(os.path.join(self.docPathDest,self.ReadmeFileDev), 'w') as file:
        file.write(filedata)
    else:
      print ("Doc ya existe. No se sobreescribe la carpeta doc")
    if not os.path.exists(self.imagesPath):
      os.makedirs(self.imagesPath)

  def addSrc(self, core):
    if not os.path.isfile(os.path.join(self.SrcDest,self.SrcFile)):
      os.makedirs(self.SrcDest)
      shutil.copyfile(self.SrcPath+'/'+self.SrcFile,self.SrcDest+'/'+self.SrcFile) #(src folder origin, src folder destination)
      with open(os.path.join(self.SrcDest,self.SrcFile), 'r') as file :
        filedata = file.read()
      filedata = filedata.replace('core', self.core)
      with open(os.path.join(self.SrcDest,self.SrcFile), 'w') as file:
        file.write(filedata)
      os.rename(os.path.join(self.SrcDest,self.SrcFile), os.path.join(self.SrcDest,core+'_top.vhd'))
    else:
      print("El ip core ya existe. No se sobreescribe el archivo VHD")

  def addPkg(self, core):
    if not os.path.isfile(os.path.join(self.SrcDest,self.PkgFile)):
      # os.makedirs(self.SrcDest)
      shutil.copyfile(self.SrcPath+'/'+self.PkgFile,self.SrcDest+'/'+self.PkgFile) #(src folder origin, src folder destination)
      with open(os.path.join(self.SrcDest,self.PkgFile), 'r') as file :
        filedata = file.read()
      filedata = filedata.replace('core', self.core)
      with open(os.path.join(self.SrcDest,self.PkgFile), 'w') as file:
        file.write(filedata)
      os.rename(os.path.join(self.SrcDest,self.PkgFile), os.path.join(self.SrcDest,core+'_top_pkg.vhd'))
    else:
      print("El ip core ya existe. No se sobreescribe el archivo VHD")

  def addTb(self, core):
    if not os.path.isfile(os.path.join(self.TbDest,self.TbFile)):
      os.makedirs(self.TbDest)
      shutil.copyfile(self.TbPath+'/'+self.TbFile,self.TbDest+'/'+self.TbFile) #(src folder origin, src folder destination)
      with open(os.path.join(self.TbDest,self.TbFile), 'r') as file :
        filedata = file.read()
      filedata = filedata.replace('core', self.core)
      with open(os.path.join(self.TbDest,self.TbFile), 'w') as file:
        file.write(filedata)
      os.rename(os.path.join(self.TbDest,self.TbFile), os.path.join(self.TbDest,core+'_top_tb.vhd'))
    else:
      print("El tb del ip core ya existe. No se sobreescribe el archivo de Testbech")

  def addFilter(self, core):
    if not os.path.isfile(os.path.join(self.TbDest,self.FiltroFile)):
      self.makefile = open(self.TbDest +'/'+ self.FiltroFile, 'a')
      cadena  = '/'+core+'_top_tb/'+core+'_top_i/**\n'
      self.makefile.write(cadena)
      self.close()
    else:
      print("El filtro ya existe. No se sobreescribe el archivo de filter.teros")

  def addYml(self,core):
    if not os.path.isfile(os.path.join(self.YmlFileDest,self.YmlFile)):
      shutil.copyfile(self.YmlPath+'/'+self.YmlFile,self.YmlFileDest+'/'+self.YmlFile) #(yml folder origin, yml folder destination)
      with open(os.path.join(self.YmlFileDest,self.YmlFile), 'r') as file :
        filedata = file.read()
      filedata = filedata.replace('core', self.core)
      with open(os.path.join(self.YmlFileDest,self.YmlFile), 'w') as file:
        file.write(filedata)
    else:
      print ("gitlab-ci.yml ya existe. No se sobreescribe el archivo gitlab-ci.yml")

  def addReadme(self, core):
    if not os.path.exists(os.path.join(self.ReadmePath,self.ReadmeFile)):
      cadena  = ' Write repository address for labels \n\n'
      cadena += ' \n\n'
      cadena += '![Teros HDL logo ](doc/logo.png) \n\n'
      cadena += '# '+core+'\n\n'
      cadena += 'A short description of the module '+core+' .\n\n'
      cadena += '- Information for [Integration](./doc/README_integration.md "Integration")\n'
      cadena += '- Information for [Development](./doc/README_development.md "Development")\n\n'
      self.makefile = open(self.ReadmePath +'/'+self.ReadmeFile, 'a')
      self.makefile.write(cadena)
      self.close()

  def addJson(self,core):
    if not os.path.isfile(os.path.join(self.JsonFileDest,self.JsonFile)):
      shutil.copyfile(self.JsonPath+'/'+self.JsonFile,self.JsonFileDest+'/'+self.JsonFile) #(json folder origin, json folder destination)
    else:
      print ("JSON ya existe. No se sobreescribe el archivo JSON")

  def addReadmeTop(self, core):
    if not os.path.isfile(os.path.join(self.path,self.ReadmeFile)):
      cadena  = ' Escribir la dirección del repositorio para las etiquetas y borrar la dirección de ejemplo \n\n'
      cadena += '[![pipeline status](http://xxx.com/gitlab/DEB_PRUEBA/badges/develop/pipeline.svg)](http://xxx.com/gitlab/DEB_PRUEBA/commits/develop) [![coverage report](http://xxx.com/gitlab/DEB_PRUEBA/badges/develop/coverage.svg)](http://xxx.com/gitlab/DEB_PRUEBA/commits/develop)\n\n'
    else:
      cadena  = '\n'
    if not os.path.exists(self.corePath):
      cadena += '# '+core+'\n\n'
      cadena += 'Una línea de descripción del módulo '+core+' .\n\n'
      cadena += 'Readme de [' +core+ '](./'+core+'/README.md )\n'
      cadena += 'Descripción de una línea.\n\n'
    self.makefile = open(self.path +'/'+self.ReadmeFile, 'a')
    self.makefile.write(cadena)
    self.close()

  def addGitignore(self):
    if not os.path.isfile(os.path.join(self.GitignoreDest,self.GitignoreFile)):
      shutil.copyfile(self.GitignorePath+'/'+self.GitignoreFile,self.GitignoreDest+'/'+self.GitignoreFile) #(lib folder origin, lib folder destination)
    else:
      print ("Gitignore ya existe. No se sobreescribe el archivo gitignore")

  def addScript(self):
    if not os.path.exists(self.CopyfilesjsDest):
      shutil.copytree(self.CopyfilesPath,self.CopyfilesjsDest) #(script origin, script destination)
    else:
      print ("Copyfiles ya existe. No se sobreescribe el archivo Copy-files.js")

  def addLib(self):
    if not os.path.exists(os.path.join(self.path,"lib")):
      shutil.copytree(self.LibPath,self.LibPathDest) #(lib folder origin, lib folder destination)
    else:
      print("La capeta lib ya existe. No se sobreescribe la carpeta lib")

  def addMainCore(self, core):
    #if not os.path.exists(os.path.join(self.MainCorePath,self.MainCoreFile)):
    self.makefile = open(self.MainCorePath +'/'+ self.MainCoreFile, 'a')
    cadena  = '['+core+']\n'
    cadena += 'version = 0.0.0\n'
    cadena += 'depend  = \n'
    cadena += '  cdc_utils (>= 1.27-2)\n'
    cadena += '  wb_common (>= 3)\n'
    cadena += 'files   = \n'
    cadena += '  /src/'+core+'/'+core+'_pkg.vhd\n'
    cadena += '  /src/'+core+'/'+core+'_top.vhd\n'
    cadena += 'description = IPCore: '+core+'.\n\n'
    self.makefile.write(cadena)
    self.close()
