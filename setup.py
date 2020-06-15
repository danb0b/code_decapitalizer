# -*- coding: utf-8 -*-
'''
Written by Daniel M. Aukes and CONTRIBUTORS
Email: danaukes<at>asu.edu.
Please see LICENSE for full license.
'''

#from setuptools import setup
from cx_Freeze import setup, Executable
import sys
import shutil
import decapitalizer
import os
import importlib
import idealab_tools.setup_tools as st


shutil.rmtree("build", ignore_errors=True)
shutil.rmtree("dist", ignore_errors=True)
shutil.rmtree('decapitalizer.egg-info', ignore_errors=True)

packages = []
packages.append('decapitalizer')
#packages.append('Qt5')

package_data = {}
package_data['decapitalizer'] = ['files/*']

includes = []
includes.append('PyQt5')

excludes = []
excludes.append('tcl')
excludes.append('tk')
#excludes.append('numpy')
#excludes.append('scipy')
#excludes.append('babel')
#excludes.append('matplotlib')
#excludes.append('gtk')
#excludes.append('_gtkagg')
#excludes.append('_tkagg')
#excludes.append('bsddb')
#excludes.append('curses')
#excludes.append('pywin.debugger')
#excludes.append('pywin.debugger.dbgcon')
#excludes.append('pywin.dialogs')
#excludes.append('Tkconstants')
#excludes.append('Tkinter')
#excludes.append('babel')
#excludes.append('notebook')
#excludes.append('spyder')
#excludes.append('ipython')
#excludes.append('jupyter_client')
#excludes.append('jupyter_core')

zip_includes = []
include_files = []
include_files.extend(st.include_entire_directory(st.fix(st.python_installed_directory,'Library/plugins/platforms'),''))
#include_files.extend(st.include_entire_directory(st.fix(st.python_installed_directory,'Library/bin'),''))
include_files.append((st.fix(st.python_installed_directory,'Library/bin/Qt5Widgets.dll'),'Library/bin/Qt5Widgets.dll'))
include_files.append((st.fix(st.python_installed_directory,'Library/bin/Qt5Core.dll'),'Library/bin/Qt5Core.dll'))
include_files.append((st.fix(st.python_installed_directory,'Library/bin/Qt5Gui.dll'),'Library/bin/Qt5Gui.dll'))

build_exe_options = {}
build_exe_options['packages']=packages
build_exe_options['includes']=includes
build_exe_options['excludes']=excludes
build_exe_options["include_files"]=include_files
build_exe_options["zip_includes"]=zip_includes
build_exe_options['include_msvcr']=True

bdist_msi_options = {}
#import uuid
#bdist_msi_options['upgrade_code']= str(uuid.uuid4())
bdist_msi_options['upgrade_code']= '6576a015-5ff7-4cf8-bc8c-297b139cf5ae'

exe = Executable(
   # what to build
   script = "python/decapitalizer/main_app.py", # the name of your main python script goes here 
   initScript = None,
   base = "Win32GUI", # if creating a GUI instead of a console app, type "Win32GUI", otherwise, None
   #targetName = "Hello World.exe", # this is the name of the executable file
   #copyDependentFiles = True,
   #compress = False,
   #appendScriptToExe = True,
   #appendScriptToLibrary = True,
   icon = 'python/decapitalizer/files/logo_4_1_icon.ico', # if you want to use an icon file, specify the file name here
   shortcutDir="ProgramMenuFolder",
   shortcutName='decapitalizer',
)
        
#executables = []
#executables.append(exe)


setup_options = {}
setup_options['build_exe']=build_exe_options
setup_options['bdist_msi']=bdist_msi_options

setup_kwargs = {}
setup_kwargs['name']='decapitalizer'
setup_kwargs['version']='0.0.1'
setup_kwargs['classifiers']=['Programming Language :: Python','Programming Language :: Python :: 3']   
setup_kwargs['description']='Empty QT Project developed by the IDEAlab.'
setup_kwargs['author']='Dan Aukes'
setup_kwargs['author_email']='danaukes@gmail.com'
#setup_kwargs['url']='https://github.com/idealabasu/code_idealab_tools.git'
setup_kwargs['license']='MIT'
setup_kwargs['packages']=packages
setup_kwargs['package_dir']={'decapitalizer' : 'python/decapitalizer'}
setup_kwargs['package_data'] = package_data
#setup_kwargs['install_requires']=[]
setup_kwargs['options'] = setup_options
setup_kwargs['executables'] = [exe]

module = importlib.import_module('tcl')
p = list(module.__path__)[0]
os.environ['TCL_LIBRARY'] = p
os.environ['TK_LIBRARY'] = p

setup(**setup_kwargs)

