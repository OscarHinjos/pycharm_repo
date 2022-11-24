
def devolver_info_alumno():
    f = open("../alumnos-colegio.txt", "r", encoding="UTF-8")
    info_alumnos = f.readlines()
    info =[]
    materia = []
    materia2 = []
    info2 = []

    for informacion in info_alumnos:
        info.append(informacion[: informacion.rfind("|") + 1])
        materia.append(informacion[informacion.rfind("|") + 1:].replace("\n", ""))

    for mate in materia:
        materia2.append(mate.split(";"))

    for inf in info:
        info2.append(inf.split("|"))

    for i, inf2 in enumerate(info2):
        inf2.pop()
        inf2.append(materia2[i])

    return info2


lista_info = devolver_info_alumno()
