import pandas as pd
import numpy as np

class EnfermedadModel:
    
    def __init__(self):
        self.df = pd.read_csv("diabetes.csv")
        
    #Total pacientes
        
    def total_pacientes(self):
        return len(self.df)
    
    #Pormedio Glucosa
    
    def promedio_glucosa(self):
        return np.mean(self.df["Glucose"])
    
    #Promedio BMI
    
    def promedio_bmi(self):
        return np.mean(self.df["BMI"])
    
    #Pacientes con Diabetes
    
    def pacientes_diabetes(self):
        return len(self.df[self.df["Outcome"] == 1])
    
    #Pacientes sin diabetes
    
    def pacientes_sanos(self):
        return len(self.df[self.df["Outcome"] == 0])
    
    #Paceitnes de riesgo
    
    def pacientes_riesgo(self):
        return self.df[(self.df["Glucose"] > 150) & (self.df["BMI"] > 35)].head(20)
        
    #Pacientes mayores
    
    def pacientes_mayores(self):
        return self.df[self.df["Age"] > 50].head(20)