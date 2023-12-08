
import sys
import threading
import time
import LogicaNegocio 
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QRegExp)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QValidator, QRegExpValidator




class Ui_TIR(QWidget):
    def __init__ (self):
        super(Ui_TIR, self).__init__()
        self.Btn_interes_simple = QPushButton(self)
        self.Btn_interes_simple.setObjectName(u"Btn_interes_simple")
        self.Btn_interes_simple.setGeometry(QRect(10, 10, 111, 23))
        self.Btn_interes_compuesto = QPushButton(self)
        self.Btn_interes_compuesto.setObjectName(u"Btn_interes_compuesto")
        self.Btn_interes_compuesto.setGeometry(QRect(120, 10, 111, 23))
        self.Btn_tir = QPushButton(self)
        self.Btn_tir.setObjectName(u"Btn_tir")
        self.Btn_tir.setGeometry(QRect(230, 10, 111, 23))
        self.Btn_tir.setStyleSheet(u"\n"
"            QPushButton {\n"
"                background-color: lightblue;\n"
"                border: 2px solid darkblue;\n"
"                border-radius: 5px;\n"
"                padding: 2px;\n"
"                font-family: \"MS Shell Dlg 2\";\n"
"                font-size: 8pt;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: lightblue;\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: lightblue;\n"
"                border: 2px solid darkblue;\n"
"            }\n"
"     ")
        self.Btn_gradientes = QPushButton(self)
        self.Btn_gradientes.setObjectName(u"Btn_gradientes")
        self.Btn_gradientes.setGeometry(QRect(340, 10, 111, 23))
        self.label_12 = QLabel(self)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(70, 80, 91, 16))
        self.Lne_inversion = QLineEdit(self)
        self.Lne_inversion.setObjectName(u"Lne_inversion")
        self.Lne_inversion.setGeometry(QRect(220, 80, 91, 20))
        self.Lbl_tipo_gradiente = QLabel(self)
        self.Lbl_tipo_gradiente.setObjectName(u"Lbl_tipo_gradiente")
        self.Lbl_tipo_gradiente.setGeometry(QRect(70, 120, 161, 16))
        self.Lne_dinero_por_tiempo = QLineEdit(self)
        self.Lne_dinero_por_tiempo.setObjectName(u"Lne_dinero_por_tiempo")
        self.Lne_dinero_por_tiempo.setGeometry(QRect(220, 120, 91, 20))
        self.Btn_calcular = QPushButton(self)
        self.Btn_calcular.setObjectName(u"Btn_calcular")
        self.Btn_calcular.setGeometry(QRect(70, 200, 81, 23))
        self.Lbl_tipo_gradiente_2 = QLabel(self)
        self.Lbl_tipo_gradiente_2.setObjectName(u"Lbl_tipo_gradiente_2")
        self.Lbl_tipo_gradiente_2.setGeometry(QRect(70, 160, 161, 16))
        self.Lne_TIR = QLineEdit(self)
        self.Lne_TIR.setObjectName(u"Lne_TIR")
        self.Lne_TIR.setGeometry(QRect(220, 160, 91, 20))
        self.Btn_agregar = QPushButton(self)
        self.Btn_agregar.setObjectName(u"Btn_agregar")
        self.Btn_agregar.setGeometry(QRect(320, 120, 81, 23))
        self.Lbl_respuesta_calculo = QLabel(self)
        self.Lbl_respuesta_calculo.setObjectName(u"Lbl_respuesta_calculo")
        self.Lbl_respuesta_calculo.setGeometry(QRect(40, 250, 431, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lbl_respuesta_calculo.sizePolicy().hasHeightForWidth())
        self.Lbl_respuesta_calculo.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.Lbl_respuesta_calculo.setPalette(palette)
        self.Lbl_respuesta_calculo.setMouseTracking(True)
        self.Lbl_respuesta_calculo.setTabletTracking(False)
        self.Lbl_respuesta_calculo.setFocusPolicy(Qt.NoFocus)
        self.Lbl_respuesta_calculo.setTextFormat(Qt.AutoText)
        self.Lbl_respuesta_calculo.setTextInteractionFlags(Qt.NoTextInteraction)

        self.Btn_interes_simple.setText(QCoreApplication.translate("Form", u"interes simpe", None))
        self.Btn_interes_compuesto.setText(QCoreApplication.translate("Form", u"interes compuesto", None))
        self.Btn_tir.setText(QCoreApplication.translate("Form", u"TIR", None))
        self.Btn_gradientes.setText(QCoreApplication.translate("Form", u"gradientes", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"agregar inversion", None))
        self.Lne_inversion.setText("")
        self.Lbl_tipo_gradiente.setText(QCoreApplication.translate("Form", u"dinero recibido en el tiempo", None))
        self.Lne_dinero_por_tiempo.setText("")
        self.Btn_calcular.setText(QCoreApplication.translate("Form", u"Calcular", None))
        self.Lbl_tipo_gradiente_2.setText(QCoreApplication.translate("Form", u"ingrese TIR", None))
        self.Lne_TIR.setText("")
        self.Btn_agregar.setText(QCoreApplication.translate("Form", u"agregar", None))
        self.Lbl_respuesta_calculo.setText("")
    # retranslateUi





class Ui_gradiente(QWidget):
    def __init__ (self):
        super(Ui_gradiente, self).__init__()
        self.label_13 = QLabel(self)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(130, 50, 91, 21))
        self.Lne_primera_cuota = QLineEdit(self)
        self.Lne_primera_cuota.setObjectName(u"Lne_primera_cuota")
        self.Lne_primera_cuota.setGeometry(QRect(220, 50, 91, 20))
        self.label_5 = QLabel(self)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 50, 47, 16))
        self.Btn_interes_compuesto = QPushButton(self)
        self.Btn_interes_compuesto.setObjectName(u"Btn_interes_compuesto")
        self.Btn_interes_compuesto.setGeometry(QRect(120, 10, 111, 23))
        self.Btn_interes_simple = QPushButton(self)
        self.Btn_interes_simple.setObjectName(u"Btn_interes_simple")
        self.Btn_interes_simple.setGeometry(QRect(10, 10, 111, 23))
        self.Btn_tir = QPushButton(self)
        self.Btn_tir.setObjectName(u"Btn_tir")
        self.Btn_tir.setGeometry(QRect(230, 10, 111, 23))
        self.Btn_gradientes = QPushButton(self)
        self.Btn_gradientes.setObjectName(u"Btn_gradientes")
        self.Btn_gradientes.setGeometry(QRect(340, 10, 111, 23))
        self.Btn_gradientes.setStyleSheet(u"\n"
"            QPushButton {\n"
"                background-color: lightblue;\n"
"                border: 2px solid darkblue;\n"
"                border-radius: 5px;\n"
"                padding: 2px;\n"
"                font-family: \"MS Shell Dlg 2\";\n"
"                font-size: 8pt;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: lightblue;\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: lightblue;\n"
"                border: 2px solid darkblue;\n"
"            }\n"
"     ")
        self.Cmb_tipo_aumento = QComboBox(self)
        self.Cmb_tipo_aumento.addItem("")
        self.Cmb_tipo_aumento.addItem("")
        self.Cmb_tipo_aumento.setObjectName(u"Cmb_tipo_aumento")
        self.Cmb_tipo_aumento.setGeometry(QRect(320, 140, 41, 22))
        self.Cmb_presente_futuro = QComboBox(self)
        self.Cmb_presente_futuro.addItem("")
        self.Cmb_presente_futuro.addItem("")
        self.Cmb_presente_futuro.addItem("")
        self.Cmb_presente_futuro.setObjectName(u"Cmb_presente_futuro")
        self.Cmb_presente_futuro.setGeometry(QRect(230, 200, 91, 22))
        self.Cmb_creciente_decreciente = QComboBox(self)
        self.Cmb_creciente_decreciente.addItem("")
        self.Cmb_creciente_decreciente.addItem("")
        self.Cmb_creciente_decreciente.setObjectName(u"Cmb_creciente_decreciente")
        self.Cmb_creciente_decreciente.setGeometry(QRect(230, 170, 71, 22))
        self.label_10 = QLabel(self)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(130, 80, 91, 21))
        self.Lne_taza_interes = QLineEdit(self)
        self.Lne_taza_interes.setObjectName(u"Lne_taza_interes")
        self.Lne_taza_interes.setGeometry(QRect(220, 80, 51, 20))
        self.label_4 = QLabel(self)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 80, 47, 21))
        self.label_11 = QLabel(self)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(130, 110, 81, 21))
        self.Lne_tiempo = QLineEdit(self)
        self.Lne_tiempo.setObjectName(u"Lne_tiempo")
        self.Lne_tiempo.setGeometry(QRect(220, 110, 51, 20))
        self.label_12 = QLabel(self)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(130, 140, 81, 16))
        self.Campo_aumento = QLineEdit(self)
        self.Campo_aumento.setObjectName(u"Campo_aumento")
        self.Campo_aumento.setGeometry(QRect(220, 140, 91, 20))
        self.Lbl_tipo_gradiente = QLabel(self)
        self.Lbl_tipo_gradiente.setObjectName(u"Lbl_tipo_gradiente")
        self.Lbl_tipo_gradiente.setGeometry(QRect(130, 170, 91, 16))
        self.Lbl_valor_hallar = QLabel(self)
        self.Lbl_valor_hallar.setObjectName(u"Lbl_valor_hallar")
        self.Lbl_valor_hallar.setGeometry(QRect(130, 200, 91, 16))
        self.Lbl_respuesta_calculo = QLabel(self)
        self.Lbl_respuesta_calculo.setObjectName(u"Lbl_respuesta_calculo")
        self.Lbl_respuesta_calculo.setGeometry(QRect(30, 270, 431, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lbl_respuesta_calculo.sizePolicy().hasHeightForWidth())
        self.Lbl_respuesta_calculo.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.Lbl_respuesta_calculo.setPalette(palette)
        self.Lbl_respuesta_calculo.setMouseTracking(True)
        self.Lbl_respuesta_calculo.setTabletTracking(False)
        self.Lbl_respuesta_calculo.setFocusPolicy(Qt.NoFocus)
        self.Lbl_respuesta_calculo.setTextFormat(Qt.AutoText)
        self.Lbl_respuesta_calculo.setTextInteractionFlags(Qt.NoTextInteraction)
        self.Btn_calcular = QPushButton(self)
        self.Btn_calcular.setObjectName(u"Btn_calcular")
        self.Btn_calcular.setGeometry(QRect(130, 230, 75, 23))
        self.Btn_agregar_otro = QPushButton(self)
        self.Btn_agregar_otro.setObjectName(u"Btn_agregar_otro")
        self.Btn_agregar_otro.setGeometry(QRect(220, 230, 75, 23))

        self.Cmb_tiempo = QComboBox(self)
        self.Cmb_tiempo.addItem("")
        self.Cmb_tiempo.addItem("")
        self.Cmb_tiempo.addItem("")
        self.Cmb_tiempo.addItem("")
        self.Cmb_tiempo.addItem("")
        self.Cmb_tiempo.addItem("")
        self.Cmb_tiempo.setObjectName(u"Cmb_creciente_decreciente")
        self.Cmb_tiempo.setGeometry(QRect(290, 110, 71, 22))
        self.Cmb_tiempo.setItemText(0, QCoreApplication.translate("Cmb_creciente_decreciente", u"meses", None))
        self.Cmb_tiempo.setItemText(1, QCoreApplication.translate("Cmb_creciente_decreciente", u"bimestre", None))
        self.Cmb_tiempo.setItemText(2, QCoreApplication.translate("Cmb_creciente_decreciente", u"a\u00f1os", None))
        self.Cmb_tiempo.setItemText(3, QCoreApplication.translate("Cmb_creciente_decreciente", u"trimestres", None))
        self.Cmb_tiempo.setItemText(4, QCoreApplication.translate("Cmb_creciente_decreciente", u"semestres", None))
        self.Cmb_tiempo.setItemText(5, QCoreApplication.translate("Cmb_creciente_decreciente", u"dias", None))

        

        self.Btn_interes_compuesto.setText(QCoreApplication.translate("Form", u"interes compuesto", None))
        self.Btn_interes_simple.setText(QCoreApplication.translate("Form", u"interes simpe", None))
        self.Btn_tir.setText(QCoreApplication.translate("Form", u"TIR", None))
        self.Btn_gradientes.setText(QCoreApplication.translate("Form", u"gradientes", None))
        self.Cmb_tipo_aumento.setItemText(0, QCoreApplication.translate("Form", u"%", None))
        self.Cmb_tipo_aumento.setItemText(1, QCoreApplication.translate("Form", u"$", None))

        self.Cmb_presente_futuro.setItemText(0, QCoreApplication.translate("Form", u"valor futuro", None))
        self.Cmb_presente_futuro.setItemText(1, QCoreApplication.translate("Form", u"valor presente", None))
        self.Cmb_presente_futuro.setItemText(2, QCoreApplication.translate("Form", u"valor infinito", None))

        self.Cmb_creciente_decreciente.setItemText(0, QCoreApplication.translate("Form", u"creciente", None))
        self.Cmb_creciente_decreciente.setItemText(1, QCoreApplication.translate("Form", u"decreciente", None))

        self.label_10.setText(QCoreApplication.translate("Form", u"taza de interes", None))
        self.Lne_taza_interes.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"%", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"tiempo", None))
        self.Lne_tiempo.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"aumento", None))
        self.Campo_aumento.setText("")
        self.Lbl_tipo_gradiente.setText(QCoreApplication.translate("Form", u"tipo de gradiente", None))
        self.Lbl_valor_hallar.setText(QCoreApplication.translate("Form", u"valor a hallar", None))
        self.Lbl_respuesta_calculo.setText("")
        self.Btn_calcular.setText(QCoreApplication.translate("Form", u"Calcular", None))
        self.Btn_agregar_otro.setText(QCoreApplication.translate("Form", u"agregar otro", None))

        self.label_13.setText(QCoreApplication.translate("Form", u"primera couta", None))
        self.Lne_primera_cuota.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"$", None))
    # retranslateUi








