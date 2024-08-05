-- Procedures

-- 1 Inserir cartão e treinador ao mesmo tempo
delimiter $$
create procedure insert_treinador_cartao (in _cpf varchar(11), in _rg varchar(10), in _nome varchar(50),
	in _telefone varchar(12), _data_nasc date, in _estado varchar(45), in _cidade varchar(45),
    in _bairro varchar(45), in _rua varchar(45), in _qtd_pokemon int, in _qtd_vitorias int, in _qtd_insignias int)
begin
	insert into treinador
    values (_cpf, _rg, _nome, _telefone, _data_nasc, _estado, _cidade, _bairro, _rua);
    insert into cartao
    values (_qtd_pokemon, _qtd_vitorias, _qtd_insignias, _cpf);
end
$$ delimiter ;

call insert_treinador_cartao ("00000000010", "0000010", "nome10", "129487125481", "1973-07-25", "PR",
	"Curitiba", "Centro", "Rua Centro", 4, 2, 2);


-- 2 Registrar um tratamento e uma cobrança ao mesmo tempo
delimiter $$
create procedure insert_tratamento_cobranca (in _valor decimal, in _treinador_cpf varchar(11),
	in _funcionario_cpf varchar(11), in _pokemon_id int)
begin
	declare id_insercao int;
	insert into tratamento
    values (null, now(), _valor, _treinador_cpf, _funcionario_cpf, _pokemon_id);
    set id_insercao = last_insert_id();
    insert into cobranca
    values (id_insercao, now());
end
$$ delimiter ;

call insert_tratamento_cobranca (30, "07880563954", "57691346077", 2);


-- 3 Insere um produto dentro de um centro junto
delimiter $$
create procedure insert_produto_centro (in _nome varchar(50), in _quantidade int, in _preco decimal,
	in _centro_id int, in _centro_cnpj varchar(14))
begin
    declare id_insercao int;
    insert into produto values (null, _nome, _quantidade, _preco);
    set id_insercao = last_insert_id();
    insert into centro_has_produto values (_centro_id, _centro_cnpj, id_insercao);
end
$$ delimiter ;

call produto_centro ("produto2", 44, 24.3, 1, 13990662000106);
select * from produto;
select * from centro_has_produto order by centro_id;

drop procedure produto_centro;


-- Functions

-- 1 Fala se certo produto está disponível ou não
delimiter $$
create function produto_disponivel (_id int)
returns bool deterministic
begin
	declare dispo bool;
		if (select quantidade from produto where produto.id = _id) > 0 
			then set dispo = true;
		else
			set dispo = false;
    end if;
    return dispo;
end
$$ delimiter ;
select produto_disponivel(1);
update produto set quantidade = 0 where id = 7;
select * from produto;


-- 2 Calcula a Idade
DELIMITER //
CREATE FUNCTION CalcularIdade(data_nasc DATE)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE Idade INT;
    SET Idade = YEAR(CURDATE()) - YEAR(data_nasc);
    IF MONTH(data_nasc) > MONTH(CURDATE()) OR (MONTH(data_nasc) = MONTH(CURDATE()) AND DAY(data_nasc) > DAY(CURDATE())) THEN
        SET Idade = Idade - 1;
    END IF;
    RETURN Idade;
END;
//
DELIMITER ;
drop function CalcularIdade;
select cpf, nome, data_nasc, CalcularIdade(treinador.data_nasc) from treinador;


-- 3 Retorna a soma dos precos dos produtos vezes a quantidade
DELIMITER //
CREATE FUNCTION SomarPrecosProduto()
RETURNS DECIMAL
DETERMINISTIC
BEGIN
    DECLARE soma DECIMAL;
    SELECT SUM(p.preco * p.quantidade) INTO soma FROM produto p;
    RETURN soma;
END;
//
DELIMITER ;
drop function SomarPrecosProduto;
SELECT SomarPrecosProduto() AS SomaDosPrecos;
select * from produto;


-- Triggers

-- 1 Aumenta o número de pokemons no cartao quando insere um pokemon novo
DELIMITER //
CREATE TRIGGER aumentar_quantidade_pokemon
AFTER INSERT ON pokemon
FOR EACH ROW
BEGIN
    UPDATE cartao
    SET cartao.qtd_pokemon = cartao.qtd_pokemon + 1
    WHERE cartao.treinador_cpf = new.treinador_cpf;
END;
//
DELIMITER ;

insert into pokemon values (null, "teste5", "m", 1, "fogo", "00000000010");
select * from cartao;

-- 2 Atualiza o nome para lower
DELIMITER //
CREATE TRIGGER AtualizarCampo
BEFORE UPDATE ON treinador
FOR EACH ROW
BEGIN
    SET NEW.nome = lower(NEW.nome);
END;
//
DELIMITER ;

UPDATE treinador
SET nome = 'igor'
WHERE treinador.cpf = '00000000010';
select * from treinador;


-- 3 Faltando