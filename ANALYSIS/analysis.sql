-- Analysis MySQL

-- USE <table_name>;

-- Quais são todos os projetos com suas atividades?
SELECT projeto.nome as nome_projeto, 
	   projeto.data_inicio as data_inicio_projeto,
       projeto.data_fim as data_fim_projeto, 
       atividade.nome as atividade,
       atividade.data_inicio as data_inicio_atividade,
       atividade.data_fim as data_fim_atividade 
	FROM projeto 
    INNER JOIN atividade 
       ON projeto.id = atividade.id_projeto;

-- Todas as atividades do usuário “oescolhido@letrus.com” no ano de 2022
SELECT atividade.nome as nome_atividade
	FROM atividade 
    INNER JOIN usuario 
       ON atividade.id_usuario = usuario.id
    WHERE usuario.login = "oescolhido@letrus.com" AND
          EXTRACT(YEAR FROM atividade.data_inicio) = 2022 AND
          EXTRACT(YEAR FROM atividade.data_fim) = 2022;

-- Quantidade de atividades por projeto do ano 2021
SELECT projeto.id as nome_projeto,
	   count(atividade.id) as num_atividades	    	
	FROM projeto
    INNER JOIN atividade
    	ON projeto.id = atividade.id_projeto
    GROUP BY projeto.id;

-- Exclua o projeto “LetrusTIC”
DELETE FROM projeto WHERE nome = 'LetrusTIC';

