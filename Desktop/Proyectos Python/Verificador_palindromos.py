#Verificador de palabras palindromas

def es_palindromo(cadena):
    revisar_cad = cadena[::-1]
    if (cadena == revisar_cad):
        return True
    else:
        return False
    
verificar = es_palindromo("racecar")
print(verificar)