class Ui_Form_2(QWidget):
    def __init__ (self):
        super(Ui_Form_2, self).__init__()
        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 10, 111, 23))
        self.pushButton_2.setStyleSheet(u"\n"
"            QPushButton {\n"
"                background-color: lightblue;\n"
"                border: 2px solid darkblue;\n"
"                border-radius: 5px;\n"
"                padding: 2px;\n"
"                font-family: \"MS Shell Dlg 2\";\n"
"                font-size: 8pt;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: lightblue;\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: lightblue;\n"
"                border: 2px solid darkblue;\n"
"            }\n"
"     ")
        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 111, 23))
        self.pushButton_4 = QPushButton(self)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(340, 10, 111, 23))
        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(230, 10, 111, 23))
        self.label_9 = QLabel(self)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 60, 391, 20))
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 140, 41, 20))
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 110, 81, 21))
        self.label_4 = QLabel(self)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 143, 47, 13))
        self.label_5 = QLabel(self)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 113, 47, 13))
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 140, 81, 16))
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 110, 101, 20))
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 140, 111, 16))
        self.label_capitalizable = QLabel(self)
        self.label_capitalizable.setObjectName(u"label_3")
        self.label_capitalizable.setGeometry(QRect(370, 140, 111, 16))
        self.comboBox_capitalizable = QComboBox(self)
        self.comboBox_capitalizable.addItem("")
        self.comboBox_capitalizable.addItem("")
        self.comboBox_capitalizable.addItem("")
        self.comboBox_capitalizable.addItem("")
        self.comboBox_capitalizable.addItem("")
        self.comboBox_capitalizable.setObjectName(u"comboBox")
        self.comboBox_capitalizable.setGeometry(QRect(430, 140, 60, 22))
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(295, 140, 71, 22))
        self.label_6 = QLabel(self)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 170, 81, 16))
        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(120, 170, 41, 20))
        self.comboBox_2 = QComboBox(self)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(170, 170, 71, 22))
        self.label_7 = QLabel(self)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QRect(250, 170, 81, 20))
        self.comboBox_3 = QComboBox(self)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(380, 170, 71, 22))
        self.label_8 = QLabel(self)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 200, 91, 16))
        self.lineEdit_5 = QLineEdit(self)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(120, 200, 101, 20))
        self.label_10 = QLabel(self)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(230, 200, 47, 16))
        self.label_retiro = QLabel(self)
        self.label_retiro.setObjectName(u"label_retiro")
        self.label_retiro.setGeometry(QRect(20, 230, 47, 16))
        self.pushButton_5 = QPushButton(self)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 250, 75, 23))
        self.Lbl_respuesta_calculo = QLabel(self)
        self.Lbl_respuesta_calculo.setObjectName(u"Lbl_respuesta_calculo")
        self.Lbl_respuesta_calculo.setGeometry(QRect(20, 270, 431, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lbl_respuesta_calculo.sizePolicy().hasHeightForWidth())
        self.Lbl_respuesta_calculo.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.Lbl_respuesta_calculo.setPalette(palette)
        self.Lbl_respuesta_calculo.setMouseTracking(True)
        self.Lbl_respuesta_calculo.setTabletTracking(False)
        self.Lbl_respuesta_calculo.setFocusPolicy(Qt.NoFocus)
        self.Lbl_respuesta_calculo.setTextFormat(Qt.AutoText)
        self.Lbl_respuesta_calculo.setTextInteractionFlags(Qt.NoTextInteraction)
        self.lineEdit_4 = QLineEdit(self)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(330, 170, 41, 20))
        self.lineEdit_retiro = QLineEdit(self)
        self.lineEdit_retiro.setObjectName(u"lineEdit_retiro")
        self.lineEdit_retiro.setGeometry(QRect(120, 230, 101, 20))

        self.pushButton_2.setText(QCoreApplication.translate("Form_2", u"interes compuesto", None))
        self.pushButton.setText(QCoreApplication.translate("Form_2", u"interes simpe", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form_2", u"gradientes", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form_2", u"TIR", None))
        self.label_9.setText(QCoreApplication.translate("Form_2", u"tenga en cuenta; que el valor que no agregue va a ser el valor a calcular", None))
        self.lineEdit_2.setText("")
        self.setup_line_edit(self.lineEdit_2)
        self.label.setText(QCoreApplication.translate("Form_2", u"ingrese capital", None))
        self.label_4.setText(QCoreApplication.translate("Form_2", u"%", None))
        self.label_5.setText(QCoreApplication.translate("Form_2", u"$", None))
        self.label_2.setText(QCoreApplication.translate("Form_2", u"tasa de interes", None))
        self.label_capitalizable.setText(QCoreApplication.translate("Form_2", u"frecuencia", None))
        self.lineEdit.setText("")
        self.setup_line_edit(self.lineEdit)
        self.label_3.setText(QCoreApplication.translate("Form_2", u"capitalizable", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form_2", u"meses", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form_2", u"bimestre", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form_2", u"a\u00f1os", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form_2", u"trimestres", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form_2", u"semestres", None))

        self.comboBox_capitalizable.setItemText(0, QCoreApplication.translate("Form_2", u"meses", None))
        self.comboBox_capitalizable.setItemText(1, QCoreApplication.translate("Form_2", u"bimestre", None))
        self.comboBox_capitalizable.setItemText(2, QCoreApplication.translate("Form_2", u"a\u00f1os", None))
        self.comboBox_capitalizable.setItemText(3, QCoreApplication.translate("Form_2", u"trimestres", None))
        self.comboBox_capitalizable.setItemText(4, QCoreApplication.translate("Form_2", u"semestres", None))

        self.label_6.setText(QCoreApplication.translate("Form_2", u"ingrese el tiempo ", None))
        self.lineEdit_3.setText("")
        self.setup_line_edit(self.lineEdit_3)
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form_2", u"meses", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form_2", u"bimestre", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Form_2", u"a\u00f1os", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Form_2", u"trimestres", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("Form_2", u"semestres", None))

        self.label_7.setText(QCoreApplication.translate("Form_2", u"tiempo restante", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form_2", u"meses", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form_2", u"bimestre", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Form_2", u"a\u00f1os", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Form_2", u"trimestres", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("Form_2", u"semestres", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("Form_2", u"dias", None))

        self.label_8.setText(QCoreApplication.translate("Form_2", u"monto compuesto", None))
        self.label_10.setText(QCoreApplication.translate("Form_2", u"$", None))
        self.label_retiro.setText(QCoreApplication.translate("Form_2", u"retiro", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form_2", u"Calcular", None))
        self.Lbl_respuesta_calculo.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_retiro.setText("")
        self.setup_line_edit(self.lineEdit_4)
        self.setup_line_edit(self.lineEdit_5)
    
    def setup_line_edit(self, line_edit):
        # Crear un validador que acepte solo números y un punto decimal
        regex = QRegExp(r'^[0-9]+(\.[0-9]+)?$')
        validator = QRegExpValidator(regex)
    
        # Conectar el validador al QLineEdit
        line_edit.setValidator(validator)



class Ui_Form(QWidget):
    def __init__ (self):
        super(Ui_Form, self).__init__()
        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 111, 23))
        estilo = '''
            QPushButton {
                background-color: lightblue;
                border: 2px solid darkblue;
                border-radius: 5px;
                padding: 2px;
                font-family: "MS Shell Dlg 2";
                font-size: 8pt;
            }

            QPushButton:hover {
                background-color: lightblue;
            }

            QPushButton:pressed {
                background-color: lightblue;
                border: 2px solid darkblue;
            }
        '''
        self.pushButton.setStyleSheet(estilo)
        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 10, 111, 23))
        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(230, 10, 111, 23))
        self.pushButton_4 = QPushButton(self)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(340, 10, 111, 23))
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 107, 171, 21))
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 137, 161, 16))
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(190, 107, 101, 20))
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 167, 151, 16))
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(190, 137, 41, 20))
        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(190, 167, 41, 20))
        self.label_4 = QLabel(self)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 140, 47, 13))
        self.label_5 = QLabel(self)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 110, 47, 13))
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(240, 167, 71, 22))
        self.lineEdit_4 = QLineEdit(self)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(398, 167, 31, 20))
        self.label_6 = QLabel(self)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(320, 167, 81, 20))
        self.label_7 = QLabel(self)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 197, 151, 16))
        self.lineEdit_5 = QLineEdit(self)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(190, 197, 101, 20))
        self.label_8 = QLabel(self)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(300, 200, 47, 13))
        self.label_9 = QLabel(self)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 60, 391, 20))
        self.pushButton_5 = QPushButton(self)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 230, 75, 23))
        self.Lbl_respuesta_calculo = QLabel(self)
        self.Lbl_respuesta_calculo.setObjectName(u"Lbl_respuesta_calculo")
        self.Lbl_respuesta_calculo.setGeometry(QRect(20, 270, 431, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lbl_respuesta_calculo.sizePolicy().hasHeightForWidth())
        self.Lbl_respuesta_calculo.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.Lbl_respuesta_calculo.setPalette(palette)
        self.Lbl_respuesta_calculo.setMouseTracking(True)
        self.Lbl_respuesta_calculo.setTabletTracking(False)
        self.Lbl_respuesta_calculo.setFocusPolicy(Qt.NoFocus)
        self.Lbl_respuesta_calculo.setTextFormat(Qt.AutoText)
        self.Lbl_respuesta_calculo.setTextInteractionFlags(Qt.NoTextInteraction)
        self.comboBox_2 = QComboBox(self)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(435, 167, 61, 22))

        self.pushButton.setText(QCoreApplication.translate("Form", u"interes simpe", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"interes compuesto", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"TIR", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"gradientes", None))
        self.label.setText(QCoreApplication.translate("Form", u"ingrese valor inicial del prestamo", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"ingrese el porcentaje de interes ", None))
        self.lineEdit.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"ingrese el tiempo del prestamo ", None))
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"%", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"$", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"dias", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"meses", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"a\u00f1os", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"trimestres", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"semestres", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Form", u"semanas", None))

        self.label_6.setText(QCoreApplication.translate("Form", u"tiempo restante", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"valor final con intereses ", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"$", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"tenga en cuenta; que el valor que no agregue va a ser el valor a calcular", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Calcular", None))
        self.Lbl_respuesta_calculo.setText("")
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"dias", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"meses", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Form", u"a\u00f1os", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Form", u"trimestres", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("Form", u"semestres", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("Form", u"semanas", None))
        self.setup_line_edit(self.lineEdit)
        self.setup_line_edit(self.lineEdit_2)
        self.setup_line_edit(self.lineEdit_3)
        self.setup_line_edit(self.lineEdit_4)
        self.setup_line_edit(self.lineEdit_5)

    def setup_line_edit(self, line_edit):
        # Crear un validador que acepte solo números y un punto decimal
        regex = QRegExp(r'^[0-9]+(\.[0-9]+)?$')
        validator = QRegExpValidator(regex)
    
        # Conectar el validador al QLineEdit
        line_edit.setValidator(validator)
    # retranslateUi


class Ui_Pagina_principal(QWidget):
    def __init__ (self):
        super(Ui_Pagina_principal, self).__init__()
        self.pushButton_1 = QPushButton(self)
        self.pushButton_1.setObjectName(u"pushButton")
        self.pushButton_1.setGeometry(QRect(10, 120, 111, 71))
        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 120, 111, 71))
        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(250, 120, 111, 71))
        self.pushButton_4 = QPushButton(self)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(370, 120, 111, 71))

        self.pushButton_1.setText(QCoreApplication.translate("Pagina_principal", u"interes simple", None))
        self.pushButton_2.setText(QCoreApplication.translate("Pagina_principal", u"interes compuesto", None))
        self.pushButton_3.setText(QCoreApplication.translate("Pagina_principal", u"TIR", None))
        self.pushButton_4.setText(QCoreApplication.translate("Pagina_principal", u"gradientes", None))
    # retranslateUi


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.apilacion_widgets = QStackedWidget(self)
        self.pagina_principal = Ui_Pagina_principal()
        self.interes_compuesto = Ui_Form_2()
        self.interes_simple = Ui_Form()
        self.gradientes = Ui_gradiente()
        self.TIR = Ui_TIR()
        self.apilacion_widgets.addWidget(self.pagina_principal)
        self.apilacion_widgets.addWidget(self.interes_simple)
        self.apilacion_widgets.addWidget(self.interes_compuesto)
        self.apilacion_widgets.addWidget(self.gradientes)
        self.apilacion_widgets.addWidget(self.TIR)
        self.setCentralWidget(self.apilacion_widgets)
        self.apilacion_widgets.setCurrentWidget(self.pagina_principal)
        self.inicializar()

    def inicializar(self):
        self.resize (500,330)
        self.setWindowTitle("Ingenieria Economica")
        self.conexiones()
        self.interaccion_botones() 
        self.verificar_hilo = threading.Thread(target=self.verificacion_campos_interes_simple) 
        self.verificar_hilo_2 = threading.Thread(target=self.verificacion_campos_interes_compuesto)
        self.verificar_hilo_2.daemon = True
        self.verificar_hilo.daemon = True  # Hacer que el hilo sea un demonio (se detendrá cuando se cierre la aplicación)
        self.verificar_hilo_2.start()
        self.verificar_hilo.start()    

    def conexiones(self):
        self.pagina_principal.pushButton_1.clicked.connect(self.cambio_interes_simple)
        self.pagina_principal.pushButton_2.clicked.connect(self.cambio_interes_compuesto)
        self.pagina_principal.pushButton_4.clicked.connect(self.cambio_gradientes)
        self.pagina_principal.pushButton_3.clicked.connect(self.cambio_TIR)

        self.interes_simple.pushButton_2.clicked.connect(self.cambio_interes_compuesto)
        self.interes_simple.pushButton_4.clicked.connect(self.cambio_gradientes)
        self.interes_simple.pushButton_3.clicked.connect(self.cambio_TIR)

        self.interes_compuesto.pushButton.clicked.connect(self.cambio_interes_simple)
        self.interes_compuesto.pushButton_4.clicked.connect(self.cambio_gradientes)
        self.interes_compuesto.pushButton_3.clicked.connect(self.cambio_TIR)

        self.gradientes.Btn_interes_simple.clicked.connect(self.cambio_interes_simple)
        self.gradientes.Btn_interes_compuesto.clicked.connect(self.cambio_interes_compuesto)
        self.gradientes.Btn_tir.clicked.connect(self.cambio_TIR)

        self.TIR.Btn_interes_simple.clicked.connect(self.cambio_interes_simple)
        self.TIR.Btn_interes_compuesto.clicked.connect(self.cambio_interes_compuesto)
        self.TIR.Btn_gradientes.clicked.connect(self.cambio_gradientes)

    def cambio_interes_simple(self):
        self.apilacion_widgets.setCurrentWidget(self.interes_simple)

    def cambio_interes_compuesto(self):
        self.apilacion_widgets.setCurrentWidget(self.interes_compuesto)

    def cambio_gradientes(self):
        self.apilacion_widgets.setCurrentWidget(self.gradientes)

    def cambio_TIR(self):
        self.apilacion_widgets.setCurrentWidget(self.TIR)

        
    def interaccion_botones(self):
        self.dinero_por_tiempo_tir = []
        self.interes_simple.pushButton_5.clicked.connect(self.actualizacion_resultado_interes_simple)
        self.interes_compuesto.pushButton_5.clicked.connect(self.actualizacion_resultado_interes_compuesto)
        self.gradientes.Btn_calcular.clicked.connect(self.actualizacion_resultado_gradientes) 
        self.TIR.Btn_agregar.clicked.connect(self.boton_agregar)
        self.TIR.Btn_calcular.clicked.connect(self.actualizacion_resultado_TIR)

    def actualizacion_resultado_TIR(self):
        self.obtencion_datos_TIR()
        if(self.tir != 0):
            resultado, lista_resultados = self.realizar_calculos_tir()
            self.apilacion_widgets.setCurrentWidget(self.TIR.Lbl_respuesta_calculo.setText("el resultado del VAN es: " + str(resultado) +"\n" + "y esta dividido asi: "', '.join(map(str, lista_resultados))))
        else:
            resultado = self.realizar_calculos_tir()
            self.apilacion_widgets.setCurrentWidget(self.TIR.Lbl_respuesta_calculo.setText("el resultado del TIR es: " + str(resultado)))
        print(resultado)
        self.dinero_por_tiempo_tir = []
        

    def actualizacion_resultado_gradientes(self):
        self.obtencion_datos_gradientes()
        self.resultado_gradientes = self.realizar_calculos_gradientes()
        print(self.resultado_gradientes)
        self.apilacion_widgets.setCurrentWidget(self.gradientes.Lbl_respuesta_calculo.setText("el resultado es: " + str(self.resultado_gradientes)))

    def actualizacion_resultado_interes_simple(self):
        self.obtencion_datos_interes_simple()
        self.resultado = self.realizar_calculos_interes_simple()
        print(self.resultado)
        self.apilacion_widgets.setCurrentWidget(self.interes_simple.Lbl_respuesta_calculo.setText("el resultado de " + self.operacion + " es: " + str(self.resultado)))

    def actualizacion_resultado_interes_compuesto(self):
        self.obtencion_datos_interes_compuesto()
        self.resultado_interes_compuesto = self.realizar_calculos_interes_compuesto()
        print(self.resultado_interes_compuesto)
        self.apilacion_widgets.setCurrentWidget(self.interes_compuesto.Lbl_respuesta_calculo.setText("el resultado de " + self.operacion_interes_compuesto + " es: " + str(self.resultado_interes_compuesto)))
        if(self.operacion_interes_compuesto == "los intereses compuestos"):
            self.interes_compuesto.lineEdit.setText(str(self.resultado_interes_compuesto - self.retiro_interes_compuesto))
            self.interes_compuesto.lineEdit_2.setText("")
            self.interes_compuesto.lineEdit_3.setText("")
            self.interes_compuesto.lineEdit_4.setText("")
            self.interes_compuesto.lineEdit_retiro.setText("")

    def obtencion_datos_TIR(self):  
        self.inversion_tir = float(self.TIR.Lne_inversion.text())*-1
        self.tir = float(self.TIR.Lne_TIR.text())

    def boton_agregar(self):
        self.dinero_por_tiempo_tir.append(float(self.TIR.Lne_dinero_por_tiempo.text()))
        self.TIR.Lne_dinero_por_tiempo.setText("")

    def realizar_calculos_tir(self):
        self.dinero_por_tiempo_tir.insert(0, self.inversion_tir)
        calculos = LogicaNegocio.CalculadoraTIRVAN(self.dinero_por_tiempo_tir, self.tir)
        print(self.dinero_por_tiempo_tir)
        if(self.tir != 0):
            return calculos.calcular_van_verdadero()
        else:
            return calculos.calcular_tir()

    def obtencion_datos_gradientes(self):
        self.taza_interes_gradientes = float(self.gradientes.Lne_taza_interes.text())
        self.tiempo_gradientes = float(self.gradientes.Lne_tiempo.text())
        self.aumento_gradientes = float(self.gradientes.Campo_aumento.text())
        self.intervalo_tiempo_gradientes = self.gradientes.Cmb_tiempo.currentText()
        self.primera_cuota_gradiente = float(self.gradientes.Lne_primera_cuota.text())
        self.tipo_aumento_gradiente = self.gradientes.Cmb_tipo_aumento.currentText()
        self.tipo_gradiente = self.gradientes.Cmb_creciente_decreciente.currentText()
        self.valor_hallar_gradiente = self.gradientes.Cmb_presente_futuro.currentText()
           
    def realizar_calculos_gradientes(self):
        calculos_aritmeticos = LogicaNegocio.GradienteAritmetico()
        calculos_geometricos = LogicaNegocio.GradienteGeometrico()
        if(self.tipo_aumento_gradiente == "%"):
            if(self.valor_hallar_gradiente == "valor presente"):
                if(self.taza_interes_gradientes != self.aumento_gradientes):
                    return calculos_geometricos.hayar_gradiente_valor_presente_cuando_i_diferente(self.taza_interes_gradientes, self.tiempo_gradientes, 
                                                                                           self.primera_cuota_gradiente, self.aumento_gradientes,
                                                                                           self.intervalo_tiempo_gradientes)
                    
                else:
                    return calculos_geometricos.hayar_gradiente_valor_presente_cuando_i_igual(self.taza_interes_gradientes, self.tiempo_gradientes, 
                                                                                       self.primera_cuota_gradiente, self.intervalo_tiempo_gradientes)
            else:
                if(self.taza_interes_gradientes != self.aumento_gradientes):
                    return calculos_geometricos.hayar_gradiente_valor_futuro_cuando_i_diferente(self.taza_interes_gradientes, self.tiempo_gradientes, 
                                                                                           self.primera_cuota_gradiente, self.aumento_gradientes,
                                                                                           self.intervalo_tiempo_gradientes)
                else:
                    return calculos_geometricos.hayar_gradiente_valor_futuro_cuando_i_igual(self.taza_interes_gradientes, self.tiempo_gradientes, 
                                                                                       self.primera_cuota_gradiente, self.intervalo_tiempo_gradientes)
        else:
            if(self.valor_hallar_gradiente == "valor presente"):
                if(self.tipo_gradiente == "creciente"):
                    return calculos_aritmeticos.hayar_anualidad_valor_presente(self.taza_interes_gradientes, self.tiempo_gradientes, 
                                                                               self.primera_cuota_gradiente, self.intervalo_tiempo_gradientes) + calculos_aritmeticos.hayar_gradiente_valor_presente(self.taza_interes_gradientes, self.tiempo_gradientes, self.aumento_gradientes, self.intervalo_tiempo_gradientes)
                else:
                    return calculos_aritmeticos.hayar_anualidad_valor_presente(self.taza_interes_gradientes, self.tiempo_gradientes, 
                                                                               self.primera_cuota_gradiente, self.intervalo_tiempo_gradientes) - calculos_aritmeticos.hayar_gradiente_valor_presente(self.taza_interes_gradientes, self.tiempo_gradientes, self.aumento_gradientes, self.intervalo_tiempo_gradientes)
            elif(self.valor_hallar_gradiente == "valor futuro"):
                if(self.tipo_gradiente == "creciente"):
                    return calculos_aritmeticos.hayar_anualidad_valor_futuro(self.taza_interes_gradientes, self.tiempo_gradientes, 
                                                                               self.primera_cuota_gradiente, self.intervalo_tiempo_gradientes) + calculos_aritmeticos.hayar_gradiente_valor_futuro(self.taza_interes_gradientes, self.tiempo_gradientes, self.aumento_gradientes, self.intervalo_tiempo_gradientes)
                else:
                    return calculos_aritmeticos.hayar_anualidad_valor_futuro(self.taza_interes_gradientes, self.tiempo_gradientes, 
                                                                               self.primera_cuota_gradiente, self.intervalo_tiempo_gradientes) - calculos_aritmeticos.hayar_gradiente_valor_futuro(self.taza_interes_gradientes, self.tiempo_gradientes, self.aumento_gradientes, self.intervalo_tiempo_gradientes)
            elif(self.valor_hallar_gradiente == "valor infinito"): 
                if(self.tipo_gradiente == "creciente"):
                    return calculos_aritmeticos.hayar_anualidad_presente_valor_infinito(self.primera_cuota_gradiente, 
                                                                                        self.taza_interes_gradientes, self.intervalo_tiempo_gradientes) + calculos_aritmeticos.hayar_gradiente_presente_valor_infinito(self.taza_interes_gradientes, self.aumento_gradientes, self.intervalo_tiempo_gradientes)
                else:
                    return calculos_aritmeticos.hayar_anualidad_presente_valor_infinito(self.primera_cuota_gradiente, 
                                                                                        self.taza_interes_gradientes, self.intervalo_tiempo_gradientes) - calculos_aritmeticos.hayar_gradiente_presente_valor_infinito(self.taza_interes_gradientes, self.aumento_gradientes, self.intervalo_tiempo_gradientes)
                
                    

        
            


    def verificacion_campos_interes_simple(self):
        while True:
            if (self.interes_simple.lineEdit.text() == "" and self.interes_simple.lineEdit_2.text() != "" and self.interes_simple.lineEdit_3.text() != "" and self.interes_simple.lineEdit_5.text() != ""):
                self.interes_simple.lineEdit.setEnabled(False)
                self.operacion = "el capital"
            else:
                self.interes_simple.lineEdit.setEnabled(True)
            if (self.interes_simple.lineEdit.text() != "" and self.interes_simple.lineEdit_2.text() == "" and self.interes_simple.lineEdit_3.text() != "" and self.interes_simple.lineEdit_5.text() != ""):
                self.interes_simple.lineEdit_2.setEnabled(False)
                self.operacion = "la tasa de interes"
            else:
                self.interes_simple.lineEdit_2.setEnabled(True)
            if (self.interes_simple.lineEdit.text() != "" and self.interes_simple.lineEdit_2.text() != "" and self.interes_simple.lineEdit_3.text() == "" and self.interes_simple.lineEdit_5.text() != ""):
                self.interes_simple.lineEdit_3.setEnabled(False)
                self.interes_simple.comboBox.setEnabled(False)
                self.interes_simple.comboBox_2.setEnabled(False)
                self.interes_simple.lineEdit_4.setEnabled(False)
                self.operacion = "el tiempo"
            else:
                self.interes_simple.lineEdit_3.setEnabled(True)
                self.interes_simple.comboBox.setEnabled(True)
                self.interes_simple.comboBox_2.setEnabled(True)
                self.interes_simple.lineEdit_4.setEnabled(True)
            if (self.interes_simple.lineEdit.text() != "" and self.interes_simple.lineEdit_2.text() != "" and self.interes_simple.lineEdit_3.text() != "" and self.interes_simple.lineEdit_5.text() == ""):
                self.interes_simple.lineEdit_5.setEnabled(False)
                self.operacion = "los intereses"
            else:
                self.interes_simple.lineEdit_5.setEnabled(True)
            time.sleep(0.5)

    def obtencion_datos_interes_simple(self):
        if (self.interes_simple.lineEdit.text() != ""):
            self.capital_interes_simple = float(self.interes_simple.lineEdit.text())
        else:
            self.capital_interes_simple = 0

        if (self.interes_simple.lineEdit_2.text() != ""):
            self.tasa_interes = float(self.interes_simple.lineEdit_2.text())
        else:
            self.tasa_interes = 0
        
        if (self.interes_simple.lineEdit_3.text() != ""):
            self.tiempo_1 = float(self.interes_simple.lineEdit_3.text())
        else:
            self.tiempo_1 = 0
        

        if (self.interes_simple.lineEdit_4.text() != ""):
            self.tiempo_2 = float(self.interes_simple.lineEdit_4.text())
        else:
            self.tiempo_2 = 0

        self.cronograma_1 = self.interes_simple.comboBox.currentText()
        self.cronograma_2 = self.interes_simple.comboBox_2.currentText()

        if (self.interes_simple.lineEdit_5.text() != ""):
            self.intereses = float(self.interes_simple.lineEdit_5.text()) 
        else:
            self.intereses = 0
           

    def verificacion_campos_interes_simple(self):
        while True:
            if (self.interes_simple.lineEdit.text() == "" and self.interes_simple.lineEdit_2.text() != "" and self.interes_simple.lineEdit_3.text() != "" and self.interes_simple.lineEdit_5.text() != ""):
                self.interes_simple.lineEdit.setEnabled(False)
                self.operacion = "el capital"
            else:
                self.interes_simple.lineEdit.setEnabled(True)
            if (self.interes_simple.lineEdit.text() != "" and self.interes_simple.lineEdit_2.text() == "" and self.interes_simple.lineEdit_3.text() != "" and self.interes_simple.lineEdit_5.text() != ""):
                self.interes_simple.lineEdit_2.setEnabled(False)
                self.operacion = "la tasa de interes"
            else:
                self.interes_simple.lineEdit_2.setEnabled(True)
            if (self.interes_simple.lineEdit.text() != "" and self.interes_simple.lineEdit_2.text() != "" and self.interes_simple.lineEdit_3.text() == "" and self.interes_simple.lineEdit_5.text() != ""):
                self.interes_simple.lineEdit_3.setEnabled(False)
                self.interes_simple.comboBox.setEnabled(False)
                self.interes_simple.comboBox_2.setEnabled(False)
                self.interes_simple.lineEdit_4.setEnabled(False)
                self.operacion = "el tiempo"
            else:
                self.interes_simple.lineEdit_3.setEnabled(True)
                self.interes_simple.comboBox.setEnabled(True)
                self.interes_simple.comboBox_2.setEnabled(True)
                self.interes_simple.lineEdit_4.setEnabled(True)
            if (self.interes_simple.lineEdit.text() != "" and self.interes_simple.lineEdit_2.text() != "" and self.interes_simple.lineEdit_3.text() != "" and self.interes_simple.lineEdit_5.text() == ""):
                self.interes_simple.lineEdit_5.setEnabled(False)
                self.operacion = "los intereses"
            else:
                self.interes_simple.lineEdit_5.setEnabled(True)
            time.sleep(0.5)
    
    def realizar_calculos_interes_simple(self):  
        calculos = LogicaNegocio.InteresSimple()
        if (self.operacion == "el capital"):
            return calculos.hallar_valor_inicial(interes_porcentual = self.tasa_interes, valor_final = self.intereses, tiempo_deuda = self.tiempo_1, intervalo_tiempo = self.cronograma_1, tiempo_deuda_2 = self.tiempo_2, intervalo_tiempo_2 = self.cronograma_2)
        if (self.operacion == "la tasa de interes"):
            return calculos.hallar_interes(valor_inicial_deuda= self.capital_interes_simple, valor_final = self.intereses, tiempo_deuda = self.tiempo_1, intervalo_tiempo = self.cronograma_1, tiempo_deuda_2 = self.tiempo_2, intervalo_tiempo_2 = self.cronograma_2)
        if (self.operacion == "el tiempo"):
            return calculos.hallar_tiempo(valor_inicial_deuda= self.capital_interes_simple, valor_final = self.intereses, interes_porcentual = self.tasa_interes)
        if (self.operacion == "los intereses"):
            return calculos.hallar_valor_final(interes_porcentual = self.tasa_interes, valor_inicial_deuda = self.capital_interes_simple, tiempo_deuda = self.tiempo_1, intervalo_tiempo = self.cronograma_1, tiempo_deuda_2 = self.tiempo_2, intervalo_tiempo_2 = self.cronograma_2)

    def verificacion_campos_interes_compuesto(self):
        while True:
            if (self.interes_compuesto.lineEdit.text() == "" and self.interes_compuesto.lineEdit_2.text() != "" and self.interes_compuesto.lineEdit_3.text() != "" and self.interes_compuesto.lineEdit_5.text() != ""):
                self.interes_compuesto.lineEdit.setEnabled(False)
                self.operacion_interes_compuesto = "el capital"
            else:
                self.interes_compuesto.lineEdit.setEnabled(True)
            if (self.interes_compuesto.lineEdit.text() != "" and self.interes_compuesto.lineEdit_2.text() == "" and self.interes_compuesto.lineEdit_3.text() != "" and self.interes_compuesto.lineEdit_5.text() != ""):
                self.interes_compuesto.lineEdit_2.setEnabled(False)
                self.interes_compuesto.comboBox.setEnabled(False)
                self.operacion_interes_compuesto = "la tasa de interes"
            else:
                self.interes_compuesto.lineEdit_2.setEnabled(True)
                self.interes_compuesto.comboBox.setEnabled(True)
            if (self.interes_compuesto.lineEdit.text() != "" and self.interes_compuesto.lineEdit_2.text() != "" and self.interes_compuesto.lineEdit_3.text() == "" and self.interes_compuesto.lineEdit_5.text() != ""):
                self.interes_compuesto.lineEdit_3.setEnabled(False)
                self.interes_compuesto.comboBox_3.setEnabled(False)
                self.interes_compuesto.comboBox_2.setEnabled(False)
                self.interes_compuesto.lineEdit_4.setEnabled(False)
                self.operacion_interes_compuesto = "el tiempo"
            else:
                self.interes_compuesto.lineEdit_3.setEnabled(True)
                self.interes_compuesto.comboBox_3.setEnabled(True)
                self.interes_compuesto.comboBox_2.setEnabled(True)
                self.interes_compuesto.lineEdit_4.setEnabled(True)
            if (self.interes_compuesto.lineEdit.text() != "" and self.interes_compuesto.lineEdit_2.text() != "" and self.interes_compuesto.lineEdit_3.text() != "" and self.interes_compuesto.lineEdit_5.text() == ""):
                self.interes_compuesto.lineEdit_5.setEnabled(False)
                self.operacion_interes_compuesto = "los intereses compuestos"
            else:
                self.interes_compuesto.lineEdit_5.setEnabled(True)
            time.sleep(0.5)

    def obtencion_datos_interes_compuesto(self):
        if (self.interes_compuesto.lineEdit_retiro.text() != ""):
            self.retiro_interes_compuesto = float(self.interes_compuesto.lineEdit_retiro.text())
        else:
            self.retiro_interes_compuesto = 0
        if (self.interes_compuesto.lineEdit.text() != ""):
            self.capital_interes_compuesto= float(self.interes_compuesto.lineEdit.text())
        else:
            self.capital_interes_compuesto = 0

        if (self.interes_compuesto.lineEdit_2.text() != ""):
            self.tasa_interes_interes_compuesto = float(self.interes_compuesto.lineEdit_2.text())
        else:
            self.tasa_interes_interes_compuesto = 0
        
        if (self.interes_compuesto.lineEdit_3.text() != ""):
            self.tiempo_1_interes_compuesto = float(self.interes_compuesto.lineEdit_3.text())
        else:
            self.tiempo_1_interes_compuesto = 0
        

        if (self.interes_compuesto.lineEdit_4.text() != ""):
            self.tiempo_2_interes_compuesto = float(self.interes_compuesto.lineEdit_4.text())
        else:
            self.tiempo_2_interes_compuesto = 0

        self.frecuencia_capitalizacion_interes_com = self.interes_compuesto.comboBox_capitalizable.currentText()
        self.frecuencia_interes_compuesto = self.interes_compuesto.comboBox.currentText()
        self.cronograma_2_interes_compuesto = self.interes_compuesto.comboBox_3.currentText()
        self.cronograma_1_interes_compuesto = self.interes_compuesto.comboBox_2.currentText()

        if (self.interes_compuesto.lineEdit_5.text() != ""):
            self.intereses_interes_compuesto = float(self.interes_compuesto.lineEdit_5.text()) 
        else:
            self.intereses_interes_compuesto = 0 
    
    def realizar_calculos_interes_compuesto(self):  
        calculos_interes_compuesto = LogicaNegocio.InteresCompuesto()
        if (self.operacion_interes_compuesto == "el capital"):
            return calculos_interes_compuesto.hallar_capital(tasa_interes = self.tasa_interes_interes_compuesto, 
                                                             monto_compuesto = self.intereses_interes_compuesto, 
                                                             frecuencia = self.frecuencia_interes_compuesto, 
                                                             tiempo_1 = self.tiempo_1_interes_compuesto, 
                                                             cronograma_1 = self.cronograma_1_interes_compuesto, 
                                                             tiempo_2 = self.tiempo_2_interes_compuesto, 
                                                             cronograma_2 = self.cronograma_2_interes_compuesto)
        if (self.operacion_interes_compuesto == "la tasa de interes"):
            return calculos_interes_compuesto.hallar_tasa_interes(capital = self.capital_interes_compuesto, 
                                                                  monto_compuesto = self.intereses_interes_compuesto, 
                                                                  frecuencia = self.frecuencia_interes_compuesto, 
                                                                  tiempo_1 = self.tiempo_1_interes_compuesto, 
                                                                  cronograma_1 = self.cronograma_1_interes_compuesto, 
                                                                  tiempo_2 = self.tiempo_2_interes_compuesto, 
                                                                  cronograma_2 = self.cronograma_2_interes_compuesto)
        if (self.operacion_interes_compuesto == "el tiempo"):
            return calculos_interes_compuesto.hallar_tiempo(capital = self.capital_interes_compuesto, 
                                                            monto_compuesto = self.intereses_interes_compuesto, 
                                                            tasa_interes = self.tasa_interes_interes_compuesto,
                                                            frecuencia = self.frecuencia_interes_compuesto)
        if (self.operacion_interes_compuesto == "los intereses compuestos"):
            if (self.frecuencia_interes_compuesto == "a\u00f1os"):
                return calculos_interes_compuesto.hallar_monto_compuesto_caso_2(capital = self.capital_interes_compuesto, 
                                                                        tasa_interes = self.tasa_interes_interes_compuesto, 
                                                                        frecuencia = self.frecuencia_interes_compuesto, 
                                                                        tiempo_1 = self.tiempo_1_interes_compuesto, 
                                                                        cronograma_1 = self.cronograma_1_interes_compuesto, 
                                                                        tiempo_2 = self.tiempo_2_interes_compuesto, 
                                                                        cronograma_2 = self.cronograma_2_interes_compuesto,
                                                                        tiempo_capitalizable = self.frecuencia_capitalizacion_interes_com)
            else:
                return calculos_interes_compuesto.hallar_monto_compuesto(capital = self.capital_interes_compuesto, 
                                                                        tasa_interes = self.tasa_interes_interes_compuesto, 
                                                                        frecuencia = self.frecuencia_interes_compuesto, 
                                                                        tiempo_1 = self.tiempo_1_interes_compuesto, 
                                                                        cronograma_1 = self.cronograma_1_interes_compuesto, 
                                                                        tiempo_2 = self.tiempo_2_interes_compuesto, 
                                                                        cronograma_2 = self.cronograma_2_interes_compuesto,
                                                                        tiempo_capitalizable = self.frecuencia_capitalizacion_interes_com)
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

    



