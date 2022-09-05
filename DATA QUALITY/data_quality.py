# -*- coding: utf-8 -*-

""" 
DATA QUALITY
Qualificando e formatando bases para uso e análise

Requirements
__________________________________
pip install xlrd
pip install openpyxl
"""

import pandas as pd
from sqlalchemy import create_engine
import numpy as np


def insert_into_mysql(df, table_name):
    # Database credentials.
    creds = {'usr': '<user>',
             'pwd': '<password>',
             'hst': '<host>',
             'prt': <porta>,
             'dbn': '<database>'}
    
    # MySQL conection string.
    connstr = 'mysql+mysqlconnector://{usr}:{pwd}@{hst}:{prt}/{dbn}?utf-8'

    # Create sqlalchemy engine for MySQL connection.
    engine = create_engine(connstr.format(**creds))
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)


if __name__ == "__main__":

    ## - Entidade Usuario

    # Extract
    # MACINTOSH text
    df_usuario = pd.read_table('DATA/Ds2.txt', encoding = 'macintosh', delimiter = '	')
    df_usuario = df_usuario[['id', 'nome', 'login', 'id_ativo', 'id_sexo']]

    # Format fields
    df_usuario['nome'] = df_usuario['nome'].astype('string')
    df_usuario['login'] = df_usuario['login'].astype('string')
    
    # Load 
    insert_into_mysql(df_usuario, "usuario")


    ## - Entidade Projeto

    # Extract 
    # ISO-8859 text
    df_projeto = pd.read_csv('DATA/Ds1.csv', encoding = 'ISO-8859-1', delimiter = ';')
    df_projeto = df_projeto[['id', 'nome', 'data_inicio', 'data_fim', 'id_usuario']]

    # Format fields
    df_projeto['nome'] = df_projeto['nome'].astype('string')
    df_projeto['data_inicio'] = pd.to_datetime(df_projeto["data_inicio"], format='%d/%m/%y')
    df_projeto['data_fim'] = pd.to_datetime(df_projeto["data_fim"], format='%d/%m/%y')

    # Load 
    insert_into_mysql(df_projeto, "projeto")


    ## - Entidade Atividade

    # Extract
    # Microsoft Excel 2007+ file

    df_atividade = pd.read_excel('DATA/Ds3.xlsx')
    df_atividade = df_atividade[['id', 'nome', 'data_inicio', 'data_fim', 'id_projeto', 'id_usuario']]

    # Format fields
    df_atividade['nome'] = df_atividade['nome'].astype('string')

    # Load 
    insert_into_mysql(df_atividade, "atividade")


    ## - Entidade Nota

    # Extract
    # ASCII text
    df_nota = pd.read_table('DATA/Ds4.txt', encoding = 'ascii', delimiter = '	')
    df_nota = df_nota[['id', 'id_atividade', 'nota1', 'nota2', 'nota3', 'nota4', 'nota_final']]
    # Format fields
    df_nota['nota1'] = df_nota['nota1'].astype(float)
    df_nota['nota2'] = df_nota['nota2'].astype(float)
    df_nota['nota3'] = df_nota['nota3'].astype(float)
    df_nota['nota4'] = df_nota['nota4'].astype(float)
    df_nota['nota_final'] = df_nota['nota_final'].astype(float)

    # Load 
    insert_into_mysql(df_nota, "nota")


    ## - Entidade Endereco

    # Extract
    # UTF-8 text
    df_endereco = pd.read_csv('DATA/Enderecos.csv', encoding = 'utf-8', delimiter = '|')
    # Format fields
    df_endereco['estado'] = df_endereco['estado'].astype('string')
    df_endereco['cidade'] = df_endereco['cidade'].astype('string')
    df_endereco['bairro'] = df_endereco['bairro'].astype('string')
    df_endereco['rua'] = df_endereco['rua'].astype('string')
    df_endereco['cep'] = df_endereco['cep'].astype('string')

    # Load 
    insert_into_mysql(df_nota, "nota")