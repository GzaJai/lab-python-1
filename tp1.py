# Ejercicio 1

print('\n-------------------- Ejercicio 1 --------------------\n')

name = 'Fernando'

print('Bienvenido', name)


# Ejercicio 2

print('\n-------------------- Ejercicio 2 --------------------\n')

name = input('Ingresa tu nombre: ')

print('Bienvenido', name)


# Ejercicio 3

print('\n-------------------- Ejercicio 3 --------------------\n')


num1, num2 = 3, 2

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)


# Ejercicio 4

print('\n-------------------- Ejercicio 4 --------------------\n')

num1, num2 = 3, 2

if num1==num2:
    print('Son iguales')
elif num1>num2:
    print(num1)
else:
    print(num2)


# Ejercicio 5

print('\n-------------------- Ejercicio 5 --------------------\n')

num1 = int(input('Ingresa un número: '))

if num1%2==0:
    print('El número que ingresaste es divisible por 2')
else:
    print('El numero NO es divisible por 2')


# Ejercicio 6

print('\n-------------------- Ejercicio 6 --------------------\n')

num_inp = float(input('Ingresa el precio del producto: '))

IVA = .21

print(num_inp+(num_inp*IVA))


# Ejercicio 7

print('\n-------------------- Ejercicio 7 --------------------\n')

counter = 1
finish_at = 100

while counter<=finish_at:
    print(counter)
    counter+=1


# Ejercicio 8

print('\n-------------------- Ejercicio 8 --------------------\n')

counter = 1
finish_at = 100

for i in range(counter, finish_at+1):
    print(i)
    

# Ejercicio 9

print('\n-------------------- Ejercicio 9 --------------------\n')

for n in range(1, 101):
    if n%2==0:
        print(n)
    elif n%3==0:
        print(n)


# Ejercicio 10

print('\n-------------------- Ejercicio 10 --------------------\n')

num_inp = int(input('Ingresa un número mayor o igual a cero: '))

while num_inp<0:
    num_inp = int(input('Ingresa un número mayor o igual a cero: '))
print('El número ingresado es válido')


# Ejercicio 11

print('\n-------------------- Ejercicio 11 --------------------\n')

password = 'hola123'
loged_in = False
block_access = False
counter = 0

while(loged_in==False and block_access==False):

    user_password = input('Ingresa la contraseña: ')
    if counter+1 >= 3:
        print('El acceso ha sido bloqueado despues de los 3 intentos\n')
        block_access = True
    if password==user_password:
        loged_in = True
        print('Acceso Correcto\n')
    else:
        counter += 1
        

# Ejercicio 12

print('\n-------------------- Ejercicio 12 --------------------\n')

def check_weekday():
    user_inp = int(input('Ingresa un día de la semana: '))
    if 0<user_inp<=7:
        match user_inp:
            case inp if 0 < inp <= 5:
                print('Dia laboral')
            case inp if 6 <= inp <= 7:
                print('Dia NO laboral')
    else:
        print('Ingresa un número válido')
        check_weekday()

check_weekday()
        

# Ejercicio 13

print('\n-------------------- Ejercicio 13 --------------------\n')

user_num = int(input('Ingrese un numero: '))

def check_prime(num):
    if num<=1:
        return False
    for n in range(2, num):
        if num%n==0:
            return False
    return True

if check_prime(user_num):
    print('Es un número primo')
else:
    print('NO un número primo')
            

# Ejercicio 14

print('\n-------------------- Ejercicio 14 --------------------\n')

import random

ran_num = random.randint(0,100)
counter = 0

while(True):
    counter += 1
    user_try = int(input('Ingrese un número entre 0 y 100 -> '))

    if user_try == ran_num:
        print(f'Correcto! Encontraste el número en {counter} intentos')
        break
    if user_try<ran_num:
        print('Es bajo')
    else:
        print('Es alto')
            

# Ejercicio 15

print('\n-------------------- Ejercicio 15 --------------------\n')

num_inp = int(input('Ingrese un número: '))

message = ''

def get_last_digit(num):
    return int(str(num)[-1])

def sum_of_digits(num):
    digits = list()
    for i in range(0, len(str(num))):
        digits.append(int(str(num)[i]))
    digit_sum = 0
    for d in digits:
        digit_sum+= d
    return digit_sum

if num_inp%2==0:
    if message=='':
        message= 'Es divisible por 2'
    else: 
        message+= ', 2'

if sum_of_digits(num_inp)%3==0:
    if message=='':
        message= 'Es divisible por 3'
    else: 
        message+= ', 3'

if get_last_digit(num_inp)==5 or get_last_digit(num_inp)==0:
    if message=='':
        message= 'Es divisible por 5'
    else: 
        message+= ', 5'

if '2' and '3' in message:
    if message=='':
        message= 'Es divisible por 6'
    else: 
        message+= ', 6'

if sum_of_digits(num_inp)%9==0:
    if message=='':
        message= 'Es divisible por 9'
    else: 
        message+= ', 9'

if get_last_digit(num_inp)==0:
    if message=='':
        message= 'Es divisible por 10'
    else: 
        message+= ', 10'

print(message)