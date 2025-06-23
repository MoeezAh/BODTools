import Bladex
import Actions
import CharStats
import Reference
import Menu
import MenuText
import MenuWidget
import netgame

print_prefix = "BOD Tools: "
InputActionName = "LaunchTools"
LevelUpLabelText = None

BackOption = {
    "Name": MenuText.GetMenuText("BACK"),
    "VSep": Menu.BackOptionVSep,
    "Command": Menu.BackMenu,
    "Font": Menu.MenuFontBig
}


def debugprint(msg):
    Reference.debugprint(print_prefix + msg)


def GiveExperiance(EntityName, Experience):
    import Scorer

    me = Bladex.GetEntity(EntityName)
    me.PartialLevel = me.PartialLevel + Experience
    LevelLimit = CharStats.GetCharExperienceCost(me.CharType, me.Level)

    if me.PartialLevel >= LevelLimit:
        while me.PartialLevel >= LevelLimit:
            me.PartialLevel = me.PartialLevel-LevelLimit
            me.Level = me.Level+1
            LevelLimit = CharStats.GetCharExperienceCost(me.CharType, me.Level)

        Scorer.LevelUp()
        Scorer.SetLevelLimits(
            0, CharStats.GetCharExperienceCost(me.CharType, me.Level))

        DisplayLevelUpFX(me)

        # Restore state of the player.
        if me.Life > 0:  # If an enemy death by poison or trowed weapons and.. You are death!
            me.ResetWounds()
            me.Life = CharStats.GetCharMaxLife(me.Kind, me.Level)

        Scorer.SlideTBS(0)
        Scorer.LevelUpFlash()

    if netgame.GetNetState() == 0:
        Scorer.SetLevelBarValue(me.PartialLevel)


def DisplayLevelUpFX(entity):
    import GenFX

    maxlevel = CharStats.GetMaxLevel()
    maxsize = 50+(140/maxlevel)*entity.Level  # 50->190
    maxPPS = 120+(600/maxlevel)*entity.Level  # 120->720
    maxint = 0.5+(4.5/maxlevel)*entity.Level  # 0.5->5.0
    AuraParams = (5, 0, 1, 0, 0, 1)
    AuraGradient = (2, 0.4, 0.6, 1.0, 0.5, 0.0, 0.1, 0.2, 1.0, 0.0, 0.8)
    AuraVar1Args = (5, maxsize, 0, 1, 0.5)
    AuraVar2Args = (maxsize, 5, 1, 0, 1.0)
    PSParams = (entity.Data.LevelUpParticleData, "LevelUpParticle", 30,
                50, 150, 255, maxPPS, -600, 0.0, 2, 2, 0.4, 30, 0.5)
    GenFX.LevelUpFX(entity.Name, 1, AuraParams, AuraGradient, AuraVar1Args, AuraVar2Args,
                    PSParams, maxint, "Timer15", 15, "../../Sounds/aparicion-escudo.wav")


def ResetDemotePlayerFlashText():
    import Scorer
    global LevelUpLabelText
    Scorer.wLevelUpLabel.SetFlash(0)
    Scorer.wLevelUpLabel.SetVisible(0)
    Scorer.wLevelUpLabel.SetText(LevelUpLabelText)


def ShowDemotePlayerFlashText():
    import Scorer
    global LevelUpLabelText
    LevelUpLabelText = Scorer.wLevelUpLabel.GetTextData()
    Scorer.wLevelUpLabel.SetText(
        MenuText.GetMenuText("LEVEL DOWN"))
    Scorer.wLevelUpLabel.SetFlash(15)
    Scorer.wLevelUpLabel.SetVisible(1)

    Bladex.AddScheduledFunc(
        Bladex.GetTime() + 2.0, ResetDemotePlayerFlashText, ())


def DemotePerson(EntityName):
    import Scorer

    entity = Bladex.GetEntity(EntityName)
    entity.PartialLevel = 0
    entity.Level = entity.Level - 1

    if netgame.GetNetState() == 0:
        Scorer.SetLevelBarValue(entity.PartialLevel)


def DemotePersonEx(EntityName):
    import Scorer
    import GenFX

    entity = Bladex.GetEntity(EntityName)

    # Entity level can not be dropped below 1.
    if entity.Level == 0:
        return

    entity.PartialLevel = 0
    entity.Level = entity.Level - 1
    Scorer.SetLevelLimits(
        0, CharStats.GetCharExperienceCost(entity.CharType, entity.Level))

    DisplayLevelUpFX(entity)
    ShowDemotePlayerFlashText()

    # Restore state of the player.
    if entity.Life > 0:  # If an enemy death by poison or trowed weapons and.. You are death!
        entity.ResetWounds()
        entity.Life = CharStats.GetCharMaxLife(entity.Kind, entity.Level)

    if netgame.GetNetState() == 0:
        Scorer.SetLevelBarValue(entity.PartialLevel)


