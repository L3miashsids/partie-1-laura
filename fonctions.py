# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 15:08:52 2020

@author: laura
"""

import numpy as np

#Fonction fit
def fit(JD1):
    print("\n\nFonction fit")
    print("\nInformations de Base\n")
    
    #information sur le dataset
    print("\nNom et type des variables\n")
    print(JD1.dtypes)
    print(JD1.columns)
    #Dimension
    print("\nDimension\n")
    print(JD1.shape)
    
    #Nombre de variables
    print("\nNombre de classes\n")
    print(JD1.TYPE.nunique())
    
    #NInformations sur les classes
    print("\nDifférentes classes\n")
    print(JD1.TYPE.unique())
    nbcl = JD1.TYPE.unique()
    print("\nNombre de classes distinctes\n")
    print(JD1.TYPE.value_counts())
    print("\Fréquence de chaque classes\n")
    print(JD1.TYPE.value_counts(normalize=True))
    
    #liste des colonnes
    print("\nNom des colones\n")
    print(JD1.columns)
    
    #Moyenne conditionnelle
    print("\nMoyenne conditionnelle\n")
    for i in nbcl:
        print(i)
        ma = np.mean(JD1.loc[JD1.TYPE==i])
        print(ma)
        
    #Matrice covariance
    print("\nMatrice covariance\n")
    '''
    J'arrive pas
    '''
    
#Fonction predict
def predict(JD2):
    print("\n\nFonction predict")
    print("\n\nPrediction\n")
    #prediction
   
'''  
#Fonction stepdisc
def stepdisc(?????):
'''
