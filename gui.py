from controller import *
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Leafs.ui', self)
        self.AddPlayerWidgetSetup()


# Add player ------------------------------------------------------
    def AddPlayerWidgetSetup(self):
        self.firstNameLineEditAddPlayerTab = self.findChild(QLineEdit, 'firstNameLineEditAddPlayerTab')
        self.lastNameLineEditAddPlayerTab = self.findChild(QLineEdit, 'lastNameLineEditAddPlayerTab')
        self.positionLineEditAddPlayerTab = self.findChild(QLineEdit, 'positionLineEditAddPlayerTab')
        self.numberLineEditAddPlayerTab = self.findChild(QLineEdit, 'numberLineEditAddPlayerTab')
        self.countryLineEditAddPlayerTab = self.findChild(QLineEdit, 'countryLineEditAddPlayerTab')
        self.addPlayerButtonAddPlayerTab = self.findChild(QPushButton, 'addPlayerButtonAddPlayerTab')


    def addPlayerButtonAddPlayerTabClickHandler(self):
        player_fname = self.firstNameLineEditAddPlayerTab.text()
        player_lname = self.lastNameLineEditAddPlayerTab.text()
        postion = self.positionLineEditAddPlayerTab.text()
        number = self.numberLineEditAddPlayerTab.text()
        country = self.countryLineEditAddPlayerTab.text()
        addplayer(player_lname, player_fname, postion, number, country)

# Edit Player ------------------------------------------------------
    def editPlayerWidgetSetup(self):
        self.nameComboBoxEditPlayerTab = self.findChild(QComboBox, 'nameComboBoxEditPlayerTab')
        self.idNameLineEditEditPlayerTab = self.findChild(QLineEdit, 'idNameLineEditEditPlayerTab')
        self.postionLineEditEditPLayerTab = self.findChild(QLineEdit, 'postionLineEditEditPLayerTab')
        self.numberLineEditEditPlayerTab = self.findChild(QLineEdit, 'numberLineEditEditPlayerTab')
        self.countryLineEditEditPlayerTab = self.findChild(QLineEdit, 'countryLineEditEditPlayerTab')
        self.firstNameLineEditPlayerTab = self.findChild(QLineEdit, 'firstNameLineEditPlayerTab')
        self.lastNameLineEditEditPlayerTab = self.findChild(QLineEdit, 'lastNameLineEditEditPlayerTab')
        self.saveChangesButton = self.findChild(QPushButton, 'saveChangesButton')
        players = getplayers()
        self.idNameLineEditEditPlayerTab.setText(str(players[0][0]))
        self.postionLineEditEditPLayerTab.setText(players[0][4])
        self.numberLineEditEditPlayerTab.setText(players[0][5])
        self.countryLineEditEditPlayerTab.setText(players[0][6])
        self.firstNameLineEditPlayerTab.setText(players[0][2])
        self.lastNameLineEditEditPlayerTab.setText(players[0][3])

        for row in players:
            self.nameComboBoxEditPlayerTab.addItem(str(row[1]), userData=[row[1], row[0], row[2], row[3], row[4], row[5], row[6]])
        self.nameComboBoxEditPlayerTab.currentIndexChanged.connect(self.nameComboBoxEditPlayerTabCurrentIndexHandler)


    def nameComboBoxEditPlayerTabCurrentIndexHandler(self):
        try:
            row = self.nameComboBoxEditPlayerTab.currentData()
            self.idNameLineEditEditPlayerTab.setText(str(row[0]))
            self.lastNameLineEditEditPlayerTab.setText(row[1])

        except Exception as e:
            print(e)


