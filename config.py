import os

PROJECT_DIR = os.getcwd()  # Must execute from project dir
# Repository Dlls
BIN_DIR = os.path.join(PROJECT_DIR, 'bin')

# List of all required Paths that need to be added in order to find
# the files needed
PATHS = [
    'C:\\Program Files\\Autodesk\\Revit 2017',
    # RevitAPIUI + Other  Revit Requirements
    'C:\\Program Files\\Autodesk\\Revit 2017\\en-US',
    # ProtoGeometry
    'C:\\Program Files\\Dynamo\\Dynamo Core\\1.2',
    # RevitServices
    'C:\\Program Files\\Dynamo\\Dynamo Revit\\1.2\\Revit_2017'
    ]

BUILTIN_MODULES = ['clr', 'wpf']

LOADABLE_ASSEMBLIES = [
   'IronPython.Wpf',
   'System',
   'PresentationFramework',
   'PresentationCore',
   'WindowsBase',
   'System.Drawing',
   'System.Windows.Forms',

   'RevitServices',
   'RevitNodes',
   'ProtoGeometry',
   'Rhino3dmIO',
    ]

# If running inside Revit, Process these only
try:
    __revit__
    LOADABLE_ASSEMBLIES.extend([ 'RevitAPI', 'RevitAPIUI'])
    # LOADABLE_ASSEMBLIES = [ 'RevitAPI', 'RevitAPIUI',] # ONLY REVIT
except NameError:
    pass
