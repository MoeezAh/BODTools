import Bladex
import Actions

def LaunchTools():
    AppMode = Bladex.GetAppMode()

    if AppMode == "Game":
        Bladex.AddScheduledFunc(
            Bladex.GetTime(), Actions.ReportMsg, ("This is Game."))

    if AppMode == "Menu":
        Bladex.AddScheduledFunc(
            Bladex.GetTime(), Actions.ReportMsg, ("This is Menu."))