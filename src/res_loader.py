from PySide6.QtGui import QIcon, QPixmap

def get_icons() -> dict[str, QIcon]:
    icons = {}

    icons["conn_black"] = QIcon(QPixmap(":/light/icons/conn_black.png"))
    icons["darklight_black"] = QIcon(QPixmap(":/light/icons/darklight_black.png"))
    icons["logs_black"] = QIcon(QPixmap(":/light/icons/logs_black.png"))
    icons["plot_black"] = QIcon(QPixmap(":/light/icons/plot_black.png"))
    icons["settings_black"] = QIcon(QPixmap(":/light/icons/settings_black.png"))
    icons["tags_black"] = QIcon(QPixmap(":/light/icons/tags_black.png"))

    icons["conn_white"] = QIcon(QPixmap(":/dark/icons/conn_white.png"))
    icons["darklight_white"] = QIcon(QPixmap(":/dark/icons/darklight_white.png"))
    icons["logs_white"] = QIcon(QPixmap(":/dark/icons/logs_white.png"))
    icons["plot_white"] = QIcon(QPixmap(":/dark/icons/plot_white.png"))
    icons["settings_white"] = QIcon(QPixmap(":/dark/icons/settings_white.png"))
    icons["tags_white"] = QIcon(QPixmap(":/dark/icons/tags_white.png"))

    return icons

