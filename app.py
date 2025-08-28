import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt, QFile
from PySide6.QtGui import QFont, QIcon
from main_ui import Ui_MainWindow
from src.palette_gen import gen_qss_withvars
from src.res_loader import get_icons
from src.theme_handler import ThemeHandler, Theme

IS_CONNECTED = False
DARK_STYLE = gen_qss_withvars("material.qss", "dark")
LIGHT_STYLE = gen_qss_withvars("material.qss", "light")
ICONS: dict[str, QIcon] = None
THEME_HANDLER = ThemeHandler(Theme.DARK)
WINDOW: Ui_MainWindow = None
QMW: QMainWindow = None

def toggle_connected(label: QLabel):
    global IS_CONNECTED
    IS_CONNECTED = not IS_CONNECTED
    if IS_CONNECTED:
        label.setStyleSheet(f"color: {THEME_HANDLER.get_theme_color("text_active")}")
        label.setText("CONNECTED")
    else:
        label.setStyleSheet(f"color: {THEME_HANDLER.get_theme_color("text_passive")}")
        label.setText("DISCONNECTED")


def set_light_theme():
    global ICONS
    WINDOW.themeButton.setText("Light")
    WINDOW.connectionButton.setIcon(ICONS["conn_black"])
    WINDOW.tagsButton.setIcon(ICONS["tags_black"])
    WINDOW.loggingButton.setIcon(ICONS["logs_black"])
    WINDOW.plottingButton.setIcon(ICONS["plot_black"])
    WINDOW.settingsButton.setIcon(ICONS["settings_black"])
    WINDOW.themeButton.setIcon(ICONS["darklight_black"])
    QMW.setStyleSheet(LIGHT_STYLE)
    
def set_dark_theme():
    global ICONS
    WINDOW.themeButton.setText("Dark")
    WINDOW.connectionButton.setIcon(ICONS["conn_white"])
    WINDOW.tagsButton.setIcon(ICONS["tags_white"])
    WINDOW.loggingButton.setIcon(ICONS["logs_white"])
    WINDOW.plottingButton.setIcon(ICONS["plot_white"])
    WINDOW.settingsButton.setIcon(ICONS["settings_white"])
    WINDOW.themeButton.setIcon(ICONS["darklight_white"])
    QMW.setStyleSheet(DARK_STYLE)

def main():
    global ICONS, WINDOW, QMW
    app = QApplication(sys.argv)
    # Load styles

    # Set application font
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    QMW = QMainWindow()
    WINDOW = Ui_MainWindow()
    
    ICONS = get_icons()
    QMW.setStyleSheet(DARK_STYLE)
    
    # QMW.setWindowTitle("S7 Interface")
    # QMW.setWindowIcon(ICONS["app_icon"])
    
    
    WINDOW.setupUi(QMW)
    WINDOW.buttonGroup.setId(WINDOW.connectionButton, 0)
    WINDOW.buttonGroup.setId(WINDOW.tagsButton, 1)
    WINDOW.buttonGroup.setId(WINDOW.loggingButton, 2)
    WINDOW.buttonGroup.setId(WINDOW.plottingButton, 3)
    WINDOW.buttonGroup.setId(WINDOW.settingsButton, 4)
    
    THEME_HANDLER.on_theme_change(Theme.LIGHT, set_light_theme)
    THEME_HANDLER.on_theme_change(Theme.DARK, set_dark_theme)
            
    WINDOW.themeButton.clicked.connect(THEME_HANDLER.toggle_theme)
    WINDOW.connectPlcButton.clicked.connect(lambda: toggle_connected(WINDOW.connectionLabel))
    THEME_HANDLER.update()
    
    QMW.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()