from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='teroshdl',
    version='3.0.0',
    description='It groups python dependencies for TerosHDL.',
    long_description=long_description,
    url='https://terostechnology.github.io',
    author='Teros Technology',
    author_email='terostechnology@gmail.com',
    license='GNU General Public License (GPL)',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='teros fpga',

    python_requires=">=3.0",

    install_requires=[
        "yowasp-yosys",
        "vunit_hdl >= 4.4.1",
        "edalize >= 0.2.5",
        "vsg >= 3.3.0"
    ],
)