def HealPlayer():
    me = Bladex.GetEntity("Player1")
    maxLife = CharStats.GetCharMaxLife(me.Kind, me.Level)
    me.Life = maxLife

#################
## Menu Events ##
#################

def CmdHeal(parent):
    Bladex.AddScheduledFunc(
        Bladex.GetTime() + 0.5, HealPlayer, ())

    Menu.BackMenu(None)
    Menu.BackMenu(None)


def CmdLevelUp(parent):
    me = Bladex.GetEntity("Player1")
    LevelLimit = CharStats.GetCharExperienceCost(me.CharType, me.Level)

    Bladex.AddScheduledFunc(
        Bladex.GetTime() + 0.5, GiveExperiance, ("Player1", LevelLimit - me.PartialLevel))

    #################################

    Menu.BackMenu(None)
    Menu.BackMenu(None)


def CmdLevelDown(parent):
    Bladex.AddScheduledFunc(
        Bladex.GetTime() + 0.5, DemotePersonEx, ("Player1",))

    Menu.BackMenu(None)
    Menu.BackMenu(None)

##########
## Menu ##
##########


LifeMenu = {
    "Name": MenuText.GetMenuText("LIFE"),
    "Kind": MenuWidget.B_MenuItemTextNoFX,
    "Font": Menu.MenuFontBig,
    "VSep": 20,
    "Size": (640, 480),
    "ListDescr": [{
        "Name": MenuText.GetMenuText("LIFE"),
        "Kind": MenuWidget.B_MenuItemTextNoFXNoFocus,
        "Font": Menu.MenuFontBig,
        "VSep": 100
    }, {
        "Name": MenuText.GetMenuText("RESTORE HEALTH"),
        "Font": Menu.MenuFontBig,
        "VSep": 20,
        "Command": CmdHeal
    }, {
        "Name": MenuText.GetMenuText("LEVEL UP"),
        "Font": Menu.MenuFontBig,
        "VSep": 5,
        "Command": CmdLevelUp
    }, {
        "Name": MenuText.GetMenuText("LEVEL DOWN"),
        "Font": Menu.MenuFontBig,
        "VSep": 5,
        "Command": CmdLevelDown
    }, BackOption, {
        "Name": "Back",
        "Kind": MenuWidget.B_BackBlank
    }]
}

WeaponsMenu = {
    "Name": MenuText.GetMenuText("WEAPONS"),
    "Kind": MenuWidget.B_MenuItemTextNoFX,
    "Font": Menu.MenuFontBig,
    "VSep": 5,
    "Size": (640, 480),
    "ListDescr": []
}

ItemsMenu = {
    "Name": MenuText.GetMenuText("ITEMS"),
    "Kind": MenuWidget.B_MenuItemTextNoFX,
    "Font": Menu.MenuFontBig,
    "VSep": 5,
    "Size": (640, 480),
    "ListDescr": []
}

CheatsMenu = {
    "Name": MenuText.GetMenuText("CHEATS"),
    "Kind": MenuWidget.B_MenuItemTextNoFX,
    "Font": Menu.MenuFontBig,
    "VSep": 5,
    "Size": (640, 480),
    "ListDescr": []
}

MapMenu = {
    "Name": MenuText.GetMenuText("MAP"),
    "Kind": MenuWidget.B_MenuItemTextNoFX,
    "Font": Menu.MenuFontBig,
    "VSep": 5,
    "Size": (640, 480),
    "ListDescr": []
}

MiscMenu = {
    "Name": MenuText.GetMenuText("MISC"),
    "Kind": MenuWidget.B_MenuItemTextNoFX,
    "Font": Menu.MenuFontBig,
    "VSep": 5,
    "Size": (640, 480),
    "ListDescr": []
}

Desc1 = {"Name": "TopMenu",
         "Size": (640, 480),
         "Kind": MenuWidget.B_MenuItemTextNoFX,
         "ListDescr": [{
             "Name": MenuText.GetMenuText("BOD Tools"),
             "Kind": MenuWidget.B_MenuItemTextNoFXNoFocus,
             "Font": Menu.MenuFontBig,
             "VSep": 100
         },
             LifeMenu,
             WeaponsMenu,
             ItemsMenu,
             CheatsMenu,
             MapMenu,
             BackOption,
             {
             "Name": "Back",
             "Kind": MenuWidget.B_BackBlank
         }]
         }

##########
##########
##########


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
        ExecToolsMenu()
