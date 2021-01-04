# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 15:08:52 2020

@author: laura
"""
#Importations
import pandas

#Fonction fit
def fit(JD1):
    print("\n\nFonction fit")
    print("\nInformations de Base\n")
    
    #information sur le dataset
    print("\nNom et type des variables\n")
    print(JD1.dtypes)
    
    #Dimension
    print("\nDimension\n")
    print(JD1.shape)
    
    #Nombre de variables
    print("\nNombre de classes\n")
    print(JD1.TYPE.nunique())
    
    #NInformations sur les classes
    print("\nDifférentes classes\n")
    print(JD1.TYPE.unique())
    print("\nNombre de classes distinctes\n")
    print(JD1.TYPE.value_counts())
    print("\nPourcentage de chaque classes\n")
    print(JD1.TYPE.value_counts(normalize=True))
    
    
    #liste des colonnes
    print("\nNom des colones\n")
    print(JD1.columns)


#Fonction predict
def predict(JD2):
    print("\n\nFonction predict")
    print("\n\nPrediction\n")
    #prediction
   
'''  
#Fonction stepdisc
def stepdisc(?????):
'''
