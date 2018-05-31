from enum import Enum
# from elements.ButtonElement import ButtonElement
# from elements.CheckElement import CheckElement
# from elements.EntryElement import EntryElement
# from elements.FrameElement import FrameElement
# from elements.IconElement import IconElement
# from elements.LinkElement import LinkElement
# from elements.ListElement import ListElement
# from elements.TextElement import TextElement
# from elements.ToggleElement import ToggleElement

# class ElementType(Enum):

#     BUTTON = ButtonElement
#     CHECK = CheckElement
#     ENTRY = EntryElement
#     FRAME = FrameElement
#     ICON = IconElement
#     LINK = LinkElement
#     LIST = ListElement
#     TEXT = TextElement
#     TOGGLE = ToggleElement

#     def __call__(self, element_id, webdriver):
#         return self._value_(element_id, webdriver)

#     def value(self):
#         pass

class NavState(Enum):

    NO_NAV = 1
    FWD_NAV = 2
    BACK_NAV = 3