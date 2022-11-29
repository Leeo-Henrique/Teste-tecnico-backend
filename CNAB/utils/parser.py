import datetime


def parserCNAB(cnab: str) -> dict:
    # Dada a string no txt e cortado de acordo a um padrao
    tipo = cnab[0]
    data = cnab[1:9]
    valor = cnab[9:20]
    cpf = cnab[19:30]
    cartao = cnab[30:42]
    hora = cnab[42:48]
    dono_da_loja = cnab[48:62]
    nome_da_loja = cnab[62:81]

    format_valor = int(valor) / 100

    date = f"{data[:4]}-{data[4:6]}-{data[6:]}"

    format_data = datetime.datetime.strptime(date, "%Y-%m-%d")

    format_hora = datetime.time(int(hora[:2]), int(hora[2:4]), int(hora[4:]))

    return {
        "tipo": int(tipo),
        "data": format_data,
        "valor": format_valor,
        "cpf": cpf,
        "cartao": cartao,
        "hora": format_hora,
        "dono_da_loja": dono_da_loja,
        "nome_da_loja": nome_da_loja,
    }
