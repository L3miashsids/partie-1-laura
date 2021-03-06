# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 15:08:52 2020

@author: laura
"""
#Importations
import pandas as pd
import numpy as np
import math as m
import matplotlib.pyplot as plt


class ADL :
    
    
    #Fonction fit
    def fit(self, JD1,CLASS):
        print("\n\nFonction fit")
        print("\nInformations de Base\n")
        print(CLASS)
        
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
        print(JD1[CLASS].nunique())
        #On stocke la valeur K = nombre de modalités
        K=JD1[CLASS].nunique()
        
        #Affichage des variables explicatives et de la variable catégorielle
        print("\nMatrice des descripteurs X\n")
        X_train=JD1.select_dtypes(include=["int64","float64"])
        print(X_train) #J'affiche pour vérif mais on l'enlevera
        
        print("\nNombre de variables explicatives\n")
        print(X_train.shape[1])
        #On stocke le nombre d'explicatives
        p=X_train.shape[1]
    
        print("\nVecteur cible y\n")
        y_train=JD1[CLASS]
        print(y_train) #IDEM
        
        print("\nDifférentes classes\n")
        d_c = JD1[CLASS].unique()
        print(d_c)
        
        print("\nEffectif par classe\n")
        print(JD1[CLASS].value_counts())
        #On stocke les effectifs
        n_k=JD1[CLASS].value_counts()
        
        #Répartition des élements de la classe
        plt.hist(list(y_train), bins=5, align="mid")
        plt.xlabel("Elements de la classe")
        plt.ylabel("Nombres d'individus")
        plt.title("Répartition des élements de la classe ")
    
        print("\nProportion par classe\n")
        print(JD1[CLASS].value_counts(normalize=True))
        #On stocke les proportions
        pi_k=JD1[CLASS].value_counts(normalize=True)
        
            
        #Moyennes conditionnelles
        print("\nMoyennes conditionnelles\n")
            
        mb_k = np.zeros(shape=(K,p))
        g = -1
        for i,rows in JD1.groupby(CLASS):
            g = g+1
            mb_k[g] = rows.mean()
        print(pd.DataFrame(mb_k, index= d_c , columns=X_train.columns))
    
        #Matrice de covariances conditionnelles
        print("\nMatrice de covariances conditionnelles\n")
        for i in d_c :
            X_train_classe = (JD1.loc[JD1[CLASS]==i])
            X_train_classe = X_train_classe.select_dtypes(include=["int64","float64"])
            V_k = np.cov(X_train_classe.values, rowvar=False)
            print("\nMatrice de la classe:",i)
            print(pd.DataFrame(V_k, index=X_train.columns, columns = X_train.columns))
        
        #Matrice de covariance totale
        print("\nMatrice de covariance totale\n")
        cov_tot = np.cov(X_train.values, rowvar=False)
        print(pd.DataFrame(cov_tot, index=X_train.columns, columns = X_train.columns))
    
        #Matrice de covariances intra-classes
        print("\nMatrice de covariance intra-classes\n")
        W = 0
        for i in d_c:
           W = W + (n_k[i]-1)*V_k
        W = W*(1/(n-K))
        wb = (n-K)/n * W
        print(pd.DataFrame(W, index=X_train.columns, columns = X_train.columns))
        print("biaisé")
        print(pd.DataFrame(wb, index=X_train.columns, columns = X_train.columns))
        
        #invW
        print("\nInverse Matrice de covariance intra-classes\n")
        invW = np.linalg.inv(W)
        print(pd.DataFrame(invW, index=X_train.columns, columns = X_train.columns))
        
        #Déterminant    
        print("\nDeterminant variance intra-classe\n")
        dvic = np.linalg.det(W)
        print(dvic)
        print("\nDeterminant variance totale\n")
        dvt = np.linalg.det(cov_tot)
        print(dvt)
        r = dvic/dvt
        print(r)
        
        print("\nCalcul des coefficients des variables akj\n")
        
        coef = np.dot(mb_k, invW)
        t_coef = np.transpose(coef)
        t_coef = pd.DataFrame(t_coef, index=X_train.columns, columns=d_c)
        print(t_coef)
        
    
        print("\n#les constantes ak0\n")
        #Multiplication des matrices
        result = np.dot(coef,np.transpose(mb_k))
        
        #diagonalisation
        diag = np.zeros(shape=(K,1))
        for i in range (0,K):
            a = result[i][i]
            diag[i] = a
    
        #Fois 0.5
        result = 0.5*diag
    
        #Logarithme
        log = np.zeros(shape=(K,1))
        for i in range (0,K):
             ab = m.log(pi_k[i])
             log[i] = ab
        print(pd.DataFrame(log, index=d_c ))
        
        print("\nintercept\n")
        intercept = log - result
        intercept = np.transpose(intercept)
        intercept = pd.DataFrame(intercept, columns=d_c)
        print(intercept)
        
        print("\nFinal\n")
        final = (t_coef.append(intercept))
        final = final.rename(index={0:'Constante'})
        print(final)
    
    
        return(final)
           
#Fonction predict
def predict(a, JD2):
    print("\n\nFonction predict")
    print("\n\nPrediction\n")
     #information sur le dataset test
    print("\nNom et type des variables\n")
    print(JD2.dtypes)
    
    #Dimension
    print("\nDimension\n")
    print(JD2.shape)
    
    
    #On stocke le nombre d'observations n
    n=JD2.shape[0]
    
    
    #affichage des premières valeurs
    print("\nAffichage des premières valeurs\n")
    print(JD2.head(5))
    
    #Affichage des variables explicatives
    print("\nMatrice des descripteurs X\n")
    X_test=JD2.select_dtypes(include=["int64","float64"])
    print(X_test) #J'affiche pour vérif mais on l'enlevera
    
     #On stocke le nombre de variables explicatives 
    p=X_test.shape[1]
    
    
    #Calcul des scores en test
    print("\n Reprise des coeficients et des constantes\n")
    constante= a[-1:]
    print(constante)
    coef= a[:p]
    print(coef)
    
    
    print("\n Calcul des scores\n")
    
    Xtestmat = np.array(X_test)
    scores = np.dot(Xtestmat, coef)#multiplication par coeficients
    scores = pd.DataFrame(scores, columns=(coef.columns))
    constantemat=np.array(constante)#Ajout des constantes
    scores = scores + constantemat
    print(pd.DataFrame(scores))
    
    
