# Copyright 2018 DAS Photonics
# Carlos Alberto Ruiz Naranjo, Ismael Pérez Rojo
#
# This file is part of ATOMato.
#
# ATOMato is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ATOMato is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ATOMato.  If not, see <https://www.gnu.org/licenses/>.


#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
from argparse import ArgumentParser
import os.path
import git
sys.path.append(os.path.dirname(__file__))
import hdlRepoClass

def main():
  parser = ArgumentParser(description='create a repository structure for an HDL module.')
  parser.add_argument('--core', help='Add IP to the repository. Run in git project. Example: --core DDC block_RAM',required=True, nargs='*')
  #parser.add_argument('--path', help='Escribe el destino del repositorio. Ejemplo: --path ./git/02_EDLP_UTILS',required=False, nargs=1)
  args = parser.parse_args()
  git_repo = git.Repo("./", search_parent_directories=True)
  path = git_repo.git.rev_parse("--show-toplevel")
  #if args.path[0]:
    #git_repo = git.Repo(os.path.dirname(args.path[0]), search_parent_directories=True)
    #path = git_repo.git.rev_parse("--show-toplevel")
  #else:
    #git_repo = git.Repo("./", search_parent_directories=True)
    #path = git_repo.git.rev_parse("--show-toplevel")
  #print(path)

  for i in range(0,len(args.core)):
    createRepo = hdlRepoClass.CreateRepo(path,args.core[i])      #creamos la clase para cada ip core
    #createRepo.addReadmeTop(args.core[i])
    # createRepo.addYml(args.core[i])
    createRepo.addDoc(args.core[i])
    createRepo.addSrc(args.core[i])
    createRepo.addPkg(args.core[0])
    createRepo.addTb(args.core[i])
    createRepo.addReadme(args.core[i])
    #createRepo.addMainCore(args.core[i])
    createRepo.addJson(args.core[i])
    createRepo.addScript()
    # createRepo.addLib()
    createRepo.addFilter(args.core[i])

    createRepo.addGitignore()

if __name__ == '__main__':
  main()
