import sys
from distutils.core import setup


PY3 = sys.version_info[0] >= 3
VERSION_FILE = 'LN_Digital_Scratch_Handler/version.py'


def get_version():
    if PY3:
        version_vars = {}
        with open(VERSION_FILE) as f:
            code = compile(f.read(), VERSION_FILE, 'exec')
            exec(code, None, version_vars)
        return version_vars['__version__']
    else:
        execfile(VERSION_FILE)
        return __version__


setup(
    name='LN_Digital_Scratch_Handler',
    version=get_version(),
    description='The LN Digital Scratch Handler.',
    author='Lemaker',
    author_email='support@lemaker.org',
    url='https://github.com/LeMaker/LN_Digital_Scratch_Handler/',
    packages=['LN_Digital_Scratch_Handler'],
    long_description=open('README.md').read(),
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or ",
        "later (AGPLv3+)",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='LN digital scratch bananapi',
    license='GPLv3+',
    requires=['LNcommon'],
    scripts=['bin/LN-Digital-Scratch-Handler'],
)
