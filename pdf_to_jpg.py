# -*- coding: utf-8 -*-
##############################################################################
#   
#    Code Create by: Ing. Luis J. Ortega 28/08/2019
#
##############################################################################
from wand.image import Image as wi
import zipfile
from os import listdir
import os.path
import os
import shutil
from time import time 
import zipfile
import zipfile


# INICIAMOS EL SCRIPT
tiempo_inicial = time() 
# REGRESA LOS ARCHIVOS DE UNA CARPETA
def ls(ruta = '.'):
    return listdir(ruta)

# CAMBIAR NOMBRE DE DIRECTORIOS Y AGREGAR PARA LOS PDF SUELTOS
def _rename_di(n):
	if n == "1. ENERO":
		os.rename("PDF/LIBROS CONTABLES/"+n, "PDF/LIBROS CONTABLES/1")
	elif n == "2. FEBRERO":
		os.rename("PDF/LIBROS CONTABLES/"+n, "PDF/LIBROS CONTABLES/2")
	elif n == "3. MARZO":
		os.rename("PDF/LIBROS CONTABLES/"+n, "PDF/LIBROS CONTABLES/3")
	elif n == "4. ABRIL":
		os.rename("PDF/LIBROS CONTABLES/"+n, "PDF/LIBROS CONTABLES/4")
	elif n == "Diarios y Polizas.pdf":
		os.mkdir("PDF/LIBROS CONTABLES/13")
		shutil.move("PDF/LIBROS CONTABLES/"+n, "PDF/LIBROS CONTABLES/13")
	elif n == "Libro Mayor Condensado.pdf":
		os.mkdir("PDF/LIBROS CONTABLES/14")
		shutil.move("PDF/LIBROS CONTABLES/"+n, "PDF/LIBROS CONTABLES/14")

	return True

# CREACION DE PAGINAS PARA TURNJS
def _create_to_page(j,lis,x):
	pdf = wi(filename = "PDF/LIBROS CONTABLES/"+lis+"/"+x, resolution=100)
	pdfImage = pdf.convert("jpg")
	for img in pdfImage.sequence:
		page = wi(image=img)
		page.save(filename="Libro Contable/pages/"+str(j)+".jpg")
		j += 1
		print "Imprimiendo pagina......"+str(j)

	return j

# DESCOMPRIR EL ARCHIVO ZIP
zf=zipfile.ZipFile("LIBROS CONTABLES.zip", "r")
for i in zf.namelist():
    zf.extract(i, path="PDF/")

lista_dir = ls('PDF/LIBROS CONTABLES')
lista_dir.sort(key=str)

for dirc in lista_dir:
	_rename_di(dirc)

lista_dir = ls('PDF/LIBROS CONTABLES')
lista_dir.sort(key=str)

listOrder =  sorted(lista_dir, key=int)

j=2
for lis in listOrder:
# for lis in listOrder[:12]:
	print lis
	pagesDir = ls("PDF/LIBROS CONTABLES/"+lis)
	pagesDir =  sorted(pagesDir, key=str)
	for x in pagesDir:
		j = _create_to_page(j,lis,x)
	shutil.rmtree("PDF/LIBROS CONTABLES/"+lis)
	j += 1

shutil.rmtree("PDF/LIBROS CONTABLES/")
shutil.copy("images/1.jpg", "Libro Contable/pages/1.jpg")
shutil.copy("images/copia.jpg", "Libro Contable/pages/2.jpg")
shutil.copy("images/copia.jpg", "Libro Contable/pages/6.jpg")
shutil.copy("images/copia.jpg", "Libro Contable/pages/12.jpg")
shutil.copy("images/copia.jpg", "Libro Contable/pages/18.jpg")
shutil.copy("images/copia.jpg", "Libro Contable/pages/24.jpg")
shutil.copy("images/copia.jpg", "Libro Contable/pages/30.jpg")
shutil.copy("images/copia.jpg", "Libro Contable/pages/36.jpg")
shutil.copy("images/copia.jpg", "Libro Contable/pages/42.jpg")
shutil.copy("images/copia.jpg", "Libro Contable/pages/48.jpg")
shutil.copy("images/copia.jpg", "Libro Contable/pages/54.jpg")
shutil.copy("images/copia.jpg", "Libro Contable/pages/60.jpg")
shutil.copy("images/copia.jpg", "Libro Contable/pages/66.jpg")

fantasy_zip = zipfile.ZipFile("ZIP/Libro_Contable.zip", 'w')
 
for folder, subfolders, files in os.walk('Libro Contable'):
 
    for file in files:
    	fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'Libro Contable'), compress_type = zipfile.ZIP_DEFLATED)
 
fantasy_zip.close()
shutil.rmtree("Libro Contable/pages")
os.mkdir("Libro Contable/pages")

tiempo_final = time()  
tiempo_ejecucion = tiempo_final - tiempo_inicial

print 'El tiempo de ejecucion fue:',tiempo_ejecucion #En segundos


 


