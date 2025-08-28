# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main2.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(865, 641)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"icons/app_icon.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainContainer = QVBoxLayout()
        self.mainContainer.setObjectName(u"mainContainer")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.menuContainer = QWidget(self.centralwidget)
        self.menuContainer.setObjectName(u"menuContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuContainer.sizePolicy().hasHeightForWidth())
        self.menuContainer.setSizePolicy(sizePolicy)
        self.menuContainer.setMaximumSize(QSize(200, 16777215))
        self.menuContainer.setStyleSheet(u"QPushButton {\n"
"text-align: left;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.menuContainer)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pagesButtons = QWidget(self.menuContainer)
        self.pagesButtons.setObjectName(u"pagesButtons")
        sizePolicy.setHeightForWidth(self.pagesButtons.sizePolicy().hasHeightForWidth())
        self.pagesButtons.setSizePolicy(sizePolicy)
        self.pagesLayout = QVBoxLayout(self.pagesButtons)
        self.pagesLayout.setSpacing(6)
        self.pagesLayout.setObjectName(u"pagesLayout")
        self.pagesLayout.setContentsMargins(0, 0, 0, 0)
        self.connectionButton = QPushButton(self.pagesButtons)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.setExclusive(True)
        self.buttonGroup.addButton(self.connectionButton)
        self.connectionButton.setObjectName(u"connectionButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.connectionButton.sizePolicy().hasHeightForWidth())
        self.connectionButton.setSizePolicy(sizePolicy1)
        self.connectionButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.connectionButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/light/icons/conn_black.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.connectionButton.setIcon(icon1)
        self.connectionButton.setIconSize(QSize(24, 24))
        self.connectionButton.setCheckable(True)
        self.connectionButton.setChecked(True)
        self.connectionButton.setFlat(True)

        self.pagesLayout.addWidget(self.connectionButton)

        self.tagsButton = QPushButton(self.pagesButtons)
        self.buttonGroup.addButton(self.tagsButton)
        self.tagsButton.setObjectName(u"tagsButton")
        sizePolicy1.setHeightForWidth(self.tagsButton.sizePolicy().hasHeightForWidth())
        self.tagsButton.setSizePolicy(sizePolicy1)
        self.tagsButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tagsButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/light/icons/tags_black.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tagsButton.setIcon(icon2)
        self.tagsButton.setIconSize(QSize(24, 24))
        self.tagsButton.setCheckable(True)
        self.tagsButton.setFlat(True)

        self.pagesLayout.addWidget(self.tagsButton)

        self.loggingButton = QPushButton(self.pagesButtons)
        self.buttonGroup.addButton(self.loggingButton)
        self.loggingButton.setObjectName(u"loggingButton")
        sizePolicy1.setHeightForWidth(self.loggingButton.sizePolicy().hasHeightForWidth())
        self.loggingButton.setSizePolicy(sizePolicy1)
        self.loggingButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.loggingButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/light/icons/logs_black.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.loggingButton.setIcon(icon3)
        self.loggingButton.setIconSize(QSize(24, 24))
        self.loggingButton.setCheckable(True)
        self.loggingButton.setFlat(True)

        self.pagesLayout.addWidget(self.loggingButton)

        self.plottingButton = QPushButton(self.pagesButtons)
        self.buttonGroup.addButton(self.plottingButton)
        self.plottingButton.setObjectName(u"plottingButton")
        sizePolicy1.setHeightForWidth(self.plottingButton.sizePolicy().hasHeightForWidth())
        self.plottingButton.setSizePolicy(sizePolicy1)
        self.plottingButton.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.plottingButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.plottingButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/light/icons/plot_black.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.plottingButton.setIcon(icon4)
        self.plottingButton.setCheckable(True)
        self.plottingButton.setFlat(True)

        self.pagesLayout.addWidget(self.plottingButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.pagesLayout.addItem(self.verticalSpacer)

        self.settingsButton = QPushButton(self.pagesButtons)
        self.buttonGroup.addButton(self.settingsButton)
        self.settingsButton.setObjectName(u"settingsButton")
        sizePolicy1.setHeightForWidth(self.settingsButton.sizePolicy().hasHeightForWidth())
        self.settingsButton.setSizePolicy(sizePolicy1)
        self.settingsButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u":/light/icons/settings_black.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsButton.setIcon(icon5)
        self.settingsButton.setIconSize(QSize(24, 24))
        self.settingsButton.setCheckable(True)
        self.settingsButton.setFlat(True)

        self.pagesLayout.addWidget(self.settingsButton)

        self.pagesLayout.setStretch(0, 2)
        self.pagesLayout.setStretch(1, 2)
        self.pagesLayout.setStretch(2, 2)
        self.pagesLayout.setStretch(3, 2)
        self.pagesLayout.setStretch(4, 3)
        self.pagesLayout.setStretch(5, 2)

        self.verticalLayout_3.addWidget(self.pagesButtons)

        self.themeButton = QPushButton(self.menuContainer)
        self.themeButton.setObjectName(u"themeButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.themeButton.sizePolicy().hasHeightForWidth())
        self.themeButton.setSizePolicy(sizePolicy2)
        icon6 = QIcon()
        icon6.addFile(u":/light/icons/darklight_black.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.themeButton.setIcon(icon6)
        self.themeButton.setIconSize(QSize(24, 24))
        self.themeButton.setCheckable(True)
        self.themeButton.setFlat(True)

        self.verticalLayout_3.addWidget(self.themeButton)


        self.horizontalLayout.addWidget(self.menuContainer)

        self.stackedWidgets = QStackedWidget(self.centralwidget)
        self.stackedWidgets.setObjectName(u"stackedWidgets")
        self.connectionPage = QWidget()
        self.connectionPage.setObjectName(u"connectionPage")
        self.connectionPage.setMinimumSize(QSize(648, 0))
        self.verticalLayout_4 = QVBoxLayout(self.connectionPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.lineEdit = QLineEdit(self.connectionPage)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(200, 50))
        font = QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask(u"000.000.000.000")
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.connectPlcButton = QPushButton(self.connectionPage)
        self.connectPlcButton.setObjectName(u"connectPlcButton")
        self.connectPlcButton.setMaximumSize(QSize(150, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.connectPlcButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.connectPlcButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 10)
        self.stackedWidgets.addWidget(self.connectionPage)
        self.tagsPage = QWidget()
        self.tagsPage.setObjectName(u"tagsPage")
        self.tagsPage.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.tagsPage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidgets.addWidget(self.tagsPage)
        self.plottingPage = QWidget()
        self.plottingPage.setObjectName(u"plottingPage")
        self.verticalLayout_6 = QVBoxLayout(self.plottingPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidgets.addWidget(self.plottingPage)
        self.loggingPage = QWidget()
        self.loggingPage.setObjectName(u"loggingPage")
        self.loggingPage.setMinimumSize(QSize(648, 524))
        self.verticalLayout_7 = QVBoxLayout(self.loggingPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stackedWidgets.addWidget(self.loggingPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_8 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stackedWidgets.addWidget(self.settingsPage)

        self.horizontalLayout.addWidget(self.stackedWidgets)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.mainContainer.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.mainContainer)

        self.statusBarContainer = QWidget(self.centralwidget)
        self.statusBarContainer.setObjectName(u"statusBarContainer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.statusBarContainer.sizePolicy().hasHeightForWidth())
        self.statusBarContainer.setSizePolicy(sizePolicy3)
        self.statusBarContainer.setMinimumSize(QSize(0, 30))
        self.statusBarContainer.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_3 = QHBoxLayout(self.statusBarContainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.connectionLabel = QLabel(self.statusBarContainer)
        self.connectionLabel.setObjectName(u"connectionLabel")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.connectionLabel.setFont(font2)
        self.connectionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.connectionLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 8)

        self.verticalLayout_2.addWidget(self.statusBarContainer)

        self.verticalLayout_2.setStretch(0, 15)
        self.verticalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 865, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.buttonGroup.idClicked.connect(self.stackedWidgets.setCurrentIndex)

        self.stackedWidgets.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"S7 Connector", None))
        self.connectionButton.setText(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.connectionButton.setProperty(u"class", QCoreApplication.translate("MainWindow", u"pages-buttons", None))
        self.tagsButton.setText(QCoreApplication.translate("MainWindow", u"Tags", None))
        self.tagsButton.setProperty(u"class", QCoreApplication.translate("MainWindow", u"pages-buttons", None))
        self.loggingButton.setText(QCoreApplication.translate("MainWindow", u"Logging", None))
        self.loggingButton.setProperty(u"class", QCoreApplication.translate("MainWindow", u"pages-buttons", None))
        self.plottingButton.setText(QCoreApplication.translate("MainWindow", u"Plotting", None))
        self.plottingButton.setProperty(u"class", QCoreApplication.translate("MainWindow", u"pages-buttons", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.settingsButton.setProperty(u"class", QCoreApplication.translate("MainWindow", u"pages-buttons", None))
        self.themeButton.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.themeButton.setProperty(u"class", QCoreApplication.translate("MainWindow", u"style-button", None))
        self.connectionPage.setProperty(u"class", QCoreApplication.translate("MainWindow", u"panel", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"___.___.___.___", None))
        self.connectPlcButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.tagsPage.setProperty(u"class", QCoreApplication.translate("MainWindow", u"panel", None))
        self.plottingPage.setProperty(u"class", QCoreApplication.translate("MainWindow", u"panel", None))
        self.loggingPage.setProperty(u"class", QCoreApplication.translate("MainWindow", u"panel", None))
        self.settingsPage.setProperty(u"class", QCoreApplication.translate("MainWindow", u"panel", None))
        self.connectionLabel.setText("")
        self.connectionLabel.setProperty(u"class", QCoreApplication.translate("MainWindow", u"connected-label", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

