# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Zone_de_bataille.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Zone_de_bataille(object):
    def setupUi(self, Zone_de_bataille):
        Zone_de_bataille.setObjectName("Zone_de_bataille")
        Zone_de_bataille.resize(1033, 580)
        Zone_de_bataille.setMinimumSize(QtCore.QSize(1033, 580))
        Zone_de_bataille.setMaximumSize(QtCore.QSize(1033, 3000))
        self.Ensemble_bataille = QtWidgets.QGroupBox(Zone_de_bataille)
        self.Ensemble_bataille.setGeometry(QtCore.QRect(-40, -30, 1091, 621))
        self.Ensemble_bataille.setTitle("")
        self.Ensemble_bataille.setObjectName("Ensemble_bataille")
        self.Arene = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Arene.setGeometry(QtCore.QRect(30, 10, 1111, 621))
        self.Arene.setText("")
        self.Arene.setPixmap(QtGui.QPixmap("../Images/Arene.png"))
        self.Arene.setScaledContents(True)
        self.Arene.setObjectName("Arene")
        self.Arriere = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Arriere.setGeometry(QtCore.QRect(30, -50, 851, 531))
        self.Arriere.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.Arriere.setText("")
        self.Arriere.setObjectName("Arriere")
        self.Hopital_1 = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Hopital_1.setGeometry(QtCore.QRect(110, 440, 161, 191))
        self.Hopital_1.setText("")
        self.Hopital_1.setPixmap(QtGui.QPixmap("../Images/Hopital.png"))
        self.Hopital_1.setScaledContents(True)
        self.Hopital_1.setObjectName("Hopital_1")
        self.Hopital_2 = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Hopital_2.setGeometry(QtCore.QRect(430, 440, 161, 191))
        self.Hopital_2.setText("")
        self.Hopital_2.setPixmap(QtGui.QPixmap("../Images/Hopital.png"))
        self.Hopital_2.setScaledContents(True)
        self.Hopital_2.setObjectName("Hopital_2")
        self.Hopital_3 = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Hopital_3.setGeometry(QtCore.QRect(750, 440, 161, 191))
        self.Hopital_3.setText("")
        self.Hopital_3.setPixmap(QtGui.QPixmap("../Images/Hopital.png"))
        self.Hopital_3.setScaledContents(True)
        self.Hopital_3.setObjectName("Hopital_3")
        self.Pokemon_KO_1 = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Pokemon_KO_1.setGeometry(QtCore.QRect(280, 460, 141, 131))
        self.Pokemon_KO_1.setText("")
        self.Pokemon_KO_1.setScaledContents(True)
        self.Pokemon_KO_1.setObjectName("Pokemon_KO_1")
        self.Pokemon_KO_2 = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Pokemon_KO_2.setGeometry(QtCore.QRect(580, 460, 151, 131))
        self.Pokemon_KO_2.setText("")
        self.Pokemon_KO_2.setScaledContents(True)
        self.Pokemon_KO_2.setObjectName("Pokemon_KO_2")
        self.Pokemon_KO_3 = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Pokemon_KO_3.setGeometry(QtCore.QRect(890, 460, 141, 131))
        self.Pokemon_KO_3.setText("")
        self.Pokemon_KO_3.setScaledContents(True)
        self.Pokemon_KO_3.setObjectName("Pokemon_KO_3")
        self.Pokemon_attaquant = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Pokemon_attaquant.setGeometry(QtCore.QRect(278, 280, 181, 171))
        self.Pokemon_attaquant.setText("")
        self.Pokemon_attaquant.setScaledContents(True)
        self.Pokemon_attaquant.setObjectName("Pokemon_attaquant")
        self.Adversaire = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Adversaire.setGeometry(QtCore.QRect(740, 270, 161, 181))
        self.Adversaire.setText("")
        self.Adversaire.setScaledContents(True)
        self.Adversaire.setObjectName("Adversaire")
        self.Joueur = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Joueur.setGeometry(QtCore.QRect(-10, 220, 301, 221))
        self.Joueur.setText("")
        self.Joueur.setPixmap(QtGui.QPixmap("../Images/masculin.png"))
        self.Joueur.setScaledContents(True)
        self.Joueur.setObjectName("Joueur")
        self.Echange = QtWidgets.QPushButton(self.Ensemble_bataille)
        self.Echange.setGeometry(QtCore.QRect(540, 30, 91, 81))
        self.Echange.setStyleSheet("background-color: \"transparent\";")
        self.Echange.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/Echange.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Echange.setIcon(icon)
        self.Echange.setIconSize(QtCore.QSize(120, 120))
        self.Echange.setObjectName("Echange")
        self.Neutre = QtWidgets.QPushButton(self.Ensemble_bataille)
        self.Neutre.setEnabled(True)
        self.Neutre.setGeometry(QtCore.QRect(660, 60, 111, 101))
        self.Neutre.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Images/Neutre.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Neutre.setIcon(icon1)
        self.Neutre.setIconSize(QtCore.QSize(150, 100))
        self.Neutre.setObjectName("Neutre")
        self.Fuir = QtWidgets.QPushButton(self.Ensemble_bataille)
        self.Fuir.setGeometry(QtCore.QRect(540, 120, 91, 91))
        self.Fuir.setStyleSheet("background-color: \"transparent\";")
        self.Fuir.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Images/Exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Fuir.setIcon(icon2)
        self.Fuir.setIconSize(QtCore.QSize(120, 120))
        self.Fuir.setObjectName("Fuir")
        self.Type1 = QtWidgets.QPushButton(self.Ensemble_bataille)
        self.Type1.setGeometry(QtCore.QRect(800, 60, 101, 101))
        self.Type1.setMinimumSize(QtCore.QSize(0, 0))
        self.Type1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Type1.setText("")
        self.Type1.setIconSize(QtCore.QSize(150, 100))
        self.Type1.setObjectName("Type1")
        self.Type2 = QtWidgets.QPushButton(self.Ensemble_bataille)
        self.Type2.setGeometry(QtCore.QRect(930, 60, 101, 101))
        self.Type2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Type2.setText("")
        self.Type2.setIconSize(QtCore.QSize(150, 100))
        self.Type2.setObjectName("Type2")
        self.PV_adversaire = QtWidgets.QLabel(self.Ensemble_bataille)
        self.PV_adversaire.setGeometry(QtCore.QRect(800, 255, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PV_adversaire.setFont(font)
        self.PV_adversaire.setText("")
        self.PV_adversaire.setAlignment(QtCore.Qt.AlignCenter)
        self.PV_adversaire.setObjectName("PV_adversaire")
        self.PV_attaquant = QtWidgets.QLabel(self.Ensemble_bataille)
        self.PV_attaquant.setGeometry(QtCore.QRect(284, 255, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PV_attaquant.setFont(font)
        self.PV_attaquant.setText("")
        self.PV_attaquant.setAlignment(QtCore.Qt.AlignCenter)
        self.PV_attaquant.setObjectName("PV_attaquant")
        self.Pokemon_1 = QtWidgets.QPushButton(self.Ensemble_bataille)
        self.Pokemon_1.setGeometry(QtCore.QRect(50, 30, 141, 161))
        self.Pokemon_1.setStyleSheet("background-color: \"transparent\";")
        self.Pokemon_1.setText("")
        self.Pokemon_1.setIconSize(QtCore.QSize(150, 140))
        self.Pokemon_1.setObjectName("Pokemon_1")
        self.Pokemon_2 = QtWidgets.QPushButton(self.Ensemble_bataille)
        self.Pokemon_2.setGeometry(QtCore.QRect(200, 30, 161, 161))
        self.Pokemon_2.setStyleSheet("background-color: \"transparent\";")
        self.Pokemon_2.setText("")
        self.Pokemon_2.setIconSize(QtCore.QSize(150, 140))
        self.Pokemon_2.setObjectName("Pokemon_2")
        self.Pokemon_3 = QtWidgets.QPushButton(self.Ensemble_bataille)
        self.Pokemon_3.setEnabled(True)
        self.Pokemon_3.setGeometry(QtCore.QRect(390, 30, 141, 161))
        self.Pokemon_3.setStyleSheet("background-color: \"transparent\";")
        self.Pokemon_3.setText("")
        self.Pokemon_3.setIconSize(QtCore.QSize(150, 140))
        self.Pokemon_3.setObjectName("Pokemon_3")
        self.Type1_adversaire = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Type1_adversaire.setGeometry(QtCore.QRect(940, 340, 61, 81))
        self.Type1_adversaire.setText("")
        self.Type1_adversaire.setScaledContents(True)
        self.Type1_adversaire.setObjectName("Type1_adversaire")
        self.Type2_adversaire = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Type2_adversaire.setGeometry(QtCore.QRect(940, 250, 61, 81))
        self.Type2_adversaire.setText("")
        self.Type2_adversaire.setScaledContents(True)
        self.Type2_adversaire.setObjectName("Type2_adversaire")
        self.Nom_attaquant = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Nom_attaquant.setGeometry(QtCore.QRect(294, 220, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Nom_attaquant.setFont(font)
        self.Nom_attaquant.setStyleSheet("color: rgb(255, 255, 255);")
        self.Nom_attaquant.setText("")
        self.Nom_attaquant.setObjectName("Nom_attaquant")
        self.Nom_adversaire = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Nom_adversaire.setGeometry(QtCore.QRect(720, 220, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Nom_adversaire.setFont(font)
        self.Nom_adversaire.setStyleSheet("color: rgb(255, 255, 255);")
        self.Nom_adversaire.setText("")
        self.Nom_adversaire.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Nom_adversaire.setObjectName("Nom_adversaire")
        self.Degats_adversaire = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Degats_adversaire.setGeometry(QtCore.QRect(220, 260, 241, 221))
        self.Degats_adversaire.setText("")
        self.Degats_adversaire.setScaledContents(True)
        self.Degats_adversaire.setObjectName("Degats_adversaire")
        self.Degats = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Degats.setGeometry(QtCore.QRect(430, 190, 291, 151))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Degats.setFont(font)
        self.Degats.setStyleSheet("color: rgb(255, 255, 255);")
        self.Degats.setText("")
        self.Degats.setAlignment(QtCore.Qt.AlignCenter)
        self.Degats.setObjectName("Degats")
        self.Degats_attaquant = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Degats_attaquant.setGeometry(QtCore.QRect(680, 250, 241, 221))
        self.Degats_attaquant.setText("")
        self.Degats_attaquant.setScaledContents(True)
        self.Degats_attaquant.setObjectName("Degats_attaquant")
        self.Arriere.raise_()
        self.Arene.raise_()
        self.Hopital_1.raise_()
        self.Hopital_2.raise_()
        self.Hopital_3.raise_()
        self.Pokemon_KO_1.raise_()
        self.Pokemon_KO_2.raise_()
        self.Pokemon_KO_3.raise_()
        self.Pokemon_attaquant.raise_()
        self.Adversaire.raise_()
        self.Joueur.raise_()
        self.Echange.raise_()
        self.Neutre.raise_()
        self.Fuir.raise_()
        self.Type1.raise_()
        self.Type2.raise_()
        self.PV_adversaire.raise_()
        self.PV_attaquant.raise_()
        self.Pokemon_1.raise_()
        self.Pokemon_2.raise_()
        self.Pokemon_3.raise_()
        self.Type1_adversaire.raise_()
        self.Type2_adversaire.raise_()
        self.Nom_attaquant.raise_()
        self.Nom_adversaire.raise_()
        self.Degats_adversaire.raise_()
        self.Degats.raise_()
        self.Degats_attaquant.raise_()

        self.retranslateUi(Zone_de_bataille)
        QtCore.QMetaObject.connectSlotsByName(Zone_de_bataille)

    def retranslateUi(self, Zone_de_bataille):
        _translate = QtCore.QCoreApplication.translate
        Zone_de_bataille.setWindowTitle(_translate("Zone_de_bataille", "Dialog"))
        Zone_de_bataille.setWindowTitle(_translate("Player_profil", "  POKEMON"))
        Zone_de_bataille.setWindowIcon(QtGui.QIcon("../Images/Pokemon_logo.png"))
