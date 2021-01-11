# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:26:39 2020
@author: laura
"""

#Importations
import os
import pandas as pd
import fonctions4 as f


#Chargement du dossier
os.chdir("C:/Users/laura/OneDrive/Bureau/PYTHON")

#Chargement premiere feuille --- Données TRAIN
DT = pd.read_excel("Data_LDA_Python.xlsx",sheet_name="DATA_TRAIN")

Classe=f.ADL()

#FIT
fit = Classe.fit(DT, "TYPE")

#Chargement seconde feuille --- Données PREDICT
DP = pd.read_excel("Data_LDA_Python.xlsx",sheet_name="DATA_PREDICT")

#PREDICT
predict = Classe.predict(fit, DP)

#STEPDISC
Classe.stepdisc(DT, "TYPE")

#HTML
htlm = f.HTML()
