import Bladex
import BODToolsFunc

def RemoveInputAction():
    InputManager = Bladex.GetInputManager()
    OldInputActionSets = InputManager.GetInputActionsSet()
    InputManager.SetInputActionsSet("Default")
    
    Bladex.RemoveBoundFunc("LaunchTools", BODToolsFunc.LaunchTools)

    InputManager.SetInputActionsSet(OldInputActionSets)

RemoveInputAction()