from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados de exemplo
dados = [
    {
        "id": 1,
        "Remetente_Nome": "BAZAM & PICHAU INFORMATICA LTDA",
        "NF": "3680830",
        "Destinatario_Nome": "FRANCISCA MARIA  GOMES",
        "Destinatario_Documento": "00978657373",
        "Destino_Logradouro": "TRAVESSA UNIAO DO BAIRRO BARCELOS 7 APAR",
        "Destino_Numero": "R",
        "Cidade_Nome": "Rio de Janeiro",
        "Estado_Nome": "Rio de Janeiro"
    },
    {
        "id": 2,
        "Remetente_Nome": "ICARO EXPRESS LOGISTICS LTDA",
        "NF": "123",
        "Destinatario_Nome": "ICARO EXPRESS LOGISTICS LTDA",
        "Destinatario_Documento": "06225952000513",
        "Destino_Logradouro": "ESTRADA DO TIMBO",
        "Destino_Numero": "123",
        "Cidade_Nome": "Rio de Janeiro",
        "Estado_Nome": "Rio de Janeiro"
    },
    {
        "id": 3,
        "Remetente_Nome": "WHITENESS DO BRASIL INDUSTRIA LTDA",
        "NF": "5634",
        "Destinatario_Nome": "DENTSCARE LTDA",
        "Destinatario_Documento": "05106945000297",
        "Destino_Logradouro": "RUA DONA FRANCISCA",
        "Destino_Numero": "8300",
        "Cidade_Nome": "Joinville",
        "Estado_Nome": "Santa Catarina"
    },
    {
        "id": 4,
        "Remetente_Nome": "WHITENESS DO BRASIL INDUSTRIA LTDA",
        "NF": "5635",
        "Destinatario_Nome": "WHITENESS DO BRASIL INDUSTRIA LTDA",
        "Destinatario_Documento": "32256235000216",
        "Destino_Logradouro": "R DONA FRANCISCA",
        "Destino_Numero": "8300",
        "Cidade_Nome": "Joinville",
        "Estado_Nome": "Santa Catarina"
    },
    {
        "id": 5,
        "Remetente_Nome": "WHITENESS DO BRASIL INDUSTRIA LTDA",
        "NF": "0258",
        "Destinatario_Nome": "DENTSCARE LTDA",
        "Destinatario_Documento": "05106945000106",
        "Destino_Logradouro": "AV EDGAR NELSON MEISTER",
        "Destino_Numero": "474",
        "Cidade_Nome": "Joinville",
        "Estado_Nome": "Santa Catarina"
    },
    {
        "id": 6,
        "Remetente_Nome": "JCS BRASIL ELETRODOMESTICOS LTDA",
        "NF": "808121",
        "Destinatario_Nome": "ADRIANA BRITO",
        "Destinatario_Documento": "29759367882",
        "Destino_Logradouro": "ESTRADA NAIM KHAIRALLA,1550",
        "Destino_Numero": "1550",
        "Cidade_Nome": "Mairipora",
        "Estado_Nome": "Sao Paulo"
    },
    {
        "id": 7,
        "Remetente_Nome": "WHITENESS DO BRASIL INDUSTRIA LTDA",
        "NF": "0259",
        "Destinatario_Nome": "DENTSCARE LTDA",
        "Destinatario_Documento": "05106945000106",
        "Destino_Logradouro": "AV EDGAR NELSON MEISTER",
        "Destino_Numero": "474",
        "Cidade_Nome": "Joinville",
        "Estado_Nome": "Santa Catarina"
    },
    {
        "id": 8,
        "Remetente_Nome": "WHITENESS DO BRASIL INDUSTRIA LTDA",
        "NF": "0260",
        "Destinatario_Nome": "DENTSCARE LTDA",
        "Destinatario_Documento": "05106945000106",
        "Destino_Logradouro": "AV EDGAR NELSON MEISTER",
        "Destino_Numero": "474",
        "Cidade_Nome": "Joinville",
        "Estado_Nome": "Santa Catarina"
    },
    {
        "id": 9,
        "Remetente_Nome": "DENTSCARE LTDA",
        "NF": "18025, 18026, 18027",
        "Destinatario_Nome": "DENTSCARE LTDA",
        "Destinatario_Documento": "05106945000297",
        "Destino_Logradouro": "RUA DONA FRANCISCA",
        "Destino_Numero": "8300",
        "Cidade_Nome": "Joinville",
        "Estado_Nome": "Santa Catarina"
    },
    {
        "id": 10,
        "Remetente_Nome": "JCS BRASIL ELETRODOMESTICOS LTDA",
        "NF": "941256",
        "Destinatario_Nome": "IVETE DE CASSIA CASTANO COUTO",
        "Destinatario_Documento": "07838105803",
        "Destino_Logradouro": "MEXICO",
        "Destino_Numero": "50",
        "Cidade_Nome": "Mairipora",
        "Estado_Nome": "Sao Paulo"
    },
    {
        "id": 11,
        "Remetente_Nome": "JCS BRASIL ELETRODOMESTICOS LTDA",
        "NF": "810630",
        "Destinatario_Nome": "TIAGO VANTI PRISCO",
        "Destinatario_Documento": "28432225835",
        "Destino_Logradouro": "RUA AMELIO KOGA",
        "Destino_Numero": "251",
        "Cidade_Nome": "Sao Paulo",
        "Estado_Nome": "Sao Paulo"
    },
    {
        "id": 12,
        "Remetente_Nome": "JCS BRASIL ELETRODOMESTICOS LTDA",
        "NF": "1459",
        "Destinatario_Nome": "EDUARDO  COTTA",
        "Destinatario_Documento": "07597718632",
        "Destino_Logradouro": "RUA PIUMI,1201",
        "Destino_Numero": "1201",
        "Cidade_Nome": "Belo Horizonte",
        "Estado_Nome": "Minas Gerais"
    },
    {
        "id": 13,
        "Remetente_Nome": "BUD COMERCIO DE ELETRODOMESTICOS LTDA",
        "NF": "3906197",
        "Destinatario_Nome": "JAQUELINE NOGUEIRA BRAGA BATISTA",
        "Destinatario_Documento": "15386016806",
        "Destino_Logradouro": "RUA MARIO AUGUSTO MUNIZ DE ARAGAO 527",
        "Destino_Numero": "527",
        "Cidade_Nome": "Campinas",
        "Estado_Nome": "Sao Paulo"
    },
    {
        "id": 14,
        "Remetente_Nome": "BUD COMERCIO DE ELETRODOMESTICOS LTDA",
        "NF": "3906204",
        "Destinatario_Nome": "JESSICA SANTOS NASCIMENTO MELO",
        "Destinatario_Documento": "03482672580",
        "Destino_Logradouro": "RUA PEDRO BRAGA 151",
        "Destino_Numero": "151",
        "Cidade_Nome": "Campinas",
        "Estado_Nome": "Sao Paulo"
    },
    {
        "id": 15,
        "Remetente_Nome": "BUD COMERCIO DE ELETRODOMESTICOS LTDA",
        "NF": "3906198",
        "Destinatario_Nome": "JERUSA DE NAZARE SILVA JACINTO",
        "Destinatario_Documento": "12044034816",
        "Destino_Logradouro": "RUA MARY HEZKIEL LEVY ZEITOUNI 183",
        "Destino_Numero": "183",
        "Cidade_Nome": "Campinas",
        "Estado_Nome": "Sao Paulo"
    },
    {
        "id": 16,
        "Remetente_Nome": "BUD COMERCIO DE ELETRODOMESTICOS LTDA",
        "NF": "3906194",
        "Destinatario_Nome": "ROSEMEIRE CAMPIONI",
        "Destinatario_Documento": "06199079833",
        "Destino_Logradouro": "RUA DONA AMELIA DE PAULA 235",
        "Destino_Numero": "235",
        "Cidade_Nome": "Campinas",
        "Estado_Nome": "Sao Paulo"
    },
    {
        "id": 17,
        "Remetente_Nome": "BUD COMERCIO DE ELETRODOMESTICOS LTDA",
        "NF": "3906201",
        "Destinatario_Nome": "VALMIRA DIAS DOS SANTOS PIRES",
        "Destinatario_Documento": "34888135843",
        "Destino_Logradouro": "RUA GESSI DA SILVA DURAES 284",
        "Destino_Numero": "284",
        "Cidade_Nome": "Campinas",
        "Estado_Nome": "Sao Paulo"
    },
    {
        "id": 18,
        "Remetente_Nome": "BUD COMERCIO DE ELETRODOMESTICOS LTDA",
        "NF": "3906192",
        "Destinatario_Nome": "NILCIENE FIGUEIREDO",
        "Destinatario_Documento": "17189956875",
        "Destino_Logradouro": "RUA MARIA RIBAS CAVALHEIRO 98",
        "Destino_Numero": "98",
        "Cidade_Nome": "Campinas",
        "Estado_Nome": "Sao Paulo"
    },
    {
        "id": 19,
        "Remetente_Nome": "BUD COMERCIO DE ELETRODOMESTICOS LTDA",
        "NF": "3906200",
        "Destinatario_Nome": "VALMIRA DIAS DOS SANTOS PIRES",
        "Destinatario_Documento": "34888135843",
        "Destino_Logradouro": "RUA GESSI DA SILVA DURAES 284",
        "Destino_Numero": "284",
        "Cidade_Nome": "Campinas",
        "Estado_Nome": "Sao Paulo"
    },
    {
        "id": 20,
        "Remetente_Nome": "BUD COMERCIO DE ELETRODOMESTICOS LTDA",
        "NF": "3906202",
        "Destinatario_Nome": "ALBERTO CITRONI",
        "Destinatario_Documento": "22638211800",
        "Destino_Logradouro": "RUA CELEIDA MALAGUTI BECK 91",
        "Destino_Numero": "91",
        "Cidade_Nome": "Campinas",
        "Estado_Nome": "Sao Paulo"
    }
]
# Rota principal para retornar todos os dados com filtros
@app.route('/api/dados', methods=['GET'])
def get_dados():
    # Obter parâmetros de consulta
    destinatario_documento = request.args.get('Destinatario_Documento')
    nf = request.args.get('NF')

    # Filtrar dados
    resultados = dados

    if destinatario_documento:
        resultados = [d for d in resultados if d["Destinatario_Documento"] == destinatario_documento]
    
    if nf:
        resultados = [d for d in resultados if d["NF"] == nf]

    return jsonify(resultados)

# Rota para retornar um único registro pelo ID
@app.route('/api/dados/<int:id>', methods=['GET'])
def get_dado_por_id(id):
    dado = next((item for item in dados if item["id"] == id), None)
    if dado:
        return jsonify(dado)
    else:
        return jsonify({"error": "Dado não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)