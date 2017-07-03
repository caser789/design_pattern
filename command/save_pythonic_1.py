import sys

"""Receiver"""


class Window(object):

    def exit(self):
        sys.exit(0)


class Document(object):

    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"

    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.contents)

"""invoker"""


class ToolbarButton(object):

    def __init__(self, name, iconname):
        self.name = name
        self.iconname = iconname

    def click(self):
        self.command.execute()


class MenuItem(object):

    def __init__(self, menu_name, menuitem_name):
        self.menu = menu_name
        self.item = menuitem_name

    def click(self):
        self.command.execute()


class KeyboardShortcut(object):

    def __init__(self, key, modifier):
        self.key = key
        self.modifier = modifier

    def keypress(self):
        self.command.execute()


def main():
    document = Document("a_document.txt")
    window = Window()

    save_button = ToolbarButton('save', 'save.png')
    save_button.command = document.save

    save_keystroke = KeyboardShortcut("s", "ctrl")
    save_keystroke.command = document.save

    exit_menu = MenuItem("File", "Exit")
    exit_menu.command = window.exit

if __name__ == "__main__":
    main()
