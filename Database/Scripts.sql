
-- Criar tabela de cartas

CREATE TABLE POKEMONS.CARTAS
(
    ID_NAME     SERIAL        PRIMARY KEY
  , NAME        VARCHAR(300)  NOT NULL
  , STATUS      VARCHAR(300)  NOT NULL

);


-- Inserir dados tabela de cartas
INSERT INTO pokemons.CARTAS (NAME, STATUS)
VALUES  ('Charmander', 'ativo');