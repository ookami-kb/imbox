from setuptools import setup
import os

version = '0.5.6'


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='swdt-imbox',
    version=version,
    description="Python IMAP for Human beings. Python3 only",
    long_description=read('README.md'),
    keywords='email, IMAP, parsing emails',
    author='Kirill Bubochkin',
    author_email='ookami.kb@gmail.com',
    url='https://github.com/ookami-kb/imbox',
    license='MIT',
    packages=['imbox'],
    package_dir={'imbox': 'imbox'},
    zip_safe=False,
    install_requires=['six'],
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ),
)
