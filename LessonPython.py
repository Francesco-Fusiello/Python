# ##Print

# print(6*24*12) #moltiplicazione

# print(65-(4+3*3)) 

# print((5+3*2)/(7+4*(9-3)))

# """Le variabili"""

# a = 7
# print(a)
# a = 5
# print(a)
# a = a*2
# a = a*2
# numero = a
# numero = numero + 1
# a = 12
# print(a)
# print(numero)

# eta =41  # int - ricordati di cambiarla ogni anno
# giorni_in_un_anno = 365.24 #bisestile ogni 4
# ore_in_un_giorno = 24
# minuti_in_un_ora = 60
# secondi_in_un_minuto = 60

# eta_in_secondi = eta * giorni_in_un_anno * \
#   ore_in_un_giorno * minuti_in_un_ora * secondi_in_un_minuto

# print(eta_in_secondi)

# a = "ciao!"
# print(a)

# a = "4+5"
# print(a)

# a = 'questo corso é "top"'
# b = "questo prof ha un'aria top"
# c = "questo corso è \"bellissimo\". Comunque il prof è top."
# print(a)
# print(b)
# print(c)

# print("Ciao" + " " + "Andrea")

# nome = "Andrea"
# messaggio = "Ciao "
# messaggio_da_stampare = messaggio + " " + nome
# print(messaggio_da_stampare)

# a = "Andrea"
# print(17 * a)
# print(a, 17, 2*a)
# print("Buongiorno" , a)
# print(a + str(17))

# """### Indexing"""

# s = "Andrea"
# print(s[0] + s[-3])

# s = "Tanto va la gatta al lardo che ci lascia lo zampino "
# print(s[3:15])
# print(s[1:])
# print(s[:10])
# print(s[-4:-2])


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

