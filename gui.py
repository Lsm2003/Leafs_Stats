from controller import *
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        uic.loadUi('Leafs.ui', self)
        self.AddPlayerWidgetSetup()



    def AddPlayerWidgetSetup(self):
        self.firstNameLineEditAddPlayerTab = self.findChild(QLineEdit, 'firstNameLineEditAddPlayerTab')
        self.lastNameLineEditAddPlayerTab = self.findChild(QLineEdit, 'lastNameLineEditAddPlayerTab')
        self.positionLineEditAddCustomerTab = self.findChild(QLineEdit, 'positionLineEditAddCustomerTab')
        self.numberLineEditAddCustomerTab = self.findChild(QLineEdit, 'numberLineEditAddCustomerTab')
        self.countryLineEditAddCustomerTab = self.findChild(QLineEdit, 'countryLineEditAddCustomerTab')
        self.addPlayerButtonAddCustomerTab = self.findChild(QPushButton, 'addPlayerButtonAddCustomerTab')


    def addPlayerButtonAddCustomerTabClickHandler(self):
        player_fname = self.firstNameLineEditAddPlayerTab.text()
        player_lname = self.lastNameLineEditAddPlayerTab.text()
        postion = self.positionLineEditAddCustomerTab.text()
        number = self.numberLineEditAddCustomerTab.text()
        country = self.countryLineEditAddCustomerTab.text()
        addplayer(player_lname, player_fname, postion, number, country)