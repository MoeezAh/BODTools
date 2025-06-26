import Bladex
import Reference
import Menu
import MenuWidget

import MenuText

ModMenu = [{
    "Name": MenuText.GetMenuText("BOD Tools"),
    "Kind": MenuWidget.B_MenuItemTextNoFXNoFocus,
    "Font": Menu.MenuFontBig,
    "VSep": 100,
}, {
    "Name": MenuText.GetMenuText("No configuration options defined."),
    "Kind": MenuWidget.B_MenuItemTextNoFXNoFocus,
    "Font": Menu.MenuFontMed,
    "VSep": 20,
}, {
    "Name": MenuText.GetMenuText("BACK"),
    "Font": Menu.MenuFontBig,
    "VSep": Menu.BackOptionVSep,
    "Command": Menu.BackMenu,
}, {
    "Name": "Back",
    "Kind": MenuWidget.B_BackBlank,
}]
