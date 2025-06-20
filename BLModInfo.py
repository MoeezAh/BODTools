####################################################################################
# BODLoader
####################################################################################

####################################################################################
# Global variables
####################################################################################

global ModName
global ModDesc
global ModVersion
global ModAuthor
global ModAuthorInfo
global ModArenaMode
global NewFiles
global RepFiles
global MakeDirs
global ModArenaMode

####################################################################################
# Mod Info
####################################################################################

# Mod Name
ModName = "BOD Tools"
# Mod Description
ModDesc = (
    """Tools for\n"""
    """Blade of Darkness\n"""
    """Use them only to have fun\n"""
)

# Multilanguage descriptions:

if Language.Current == "Spanish":
    ModDesc = (
        """Tools for\n"""
        """Blade of Darkness\n"""
        """Use them only to have fun\n"""
    )
else:
    ModDesc = (
        """Tools for\n"""
        """Blade of Darkness\n"""
        """Use them only to have fun\n"""
    )

# Mod Version
ModVersion = "1.0"
# Author name
ModAuthor = "Moeez Ahmed"
# Author info: email, url,...
ModAuthorInfo = "moeez.ahmad@outlook.com"

####################################################################################
# Mod Data
####################################################################################

# Base dir for all paths: BOD\Maps\Casa

# Make new directories

# Enable following to create new directories.
# MakeDirs = ['..\MapName']

# New Files added by Mod and destination directory

NewFiles[0] = {"File": "BODToolsMenu.py",      "Dest": "../../Scripts"}
NewFiles[1] = {'File': 'BODToolsFunc.py',      'Dest': '../../Scripts'}
# NewFiles[2]      = {'File': '..\Arena1\Blade_progress.jpg',  'Dest': '..\MapName'}

# Replaced Files
# RepFiles[1]    = {'File': 'Blade.exe',         'Dest': '..\..\bin'}

# Setup to 1 for enable this mod in Arena mode
ModArenaMode = 0

