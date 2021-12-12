import pandas as pd

archivoPath = "C:/Hoja.xlsx"
datos = pd.read_excel(archivoPath,header=0,engine = 'openpyxl')
print(datos)
print("_____________________________________")
#primeros valores
print(datos.head(2))
print("_____________________________________")
#ultimos valores
print(datos.tail(2))
print("_____________________________________")
#filas x columnas
print("Fila x columnas: ",datos.shape)
print("_____________________________________")
#nombre de las columnas
print("Columnas en el excel: ",list(datos.columns))
print("_____________________________________")

print("Cantidad de index: ",datos.index)
print("_____________________________________")

print(datos["Semestre"])
print("_____________________________________")
print(list(datos.Semestre))
print("_____________________________________")
print(datos[["Empleado","Hora","Turno","Semestre"]])

print("___________________Eliminar una columna__________________")
segundo_datos = list(datos.columns)
segundo_datos.remove("Semestre")
datos2 = datos[segundo_datos]
print(datos)

print("_____________________________________")
print("Cantidad de registros: ",len(datos))
for i in range(len(datos)):
	valor = datos.loc[i]
	print("_____________________________________")
	
	"""print(valor[0])
	print(valor[1])
	print(valor[2])
	print(valor[3])"""

	for x in valor:
		print("Valor: ", x)