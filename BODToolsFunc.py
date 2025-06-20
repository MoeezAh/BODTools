import Bladex
import Actions
import Reference
import Menu
import MenuText
import MenuWidget

print_prefix = "BOD Tools: "
InputActionName = "LaunchTools"

BackOption = {
    "Name": MenuText.GetMenuText("BACK"),
    "VSep": Menu.BackOptionVSep,
    "Command": Menu.BackMenu,
    "Font": Menu.MenuFontBig
}


##########
## Menu ##
##########

Desc1 = {"Name": "TopMenu",
         "Size": (640, 480),
         "Kind": MenuWidget.B_MenuItemTextNoFX,
         "ListDescr": [{
             "Name": MenuText.GetMenuText("LIFE"),
             "Font": Menu.MenuFontBig,
             "VSep": 100,
             "Size": (640, 480),
             "ListDescr": []
         },
         BackOption, {
             "Name": "Back",
             "Kind": MenuWidget.B_BackBlank
         }]
         }

##########
##########
##########


def debugprint(msg):
    Reference.debugprint(print_prefix + msg)

def ExecToolsMenu():
    import GameText
    import Scorer

    GameText.AbortText()

    if not Menu.MENU_PREACTIVATED:
        Menu.TB_ACTIVATED = 1
        Menu.MENU_PREACTIVATED = 1
        backup_menu = Menu.Desc1
        Menu.Desc1 = Desc1

        Menu.ActivateMenu()
        Menu.Desc1 = backup_menu
        Scorer.HideTBS()
    else:
        Bladex.AddScheduledFunc(
            Bladex.GetTime(), Actions.ReportMsg, ("Menu already activated.",))


def LaunchTools():
    AppMode = Bladex.GetAppMode()

    if AppMode == "Game":
        Bladex.AddScheduledFunc(
            Bladex.GetTime(), Actions.ReportMsg, ("This is Game.",))

    if AppMode == "Menu":
        Bladex.AddScheduledFunc(
            Bladex.GetTime(), Actions.ReportMsg, ("This is Menu.",))

    ExecToolsMenu()
