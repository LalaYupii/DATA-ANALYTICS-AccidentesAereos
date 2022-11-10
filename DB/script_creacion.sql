create database aeroaccidente;

use aeroaccidente;

create table accidente (
	IdAccidente int auto_increment not null,
    Fecha date not null,
    LugarAccidente varchar(100),
    Operador varchar(70),
    OrigenDestino varchar(100),
    TipoAeronave varchar(70),
    TotalAbordo int,
    TripulacionAbordo int,
    PasajerosAbordo int,
    TotalFallecidos int,
    TripulacionFallecida int,
    PasajerosFallecidos int,
    FallecidosEnTierra int,
    Longitud decimal(10, 7),
    Latitud decimal(10, 7),
    AnioFinFabricacion int,
    primary key(IdAccidente)
);


select * from accidente;

select count(*) as Total_registros from accidente;