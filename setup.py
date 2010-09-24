# bootstrap easy_install
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name = 'imgdupcheck',
    version = '0.0.1',
    description = "fork of a tool that looks for duplicate images",
    author = "Mike G.",
    author_email = "leftwing@alumni.rutgers.edu",
    url = "http://github.com/mjgiarlo/ImageDuplicateCheck",
    py_modules = ['imgdupcheck', 'ez_setup'],
    test_suite = 'test',
    scripts = ['bin/imgdupcheck'],
    requires = ["Image"]
)
