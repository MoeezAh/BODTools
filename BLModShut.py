import Bladex
import BODToolsFunc
import BInput

BODToolsFunc.debugprint("Start of ""RemoveInputAction()""")

InputManager = BInput.GetInputManager()
OldInputActionSets = InputManager.GetInputActionsSet()

# Changing input action set to remove control bindings
InputManager.SetInputActionsSet("Default")
IActions = InputManager.GetInputActions()

BODToolsFunc.debugprint("Found" + str(IActions.nElements()) + ".")

IAction = IActions.Find(BODToolsFunc.InputActionName)

if (Bladex.RemoveBoundFunc("LaunchTools", BODToolsFunc.LaunchTools)):
    BODToolsFunc.debugprint("Bound function removed successfully.")

# Remove input action from input actions set.
if (Bladex.RemoveInputAction(BODToolsFunc.InputActionName)):
    BODToolsFunc.debugprint("Input action removed successfully.")

# Restore old input action set
InputManager.SetInputActionsSet(OldInputActionSets)

# End of shutdown script
BODToolsFunc.debugprint("End of ""RemoveInputAction()""")