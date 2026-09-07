RUAS = [
    "Gotham City",
    "Coast City",
    "Metropoles",
    "Central City",
    "Star City",
    "Bludhaven",
    "Smallville",
    "Vila Sésamo",
    "Tatooine",
    "Naboo",
]


def _parse_no(nome_no):
    i_str, j_str = nome_no[1:].split("-")
    return int(i_str), int(j_str)


def gerar_enderecos(G):
    no_para_endereco = {}
    for no in G.nodes:
        i, j = _parse_no(no)
        rua = RUAS[i % len(RUAS)]
        numero = (j + 1) * 10
        no_para_endereco[no] = f"{rua}, {numero}"

    endereco_para_no = {v: k for k, v in no_para_endereco.items()}
    return no_para_endereco, endereco_para_no


def buscar_enderecos(query, endereco_para_no):
    query_norm = query.strip().lower()
    resultados = [
        (endereco, no)
        for endereco, no in endereco_para_no.items()
        if query_norm in endereco.lower()
    ]
    return sorted(resultados)
