# Copyright 2019
#
# Ismael Perez Rojo (ismaelprojo@gmail.com)
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


from setuptools import find_packages, setup

setup(
    name='TerosHDL',
    version='0.1.1',
    author='Ismael Perez Rojo, Carlos Alberto Ruiz Naranjo',
    author_email='ismaelprojo@gmail.com, carlosruiznaranjo@gmail.com',
    description=('Teros HDL backend.'),
    url = 'https://github.com/TerosTechnology/terosHDLbackend',
    download_url = 'https://github.com/TerosTechnology/terosHDLbackend/tarball/0.1',
    keywords='fpga hdl vhdl ise vivado vunit verilog ghdl',
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
          'terosHdlRepo   = terosHdlBackend.terosHdlRepo.terosHdlRepo:main',
          'terosHdlRunpy  = terosHdlBackend.terosHdlRunpy.terosHdlRun:main'
        ]
    },
    include_package_data = True,
    install_requires=[
        'gitpython>2.1.0',
        'vunit_hdl>=4.0.0'
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
        'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)'
    ]
)
