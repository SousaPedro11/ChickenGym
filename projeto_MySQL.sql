 
#EXCLUIR BASE
-- drop database if exists academia;

#---------------------------------------------------------------------------------
# CRIACAO DA BASE
-- create database if not exists academia
-- default character set utf8mb4
-- collate utf8mb4_general_ci;

-- CREATE TABLE IF NOT EXISTS academia.unidade (
--     cod SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     nome VARCHAR(120) NOT NULL,
--     fk_endereco SMALLINT UNIQUE NOT NULL,
--     CONSTRAINT ak_unidade UNIQUE (nome , fk_endereco)
-- )  DEFAULT CHARSET UTF8MB4;

-- CREATE TABLE IF NOT EXISTS academia.endereco (
--     cod SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     rua VARCHAR(80) NOT NULL,
--     numero VARCHAR(5) NOT NULL,
--     cep VARCHAR(10) NOT NULL,
--     complemento TEXT,
--     cidade VARCHAR(30),
--     bairro VARCHAR(20),
--     telefone VARCHAR(15) UNIQUE,
--     CONSTRAINT ak_endereco UNIQUE (rua , cep , numero)
-- )  DEFAULT CHARSET UTF8MB4;

-- CREATE TABLE IF NOT EXISTS academia.modalidade (
--     cod SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     categoria VARCHAR(100) NOT NULL,
--     nivel VARCHAR(20),
--     fk_categoria_pai SMALLINT,
--     fk_unidade SMALLINT NOT NULL,
--     fk_professor varchar(10),
--     constraint ak_categoria unique (categoria, fk_unidade, nivel)
-- )  DEFAULT CHARSET UTF8MB4;

-- CREATE TABLE IF NOT EXISTS academia.turma (
--     cod SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     horario TIME NOT NULL,
--     fk_modalidade smallint
-- )  DEFAULT CHARSET UTF8MB4;

-- CREATE TABLE IF NOT EXISTS academia.funcionario (
--     registro VARCHAR(10) NOT NULL PRIMARY KEY,
--     nome VARCHAR(120) NOT NULL,
--     nome_mae VARCHAR(120) NOT NULL,
--     documento_tipo ENUM('RG', 'CPF', 'CNH', 'PASSAPORTE', 'OUTRO'),
--     documento VARCHAR(20) NOT NULL,
--     ativado BOOLEAN DEFAULT TRUE,
--     fk_endereco SMALLINT NOT NULL,
--     cargo smallint not null,
--     CONSTRAINT AK_funcionario UNIQUE (nome , nome_mae , fk_endereco)
-- )  DEFAULT CHARSET UTF8MB4;

-- CREATE TABLE IF NOT EXISTS academia.aluno (
--     matricula VARCHAR(12) NOT NULL PRIMARY KEY,
--     nome VARCHAR(120) NOT NULL,
--     nome_mae VARCHAR(120) NOT NULL,
--     documento_tipo ENUM('RG', 'CPF', 'CNH', 'PASSAPORTE', 'OUTRO'),
--     documento_num VARCHAR(20) NOT NULL,
--     ativado BOOL DEFAULT TRUE,
--     fk_endereco SMALLINT NOT NULL,
--     fk_plano smallint not null,
--     CONSTRAINT AK_funcionario UNIQUE (nome , nome_mae , fk_endereco)
-- )  DEFAULT CHARSET UTF8MB4;

-- CREATE TABLE IF NOT EXISTS academia.pagamento (
--     cod SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     tipo VARCHAR(10) NOT NULL,
--     vencimento DATE NOT NULL,
--     periodo DATE NOT NULL,
--     status_pagamento ENUM('efetuado', 'atrasado', 'pendente'),
--     fk_aluno varchar(12) not null,
-- 	fk_valor_plano smallint NOT NULL
-- )  DEFAULT CHARSET UTF8MB4;

-- CREATE TABLE IF NOT EXISTS academia.cargo (
--     cod SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     nome VARCHAR(20) NOT NULL
-- )  DEFAULT CHARSET UTF8MB4;

