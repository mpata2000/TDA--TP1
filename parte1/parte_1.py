import sys

def leer_habilidades(path):
    habilidades = set()

    with open(path, 'r') as archivo:
        for linea in archivo:
            id_hab, nombre_hab = linea.strip().split(',')
            habilidades.add(int(id_hab))

    return habilidades

def leer_candidatos(path):
    candidatos = []

    with open(path, 'r') as archivo:
        for linea in archivo:
            partes_linea = linea.strip().split(',')
            nombre_cand = partes_linea[0]
            habilidades_cand = set(int(id_hab) for id_hab in partes_linea[1:])
            candidatos.append((nombre_cand, habilidades_cand))

    return candidatos


def obtener_candidatos(habilidades, candidatos):
    def branch_and_bound(nro_cand_actual, hab_cubiertas):
        
        if hab_cubiertas == habilidades:  # Todas las habilidades fueron cubiertas
            return set()
        if nro_cand_actual == len(candidatos):  #Recorrí todos los candidatos
            return None
        
        incluidos = None 
        # Si el candidato aporta por lo menos 1 nueva habilidad, lo incluyo
        if candidatos[nro_cand_actual][1] - hab_cubiertas:
            incluidos = branch_and_bound(nro_cand_actual + 1, hab_cubiertas | candidatos[nro_cand_actual][1])
            if incluidos is not None:
                incluidos.add(candidatos[nro_cand_actual][0])
        # Excluyo al candidato actual
        excluidos = branch_and_bound(nro_cand_actual + 1, hab_cubiertas)
        
        # Comparo ambas soluciones y elijo la mejor
        if excluidos is None or (incluidos is not None and len(incluidos) < len(excluidos)):
            return incluidos
        else:
            return excluidos

    return branch_and_bound(0, set())


#Si no pasaron bien los argumentos, imprimo mensaje y corto la ejecución
if len(sys.argv) != 3:
    print("La cantidad de argumentos ingresados es incorrecta. Debe ingresar el archivo de habilidades y el de candidatos")
    sys.exit(1)

#Leo las habilidades y candidatos de los archivos
habilidades = leer_habilidades(sys.argv[1])
candidatos = leer_candidatos(sys.argv[2])
candidatos = sorted(candidatos, key=lambda x: len(x[1]), reverse=True)

candidatos_seleccionados = obtener_candidatos(habilidades, candidatos)

for candidato in candidatos_seleccionados:
    print(candidato)


