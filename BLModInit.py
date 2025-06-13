####################################################################################
# BODLoader Mod Init File
####################################################################################

# Mod imports

import Bladex
import Reference
import GameText
import BInput
import Actions
import BODToolsFunc

# Translations

import Language
import MenuText

import BODToolsMenu

if Language.Current == "Spanish":
    MenuText.ForeingDict['Respawn  disabled'] = 'Respawn Activado'
    MenuText.ForeingDict['Respawn  enabled'] = 'Respawn Desactivado'

# import acts
# acts.ConfigurableActions


IManager = BInput.GetInputManager()
OldInputActionsSet = IManager.GetInputActionsSet()
IManager.SetInputActionsSet("Default")

Bladex.AddInputAction("LaunchTools", 0)
Bladex.AddBoundFunc("LaunchTools", BODToolsFunc.LaunchTools)
Bladex.AssocKey("LaunchTools", "Keyboard", "F12")

IManager.SetInputActionsSet(OldInputActionsSet)

global ModMenu
ModMenu = BODToolsMenu.ModMenu
