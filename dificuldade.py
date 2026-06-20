import fase


def obter_nivel():

    progresso = fase.obter_progresso()

    if progresso < 0.33:
        return "facil"

    elif progresso < 0.66:
        return "medio"

    else:
        return "dificil"


def obter_intervalo_spawn():

    nivel = obter_nivel()

    if nivel == "facil":
        return (4.5, 6.5)

    elif nivel == "medio":
        return (3.8, 5.2)

    return (3.0, 4.2)


def obter_chance_tronco():

    nivel = obter_nivel()

    if nivel == "facil":
        return 0.06

    elif nivel == "medio":
        return 0.08

    return 0.10