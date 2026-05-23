import pandas as pd


#leer archivo
df = pd.read_csv("diabetes.csv")

#filtrar todos los pacientes que tiene diabetes
diabetes = df[df["Outcome"] == 1]

print("Personas con diabetes")
print(diabetes)

promedio = diabetes["Pregnancies"].mean()

print("Promedio de Embarazos")
print(promedio)

personas_en_riesgo = df[(df["Glucose"]>150) & (df["BMI"]>35) & (df["Age"]>50)]
print(personas_en_riesgo)

#porcentaje de personas con diabetes

#porcentaje = personas_con_diabetes/total * 100

total = len(df)
personas_con_diabetes = len(diabetes)

porcentaje = personas_con_diabetes/total*100
print(f"Porcentaje = {porcentaje}%")

#max()

max_glucosa = (df["Glucose"].max())
print(max_glucosa)

print(df[df["Glucose"] == max_glucosa])

promedio_glucosa_por_diagnostico = df.groupby("Outcome")["Glucose"].mean()
print(promedio_glucosa_por_diagnostico)

personas_con_presion_arterial = df[df["BloodPressure"] < 60]
print(personas_con_presion_arterial)

promedio_presion_arterial_todo = df.mean()
promedio_presion_arterial = df[df["BloodPressure"] > 60].mean()

print(f"Presion arterial todos: {promedio_presion_arterial_todo}")
print(f"Presion arterial: {promedio_presion_arterial}")

#Ordenamiento
ordenados = df.sort_values(
    by = "Glucose",
    ascending = False #o True para ascendente
)

print(ordenados)