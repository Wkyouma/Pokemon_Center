select * from tratamento_has_centro;

update cobranca set data_hora = now() where tratamento_id = 4;
update treinador set nome = "Rafaela" where cpf = "13302978901";
update funcionario set funcao = "gerente geral" where cpf = "42940957096";
update pokemon set sexo = "M" where id = 4;
update cartao set qtd_insignias = 4 where treinador_cpf = "07880563954";

delete from cobranca where tratamento_id = 3;
delete from funcionario where cpf = "56914592012";
delete from centro_has_produto where centro_id = 1;
delete from tratamento_has_centro where tratamento_id = 2;
delete from centro_loja where id = 1;