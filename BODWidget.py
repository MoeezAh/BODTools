import BUIx
import Language
import MenuText
import MenuWidget
import ScorerWidgets
import SpinWidget
import types


class B_SpinWidgetAux(BUIx.B_FrameWidget):
    def __init__(self, Parent, Name, Width, Height, font_server, font):
        BUIx.B_FrameWidget.__init__(self, Parent, Name, Width, Height)
        self.LeftArrow = BUIx.B_TextWidget(
            self, "SpinLArrow "+Name, "<", font_server, font)
        self.LeftArrow.SetColor(252, 247, 167)
        self.LeftArrow.SetAlpha(1)
        self.AddWidget(self.LeftArrow, 1, 0.5, BUIx.B_FrameWidget.B_FR_AbsoluteLeft, BUIx.B_FrameWidget.B_FR_Left,
                       BUIx.B_FrameWidget.B_FR_VRelative, BUIx.B_FrameWidget.B_FR_VCenter)

        self.RightArrow = BUIx.B_TextWidget(
            self, "SpinRArrow "+Name, ">", font_server, font)
        self.RightArrow.SetColor(252, 247, 167)
        self.RightArrow.SetAlpha(1)
        self.AddWidget(self.RightArrow, 1, 0.5, BUIx.B_FrameWidget.B_FR_AbsoluteRight, BUIx.B_FrameWidget.B_FR_Right,
                       BUIx.B_FrameWidget.B_FR_VRelative, BUIx.B_FrameWidget.B_FR_VCenter)

        self.Text = BUIx.B_TextWidget(
            self, "SpinTextAux "+Name, "0", font_server, font)
        self.Text.SetColor(252, 247, 167)
        self.Text.SetAlpha(1)
        self.AddWidget(self.Text, 0.5, 0.5, BUIx.B_FrameWidget.B_FR_HRelative, BUIx.B_FrameWidget.B_FR_HCenter,
                       BUIx.B_FrameWidget.B_FR_VRelative, BUIx.B_FrameWidget.B_FR_VCenter)

        self.Options = ["No options"]
        self.Value = 0
        self.UpdateDisplayValue()

        w, h = self.Text.GetSize()
        self.SetSize(Width, h)
        self.RecalcLayout()

    def SetOptions(self, options):
        self.Options = options
        self.SetValue(0)

    def GetText(self):
        return self.Options[self.Value]

    def SetText(self, text):
        index = -1
        try:
            index = self.Options.index(text)
        except KeyError:
            index = 0

        self.SetValue(index)

    def SetValue(self, index):
        if index < 0 or index >= len(self.Options):
            index = 0

        self.Value = index
        self.UpdateDisplayValue()

    def AdjustArrows(self):
        if self.Value <= 0:
            self.LeftArrow.SetVisible(0)
        else:
            self.LeftArrow.SetVisible(1)

        if self.Value >= len(self.Options) - 1:
            self.RightArrow.SetVisible(0)
        else:
            self.RightArrow.SetVisible(1)

    def IncrementValue(self):
        if self.Value < len(self.Options) - 1:
            self.Value = self.Value + 1
            self.UpdateDisplayValue()

    def DecrementValue(self):
        if self.Value > 0:
            self.Value = self.Value - 1
            self.UpdateDisplayValue()

    def UpdateDisplayValue(self):
        text = self.GetText()
        self.Text.SetText(text)

        self.AdjustArrows()
        self.RecalcLayout()


