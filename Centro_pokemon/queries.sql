use centropokemon;

-- 20 Consultas do banco de dados

--  1 Listar todos os treinadores
select * from treinador;

--  2 Listar todos os funcionarios
select * from funcionario;

--  3 Listar todos os pokemon
select * from pokemon;

--  4 Listar todos os produtos
select * from produto;

--  5 Listar todos os centros
select * from centro_loja;

--  6 Listar todos os tratamentos
select * from tratamento;

--  7 Listar todas as cobranças e seus tratamentos/ join
select t.*, c.data_hora from tratamento t join cobranca c on t.id = c.tratamento_id;

--  8 Listar todos os pokemons e seus treinadores / join
select * from pokemon p join treinador t on p.treinador_cpf = t.cpf;

--  9 Listar a quantidade de funcionarios que trabalham no mesmo centro / group by
select count(funcionario_cpf) num_func, centro_id from funcionario_has_centro group by centro_id order by num_func desc;

-- 10 Listar quantos tratamentos cada funcionario fez / group by
select count(id) qtd_trat, funcionario_cpf from tratamento group by funcionario_cpf order by qtd_trat desc;

-- 11 Listar os tratamentos e seus respectivos pokemons / join
select * from tratamento t join pokemon p on t.pokemon_id = p.id;

-- 12 Listar os tratamentos e seus respectivos funcionarios / join
select * from tratamento t join funcionario f on t.funcionario_cpf = f.cpf;

-- 13 Listar todos os cartões e seus treinadores / join
select * from cartao c join treinador t on c.treinador_cpf = t.cpf;

-- 14 Listar os pokemons por ordem de mais tratamentos / group by e order by
select count(id) qtd_trat, pokemon_id from tratamento group by pokemon_id order by qtd_trat desc;

-- 15 Listar os pokemons por numero de pokedex / order by
select * from pokemon order by n_pokedex asc;

-- 16 Listar os treinadores por idade / order by
select *, timestampdiff(year, data_nasc, current_timestamp()) idade from treinador order by idade;

-- 17 Listar os treinadores por maior numero de tratamentos / group by e order by
select count(id) qtd_trat, treinador_cpf from tratamento group by treinador_cpf order by qtd_trat desc;

-- 18 Listar e juntar os treinadores que tem a mesma idade / group by
select count(cpf) qtd_idades, timestampdiff(year, data_nasc, current_timestamp()) idade from treinador group by idade order by idade;

-- 19 Listar e juntar os cartões que tem a mesma quantidade de insígnias / group by
select count(treinador_cpf) qtd_trei_insig, qtd_insignias from cartao group by qtd_insignias order by qtd_insignias desc;

-- 20 Listar os produtos por quantidade / order by
select * from produto order by quantidade desc;


-- 3 Views do banco de dados

-- 1 Listar os produtos que tem o preço maior que 10 reais
CREATE VIEW Informacoestreinador AS
SELECT cpf, Nome, data_nasc
FROM treinador;

select * from Informacoestreinador;

-- 2 Listar os produtos que tem menos que 75 unidades no estoque
create view produtos_menos_75_estoque as
select *
from produto
where quantidade < 75;

select * from produtos_menos_75_estoque;

-- 3 Listar as informações dos funcionários
CREATE VIEW Informacoesfuncionario AS
SELECT cpf, Nome, data_nasc,salario,funcao
FROM funcionario;

select * from Informacoesfuncionario;