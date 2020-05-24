import keyboard
import sys

def writea_():
    keyboard.write('ā')
    keyboard.unhook_all()
    init_hook()
def writeA_():
    keyboard.write('Ā')
    keyboard.unhook_all()
    init_hook()
def writei_():
    keyboard.write('ī')
    keyboard.unhook_all()
    init_hook()
def writeI_():
    keyboard.write('Ī')
    keyboard.unhook_all()
    init_hook()
def writeu_():
    keyboard.write('ū')
    keyboard.unhook_all()
    init_hook()
def writeU_():
    keyboard.write('Ū')
    keyboard.unhook_all()
    init_hook()
def writee_():
    keyboard.write('ē')
    keyboard.unhook_all()
    init_hook()
def writeE_():
    keyboard.write('Ē')
    keyboard.unhook_all()
    init_hook()
def writeo_():
    keyboard.write('ō')
    keyboard.unhook_all()
    init_hook()
def writeO_():
    keyboard.write('Ō')
    keyboard.unhook_all()
    init_hook()
def exit_():
    keyboard.unhook_all()
    init_hook()

def enterMakronMode():
    keyboard.add_hotkey('a', writea_, suppress=True)
    keyboard.add_hotkey('shift + a', writeA_, suppress=True)
    keyboard.add_hotkey('i', writei_, suppress=True)
    keyboard.add_hotkey('shift + I', writeI_, suppress=True)
    keyboard.add_hotkey('u', writeu_, suppress=True)
    keyboard.add_hotkey('shift + U', writeU_, suppress=True)
    keyboard.add_hotkey('e', writee_, suppress=True)
    keyboard.add_hotkey('shift + E', writeE_, suppress=True)
    keyboard.add_hotkey('o', writeo_, suppress=True)
    keyboard.add_hotkey('shift + O', writeO_, suppress=True)
    keyboard.add_hotkey('ctrl + esc', exit_, suppress=True)

def init_hook():
    keyboard.add_hotkey('ctrl + shift + -', enterMakronMode)

### Traycode by Jie Jenn
def main(resource_dir):
    from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
    from PyQt5.QtGui import QIcon
    init_hook()
    app = QApplication(sys.argv)
    resource_dir='{0}\\256.png'.format(resource_dir)
    trayIcon = QSystemTrayIcon(QIcon(resource_dir), parent=app)
    trayIcon.setToolTip('JapoRomaHelper')
    trayIcon.show()
    menu = QMenu()
    exitAction = menu.addAction('Exit')
    exitAction.triggered.connect(app.quit)
    trayIcon.setContextMenu(menu)
    sys.exit(app.exec_())
