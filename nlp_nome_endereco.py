import spacy, re
nlp_pt = spacy.load("pt_core_news_lg")
s_pt = """
EXCELENTÍSSIMO SR DR JUIZ DE DIREITO DA 6ª VARA DA FAZENDA PÚBLICA DA COMARCA DA CAPITAL – SÃO PAULO

MANDADO DE SEGURANÇA
PROCESSO Nº 1007898-19.2022.8.26.0053

HUNO MOLINA RODRIGUES DOS SANTOS, dentista, portador do RG nº 12.345.678-9, inscrito no CPF/MF sob nº 123.456.789-10, residente e domiciliado na Rua dos Enforcados, nº 21, CEP 02104-010, por seu procurador, vem propor a presente
AÇÃO DE COBRANÇA,
Em face do Município de São Paulo, pessoa jurídica de direito público, CNPJ nº 12.345.678/0001-01, com sede no Viaduto do Chá, s/ n.
SEI 6029.2024/0016634-1
Autos 2276828-82.2024.8.26.0000 (1)

CRM 60159 

São Paulo, 30 de nov. de 24
Rui Barbosa

OAB/SP 12.345
"""
doc_pt = nlp_pt(s_pt)
ner = [(ent.text, ent.label_) for ent in doc_pt.ents]

lista_excep = ["SP","SÃO PAULO", "RG" , "MUNICÍPIO DE SÃO PAULO"]

for i in ner: 
     if i[1] == "PER" and i[0].upper() not in lista_excep:
        s_pt = re.sub(i[0], "<< nome >>", s_pt, flags=re.IGNORECASE)
        
for i in ner:
    if i[1] == "LOC" and i[0].upper() not in lista_excep:
        s_pt = re.sub(i[0], "<< local >>", s_pt, flags=re.IGNORECASE)

print(s_pt)