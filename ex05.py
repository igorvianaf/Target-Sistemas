string = input('Digite o palavra/frase para eu te mostrar ele invertido: ')
#variavel para armazenar cada letra ao contrario
string_contrario = ''

#loop para pegar letra do final para o inicio e armazenar em variavel
for letra in string[::-1]:
    string_contrario += letra

print(string_contrario)
