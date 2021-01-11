# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:26:39 2020

@author: laura
"""

#Importations
import os
import pandas as pd
import numpy as np
import math as m
import fonctions as f


#Chargement du dossier
os.chdir("C:/Users/Utilisateur/Documents/L3 MIASHS/Python/python Laura")

#Chargement premiere feuille --- Données TRAIN
DT = pd.read_excel("Data_LDA_Python.xlsx",sheet_name="DATA_TRAIN")

import numpy as np

Classe=f.ADL()

#FIT
fit= Classe.fit(DT, "TYPE")

#Chargement seconde feuille --- Données PREDICT
DP = pd.read_excel("Data_LDA_Python.xlsx",sheet_name="DATA_PREDICT")

#PREDICT
predict = f.predict(fit, DP)

'''
stepdisc = f.stepdisc(???)
'''



















