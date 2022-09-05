-- Script MySQL

-- USE <table_name>;

-- sexo
CREATE TABLE sexo (
    id int NOT NULL,
    descricao varchar(255),
    PRIMARY KEY (id)
);

-- ativo
CREATE TABLE ativo (
    id int NOT NULL,
    descricao varchar(255),
    PRIMARY KEY (id)
);

-- usuario
CREATE TABLE usuario (
    id int NOT NULL,
    nome varchar(255),
    login varchar(255),
    id_ativo int,
    id_sexo int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_ativo) REFERENCES ativo(id),
    FOREIGN KEY (id_sexo) REFERENCES sexo(id)
);

-- projeto
CREATE TABLE projeto (
    id int NOT NULL,
    nome varchar(255),
    data_inicio date,
    data_fim date,
    id_usuario int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);

-- atividade
CREATE TABLE atividade (
    id int NOT NULL,
    nome varchar(255),
    data_inicio date,
    data_fim date,
    id_projeto int,
    id_usuario int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_projeto) REFERENCES projeto(id),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);

-- nota
CREATE TABLE nota (
    id_nota int NOT NULL,
    id_atividade int,
    nota1 float,
    nota2 float,
    nota3 float,
    nota4 float,
    nota_final float,
    PRIMARY KEY (id_nota),
    FOREIGN KEY (id_atividade) REFERENCES atividade(id)
);