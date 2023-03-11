
nombre = str(input('Ingrese el nombre del estudiante: '))
elec = int(input('Presione el numero de la funcion de desea hacer.\n 1. asignar notas. \n 2. Eliminar materia.  \n'))

if elec == 1:
    print('A continuacion ingrese las 3 notas del alumno ')
    a = float(input('Ingrese la primera nota: '))
    b = float(input('Ingrese la segunda nota: '))
    c = float(input('Ingrese la tercera nota: '))
    midic = { 'Primera Nota': a ,'Segunda Nota': b,'Tercera Nota': c}
    promn = a + b + c
    prom = float(promn) / 3
    elec1_1 = int(input('Presione el numero de la funcion de desea hacer.\n 1. Imprimir notas. \n 2. cambiar notas. \n 3. Eliminar materia.\n'))
    if elec1_1 == 1:
        print(midic)
        print('El prmedio de ',nombre,' es: ', prom)
    if elec1_1 == 2:
        elec2=int(input('Has seleccionado el cambio de notas. \n Que nota deseas cambiar? \n 1. \n 2.\n 3.\n'))
        if elec2 == 1:
            q =  float(input('Ingrese la primera nota: '))
            midic = { 'Primera Nota': q ,'Segunda Nota': b,'Tercera Nota': c}
            correc1 = q + b + c 
            prom1=float(correc1) / 3
            elec1_2=int(input('Desea cambiar otra nota ? \n 1. Si \n 2. No'))
            if elec1_2 == 1:
                pregunta = int(input('Cual desea cambiar ? \n 1. Segunda nota.  \n 2. Tercera nota.'))
                if pregunta == 1:
                    r =  float(input('Ingrese la segunda nota: '))
                    midic = { 'Primera Nota': q ,'Segunda Nota': r,'Tercera Nota': c}
                    correc1_1 = q + r + c 
                    prom1_1=float(correc1_1) / 3
                    elec1_3=int(input('Desea cambiar la tercera nota ? \n 1. Si \n 2. No'))
                    if elec1_3 == 1:
                        u =  float(input('Ingrese la tercera nota: '))
                        midic = { 'Primera Nota': q ,'Segunda Nota': r,'Tercera Nota': u}
                        correc1_1_1 = q + r + u 
                        prom1_1_1=float(correc1_1_1) / 3
                        print(midic)
                        print('El prmedio de ',nombre,' es: ',  prom1_1_1)
                    else:
                        print(midic)
                        print('El prmedio de ',nombre,' es: ',  prom1_1)
                if pregunta == 2:
                        u =  float(input('Ingrese la tercera nota: '))
                        midic = { 'Primera Nota': q ,'Segunda Nota': b,'Tercera Nota': u}
                        correc1_1_1 = q + b + u 
                        prom1_1_1=float(correc1_1_1) / 3
                        elec1_4=int(input('Desea cambiar la segunda nota ? \n 1. Si \n 2. No'))
                        if elec1_4 == 1:
                            r =  float(input('Ingrese la segunda nota: '))
                            midic = { 'Primera Nota': q ,'Segunda Nota': r,'Tercera Nota': u}
                            correc1_1_2 = q + r + u 
                            prom1_1_2=float(correc1_1_2) / 3
                            print(midic)
                            print('El prmedio de ',nombre,' es: ',  prom1_1_2)
                        else:
                            print(midic)
                            print('El prmedio de ',nombre,' es: ',  prom1_1_1)
            else:
                print(midic)
                print('El prmedio de ',nombre,' es: ',  prom)
        if elec2 == 2: 
            # w =  int(input('Ingrese la segunda nota: '))
            # midic = { 'Primera Nota': a ,'Segunda Nota': w ,'Tercera Nota': c}
            # correc2 = a + w + c 
            # prom2=int(correc2) / 3
            # elec2_1=int(input('Has seleccionado el cambio de notas. \n Que nota deseas cambiar? \n 1. \n 2.\n 3.\n'))
            w =  float(input('Ingrese la segunda nota: '))
            midic = { 'Primera Nota': a ,'Segunda Nota': w,'Tercera Nota': c}
            correc1 = a + w + c 
            prom1=float(correc1) / 3
            elec1_2=int(input('Desea cambiar otra nota ? \n 1. Si \n 2. No'))
            if elec1_2 == 1:
                pregunta = int(input('Cual desea cambiar ? \n 1. primea nota.  \n 2. Tercera nota.'))
                if pregunta == 1:
                    t =  float(input('Ingrese la primera nota: '))
                    midic = { 'Primera Nota': t ,'Segunda Nota': w,'Tercera Nota': c}
                    correc1_1 = t + w + c 
                    prom1_1=float(correc1_1) / 3
                    elec1_3=int(input('Desea cambiar la tercera nota ? \n 1. Si \n 2. No'))
                    if elec1_3 == 1:
                        i =  float(input('Ingrese la tercera nota: '))
                        midic = { 'Primera Nota': t ,'Segunda Nota': w,'Tercera Nota': i}
                        correc1_1_1 = t + w + i 
                        prom1_1_1=float(correc1_1_1) / 3
                        print(midic)
                        print('El prmedio de ',nombre,' es: ',  prom1_1_1)
                    else:
                        print(midic)
                        print('El prmedio de ',nombre,' es: ',  prom1_1)
                if pregunta == 2:
                        i =  float(input('Ingrese la tercera nota: '))
                        midic = { 'Primera Nota': a ,'Segunda Nota': w,'Tercera Nota': i}
                        correc1_1_1 = a + w + i 
                        prom1_1_1=float(correc1_1_1) / 3
                        elec1_4=int(input('Desea cambiar la primera nota ? \n 1. Si \n 2. No'))
                        if elec1_4 == 1:
                            t =  float(input('Ingrese la primera nota: '))
                            midic = { 'Primera Nota': t ,'Segunda Nota': w,'Tercera Nota': i}
                            correc1_1_2 = t + w + i 
                            prom1_1_2=float(correc1_1_2) / 3
                            print(midic)
                            print('El prmedio de ',nombre,' es: ',  prom1_1_2)
                        else:
                            print(midic)
                            print('El prmedio de ',nombre,' es: ',  prom1_1_1)
            else:               
                print(midic)
                print('El prmedio de ',nombre,' es: ',  prom1 )
        if elec2 == 3:
            # e =  int(input('Ingrese la segunda nota: '))
            # midic = { 'Primera Nota': a ,'Segunda Nota': b ,'Tercera Nota': e}
            # correc3 = a + b + e
            # prom3=int(correc3) / 3
            e =  float(input('Ingrese la tercera nota: '))
            midic = { 'Primera Nota': a ,'Segunda Nota': b,'Tercera Nota': e}
            correc1 = a + b + e 
            prom1=float(correc1) / 3
            elec1_2=int(input('Desea cambiar otra nota ? \n 1. Si \n 2. No'))
            if elec1_2 == 1:
                pregunta = int(input('Cual desea cambiar ? \n 1. primera nota.  \n 2. Segunda nota.'))
                if pregunta == 1:
                    y =  float(input('Ingrese la primera nota: '))
                    midic = { 'Primera Nota': y ,'Segunda Nota': b,'Tercera Nota': e}
                    correc1_1 = y + b + e 
                    prom1_1=float(correc1_1) / 3
                    elec1_3=int(input('Desea cambiar la segunda nota ? \n 1. Si \n 2. No'))
                    if elec1_3 == 1:
                        o =  float(input('Ingrese la segunda nota: '))
                        midic = { 'Primera Nota': y ,'Segunda Nota': o,'Tercera Nota': e}
                        correc1_1_1 = y + o + e 
                        prom1_1_1=float(correc1_1_1) / 3
                        print(midic)
                        print('El prmedio de ',nombre,' es: ',  prom1_1_1)
                    else:
                        print(midic)
                        print('El prmedio de ',nombre,' es: ',  prom1_1)
                if pregunta == 2:
                        o =  float(input('Ingrese la segunda nota: '))
                        midic = { 'Primera Nota': a ,'Segunda Nota': o,'Tercera Nota': e}
                        correc1_1_1 = a + o + e 
                        prom1_1_1=float(correc1_1_1) / 3
                        elec1_4=int(input('Desea cambiar la primera nota ? \n 1. Si \n 2. No'))
                        if elec1_4 == 1:
                            y =  float(input('Ingrese la segunda nota: '))
                            midic = { 'Primera Nota': y ,'Segunda Nota': o,'Tercera Nota': e}
                            correc1_1_2 = y + o + e 
                            prom1_1_2=float(correc1_1_2) / 3
                            print(midic)
                            print('El prmedio de ',nombre,' es: ',  prom1_1_2)
                        else:
                            print(midic)
                            print('El prmedio de ',nombre,' es: ',  prom1_1_1)
            else:
                print(midic)
                print('El prmedio de ',nombre,' es: ',  prom1 )
    if elec1_1 == 3:
        print('Se elimino satisfactoriamente la materia. ')            
if elec == 2:
    print('Se elimino satisfactoriamente la materia. ')