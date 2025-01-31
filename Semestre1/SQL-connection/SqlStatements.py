killDb = '''USE master; 
ALTER DATABASE [DB_PYTHON] SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
DROP DATABASE [DB_PYTHON] ;'''

createDb = '''CREATE DATABASE DB_PYTHON'''

createTableDatos = '''CREATE TABLE Datos_Personales_Python (Id_num INTEGER IDENTITY(1, 1),Nombre VARCHAR(255) NOT NULL, Correo VARCHAR(255), 
Direccion VARCHAR(255), Ciudad VARCHAR(255) NOT NULL, Telefono VARCHAR(15), Genero CHAR(1), Estado_Civil VARCHAR(12), PRIMARY KEY (Id_num))'''

createTableCiudad = '''CREATE TABLE Ciudad(Ciudad VARCHAR(255) NOT NULL, Pais VARCHAR(100) NOT NULL, PRIMARY KEY (Ciudad))'''

createTableRegion = '''CREATE TABLE Region(Pais VARCHAR(100) NOT NULL, Region VARCHAR(100) NOT NULL, PRIMARY KEY (Pais))'''

