# Copyright 2019
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


# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import os.path

class RunPy:
  def __init__(self, filename, name, src, tb, complex,outPath,lang,uvvm,precheck,poscheck,disableIeeeWarnings,synopsysLibraries,xilib,pslSupport,uvvmGhdlPath,uvvmModelsimPath,xilibIseGhdlPath,xilibVivadoGhdlPath,xilibVivadoModelsimPath,coverageReport):
    self.name     = name
    self.filename = filename
    self.src      = src
    self.tb       = tb
    self.outPath  = outPath
    self.lang     = lang
    self.complex  = complex
    self.uvvm     = uvvm
    self.precheck = precheck
    self.poscheck = poscheck
    self.disableIeeeWarnings     = disableIeeeWarnings
    self.synopsysLibraries       = synopsysLibraries
    self.xilib                   = xilib
    self.pslSupport              = pslSupport
    self.uvvmGhdlPath            = uvvmGhdlPath
    self.uvvmModelsimPath        = uvvmModelsimPath
    self.xilibIseGhdlPath        = xilibIseGhdlPath
    self.xilibVivadoGhdlPath     = xilibVivadoGhdlPath
    self.xilibVivadoModelsimPath = xilibVivadoModelsimPath
    self.coverageReport          = coverageReport


  def generate(self):
    self.setPath()
    self.setCabecera()
    self.setLibreriasPython()
    self.setLang()
    if self.complex==True:
      self.setLibreriasPythonComplex()
    if self.complex==True or self.precheck==True or self.poscheck==True:
      self.separator()
    if self.complex==True or self.precheck==True:
      self.setPreCheck()
    if self.complex==True or self.poscheck==True:
      self.setPostCheck()
    self.separator()
    # self.setCheckCobertura()
    self.setCheckSimulador()
    self.separator()
    # self.setParameter()
    # self.setCreateVunit()
    if self.complex==True or self.xilib==True:
      self.setVunitArgs()
    self.setVunitInstance()
    if self.complex==True or self.xilib==True:
      self.setLibreriasXilinx()
    if self.complex==True or self.uvvm==True:
      self.setLibreriasUVVM()
    if self.complex==True or self.uvvm==True:
      self.setExternalUVVM()
    self.setSrc()
    self.setTb()
    #self.setExternalXilinx()
    # if self.complex==True or (self.precheck==True or self.poscheck==True):
    if self.complex==True:
      self.setAsociacionChecks()
    elif self.precheck==True and self.poscheck==True:
      self.setAsocPrePosCheck()
    elif self.precheck==True:
      self.setAsocPreCheck()
    elif self.poscheck==True:
      self.setAsocPosCheck()
    self.separator()
    self.setParametrosGHDL()
    self.separator()
    self.checkCobertura()
    self.separator()
    self.run()

  def setPath(self):
    if not os.path.exists(self.outPath):
      os.makedirs(self.outPath)

  def setCabecera(self):
    f = open (self.filename, "w+")
    cadena = "# -*- coding: utf-8 -*-\n"
    f.write(cadena)
    f.close()

  def setLibreriasPython(self):
    f = open (self.filename, "a")
    cadena = "from pathlib import Path\nfrom os.path import join , dirname, abspath\nimport subprocess\nfrom vunit.sim_if.ghdl import GHDLInterface\nfrom vunit.sim_if.factory import SIMULATOR_FACTORY\n"
    for i in range(0,len(self.src)):
        filename, file_extension = os.path.splitext(self.src[i])
        if (file_extension == ".xpr"):
            cadena += "from vunit.vivado.vivado_util import add_vivado_ip\n"
            break

    f.write(cadena)
    f.close()

  def setLibreriasPythonComplex(self):
    f = open (self.filename, "a")
    cadena = "import os\nimport sys\nimport numpy as np\n"
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setLang(self):
    f = open (self.filename, "a")
    if self.lang=="vhdl":
        cadena = "from vunit   import VUnit, VUnitCLI\n"
    if self.lang=="verilog":
        cadena = "from vunit.verilog   import VUnit, VUnitCLI\n"
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setCheckCobertura(self):
    f = open (self.filename, "a")
    cadena =  '#Check GHDL backend.\n'
    cadena += 'code_coverage=False\ntry:\n  if( GHDLInterface.determine_backend("")=="gcc" or  GHDLInterface.determine_backend("")=="GCC"):\n    code_coverage=True\n  else:\n    code_coverage=False\nexcept:\n  print("")\n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setCheckSimulador(self):
    f = open (self.filename, "a")
    cadena ='#Check simulator.\n'
    cadena +='print ("=============================================")\n'
    cadena +='simname = SIMULATOR_FACTORY.select_simulator().name\n'
    cadena +='code_coverage = False\n'
    cadena +='if (simname == "modelsim"):\n'
    cadena +='    f= open("modelsim.do","w+")\n'
    cadena +='    f.write("add wave * \\nlog -r /*\\nvcd file\\nvcd add -r /*\\n")\n'
    cadena +='    f.close()\n'
    cadena +='code_coverage = (simname == "ghdl" and \\\n'
    cadena +='                (GHDLInterface.determine_backend("")=="gcc" or  \\\n'
    cadena +='                    GHDLInterface.determine_backend("")=="GCC"))\n'
    cadena +='print ("Simulator = " + simname)\n'
    cadena +='print ("=============================================")\n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setPreCheck(self):
    f = open (self.filename, "a")
    cadena =  '#pre_config func\n'
    cadena += 'def pre_config_func():\n    """\n    Before test.\n    """'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setPostCheck(self):
    f = open (self.filename, "a")
    cadena =  '#post_check func\n'
    cadena += 'def post_check_func():\n'
    cadena += '    """                            \n'
    cadena += '    After test.                    \n'
    cadena += '    """                            \n'
    cadena += '    def post_check(output_path):   \n'
    cadena += '        check = True                 \n'
    cadena += '        return check                 \n'
    cadena += '    return post_check              \n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setLibreriasUVVM(self):
    f = open (self.filename, "a")
    cadena = '#UVVM libraries path.\n'
    cadena += 'if (simname=="ghdl" or simname=="GHDL"):\n'
    cadena += '    uvvm_util_root    = "'+self.uvvmGhdlPath+'/uvvm_util/v08"\n'
    cadena += '    uvvm_axilite_root = "'+self.uvvmGhdlPath+'/bitvis_vip_axilite/v08"\n'
    cadena += 'elif (simname=="modelsim" or simname=="MODELSIM"):\n'
    cadena += '    uvvm_util_root    = "'+self.uvvmModelsimPath+'/uvvm_util"\n'
    cadena += '    uvvm_axilite_root = "'+self.uvvmModelsimPath+'/bitvis_vip_axilite"\n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setVunitInstance(self):
    f = open (self.filename, "a")
    cadena = '#VUnit instance.\n'
    if self.complex==True:
      cadena += 'ui = VUnit.from_args(args=args)\n'
    else:
      cadena += 'ui = VUnit.from_argv()\n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setVunitArgs(self):
      f = open (self.filename, "a")
      cadena  = '#Add custom command line argument to standard CLI\n'
      cadena += '#Beware of conflicts with existing arguments       \n'
      cadena += 'cli = VUnitCLI()                                   \n'
      cadena += "cli.parser.add_argument('--ide',required=False)    \n"
      cadena += 'args = cli.parse_args()                            \n'
      cadena += 'if (args.ide is None):                             \n'
      cadena += '    print("IDE not selected. Default: Vivado")       \n'
      cadena += '    ide="vivado"        \n'
      cadena += 'else:                                              \n'
      cadena += '    ide=args.ide                                     \n'
      cadena += '\n'
      f.write(cadena)
      f.close()

  def setLibreriasXilinx(self):
    f = open (self.filename, "a")
    cadena  = '#Add Xilinx ISE libraries.                                       \n'
    cadena += 'if(ide=="ise"):                                                             \n'
    cadena += '    print("IDE ISE selected")                                          \n'
    cadena += '    xilinx_libraries_path = "'+self.xilibIseGhdlPath+'"             \n'
    cadena += '    unisim_path   = join(xilinx_libraries_path,"unisim","v08")                \n'
    cadena += '    corelib_path  = join(xilinx_libraries_path,"xilinxcorelib","v08")         \n'
    cadena += '    unimacro_path = join(xilinx_libraries_path,"unimacro","v08")              \n'
    cadena += '    ui.add_external_library("unisim",unisim_path)                             \n'
    cadena += '    ui.add_external_library("xilinxcorelib",corelib_path)                     \n'
    cadena += '    ui.add_external_library("unimacro",unimacro_path)                         \n'
    cadena += '                                                                            \n'
    cadena += '#Xilinx Vivado libraries.                                      \n'
    cadena += 'if(ide=="vivado"):                                                          \n'
    cadena += '    print("IDE Vivado selected")                                          \n'
    cadena += '    if(simname=="modelsim" or simname=="MODELSIM"):\n'
    cadena += '        xilinx_libraries_path="'+self.xilibVivadoModelsimPath+'"\n'
    cadena += '        unisim_path   = join(xilinx_libraries_path,"unisim")\n'
    cadena += '        unifast_path  = join(xilinx_libraries_path,"unifast")\n'
    cadena += '        unimacro_path = join(xilinx_libraries_path,"unimacro")\n'
    cadena += '        secureip_path = join(xilinx_libraries_path,"secureip")\n'
    cadena += '        xpm_path      = join(xilinx_libraries_path,"xpm")\n'
    cadena += '        ui.add_external_library("xpm",xpm_path)                         \n'
    cadena += '    else:\n'
    cadena += '        xilinx_libraries_path = "'+self.xilibVivadoGhdlPath+'"\n'
    cadena += '        unisim_path   = join(xilinx_libraries_path,"unisim","v08")\n'
    cadena += '        unifast_path  = join(xilinx_libraries_path,"unifast","v08")\n'
    cadena += '        unimacro_path = join(xilinx_libraries_path,"unimacro","v08")\n'
    cadena += '        secureip_path = join(xilinx_libraries_path,"secureip","v08")            \n'
    cadena += '    ui.add_external_library("unisim",unisim_path)                             \n'
    cadena += '    ui.add_external_library("unifast",unifast_path)                           \n'
    cadena += '    ui.add_external_library("unimacro",unimacro_path)                         \n'
    cadena += '    ui.add_external_library("secureip",secureip_path)                         \n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setParameter(self):
    f = open(self.filename, "a")
    cadena  = '#Add custom command line argument to standard CLI\n'
    cadena += '#Beware of conflicts with existing arguments       \n'
    cadena += 'cli = VUnitCLI()                                   \n'
    cadena += "cli.parser.add_argument('--ide')                   \n"
    cadena += 'args = cli.parse_args()                            \n'
    cadena += 'if (args.ide is None):                             \n'
    cadena += '    print("Wrong IDE")                               \n'
    cadena += 'else:                                              \n'
    cadena += '    ide=args.ide                                     \n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setCreateVunit(self):
    f = open(self.filename, "a")
    cadena  = '#New VUnit instance.\n'
    cadena += 'ui = VUnit.from_args(args=args)\n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setAddArray(self):
    f = open(self.filename, "a")
    cadena  = '#Add array pkg.\n'
    cadena += 'ui.add_array_util()\n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setSrc(self):
    f = open (self.filename, "a")
    cadena  = '#Add module sources.\n'
    cadena  = 'ROOT = str(Path(__file__).parent.absolute())\n'
    cadena += self.name + '_src_lib = ui.add_library("src_lib")\n'
    for i in range(0,len(self.src)):
        filename, file_extension = os.path.splitext(self.src[i])
        if (file_extension == ".xpr"):
            cadena += 'add_vivado_ip(\n'
            cadena += '    ui,\n'
            cadena += '    output_path = ROOT + "/vivado_libs",\n'
            cadena += '    project_file= "./' + self.src[i] + '"\n'
            cadena += ')\n'
        else:
            cadena += self.name + '_src_lib.add_source_files("' + self.src[i].replace("\\", "\\\\") + '")' + '\n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setTb(self):
    f = open (self.filename, "a")
    cadena  = '#Add tb sources.\n'
    cadena += self.name + '_tb_lib = ui.add_library("tb_lib")\n'
    for i in range(0,len(self.tb)):
      cadena += self.name + '_tb_lib.add_source_files("' + self.tb[i].replace("\\", "\\\\") + '")' + '\n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setExternalUVVM(self):
    f = open (self.filename, "a")
    cadena  = '#Add UVVM libraries.\n'
    cadena += 'ui.add_external_library("uvvm_util",uvvm_util_root)\n'
    cadena += 'ui.add_external_library("bitvis_vip_axilite",uvvm_axilite_root)\n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setExternalXilinx(self):
    f = open (self.filename, "a")
    cadena  = '#Add Xilinx libraries.\n'
    cadena += 'ui.add_external_library("unisim",unisim_path)\n'
    cadena += 'ui.add_external_library("xilinxcorelib",corelib_path)\n'
    cadena += 'ui.add_external_library("unimacro",unimacro_path)\n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setParametrosGHDL(self):
    f = open (self.filename, "a")
    if self.pslSupport==True:
      psl_var=',"-fpsl"'
    else:
      psl_var=' '
    if self.synopsysLibraries==True:
      synopsys_var='"-fexplicit","--ieee=synopsys","--no-vital-checks","-frelaxed-rules",'
      synopsys_var_opt='"-fexplicit","--ieee=synopsys","--no-vital-checks","-frelaxed-rules"'
    else:
      synopsys_var=' '
      synopsys_var_opt='"-fexplicit","--no-vital-checks","-frelaxed-rules"'
    cadena  = '#GHDL parameters.\n'
    cadena += 'if(code_coverage == True):\n'
    cadena += '    ' + self.name + '_src_lib.add_compile_option   ("ghdl.flags"     , [ '+synopsys_var+'"-fprofile-arcs","-ftest-coverage"'+psl_var+'])\n'
    cadena += '    ' + self.name + '_tb_lib.add_compile_option("ghdl.flags"     , [ '+synopsys_var+'"-fprofile-arcs","-ftest-coverage"'+psl_var+'])\n'
    cadena += '    ui.set_sim_option("ghdl.elab_flags"      , ['+synopsys_var+'"-Wl,-lgcov"'+psl_var+'])\n'
    cadena += '    ui.set_sim_option("modelsim.init_files.after_load" ,["modelsim.do"])\n'

    cadena += 'else:\n'
    if self.synopsysLibraries==True or self.pslSupport==True:
      cadena += '    ' + self.name + '_src_lib.add_compile_option   ("ghdl.flags"     , ['+synopsys_var_opt+''+psl_var+'])\n'
      cadena += '    ' + self.name + '_tb_lib.add_compile_option("ghdl.flags"     , ['+synopsys_var_opt+''+psl_var+'])\n'
      cadena += '    ui.set_sim_option("ghdl.elab_flags"      , ["-fexplicit","--no-vital-checks","-frelaxed-rules"])\n'
    cadena += '    ui.set_sim_option("modelsim.init_files.after_load" ,["modelsim.do"])\n\n'

    if self.complex==True:
      cadena += 'ui.set_sim_option("ghdl.sim_flags"        ,["--read-wave-opt=./filter.teros"])\n'
    if self.disableIeeeWarnings==True:
      cadena += 'ui.set_sim_option("disable_ieee_warnings", True)\n'
    if self.pslSupport==True:
      cadena += 'ui.set_sim_option("ghdl.sim_flags", ["--psl-report=./psl_coverage.json"])\n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setAsociacionChecks(self):
    f = open (self.filename, "a")
    cadena  = '#func relations\n'
    cadena += 'tb_generated = '+self.name+'_tb_lib.entity("'+self.tb[0].split(".")[0]+'")\n'
    cadena += 'for test in tb_generated.get_tests():\n'
    cadena += '    print(test.name)\n'

    cadena += 'for test in tb_generated.get_tests():\n'
    cadena += '    if test.name == "'+self.name+'_test":\n'
    cadena += '      num_test = 5 \n'
    cadena += '      for i in range (0,num_test):\n'
    cadena += '        test.add_config(name="'+self.name+'_"+str(i), generics=dict(num_test=i,parameter_generic=parameter),pre_config=pre_config_func(i,parameter),post_check=post_check_func(i))\n'
    cadena += '    else:\n'
    cadena += '      pass\n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setAsocPreCheck(self):
    f = open (self.filename, "a")
    cadena  = '#func precheck\n'
    cadena += 'tb_generated = '+self.name+'_tb_lib.entity("'+self.tb[0].split(".")[0]+'")\n'
    # cadena += 'for test in tb_generated.get_tests():\n'
    # cadena += '  print(test.name)\n'
    cadena += 'for test in tb_generated.get_tests():\n'
    # cadena += '  if test.name == "'+self.name+'_test":\n'
    # cadena += '    for i in range (0,num_test):\n'
    cadena += '  test.add_config(name="'+self.name+'", pre_config=pre_config_func())\n'
    # cadena += '  else:\n'
    # cadena += '    pass\n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setAsocPosCheck(self):
    f = open (self.filename, "a")
    cadena  = '#func poscheck\n'
    cadena += 'tb_generated = '+self.name+'_tb_lib.entity("'+self.tb[0].split(".")[0]+'")\n'
    # cadena += 'for test in tb_generated.get_tests():\n'
    # cadena += '  print(test.name)\n'
    cadena += 'for test in tb_generated.get_tests():\n'
    # cadena += '  if test.name == "'+self.name+'_test":\n'
    # cadena += '    for i in range (0,num_test):\n'
    cadena += '    test.add_config(name="'+self.name+'", post_check=post_check_func())\n'
    # cadena += '  else:\n'
    # cadena += '    pass\n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def setAsocPrePosCheck(self):
    f = open (self.filename, "a")
    cadena  = '#func checks\n'
    cadena += 'tb_generated = '+self.name+'_tb_lib.entity("'+self.tb[0].split(".")[0]+'")\n'
    # cadena += 'for test in tb_generated.get_tests():\n'
    # cadena += '  print(test.name)\n'
    cadena += 'for test in tb_generated.get_tests():\n'
    # cadena += '  if test.name == "'+self.name+'_test":\n'
    # cadena += '    for i in range (0,num_test):\n'
    cadena += '    test.add_config(name="'+self.name+'", pre_config=pre_config_func(),post_check=post_check_func())\n'
    # cadena += '  else:\n'
    # cadena += '    pass\n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def run(self):
    f = open (self.filename, "a")
    cadena = '#Run tests.\n'
    cadena += 'ui.main(post_run=post_run_fcn)'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def checkCobertura(self):
    f = open (self.filename, "a")
    cadena = 'def post_run_fcn(results):\n'
    cadena += '    if(code_coverage == True ):\n'
    for i in range(0,len(self.src)):
        filename, file_extension = os.path.splitext(self.src[i])
        if (file_extension != ".xpr"):
            cadena += '        subprocess.call(["lcov", "--capture", "--directory", "' + os.path.splitext(os.path.basename(self.src[i]))[0] + '.gcda", "--output-file",  "code_' + str(i)+ '.info" ])\n'
    cadena += '        subprocess.call(["genhtml"'
    for i in range(0,len(self.src)):
        filename, file_extension = os.path.splitext(self.src[i])
        if (file_extension != ".xpr"):
            cadena += ',"code_' + str(i)+ '.info"'
    cadena += ',"--output-directory", "'+self.coverageReport+'"])\n'
    cadena += '\n'
    f.write(cadena)
    f.close()

  def separator(self):
    f = open (self.filename, "a")
    cadena  = '################################################################################\n'
    f.write(cadena)
    f.close()