class B_SpinWidget(BUIx.B_FrameWidget):
    def __init__(self, Parent, Name, Width, Height, SpinnerWidth, font_server, font, default_value):
        BUIx.B_FrameWidget.__init__(self, Parent, Name, Width, Height)
        print("Height: " + str(Height))
        print("B_SpinWidget -- After init: " + str(self.GetSize()[1]))
        self.Text = BUIx.B_TextWidget(
            self, "SpinLArrow "+Name, Name, font_server, font)
        
        v1 = self.AddWidget(self.Text, 1, 0.5, BUIx.B_FrameWidget.B_FR_AbsoluteLeft, BUIx.B_FrameWidget.B_FR_Left,
                       BUIx.B_FrameWidget.B_FR_VRelative, BUIx.B_FrameWidget.B_FR_VCenter)
        print("B_SpinWidget -- First Widget:  " + str(self.GetSize()[1]))
        print(self.Text.GetSize())
        print(v1)

        self.DefaultText = BUIx.B_TextWidget(
            self, "DefaultText", Name, font_server, font)
        self.DefaultText.SetText("(" + MenuText.GetMenuText("Default") + ")")

        v2 = self.AddWidget(self.DefaultText, 90, 0.5, BUIx.B_FrameWidget.B_FR_AbsoluteRight, BUIx.B_FrameWidget.B_FR_Right,
                       BUIx.B_FrameWidget.B_FR_VRelative, BUIx.B_FrameWidget.B_FR_VCenter)
        print("B_SpinWidget -- Second Widget: " + str(self.GetSize()[1]))
        print(self.DefaultText.GetSize())
        print(v2)

        w, h = self.Text.GetSize()

        self.Spin = B_SpinWidgetAux(
            self, "SpinText "+Name, SpinnerWidth, h, font_server, font)

        v3 = self.AddWidget(self.Spin, 1, 0.5, BUIx.B_FrameWidget.B_FR_AbsoluteRight, BUIx.B_FrameWidget.B_FR_Right,
                       BUIx.B_FrameWidget.B_FR_VRelative, BUIx.B_FrameWidget.B_FR_VCenter)
        print("B_SpinWidget -- Third Widget: " + str(self.GetSize()[1]))
        print(self.Spin.GetSize())
        print(v3)

        self.SetDrawFunc(self.Draw)
        self.DefaultValue = default_value

        self.SetSize(Width, h)
        self.RecalcLayout()

    def IncrementValue(self):
        self.Spin.IncrementValue()

    def DecrementValue(self):
        self.Spin.DecrementValue()

    def SetValue(self, value):
        self.Spin.SetValue(value)

    def GetValue(self):
        return self.Spin.Value

    def SetOptions(self, options):
        self.Spin.SetOptions(options)

    def Draw(self, x, y, time):
        foc = self.GetHasFocus()
        self.Text.SetAlpha(1.0)
        self.Spin.Text.SetAlpha(1.0)
        self.Spin.LeftArrow.SetAlpha(1.0)
        self.Spin.RightArrow.SetAlpha(1.0)

        if (self.DefaultValue == self.GetValue()):
            self.DefaultText.SetAlpha(1.0)
        else:
            self.DefaultText.SetAlpha(0.0)

        if foc:
            self.Text.SetColor(252, 247, 167)
            self.Spin.Text.SetColor(252, 247, 167)
            self.Spin.LeftArrow.SetColor(252, 247, 167)
            self.Spin.RightArrow.SetColor(252, 247, 167)
            self.DefaultText.SetColor(252, 247, 167)
        else:
            self.Text.SetColor(207, 144, 49)
            self.Spin.Text.SetColor(207, 144, 49)
            self.Spin.LeftArrow.SetColor(207, 144, 49)
            self.Spin.RightArrow.SetColor(207, 144, 49)
            self.DefaultText.SetColor(207, 144, 49)

        self.DefDraw(x, y, time)


class B_MenuSpin(B_SpinWidget, MenuWidget.B_MenuTreeItem):
    def __init__(self, Parent, MenuDescr, StackMenu, font_server=ScorerWidgets.font_server):
        if MenuDescr.has_key("Size"):
            w, h = MenuDescr["Size"]
        else:
            w, h = (300, 19)

        if MenuDescr.has_key("SpinnerWidth"):
            spinnerWidth = MenuDescr["SpinnerWidth"]
        else:
            spinnerWidth = 150

        if MenuDescr.has_key("Font"):
            font = MenuDescr["Font"]
        else:
            font = Language.LetrasMenu

        if MenuDescr.has_key("DefaultValue"):
            defaultValue = MenuDescr["DefaultValue"]
        else:
            defaultValue = None

        B_SpinWidget.__init__(
            self, Parent, MenuDescr["Name"], w, h, spinnerWidth, font_server, font, defaultValue)
        MenuWidget.B_MenuTreeItem.__init__(self, MenuDescr, StackMenu)

        if MenuDescr.has_key("Options"):
            B_SpinWidget.SetOptions(self, MenuDescr["Options"])

    def IncMenuItem(self):
        self.IncrementValue()

    def DecMenuItem(self):
        self.DecrementValue()

    def ActivateItem(self, activate):
        # Call existing implementation if we have "ListDescr"
        # option provided to call up a new menu on activation.
        if activate != 1 or self.MenuDescr.has_key("ListDescr"):
            return MenuWidget.B_MenuTreeItem.ActivateItem(self, activate)
        
        # Following implementation will only be called in case
        # of activate == 1, otherwise we wouldn't be here.
        if self.MenuDescr.has_key("Command") and type(self.MenuDescr["Command"]) == types.FunctionType:
            try:
                self.MenuDescr["Command"](self)
                return 1
            except Exception, e:
                print("Failed to call function associated with Command value of '" + str(self) + "'. " + e)
                return 0
        else:
            # On option activation if COMMAND option has
            # not be set theN increament current option.
            self.IncMenuItem()

    # def FinalRelease(self):
    #     if self.SetValueEnd is not None:
    #     self.SetValueEnd(self.GetValue())
