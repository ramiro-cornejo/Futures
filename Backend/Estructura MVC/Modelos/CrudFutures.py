import os
import usuario

usuario = []    

def mostrar_opciones():
    print('CRUD EJEMPLO')
    print('*' * 50)
    print('Selecciona una opción:')
    print('[C]reate')
    print('[R]ead - Leer')
    print('[U]pdate - Actualizar')
    print('[D]elete  - Elimnar')
    print('[S]ALIR')

    

def run():
    mostrar_opciones()
    
    command = input()
    command = command.upper()
    

    while True:
        if command == 'C':
            print('CREACIÓN DE USUARIO')
            print('*' * 50)
            print('Inserta tu nombre:')
            nombreUser = input()
            print('Inserta tu apellido:')
            apellidoUser = input()
            print('Inserta tu DNI:')
            dniUser = input()
            print('Inserta tu mail:')
            mailUser = input()
            print('Inserta el Link de tu repositorio')
            link_repo = input()
            lista_usuarios.append(Usuario.usuario (nombreUser, apellidoUser, dniUser, mailUser, link_repo))      
            print(Usuario)
            command = ""
        elif command == 'R':
            print('PRINT DE TODOS LOS USUARIOS')
            print('*' * 50)
            for i in lista_usuarios:
                print (i.nombreUser,i.apellidoUser, i.dniUser, i.mailUser, i.link_repo)
            
            command = ""
        elif command == 'U':
            print('Inserta el DNI:')
            dniUserBusqueda = input()

                
        elif command == 'D':
            print('Inserta el DNI:')
            dniUserBusqueda = input()

                
        elif command == 'S':
                os._exit(1)
        else:
                run()
        

  

  

        

if __name__ == "__main__":
    run()