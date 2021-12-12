import pandas as pd
from tkinter import filedialog

data_null={}
df_null = pd.DataFrame(data_null)

a = filedialog.asksaveasfilename(title="Abrir", initialdir = "C:/",filetypes = [("Archivo excel","*.xlsx")])

if a != "":
	df_null.to_excel(f"{a}.xlsx",index=False)

	#df_null.to_excel("Reporte.xlsx",index=False)

	writer = pd.ExcelWriter(f"{a}.xlsx")

	b=["1","2","3"]
	c=["Matutino","Vespertino","Nocturno"]
	data1 = {"Semestre":b, "Turno":c}
	df1=pd.DataFrame(data1)

	#data1 = {"Semestre":["1","2","3"], "Turno":["Matutino","Vespertino","Nocturno"]}
    #df1=pd.DataFrame(data1)

	data2 = {"Clave":["123","1231","512"], "Plan":["401","401","401"]}
	df2=pd.DataFrame(data2)

	df1.to_excel(writer,"Agrupaciones",index=False)
	df2.to_excel(writer,"Materias",index=False)

	writer.save()
	writer.close()