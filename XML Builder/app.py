# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from fileinput import filename
import queue
from textwrap import indent
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
import subprocess
from functools import partial


"""
Generamos las variables de las etiquetas del archivo XML
"""
# Generamos nuestras las etiquetas (<folder>, <filename>, <path> y <source>) que se localizaran dentro de la etiqueta <annotation>
xml_doc = ET.Element('annotation')
item_folder = ET.SubElement(xml_doc, 'folder')
item_filename = ET.SubElement(xml_doc, 'filename')
item_path = ET.SubElement(xml_doc, 'path')
# Generamos la etiqueta <database> que se localizara dentro de la etiqueta <source>
item_source = ET.SubElement(xml_doc, 'source')
item_database = ET.SubElement(item_source, 'database')
# Generamos las variables que se localizaran dentro de la etiqueta <size>
item_size = ET.SubElement(xml_doc, 'size')
item_width = ET.SubElement(item_size, 'width')
item_height = ET.SubElement(item_size, 'height')
item_depth = ET.SubElement(item_size, 'depth')
# <segmented>
item_segmented = ET.SubElement(xml_doc, 'segmented')
# Generamos las etiquetas (<name>, <pose>, <truncated>, <difficult>, <bndbox>) que se localizaran dentro de la etiqueta <object>
item_object = ET.SubElement(xml_doc, 'object')
item_name = ET.SubElement(item_object, 'name')
item_pose = ET.SubElement(item_object, 'pose')
item_truncated = ET.SubElement(item_object, 'truncated')
item_difficult = ET.SubElement(item_object, 'difficult')
# Generamos las etiquetas (<xmin>, <ymin>, <xmax>,<ymax>) que se localizaran dentro de la etiqueta <bndbox>
item_bndbox = ET.SubElement(item_object, 'bndbox')
item_xmin = ET.SubElement(item_bndbox, 'xmin')
item_ymin = ET.SubElement(item_bndbox, 'ymin')
item_xmax = ET.SubElement(item_bndbox, 'xmax')
item_ymax = ET.SubElement(item_bndbox, 'ymax')


"""
Generamos las variables dinamicas que proporcionaran los valores a las etiquetas XML
"""
folder_dir = None
folder_content = None
item_path_content = None
database_content = None
item_width_content = None
item_height_content = None
item_depth_content = '3'
item_segmented_content = '0'
item_name_content = None
item_pose_content = 'Unspecified'
item_truncated_content = '1'
item_difficult_content = '0'
item_xmin_content = None
item_ymin_content = None
item_xmax_content = None
item_ymax_content = None

def prettify(elem, indent='    '):
    """
    Regresa una version ordenada del archivo XML
    """
    queue = [(0, elem)]  # (Nivel, elemento)
    while queue:
        level, elem = queue.pop(0)
        children = [(level+1, child) for child in list(elem)]
        if children:
            elem.text = '\n' + indent * (level+1)  # Children
        if queue:
            elem.tail = '\n' + indent * queue[0][0]  # Sibling
        else:
            elem.tail = '\n' + indent * (level-1)  # Parent close
        # Agregamos a los children antes que a los sibling
        queue[0:0] = children

def xml_builder(folder_dir,folder_content,database_content,item_name_content,item_pose_content,item_truncated_content
                ,item_difficult_content,item_width_content,item_height_content,item_depth_content,
                item_segmented_content,item_xmin_content,item_ymin_content,item_xmax_content,item_ymax_content):
    """
    Genera X numero de archivos XML desde una ruta especificada
    Modo de uso: generate_xml(DIRECCION DE IMAGENES)
    """
    print(folder_dir)
    item_path_content = folder_dir
    for images in os.listdir(folder_dir):
        if(images.endswith(".jpg") or images.endswith(".png")):
            item_folder.text = folder_content
            item_filename.text = os.path.basename(images)
            item_path.text = item_path_content+"/"+item_filename.text
            item_database.text = database_content
            item_width.text = item_width_content
            item_height.text = item_height_content
            item_depth.text = item_depth_content
            item_segmented.text = item_segmented_content
            item_name.text = item_name_content
            item_pose.text = item_pose_content
            item_truncated.text = item_truncated_content
            item_difficult.text = item_difficult_content
            item_xmin.text = item_xmin_content
            item_ymin.text = item_ymin_content
            item_xmax.text = item_xmax_content
            item_ymax.text = item_ymax_content
            prettify(xml_doc)
            tree = ET.ElementTree(xml_doc)
            tree.write('E:\Proyecto\Script para generar XML\Prueba\\' +images.split(".", 1)[0]+'.xml') 

