-- MySQL Script generated by MySQL Workbench
-- Wed Oct 25 13:48:38 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema centroPokemon
-- -----------------------------------------------------
-- drop schema centropokemon;
-- -----------------------------------------------------
-- Schema centroPokemon
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `centroPokemon` DEFAULT CHARACTER SET utf8 ;
USE `centroPokemon` ;

-- -----------------------------------------------------
-- Table `centroPokemon`.`treinador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `centroPokemon`.`treinador` (
  `cpf` VARCHAR(11) NOT NULL,
  `rg` VARCHAR(10) NOT NULL,
  `nome` VARCHAR(50) NOT NULL,
  `telefone` VARCHAR(12) NOT NULL,
  `data_nasc` DATE NOT NULL,
  `estado` VARCHAR(45) NULL,
  `cidade` VARCHAR(45) NULL,
  `bairro` VARCHAR(45) NULL,
  `rua` VARCHAR(45) NULL,
  PRIMARY KEY (`cpf`),
  UNIQUE INDEX `cpf_UNIQUE` (`cpf` ASC) VISIBLE,
  UNIQUE INDEX `telefone_UNIQUE` (`telefone` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `centroPokemon`.`pokemon`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `centroPokemon`.`pokemon` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(50) NOT NULL,
  `sexo` CHAR(1) NOT NULL,
  `n_pokedex` TINYINT UNSIGNED NOT NULL,
  `tipo` VARCHAR(50) NOT NULL,
  `treinador_cpf` VARCHAR(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `Id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_pokemon_treinador1_idx` (`treinador_cpf` ASC) VISIBLE,
  CONSTRAINT `fk_pokemon_treinador1`
    FOREIGN KEY (`treinador_cpf`)
    REFERENCES `centroPokemon`.`treinador` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `centroPokemon`.`cartao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `centroPokemon`.`cartao` (
  `qtd_pokemon` INT NOT NULL,
  `qtd_vitorias` INT NOT NULL,
  `qtd_insignias` INT NOT NULL,
  `treinador_cpf` VARCHAR(11) NOT NULL,
  PRIMARY KEY (`treinador_cpf`),
  CONSTRAINT `fk_cartao_treinador`
    FOREIGN KEY (`treinador_cpf`)
    REFERENCES `centroPokemon`.`treinador` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `centroPokemon`.`funcionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `centroPokemon`.`funcionario` (
  `cpf` VARCHAR(11) NOT NULL,
  `rg` VARCHAR(10) NOT NULL,
  `nome` VARCHAR(50) NOT NULL,
  `salario` DECIMAL(10,2) UNSIGNED NOT NULL,
  `telefone` VARCHAR(12) NOT NULL,
  `data_nasc` DATE NOT NULL,
  `funcao` VARCHAR(50) NOT NULL,
  `estado` VARCHAR(50) NULL,
  `cidade` VARCHAR(50) NULL,
  `bairro` VARCHAR(50) NULL,
  `rua` VARCHAR(50) NULL,
  PRIMARY KEY (`cpf`),
  UNIQUE INDEX `cpf_UNIQUE` (`cpf` ASC) VISIBLE,
  UNIQUE INDEX `rg_UNIQUE` (`rg` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `centroPokemon`.`tratamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `centroPokemon`.`tratamento` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `data_hora` DATETIME NOT NULL,
  `valor` DECIMAL(10,2) NOT NULL,
  `treinador_cpf` VARCHAR(11) NOT NULL,
  `funcionario_cpf` VARCHAR(11) NOT NULL,
  `pokemon_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_tratamento_treinador1_idx` (`treinador_cpf` ASC) VISIBLE,
  INDEX `fk_tratamento_funcionario1_idx` (`funcionario_cpf` ASC) VISIBLE,
  INDEX `fk_tratamento_pokemon1_idx` (`pokemon_id` ASC) VISIBLE,
  CONSTRAINT `fk_tratamento_treinador1`
    FOREIGN KEY (`treinador_cpf`)
    REFERENCES `centroPokemon`.`treinador` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tratamento_funcionario1`
    FOREIGN KEY (`funcionario_cpf`)
    REFERENCES `centroPokemon`.`funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tratamento_pokemon1`
    FOREIGN KEY (`pokemon_id`)
    REFERENCES `centroPokemon`.`pokemon` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `centroPokemon`.`centro_loja`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `centroPokemon`.`centro_loja` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `cnpj_loja` CHAR(14) NOT NULL,
  `num_maquinas` TINYINT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `cnpj_loja`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `cnpj_loja_UNIQUE` (`cnpj_loja` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `centroPokemon`.`produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `centroPokemon`.`produto` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(50) NOT NULL,
  `quantidade` INT UNSIGNED NOT NULL,
  `preco` DECIMAL(8,2) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `centroPokemon`.`cobranca`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `centroPokemon`.`cobranca` (
  `tratamento_id` INT UNSIGNED NOT NULL,
  `data_hora` DATETIME NOT NULL,
  PRIMARY KEY (`tratamento_id`),
  CONSTRAINT `fk_cobranca_tratamento1`
    FOREIGN KEY (`tratamento_id`)
    REFERENCES `centroPokemon`.`tratamento` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `centroPokemon`.`tratamento_has_centro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `centroPokemon`.`tratamento_has_centro` (
  `tratamento_id` INT UNSIGNED NOT NULL,
  `centro_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`tratamento_id`, `centro_id`),
  INDEX `fk_tratamento_has_centro_centro1_idx` (`centro_id` ASC) VISIBLE,
  INDEX `fk_tratamento_has_centro_tratamento1_idx` (`tratamento_id` ASC) VISIBLE,
  CONSTRAINT `fk_tratamento_has_centro_tratamento1`
    FOREIGN KEY (`tratamento_id`)
    REFERENCES `centroPokemon`.`tratamento` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tratamento_has_centro_centro1`
    FOREIGN KEY (`centro_id`)
    REFERENCES `centroPokemon`.`centro_loja` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `centroPokemon`.`funcionario_has_centro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `centroPokemon`.`funcionario_has_centro` (
  `funcionario_cpf` VARCHAR(11) NOT NULL,
  `centro_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`funcionario_cpf`, `centro_id`),
  INDEX `fk_funcionario_has_centro_centro1_idx` (`centro_id` ASC) VISIBLE,
  INDEX `fk_funcionario_has_centro_funcionario1_idx` (`funcionario_cpf` ASC) VISIBLE,
  CONSTRAINT `fk_funcionario_has_centro_funcionario1`
    FOREIGN KEY (`funcionario_cpf`)
    REFERENCES `centroPokemon`.`funcionario` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_funcionario_has_centro_centro1`
    FOREIGN KEY (`centro_id`)
    REFERENCES `centroPokemon`.`centro_loja` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `centroPokemon`.`centro_has_produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `centroPokemon`.`centro_has_produto` (
  `centro_id` INT UNSIGNED NOT NULL,
  `centro_cnpj_loja` CHAR(14) NOT NULL,
  `produto_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`centro_id`, `centro_cnpj_loja`, `produto_id`),
  INDEX `fk_centro_has_produto_produto1_idx` (`produto_id` ASC) VISIBLE,
  INDEX `fk_centro_has_produto_centro1_idx` (`centro_id` ASC, `centro_cnpj_loja` ASC) VISIBLE,
  CONSTRAINT `fk_centro_has_produto_centro1`
    FOREIGN KEY (`centro_id` , `centro_cnpj_loja`)
    REFERENCES `centroPokemon`.`centro_loja` (`id` , `cnpj_loja`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_centro_has_produto_produto1`
    FOREIGN KEY (`produto_id`)
    REFERENCES `centroPokemon`.`produto` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;