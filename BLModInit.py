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
import acts

# Translations

import Language
import MenuText

import BODToolsMenu

if Language.Current == "Spanish":
    MenuText.ForeingDict['Respawn  disabled'] = 'Respawn Activado' # type: ignore
    MenuText.ForeingDict['Respawn  enabled'] = 'Respawn Desactivado' # type: ignore

BODToolsFunc.debugprint("Adding input action")

InputManager = BInput.GetInputManager()
OldInputActionsSet = InputManager.GetInputActionsSet()
InputManager.SetInputActionsSet("Default")

Bladex.AddInputAction("LaunchTools", 0)
Bladex.AddBoundFunc("LaunchTools", BODToolsFunc.LaunchTools)
Bladex.AssocKey("LaunchTools", "Keyboard", "F12")

InputManager.SetInputActionsSet(OldInputActionsSet)

BODToolsFunc.debugprint("Added input action")

BODToolsFunc.debugprint("Adding configureable actions")

acts.ConfigurableActions.append(
    ("Launch Tools", "LaunchTools", [])
)

BODToolsFunc.debugprint("Added configureable actions")

global ModMenu
ModMenu = BODToolsMenu.ModMenu