class Ui_MainWindow(object):
          
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.archivos_total = QtWidgets.QLabel(self.centralwidget)
        self.archivos_total.setGeometry(QtCore.QRect(400, 70, 271, 20))
        self.archivos_total.setObjectName("archivos_total")
        self.open_directory = QtWidgets.QPushButton(self.centralwidget)
        self.open_directory.setGeometry(QtCore.QRect(410, 180, 181, 31))
        self.open_directory.setObjectName("open_directory")
        self.directorio_actual = QtWidgets.QLabel(self.centralwidget)
        self.directorio_actual.setGeometry(QtCore.QRect(400, 10, 271, 20))
        self.directorio_actual.setObjectName("directorio_actual")
        self.generate_xml = QtWidgets.QPushButton(self.centralwidget)
        self.generate_xml.setGeometry(QtCore.QRect(410, 230, 181, 31))
        self.generate_xml.setObjectName("generate_xml")
        self.folder_input = QtWidgets.QLineEdit(self.centralwidget)
        self.folder_input.setGeometry(QtCore.QRect(9, 20, 133, 20))
        self.folder_input.setObjectName("folder_input")
        self.width_title = QtWidgets.QLabel(self.centralwidget)
        self.width_title.setGeometry(QtCore.QRect(10, 281, 28, 16))
        self.width_title.setObjectName("width_title")
        self.x_min_input = QtWidgets.QLineEdit(self.centralwidget)
        self.x_min_input.setGeometry(QtCore.QRect(180, 159, 133, 20))
        self.x_min_input.setObjectName("x_min_input")
        self.height_title = QtWidgets.QLabel(self.centralwidget)
        self.height_title.setGeometry(QtCore.QRect(180, 1, 31, 16))
        self.height_title.setObjectName("height_title")
        self.folder_title = QtWidgets.QLabel(self.centralwidget)
        self.folder_title.setGeometry(QtCore.QRect(9, 1, 30, 16))
        self.folder_title.setObjectName("folder_title")
        self.x_max_input = QtWidgets.QLineEdit(self.centralwidget)
        self.x_max_input.setGeometry(QtCore.QRect(180, 249, 133, 20))
        self.x_max_input.setObjectName("x_max_input")
        self.y_min_title = QtWidgets.QLabel(self.centralwidget)
        self.y_min_title.setGeometry(QtCore.QRect(180, 190, 25, 16))
        self.y_min_title.setObjectName("y_min_title")
        self.y_max_input = QtWidgets.QLineEdit(self.centralwidget)
        self.y_max_input.setGeometry(QtCore.QRect(180, 300, 131, 20))
        self.y_max_input.setObjectName("y_max_input")
        self.segmented_input = QtWidgets.QLineEdit(self.centralwidget)
        self.segmented_input.setGeometry(QtCore.QRect(180, 109, 133, 20))
        self.segmented_input.setObjectName("segmented_input")
        self.height_input = QtWidgets.QLineEdit(self.centralwidget)
        self.height_input.setGeometry(QtCore.QRect(180, 20, 133, 20))
        self.height_input.setObjectName("height_input")
        self.y_max_title = QtWidgets.QLabel(self.centralwidget)
        self.y_max_title.setGeometry(QtCore.QRect(180, 281, 29, 16))
        self.y_max_title.setObjectName("y_max_title")
        self.name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(10, 111, 133, 20))
        self.name_input.setObjectName("name_input")
        self.truncated_title = QtWidgets.QLabel(self.centralwidget)
        self.truncated_title.setGeometry(QtCore.QRect(10, 186, 49, 16))
        self.truncated_title.setObjectName("truncated_title")
        self.segmented_title = QtWidgets.QLabel(self.centralwidget)
        self.segmented_title.setGeometry(QtCore.QRect(180, 90, 54, 16))
        self.segmented_title.setObjectName("segmented_title")
        self.width_input = QtWidgets.QLineEdit(self.centralwidget)
        self.width_input.setGeometry(QtCore.QRect(10, 300, 133, 20))
        self.width_input.setObjectName("width_input")
        self.database_title = QtWidgets.QLabel(self.centralwidget)
        self.database_title.setGeometry(QtCore.QRect(9, 46, 46, 16))
        self.database_title.setObjectName("database_title")
        self.database_input = QtWidgets.QLineEdit(self.centralwidget)
        self.database_input.setGeometry(QtCore.QRect(9, 65, 133, 20))
        self.database_input.setObjectName("database_input")
        self.x_max_title = QtWidgets.QLabel(self.centralwidget)
        self.x_max_title.setGeometry(QtCore.QRect(180, 230, 29, 16))
        self.x_max_title.setObjectName("x_max_title")
        self.y_min_input = QtWidgets.QLineEdit(self.centralwidget)
        self.y_min_input.setGeometry(QtCore.QRect(180, 205, 133, 20))
        self.y_min_input.setObjectName("y_min_input")
        self.difficult_input = QtWidgets.QLineEdit(self.centralwidget)
        self.difficult_input.setGeometry(QtCore.QRect(10, 250, 133, 20))
        self.difficult_input.setObjectName("difficult_input")
        self.name_title = QtWidgets.QLabel(self.centralwidget)
        self.name_title.setGeometry(QtCore.QRect(10, 92, 27, 16))
        self.name_title.setObjectName("name_title")
        self.difficult_title = QtWidgets.QLabel(self.centralwidget)
        self.difficult_title.setGeometry(QtCore.QRect(10, 231, 36, 16))
        self.difficult_title.setObjectName("difficult_title")
        self.pose_title = QtWidgets.QLabel(self.centralwidget)
        self.pose_title.setGeometry(QtCore.QRect(10, 141, 23, 16))
        self.pose_title.setObjectName("pose_title")
        self.depth_title = QtWidgets.QLabel(self.centralwidget)
        self.depth_title.setGeometry(QtCore.QRect(180, 50, 29, 16))
        self.depth_title.setObjectName("depth_title")
        self.depth_input = QtWidgets.QLineEdit(self.centralwidget)
        self.depth_input.setGeometry(QtCore.QRect(180, 69, 133, 20))
        self.depth_input.setObjectName("depth_input")
        self.x_min_title = QtWidgets.QLabel(self.centralwidget)
        self.x_min_title.setGeometry(QtCore.QRect(180, 140, 25, 16))
        self.x_min_title.setObjectName("x_min_title")
        self.truncated_input = QtWidgets.QLineEdit(self.centralwidget)
        self.truncated_input.setGeometry(QtCore.QRect(10, 205, 133, 20))
        self.truncated_input.setObjectName("truncated_input")
        self.pose_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pose_input.setGeometry(QtCore.QRect(10, 160, 133, 20))
        self.pose_input.setObjectName("pose_input")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XML Builder"))
        self.archivos_total.setText(_translate(
            "MainWindow", "Archivos en total:"))
        self.open_directory.setText(
            _translate("MainWindow", "Abrir directorio"))
        self.directorio_actual.setText(
            _translate("MainWindow", "Directorio actual:"))
        self.generate_xml.setText(_translate("MainWindow", "Generar XML"))
        self.width_title.setText(_translate("MainWindow", "Width"))
        self.height_title.setText(_translate("MainWindow", "Height"))
        self.folder_title.setText(_translate("MainWindow", "Folder"))
        self.y_min_title.setText(_translate("MainWindow", "Y Min"))
        self.y_max_title.setText(_translate("MainWindow", "Y Max"))
        self.truncated_title.setText(_translate("MainWindow", "Truncated"))
        self.segmented_title.setText(_translate("MainWindow", "Segmented"))
        self.database_title.setText(_translate("MainWindow", "Database"))
        self.x_max_title.setText(_translate("MainWindow", "X Max"))
        self.name_title.setText(_translate("MainWindow", "Name"))
        self.difficult_title.setText(_translate("MainWindow", "Difficult"))
        self.pose_title.setText(_translate("MainWindow", "Pose"))
        self.depth_title.setText(_translate("MainWindow", "Depth"))
        self.x_min_title.setText(_translate("MainWindow", "X Min"))
        self.open_directory.clicked.connect(self.pushButton_handler)
        self.folder_input.textChanged.connect(self.saveFolderInput)
        self.database_input.textChanged.connect(self.saveDatabaseInput)
        self.name_input.textChanged.connect(self.saveNameInput)
        self.pose_input.textChanged.connect(self.savePoseInput)
        self.truncated_input.textChanged.connect(self.saveTruncatedInput)
        self.difficult_input.textChanged.connect(self.saveDifficultInput)
        self.width_input.textChanged.connect(self.saveWidthInput)
        self.height_input.textChanged.connect(self.saveHeightInput)
        self.depth_input.textChanged.connect(self.saveDepthInput)
        self.segmented_input.textChanged.connect(self.saveSegmentedInput)
        self.x_min_input.textChanged.connect(self.saveXMinInput)
        self.y_min_input.textChanged.connect(self.saveYMinInput)
        self.x_max_input.textChanged.connect(self.saveXMaxInput)
        self.y_max_input.textChanged.connect(self.saveYMaxInput)
        self.generate_xml.clicked.connect(lambda: xml_builder(self.folder_path_ui, 
        self.folder_content_ui, self.database_content_ui,self.item_name_content_ui
        ,self.item_pose_content_ui,self.item_truncated_content_ui,self.item_difficult_content_ui
        ,self.item_width_content_ui,self.item_height_content_ui,self.item_depth_content_ui
        ,self.item_segmented_content_ui,self.item_xmin_content_ui,self.item_ymin_content_ui,self.item_xmax_content_ui,
        self.item_ymax_content_ui))
        

    
    
    def pushButton_handler(self):
        self.open_file_explorer()

    def open_file_explorer(self):
        folder_dir = QFileDialog.getExistingDirectory()
        self.folder_path_ui = folder_dir
        self.directorio_actual.setText('Directorio actual: \n'+folder_dir)
        self.directorio_actual.adjustSize()
        count = sum(len(files) for _, _, files in os.walk(folder_dir))
        self.archivos_total.setText('Archivos en total: '+str(count))

    def saveFolderInput(self):
        self.folder_content_ui = self.folder_input.text()

    def saveDatabaseInput(self):
        self.database_content_ui = self.database_input.text()

    def saveNameInput(self):
        self.item_name_content_ui = self.name_input.text()

    def savePoseInput(self):
        self.item_pose_content_ui = self.pose_input.text()

    def saveTruncatedInput(self):
        self.item_truncated_content_ui = self.truncated_input.text()

    def saveDifficultInput(self):
        self.item_difficult_content_ui = self.difficult_input.text()

    def saveWidthInput(self):
        self.item_width_content_ui = self.width_input.text()

    def saveHeightInput(self):
        self.item_height_content_ui = self.height_input.text()

    def saveDepthInput(self):
        self.item_depth_content_ui = self.depth_input.text()

    def saveSegmentedInput(self):
        self.item_segmented_content_ui = self.segmented_input.text()

    def saveXMinInput(self):
        self.item_xmin_content_ui = self.x_min_input.text()

    def saveYMinInput(self):
        self.item_ymin_content_ui = self.y_min_input.text()

    def saveXMaxInput(self):
        self.item_xmax_content_ui = self.x_max_input.text()

    def saveYMaxInput(self):
        self.item_ymax_content_ui = self.y_max_input.text()
    
    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
