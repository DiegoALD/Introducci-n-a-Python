"""
Para crear la BBDD hay que ir a PHPMyAdmin
y en la pestaña SQL pegáis el código, hacéis
click en "continuar", corregís los errores 
y cuando todos estén corregidos se crea la BBDD
con las tablas correspondientes.
"""

CREATE DATABASE IF NOT EXISTS proyecto_1;

use proyecto_1;

CREATE TABLE usuarios(
    id int(10) auto_increment not null,
    nombre varchar(30),
    apellidos varchar(30),
    email varchar(50) not null,
    password varchar(30) not null,
    fecha date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE notas(
    id int(10) auto_increment not null,
    usuario_id int(10) not null,
    titulo varchar(50) not null,
    descripcion MEDIUMTEXT,
    fecha date not null,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;