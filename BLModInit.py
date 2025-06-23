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
    MenuText.ForeingDict["BOD Tools"] = "BOD Tools" # type: ignore
    MenuText.ForeingDict["BACK"] = "BACK" # type: ignore
    MenuText.ForeingDict['Respawn  disabled'] = 'Respawn Activado' # type: ignore
    MenuText.ForeingDict['Respawn  enabled'] = 'Respawn Desactivado' # type: ignore
    MenuText.ForeingDict["LIFE"] = "LIFE" # type: ignore
    MenuText.ForeingDict["WEAPONS"] = "WEAPONS" # type: ignore
    MenuText.ForeingDict["ITEMS"] = "CHEATS" # type: ignore
    MenuText.ForeingDict["MAP"] = "MAP" # type: ignore
    MenuText.ForeingDict["MISC"] = "MISC" # type: ignore
    MenuText.ForeingDict["RESTORE HEALTH"] = "RESTORE HEALTH" # type: ignore
    MenuText.ForeingDict["LEVEL UP"] = "LEVEL UP" # type: ignore
    MenuText.ForeingDict["LEVEL DOWN"] = "LEVEL DOWN" # type: ignore
    MenuText.ForeingDict["Menu already activated."] = "Menu already activated." # type: ignore
    MenuText.ForeingDict[""] = "" # type: ignore
    MenuText.ForeingDict[""] = "" # type: ignore
    MenuText.ForeingDict[""] = "" # type: ignore
    MenuText.ForeingDict[""] = "" # type: ignore
    MenuText.ForeingDict[""] = "" # type: ignore
    MenuText.ForeingDict[""] = "" # type: ignore


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
