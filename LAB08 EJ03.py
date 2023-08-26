import random
import string


def generar_contraseña():
    l_may = string.ascii_uppercase
    l_min = string.ascii_lowercase
    nums = string.digits
    c_esp = string.punctuation
    l_contraseña = []
    for i in range(2):
        l_contraseña.append(random.choice(l_may))
        l_contraseña.append(random.choice(l_min))
        l_contraseña.append(random.choice(nums))
        l_contraseña.append(random.choice(c_esp))
    contraseña=''.join(l_contraseña)
    print(contraseña)

generar_contraseña()