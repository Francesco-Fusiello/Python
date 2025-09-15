# # Tipi di dati e variabili

# a = 12 #int
# b = 12.7 #float
# c = "Hello" #string
# c_bis ="17" #string
# c_ter = '17.24' #string
# d = True #boolean
# e = False #boolean

# print(type(d)) #<class 'bool'>
# print(type(str(d))) #<class 'str'>
# print(int(d)) #1
# print(int(e)) #0
# print(float(e)) #0.0
# print(float(a)) #12.0

# Altri Operatori e funzioni simpatiche

print(7 %2) #1 (resto della divisione)
print(29 %  5) #4 (resto della divisione)

dividendo = 29
divisore = 5
risultato = dividendo / divisore #5.8 (float)
risultato_int = int(risultato) #5 (int)
resto= dividendo % divisore #4 (int)
print(dividendo,"diviso",divisore,"fa",risultato_int,"col resto di",str(resto)+".") #29 diviso 5 fa 5 col resto di 4.     

print(7 // 2) #3 (divisione intera)
print(29 // 5) #5 (divisione intera)

print(17**3) #8 (potenza)