CREATE TABLE IF NOT EXISTS academia.avaliacaofisica (
    cod SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    avaliador VARCHAR(120) NOT NULL,
    data_avaliacao DATE NOT NULL,
    abdominal SMALLINT,
    flexoes_braco SMALLINT,
    altura DECIMAL(3 , 2 ) NOT NULL,
    peso DECIMAL(5 , 2 ) NOT NULL,
    busto DECIMAL(5 , 2 ) NOT NULL,
    braco_esq DECIMAL(4 , 2 ) NOT NULL,
    braco_dir DECIMAL(4 , 2 ) NOT NULL,
    abdomen DECIMAL(5 , 2 ) NOT NULL,
    cintura DECIMAL(5 , 2 ) NOT NULL,
    quadril DECIMAL(5 , 2 ) NOT NULL,
    culote DECIMAL(4 , 2 ) NOT NULL,
    coxa_esq DECIMAL(4 , 2 ) NOT NULL,
    coxa_dir DECIMAL(4 , 2 ) NOT NULL,
    panturrilha_esq DECIMAL(4 , 2 ) NOT NULL,
    panturrilha_dir DECIMAL(4 , 2 ) NOT NULL,
    fk_aluno varchar(12)
)  DEFAULT CHARSET UTF8MB4;

CREATE TABLE IF NOT EXISTS academia.plano (
    cod SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    valor decimal(6, 2) not null
)  DEFAULT CHARSET UTF8MB4;

CREATE TABLE IF NOT EXISTS academia.sala (
    cod SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    numero VARCHAR(5) NOT NULL
)  DEFAULT CHARSET UTF8MB4;

CREATE TABLE IF NOT EXISTS academia.ficha (
    cod SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    data_elaboracao DATE NOT NULL,
    fk_aluno VARCHAR(12) NOT NULL
)  DEFAULT CHARSET UTF8MB4;

CREATE TABLE IF NOT EXISTS academia.aparelho (
    cod SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    fabricante VARCHAR(20) NOT NULL,
    modelo VARCHAR(20) NOT NULL
)  DEFAULT CHARSET UTF8MB4;

#---------------------------------------------------------------------------------
#DEFINICAO DE TABELAS INTERMEDIARIAS
CREATE TABLE IF NOT EXISTS academia.linha_ficha (
    cod SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fk_aparelho SMALLINT,
    fk_ficha SMALLINT,
    ciclo1 DECIMAL(5 , 2 ),
    ciclo2 DECIMAL(5 , 2 ),
    ciclo3 DECIMAL(5 , 2 ),
    ciclo4 DECIMAL(5 , 2 )
)  DEFAULT CHARSET UTF8MB4;

CREATE TABLE IF NOT EXISTS academia.modalidade_sala (
    cod SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fk_modalidade SMALLINT,
    fk_sala SMALLINT
)  DEFAULT CHARSET UTF8MB4;

CREATE TABLE IF NOT EXISTS academia.modalidade_sala (
    cod SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fk_modalidade SMALLINT,
    fk_sala SMALLINT
)  DEFAULT CHARSET UTF8MB4;

CREATE TABLE IF NOT EXISTS academia.turma_sala (
    cod SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fk_turma SMALLINT,
    fk_sala SMALLINT
)  DEFAULT CHARSET UTF8MB4;

CREATE TABLE IF NOT EXISTS academia.plano_turma (
    cod SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fk_plano SMALLINT,
    fk_turma SMALLINT
)  DEFAULT CHARSET UTF8MB4;

CREATE TABLE IF NOT EXISTS academia.plano_modalidade (
    cod SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fk_modalidade SMALLINT,
    fk_plano SMALLINT
)  DEFAULT CHARSET UTF8MB4;

CREATE TABLE IF NOT EXISTS academia.plano_aluno (
    cod SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fk_plano SMALLINT,
    fk_aluno VARCHAR(12)
)  DEFAULT CHARSET UTF8MB4;

CREATE TABLE IF NOT EXISTS academia.funcionario_modalidade (
    cod SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fk_funcionario VARCHAR(12),
    fk_modalidade SMALLINT
)  DEFAULT CHARSET UTF8MB4;
#---------------------------------------------------------------------------------
#DEFINICAO DE CONSTRAINTS
## CHECK
alter table academia.funcionario
add constraint CH_funcionario_tipo_doc
check(documento_tipo IN ('RG','CPF','CNH','PASSAPORTE', 'OUTRO'));

