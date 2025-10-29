# Bigdata_Apache_Spark
Procesamiento de datos con apache spark

Conjunto de Datos

•	Fuente: kaggle
•	URL: https://www.kaggle.com/datasets/imdevskp/corona-virus-report?resource=download
•	Nombre del dataset: country_wise_latest
•	Formato: CSV
•	Cobertura geográfica: Abarca países a nivel mundial

Pasos para ejecutar dataset

1) Conectarse a la máquina virtual
Abrir PuTTY → conectar vía SSH con la IP de la VM
Usuario: vboxuser
Password: bigdata

2) Descargar y preparar el dataset COVID
Descargamos la dataset directamente por link https://www.kaggle.com/datasets/imdevskp/corona-virus-report?resource=download
Identificar el archivo que usaremos, por ejemplo:
country_wise_latest.csv

4) Subir el dataset COVID a HDFS (como en Anexo 2)
Cambiar a usuario hadoop:
su - hadoop
Password: hadoop

Crear carpeta en HDFS:
hdfs dfs -mkdir /CovidDataset
Subir el archivo:
hdfs dfs -put /home/hadoop/country_wise_latest.csv /CovidDataset
Verificar:
hdfs dfs -ls /CovidDatasetWilbin Marriaga

4) Ver/usar el dataset en Spark (validación previa)
Volver a usuario vboxuser (si sales de sesión)
pyspark
Dentro de Spark:
df = spark.read.csv("hdfs://localhost:9000/CovidDataset/country_wise_latest.csv", header=True, inferSchema=True)
df.show(5)
df.printSchema()
Salir de pyspark con CTRL+D

5) Instalar y preparar Kafka (si no se había hecho antes)
pip install kafka-python
wget https://downloads.apache.org/kafka/3.6.2/kafka_2.13-3.6.2.tgz
tar -xzf kafka_2.13-3.6.2.tgz
sudo mv kafka_2.13-3.6.2 /opt/Kafka

6) Iniciar servicios Kafka y ZooKeeper
sudo /opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties &
sudo /opt/Kafka/bin/kafka-server-start.sh /opt/Kafka/config/server.properties &

7) Crear el tópico Kafka (para mandar datos COVID)
/opt/Kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic covid_data

8) Crear Producer en Python para enviar datos del CSV a Kafka
nano covid_producer.py
(luego se llenará el código, no lo pongo ahora porque solo pediste pasos)
Guardar y ejecutar más tarde.

9) Crear Consumer con Spark Streaming (lectura del topic)
nano spark_covid_consumer.py
(luego se llenará el código de consumo)

10) Ejecutar
Primero ejecutar el producer:
python3 covid_producer.py

Luego el consumer:
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3 spark_covid_consumer.py

11) Monitoreo
Abrir en navegador:
http://IP_VM:4040    ← Spark UI

12) Finalizar
CTRL + C en ambas terminales
Cerrar PuTTY