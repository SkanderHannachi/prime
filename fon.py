"""simple program to generate prime numbers and study their occurence. """

import math 
import random as rdm 
import numpy as np
from matplotlib import pyplot as plt
#--------------------------------------------------------------------------
PLAFOND = 10000
GROUPE_DIV = 10
#--------------------------------------------------------------------------
    
class Generator : 
    def __init__(self,plafond,group_div) :
        self.lenght = plafond
        self.y_axis = self.generator(self.lenght)
        self.x_axis = range(len(self.y_axis))
        self.group_div = group_div 
        self.self_sub_ls = self.compute_group()  # list of list
        self.percent  = self.compt(self.self_sub_ls)
        
    def compute_group(self) : 
        """fast extract of a in list in a list """
        ls = self.y_axis
        ind = self.group_div
        index = ls.index(self.nearest_prime(ind))
        sfom = []
        ls_renev = ls
        while(len(ls_renev)>self.group_div) : 
            ls_sub  = ls[:index]
            sfom.append(ls_sub)
            ls_renev = ls[index:]
            ind += self.group_div 
            index = ls.index(self.nearest_prime(ind))
        return sfom
        print(len(sfom))
    
    def nearest_prime(self,a) : 
        while not (self.is_prime(a)) : 
            if self.is_prime(a) : 
                return a 
            else : 
                a+= 1
        return a
                
    def is_prime(self,x) : 
        state = True 
        i = 2 
        while (state) and i <= (x//2) : 
            if x % i == 0 : 
                state = False
                return state 
            else : 
                i+=1 
        return state
        
    def generator(self,plaf) :
        ls = []
        for i in range(plaf) : 
            if self.is_prime(i) : 
                ls.append(i)
        return ls
    
    def histo(self,ran) : 
        plt.hist(range(len(self.self_sub_ls)),self.percent)
        #plt.hist(self.percent,)
        plt.title("")
        plt.xlabel(str(ran) + " range")
        plt.ylabel("Frequency")
        fig = plt.gcf()
        plt.show()
    
    def compt(self,g) : 
        l = [] 
        for elm in g :
            l.append(len(elm))
        return l
    
    def plotter(self) : 
        plt.subplot(212)
        plt.plot(self.x_axis, self.y_axis , 'r--')
        plt.show()
    
def main() : 
    generator = Generator(PLAFOND,GROUPE_DIV)
    generator.histo(GROUPE_DIV)
    print(generator.self_sub_ls[0])
if __name__ == '__main__' : 
    main()
    