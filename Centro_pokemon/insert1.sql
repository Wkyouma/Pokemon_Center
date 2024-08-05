use centropokemon;

insert into treinador
values ("06592398922", "378578340", "Jonas", "998690267", "1997-10-17", "PR", "Colombo", "Guaraituba", "Leonidas Alberti");

insert into treinador
values ("07880563954", "8546982", "Gabriel", "9999999999", "2005-05-07", "PR", "Curitiba", "Boqueirão", "Oliveira Viana");

insert into treinador
values ("13302978901", "888888888", "Igor", "91246140", "2004-10-30", "PR", "Curitiba", "Juvevê", "Conselheiro Carrão");

insert into treinador
values ("04431381252", "777777777", "Antonio", "981024233", "2005-04-26", "PR", "Curitiba", "Boqueirão", "Salvador Ferrante");

insert into treinador
values ("01234567891", "666666666", "Marcelly", "985201478", "2000-05-24", "SP", "Santos", "Centro", "Avenida Brasil");

insert into treinador
values ("06592397950", "578346589", "Jonatas", "999160029", "1991-12-04", "SP", "São Bernardo do Campo", "Centro", "Marechal Deodoro");

insert into pokemon
values (null, "Empoleon", "M", 114, "agua e aço", "06592398922");

insert into pokemon
values (null, "Lucario", "M", 123, "lutador e aço", "07880563954");

insert into pokemon
values (null, "Zoruark", "M", 2, "sombrio", "04431381252");

insert into pokemon
values (null, "Greninja", "F", 5, "agua e sombrio", "13302978901");

insert into pokemon
values (null, "Dialga", "M", 9, "aço", "01234567891");

insert into pokemon
values (null, "Charizard", "F", 7, "fogo e voador", "06592397950");

insert into produto
values (null, "poção", 99, 100);

insert into produto
values (null, "reviver", 99, 300);

insert into produto
values (null, "pokebola", 99, 50);

insert into produto
values (null, "antidodo", 99, 75);

insert into produto
values (null, "repelente", 99, 50);

insert into produto
values (null, "bicicleta", 10, 1000);

insert into centro_loja
values (null, "13990662000106", 2);

insert into centro_loja
values (null, "69306570000100", 2);

insert into centro_loja
values (null, "73414826000170", 4);

insert into centro_loja
values (null, "19983617000100", 4);

insert into centro_loja
values (null, "80085833000131", 6);

insert into centro_loja
values (null, "29043459000154", 6);

insert into funcionario
values ("57691346077", "1111111111", "Leila", 2300.00, "041915616561", "2001-05-26", "atendente", "pr", "curitiba", "centro", "XV de novembro");

insert into funcionario
values ("24263941020", "2222222222", "Sergio", 2300.00, "041998746512", "2000-10-08", "atendente", "pr", "curitiba", "agua verde", "avenida republica argentina");

insert into funcionario
values ("05649238006", "3333333333", "Natalia", 3700.0, "041312546879", "1997-07-12", "gerente", "pr", "curitiba", "cabral", "rua dos funcionarios");

insert into funcionario
values ("42940957096", "4444444444", "Cintia", 1800.0, "041914253653", "2004-04-14", "vendedor", "pr", "curitiba", "centro", "alameda dr muricy");

insert into funcionario
values ("91343155002", "5555555555", "Tereza", 5500.0, "041645254521", "1995-02-03", "coordenador", "pr", "curitiba", "batel", "alameda princesa izabel");

insert into funcionario
values ("56914592012", "6666666666", "Akira", 7000.0, "041924345634", "1991-11-11", "gerente geral", "pr", "curitiba", "juveve", "augusto stresser");

insert into tratamento
values (null, now(), 150.0, "07880563954", "57691346077", 1);

insert into tratamento
values (null, now(), 780.0, "06592397950", "57691346077", 2);

insert into tratamento
values (null, now(), 75.0, "01234567891", "24263941020", 3);

insert into tratamento
values (null, now(), 50.0, "06592398922", "42940957096", 4);

insert into tratamento
values (null, now(), 230.0, "07880563954", "24263941020", 5);

insert into tratamento
values (null, now(), 490.0, "06592397950", "24263941020", 6);

insert into cartao
values (0, 367, 8, "06592398922");

insert into cartao
values (0, 124, 3, "07880563954");

insert into cartao
values (0, 210, 5, "13302978901");

insert into cartao
values (0, 326, 7, "04431381252");

insert into cartao
values (0, 652, 8, "01234567891");

insert into cartao
values (0, 97, 2, "06592397950");



