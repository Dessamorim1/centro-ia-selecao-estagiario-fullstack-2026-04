def classificar_popularidade(qtd):
    if qtd < 3:
        return "baixa"
    elif qtd < 10:
        return "media"
    else:
        return "alta"   