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
        self.editPlayerWidgetSetup()
        self.updateStatsWidgetSetup()


# Add player ------------------------------------------------------
    def AddPlayerWidgetSetup(self):
        self.firstNameLineEditAddPlayerTab = self.findChild(QLineEdit, 'firstNameLineEditAddPlayerTab')
        self.lastNameLineEditAddPlayerTab = self.findChild(QLineEdit, 'lastNameLineEditAddPlayerTab')
        self.positionLineEditAddPlayerTab = self.findChild(QLineEdit, 'positionLineEditAddPlayerTab')
        self.numberLineEditAddPlayerTab = self.findChild(QLineEdit, 'numberLineEditAddPlayerTab')
        self.countryLineEditAddPlayerTab = self.findChild(QLineEdit, 'countryLineEditAddPlayerTab')
        self.addPlayerButtonAddPlayerTab = self.findChild(QPushButton, 'addPlayerButtonAddPlayerTab')
        self.addPlayerButtonAddPlayerTab.clicked.connect(self.addPlayerButtonAddPlayerTabClickHandler)


    def addPlayerButtonAddPlayerTabClickHandler(self):
        player_fname = self.firstNameLineEditAddPlayerTab.text()
        player_lname = self.lastNameLineEditAddPlayerTab.text()
        postion = self.positionLineEditAddPlayerTab.text()
        number = self.numberLineEditAddPlayerTab.text()
        country = self.countryLineEditAddPlayerTab.text()
        addToPlayer(player_fname, player_lname, postion, number, country)
        addToStats(player_lname)

# Edit Player ------------------------------------------------------
    def editPlayerWidgetSetup(self):
        self.nameComboBoxEditPlayerTab = self.findChild(QComboBox, 'nameComboBoxEditPlayerTab')
        self.idNameLineEditEditPlayerTab = self.findChild(QLineEdit, 'idNameLineEditEditPlayerTab')
        self.postionLineEditEditPLayerTab = self.findChild(QLineEdit, 'postionLineEditEditPLayerTab')
        self.numberLineEditEditPlayerTab = self.findChild(QLineEdit, 'numberLineEditEditPlayerTab')
        self.countryLineEditEditPlayerTab = self.findChild(QLineEdit, 'countryLineEditEditPlayerTab')
        self.firstNameLineEditPlayerTab = self.findChild(QLineEdit, 'firstNameLineEditPlayerTab')
        self.lastNameLineEditEditPlayerTab = self.findChild(QLineEdit, 'lastNameLineEditEditPlayerTab')
        self.removePlayerEditPlayerTabButton = self.findChild(QPushButton, 'removePlayerEditPlayerTabButton')
        self.saveChangesButton = self.findChild(QPushButton, 'saveChangesButton')
        self.saveChangesButton.clicked.connect(self.saveChangesButtonClickHandler)
        self.removePlayerEditPlayerTabButton.clicked.connect(self.removePlayerEditPlayerTabButtonClickHandler)
        players = getplayers()
        for row in players:
            self.nameComboBoxEditPlayerTab.addItem(str(row[2]), userData=[row[0], row[1], row[2], row[3], row[4], row[5]])
        self.nameComboBoxEditPlayerTab.currentIndexChanged.connect(self.nameComboBoxEditPlayerTabCurrentIndexHandler)


    def nameComboBoxEditPlayerTabCurrentIndexHandler(self):
        try:
            row = self.nameComboBoxEditPlayerTab.currentData()
            self.idNameLineEditEditPlayerTab.setText(str(row[0]))
            self.firstNameLineEditPlayerTab.setText(row[1])
            self.lastNameLineEditEditPlayerTab.setText(row[2])
            self.postionLineEditEditPLayerTab.setText(row[3])
            self.numberLineEditEditPlayerTab.setText(row[4])
            self.countryLineEditEditPlayerTab.setText(row[5])
        except Exception as e:
            print(e)


    def saveChangesButtonClickHandler(self):
        id = self.idNameLineEditEditPlayerTab.text()
        fname = self.firstNameLineEditPlayerTab.text()
        lname = self.lastNameLineEditEditPlayerTab.text()
        position = self.postionLineEditEditPLayerTab.text()
        number = self.numberLineEditEditPlayerTab.text()
        country = self.countryLineEditEditPlayerTab.text()
        updateplayer(id, fname, lname, position, number, country)

    def removePlayerEditPlayerTabButtonClickHandler(self):
        id = self.idNameLineEditEditPlayerTab.text()
        deleteFromStats(id)
        deleteFromPlayer(id)


# Update Stats -----------------------------------------------------

    def updateStatsWidgetSetup(self):
        self.nameComboBoxUpdateStatsTab = self.findChild(QComboBox, 'nameComboBoxUpdateStatsTab')
        self.goalsLineEditUpdateStatsTab = self.findChild(QLineEdit, 'goalsLineEditUpdateStatsTab')
        self.AssistsLineEditUpdateStatsTab = self.findChild(QLineEdit, 'AssistsLineEditUpdateStatsTab')
        self.pointsLineEditUpdateStatsTab = self.findChild(QLineEdit, 'pointsLineEditUpdateStatsTab')
        self.idLineEditUpdateStatsTab = self.findChild(QLineEdit, 'idLineEditUpdateStatsTab')
        self.updateButtonEditStatsTab = self.findChild(QPushButton, 'updateButtonEditStatsTab')
        self.updateButtonEditStatsTab.clicked.connect(self.updateButtonEditStatsTabClickHandler)
        stats = getStats()
        for row in stats:
            self.nameComboBoxUpdateStatsTab.addItem(str(row[1]), userData=[row[0], row[1], row[2], row[3], row[4]])
        self.nameComboBoxUpdateStatsTab.currentIndexChanged.connect(self.nameComboBoxUpdateStatsTabCurrentIndexHandler)

    def nameComboBoxUpdateStatsTabCurrentIndexHandler(self):
        try:
            row = self.nameComboBoxUpdateStatsTab.currentData()
            self.idLineEditUpdateStatsTab.setText(str(row[0]))
            self.goalsLineEditUpdateStatsTab.setText(row[2])
            self.AssistsLineEditUpdateStatsTab.setText(row[3])
            self.pointsLineEditUpdateStatsTab.setText(row[4])
        except Exception as e:
            print(e)


    def updateButtonEditStatsTabClickHandler(self):
        id = self.idLineEditUpdateStatsTab.text()
        goals = self.goalsLineEditUpdateStatsTab.text()
        assists = self.AssistsLineEditUpdateStatsTab.text()
        points = self.pointsLineEditUpdateStatsTab.text()
        updateStats(id, goals, assists, points)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()