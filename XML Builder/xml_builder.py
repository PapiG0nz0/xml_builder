from fileinput import filename
import queue
from textwrap import indent
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
from os import listdir, walk
from os.path import isfile, join


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
folder_dir = 'E:/Proyecto/Script para generar XML/Prueba'
folder_content = 'Data Set Prueba'
item_path_content = 'E:\Proyecto\Script para generar XML\Prueba\\'
database_content = 'Lenguaje de Senas Mexicano By [PapiGonz0]'
item_width_content = '320'
item_height_content = '320'
item_depth_content = '3'
item_segmented_content = '0'
item_name_content = 'A'
item_pose_content = 'Unspecified'
item_truncated_content = '1'
item_difficult_content = '0'
item_xmin_content = '1'
item_ymin_content = '1'
item_xmax_content = '320'
item_ymax_content = '320'

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

def generate_xml(dir):
    """
    Genera X numero de archivos XML desde una ruta especificada
    Modo de uso: generate_xml(DIRECCION DE IMAGENES)
    """
    for images in os.listdir(dir):
        if(images.endswith(".jpg") or images.endswith(".png")):
            item_folder.text = folder_content
            item_filename.text = os.path.basename(images)
            item_path.text = item_path_content+item_filename.text
            item_database.text = database_content
            item_width.text = item_width_content
            item_height.text = item_height_content
            item_depth.text = item_depth_content
            item_segmented.text = item_segmented_content
            item_name.text = item_name_content
            item_pose.text =  item_pose_content
            item_truncated.text = item_truncated_content
            item_difficult.text = item_difficult_content
            item_xmin.text = item_xmin_content
            item_ymin.text = item_ymin_content
            item_xmax.text = item_xmax_content
            item_ymax.text = item_ymax_content
            prettify(xml_doc)
            tree = ET.ElementTree(xml_doc)
            tree.write('E:\Proyecto\Script para generar XML\Prueba\\'+images.split(".", 1)[0]+'.xml')


generate_xml(folder_dir)