alter table academia.aluno
add constraint CH_aluno_tipo_doc
check(documento_tipo IN ('RG','CPF','CNH','PASSAPORTE', 'OUTRO'));

alter table academia.pagamento
add constraint CH_pagamento_status
check(status_pagamento IN ('efetuado', 'atrasado', 'pendente'));

## FOREIGN KEYS
### TABELAS NORMAIS
alter table academia.modalidade
add constraint FK_modalidade_categoria foreign key (fk_categoria_pai)
references academia.modalidade (cod)
on update no action
on delete no action
;

alter table academia.modalidade
add constraint FK_modalidade_unidade foreign key (fk_unidade)
references academia.unidade (cod)
on update no action
on delete no action
;

alter table academia.turma
add constraint FK_turma_modalidade foreign key (fk_modalidade)
references academia.modalidade (cod)
on update no action
on delete no action
;

alter table academia.pagamento
add constraint FK_pagamento_aluno foreign key (fk_aluno)
references academia.aluno (matricula)
on update no action
on delete no action
;

alter table academia.pagamento
add constraint FK_pagamento_plano foreign key (fk_valor_plano)
references academia.plano (cod)
on update no action
on delete no action
;

alter table academia.aluno
add constraint FK_aluno_endereco foreign key (fk_endereco)
references academia.endereco (cod)
on update no action
on delete no action
;

alter table academia.aluno
add constraint FK_aluno_plano foreign key (fk_plano)
references academia.plano (cod)
on update no action
on delete no action
;

alter table academia.funcionario
add constraint FK_funcionario_endereco foreign key (fk_endereco)
references academia.endereco (cod)
on update no action
on delete no action
;

alter table academia.avaliacaofisica
add constraint FK_avaliacaofisica_aluno foreign key (fk_aluno)
references academia.aluno (matricula)
on update no action
on delete no action
;

alter table academia.ficha
add constraint FK_ficha_aluno foreign key (fk_aluno)
references academia.aluno (matricula)
on update no action
on delete no action
;

### TABELAS INTERMEDIARIAS
alter table academia.linha_ficha
add constraint FK_linha_ficha_ficha foreign key (fk_ficha)
references academia.ficha(cod);

alter table academia.linha_ficha
add constraint FK_linha_ficha_aparelho foreign key (fk_aparelho)
references academia.aparelho(cod);

alter table academia.modalidade_sala
add constraint FK_modalidade_sala_mod foreign key (fk_modalidade)
references academia.modalidade(cod);

alter table academia.modalidade_sala
add constraint FK_modalidade_sala_sala foreign key (fk_sala)
references academia.sala(cod);

alter table academia.turma_sala
add constraint FK_turma_sala_sala foreign key (fk_sala)
references academia.sala(cod);

alter table academia.turma_sala
add constraint FK_turma_sala_turma foreign key (fk_turma)
references academia.turma(cod);

alter table academia.plano_turma
add constraint FK_plano_turma_turma foreign key (fk_turma)
references academia.turma(cod);

alter table academia.plano_turma
add constraint FK_plano_turma_plano foreign key (fk_plano)
references academia.plano(cod);

alter table academia.plano_modalidade
add constraint FK_plano_modalidade_plano foreign key (fk_plano)
references academia.plano(cod);

alter table academia.plano_modalidade
add constraint FK_plano_modalidade_modalidade foreign key (fk_modalidade)
references academia.modalidade(cod);

alter table academia.plano_aluno
add constraint FK_plano_aluno_aluno foreign key (fk_aluno)
references academia.aluno(matricula);

alter table academia.plano_aluno
add constraint FK_plano_aluno_plano foreign key (fk_plano)
references academia.plano(cod);

alter table academia.funcionario_modalidade
add constraint FK_funcionario_modalidade_funcionario foreign key (fk_funcionario)
references academia.funcionario(registro);

alter table academia.funcionario_modalidade
add constraint FK_funcionario_modalidade_modalidade foreign key (fk_modalidade)
references academia.modalidade(cod);
