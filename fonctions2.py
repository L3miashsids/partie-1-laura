# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 15:08:52 2020

@author: laura
"""
#Importations
import pandas as pd
import numpy as np

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
    #On stocke le nombre d'observations n
    n=JD1.shape[0]
    
    #NInformations sur les classes
    print("\nNombre de classes\n")
    print(JD1.TYPE.nunique())
    #On stocke la valeur K = nombre de modalités
    K=JD1.TYPE.nunique()
    
    #Affichage des variables explicatives et de la variable catégorielle
    print("\nMatrice des descripteurs X\n")
    X_train=JD1.select_dtypes(include=["int64","float64"])
    print(X_train) #J'affiche pour vérif mais on l'enlevera
    
    print("\nNombre de variables explicatives\n")
    print(X_train.shape[1])
    #On stocke le nombre d'explicatives
    p=X_train.shape[1]
    
    print("\nVecteur cible y\n")
    y_train=JD1.select_dtypes(include=["object"])
    print(y_train) #IDEM
    
    print("\nDifférentes classes\n")
    print(JD1.TYPE.unique())
    
    print("\nEffectif par classe\n")
    print(JD1.TYPE.value_counts())
    #On stocke les effectifs
    n_k=JD1.TYPE.value_counts()
    
    print("\nProportion par classe\n")
    print(JD1.TYPE.value_counts(normalize=True))
    #On stocke les proportions
    pi_k=JD1.TYPE.value_counts(normalize=True)
    
    
    #liste des colonnes --- INUTILE POUR MOI
    print("\nNom des colones\n")
    print(JD1.columns)

    #Apprentissage, on enlève les noms des colones --- INTERDIT car utilise adl
    #ad.fit(X=JD1[JD1.columns[:-1]],y=JD1.TYPE)
    
    #Propriétés et méthodes de l'objet
    #dir(ad)
    
    #Affichage --- IDEM
    #print("\nCoefficiants\n")
    #print(pandas.DataFrame(ad.coef_.transpose(),index=JD1.columns[:-1],columns=ad.classes_))
    
    #Constantes --- IDEM
    #print("\nCoefficiants constantes\n")
    #print(ad.intercept_)
    
    #De plus, je ne sais pas à quoi correspondent ces coefficiants et constantes
    #(je les vois pas dans le bouquins du prof, pas ici en tout cas)
    #Du coup j'ai supprimé "ad" des paramètres de la fonction
    
    nomcol=JD1.TYPE.unique()
    
    #Moyennes conditionnelles --- Il faut essayer de faire un seul tableau avec les var en colonnes
    print("\nMoyennes conditionnelles\n")
    for i in nomcol:
        print(i)
        mc = np.mean(JD1.loc[JD1.TYPE==i])
        print(mc)
    
    #Mtnt il faut calculer les matrices en fonctions des objets que j'ai créé
    
    print("\nMatrice de covariance totale\n")
    cov_tot = np.cov(X_train.values, rowvar=False)
    print(cov_tot)
    
    print("\nMatrice de covariance inter-classes\n")
    
    
    print("\nMatrice de covariance intra-classes\n")
    
    

#Fonction predict
def predict(ad,JD2):
    print("\n\nFonction predict")
    print("\n\nPrediction\n")
    #prediction
    pred = ad.predict(JD2)
    print(pred)
    print("\nComptage prediciton\n")
    #comptage des prédictions
    print(pandas.Series(pred).value_counts())
'''  
#Fonction stepdisc
def stepdisc(?????):
'''
