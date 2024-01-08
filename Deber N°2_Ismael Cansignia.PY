#%% DEBER N°2: Ismael Cansignia
"""
Crea una tupla con un numero par de elementos
Escribe un program que divida la tupla en dos mitades y las muestre en pantalla
"""

tn= ("Xenovia",10,"Mario",15,80,14,10,"Dk",9,"Chisato")
t1= []
t2= []

division= len(tn)//2

t1= tn[:division]
t2= tn[division:]

print("Listado original: ",tn)
print("Primera mitad de su tupla: ",t1)
print("Seguna mitad de su tupla: ",t2)
# %%
