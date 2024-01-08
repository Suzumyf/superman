#%%
#Estructura de dicionario
husbandos= {"nombre":"Luffy","edad": 19 ,"serie": "one piece"}
print(husbandos.get("serie"))
for n in husbandos.keys():
    print(n)
    
for n in husbandos.values():
    print(n)

husbandos["apellido"]= "Monkey D."
 
for k, v in husbandos.items():
    print(f"{k}:{v}")