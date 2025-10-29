# Bigdata_Apache_Spark
Procesamiento de datos con apache spark
______________________________________________________________________________________________________________

Conjunto de Datos

•	Fuente: kaggle

•	URL: https://www.kaggle.com/datasets/imdevskp/corona-virus-report?resource=download

•	Nombre del dataset: country_wise_latest

•	Formato: CSV

•	Cobertura geográfica: Abarca países a nivel mundial

_______________________________________________________________________________________________________________

Pasos sencillos para realizar el anexo (Spark Streaming + Kafka)

1.	Entrar a la máquina virtual

o	Abrir PuTTY
o	Conectarse por SSH usando la IP local
o	Usuario: vboxuser
o	Password: bigdata

2.	Instalar librería de Kafka para Python

pip install kafka-python

3.	Descargar e instalar Kafka

wget https://downloads.apache.org/kafka/3.6.2/kafka_2.13-3.6.2.tgz
tar -xzf kafka_2.13-3.6.2.tgz
sudo mv kafka_2.13-3.6.2 /opt/Kafka

4.	Iniciar los servicios

o	Iniciar ZooKeeper:
o	sudo /opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties &
o	Iniciar Kafka:
o	sudo /opt/Kafka/bin/kafka-server-start.sh /opt/Kafka/config/server.properties &

5.	Crear un tópico en Kafka

/opt/Kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic sensor_data

6.	Crear y ejecutar el productor (Kafka Producer)

o	Crear archivo:
o	nano kafka_producer_covid.py
o	Pegar el código del productor (el del PDF)
o	Guardar y ejecutar:
o	python3 kafka_producer_covid.py

7.	Crear y ejecutar el consumidor (Spark Streaming)
o	Abrir una nueva terminal PuTTY (sin cerrar la del productor)
o	Crear archivo:
o	nano spark_streaming_covid.py
o	Pegar el código del consumidor
o	Ejecutar con spark-submit:
o	spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3 spark_streaming_covid.py

8.	Observar resultados
o	Ver datos llegando en consola
o	Opcional: abrir interfaz Web de Spark
o	http://IP-DE-LA-VM:4040

9.	Para finalizar

o	Presionar CTRL + C en ambas terminales para detener productor y consumidor
