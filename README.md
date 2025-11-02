# Bigdata_Apache_Spark
Procesamiento de datos con apache spark

Pasos para ejecutar codigo (Spark Streaming + Kafka)

Realizar el cargue del dataset en la herramienta Hadoop.

----------------------------------------------
1.	Ingresamos con las siguientes credenciales 
----------------------------------------------

Usuario: hadoop 

Password: hadoop 

Iniciamos el clúster de Hadoop con el siguiente comando 

start-all.sh

------------------------------------------------------------------
2.	Se crea una carpeta en el sistema HDFS utilizando el comando 
------------------------------------------------------------------

hdfs dfs -mkdir /Covid19

----------------------------------------------------------------------
3.	En la máquina virtual descargamos el dataset, del siguiente link
----------------------------------------------------------------------

https://www.kaggle.com/datasets/imdevskp/corona-virus-report?resource=download

---------------------------------------------------------------------------------------
4.	Una vez con el dataset descargado, entramos a la máquina virtual seguimos los pasos
---------------------------------------------------------------------------------------
Abrir PuTTY

Conectarse por SSH usando la IP local

Usuario: vboxuser

Password: bigdata

--------------------------------------------
5.	Instalar librería de Kafka para Python
--------------------------------------------

pip install kafka-python

-------------------------------------
6.	Descargar e instalar Kafka
-------------------------------------

wget https://downloads.apache.org/kafka/3.6.2/kafka_2.13-3.6.2.tgz

tar -xzf kafka_2.13-3.6.2.tgz

sudo mv kafka_2.13-3.6.2 /opt/Kafka

---------------------------
7.	Iniciar los servicios
---------------------------

Iniciar ZooKeeper:

sudo /opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties &

Ahora puedes iniciar Kafka:

sudo /opt/Kafka/bin/kafka-server-start.sh /opt/Kafka/config/server.properties &

-----------------------------
8.	Crear un tópico en Kafka
-----------------------------

/opt/Kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic covid_data

--------------------------------------------------
9.	Crear y ejecutar el productor (Kafka Producer)
--------------------------------------------------

Crear archivo:

Pegar el código del productor (el del PDF)

Guardar y ejecutar:

python3 kafka_producer_covid.py

-----------------------------------------------------
10.	Crear y ejecutar el consumidor (Spark Streaming)
-----------------------------------------------------

Abrir una nueva terminal PuTTY (sin cerrar la del productor)

Crear archivo:

nano spark_streaming_covid.py

Pegar el código del consumidor

Ejecutar con spark-submit:

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 spark_streaming_covid.py

----------------------------
11.	Observar resultados
----------------------------

Ver datos llegando en consola

Opcional: abrir interfaz Web de Spark

http://IP-DE-LA-VM:4040

---------------------
12.	Para finalizar
---------------------

Presionar CTRL + C en ambas terminales para detener productor y consumidor
