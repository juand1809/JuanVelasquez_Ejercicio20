import numpy as np
import math

class Complejo ():
    def __init__ (self,real,imaginario):
        self.real = real
        self.imaginario = imaginario
        
    def conjugado(self):
        self.imaginario = -self.imaginario
    
    def calcula_norma(self):
        self.norma = np.sqrt((self.real ** 2) + (self.imaginario **2))
    
    def pow(self,n):
        num = self(self.real,self.imaginario)
        self.pow = np.power(num,n)
    

        


