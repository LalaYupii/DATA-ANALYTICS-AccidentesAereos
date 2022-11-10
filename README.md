# Accidentes de Aviones

## Contexto
La Organización de Aviación Civil Internacional (OACI), organismo de la Organización de las Naciones Unidas, quiere investigar en profundidad los accidentes producidos desde inicios del siglo XX. Para ello, nos solicita la elaboración de un informe y un dashboard interactivo que recopile tal información.
La OACI únicamente cuenta con un dataset sobre datos de accidentes de aviones, pero insta a la consultora de datos -de la que formamos parte- que intente cruzar esta información con otras fuentes de su interés. Esto con el objetivo de obtener mayor claridad y consistencia en los fundamentos del estudio.

## Diccionario de Datos
El dataset brindado por la OACI llamado AccidentesAviones_Henry presenta las siguientes columnas:
- Unnamed: índice de los registros.
- fecha: fecha del accidente en el formato Mes (texto), Día, Año.
- HORA declarada: hora del accidente en diferentes formatos.
- Ruta: lugar del accidente.
- OperadOR: empresa u organismo que utilizaba la aeronave. 
- flight_no: número de vuelo.
- route: origen y destino del vuelo.
- ac_type: tipo de aeronave.
- registration: registro OACI de la aeronave. 
- cn_ln: número de construcción / número de fuselaje. 
- PASAJEROS A BORDO: cantidad de pasajeros a bordo.
- crew_aboard: cantidad de tripulación a bordo. 
- cantidad de fallecidos: cantidad total de fallecidos teniendo en cuenta pasajeros y tripulantes.
- passenger_fatalities: cantidad de pasajeros fallecidos.
- crew_fatalities: cantidad de tripulantes fallecidos.
- ground: cantidad de fallecidos de manera indirecta en tierra por el accidente de la aeronave.
- summary: breve descripción del accidente.

El dataset buscado para el cruzamiento de la información llamado aircraft_data presenta las siguientes columnas:
- Unnamed: índice de los registros.
- aircraft: nombre de la aeronave. 
- nbBuilt: cantidad de unidades construidas.
- startDate: año en que se comenzó a fabricar.
- endDate: año en que dejó de fabricar. Si el campo está vacío o NaN significa que todavía se está fabricando.
- Retired: algunas aeronaves tienen el año de caducidad recomendada por el fabricante.

A partir del cruzamiento de datos entre los datasets anteriores se creó uno nuevo llamado AccidentesAereosDefinitivos que presenta las siguientes columnas:
- Fecha: fecha del accidente en formato Año, Mes, Día.
- LugarAccidente: lugar dónde se produjo el accidente.
- Operador: empresa u organismo que utilizaba la aeronave.
- OrigenDestino: origen y destino del vuelo.
- TipoAeronave: tipo de aeronave.
- TotalAbordo: cantidad de pasajeros y tripulantes a bordo.
- TripulacionAbordo: cantidad de tripulantes a bordo.
- PasajerosAbordo: cantidad de pasajeros a bordo.
- TotalFallecidos: cantidad total de fallecidos teniendo en cuenta pasajeros y tripulantes. 
- TripulacionFallecida: cantidad de tripulantes fallecidos.
- PasajerosFallecidos: cantidad de pasajeros fallecidos.
- FallecidosEnTierra: cantidad de fallecidos de manera indirecta en tierra por el accidente de la aeronave.
- Longitud: coordenada geográfica de longitud.
- Latitud: coordenada geográfica de latitud. 
- FechaFinFabricacion: año en que se dejó de fabricar el modelo de la aeronave. Si el valor es -1 no hay registro y si es 0 el modelo todavía se está fabricando.

## Stack Tecnológico
- Para este proyecto se usaron las siguientes tecnologías:
- Python junto con Pandas para realizar el EDA.
- Python y pymysql para cargar los datos definitivos a la base de datos.
- MySQL para crear la base de datos. Específicamente se utilizó MySQL Workbench.
- Power BI para la realización del dashborad. 

## Análisis del Dataset brindado por la OACI
