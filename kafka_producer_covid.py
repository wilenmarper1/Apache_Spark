# kafka_producer_covid.py
from kafka import KafkaProducer
import json, time, random
from datetime import datetime

countries = ["Colombia", "Argentina", "Chile", "Peru", "Brazil", "Mexico", "Spain", "Italy", "France", "Germany"]
regions = ["Americas", "Europe", "Eastern Mediterranean", "Western Pacific", "Africa"]

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        "country": random.choice(countries),
        "confirmed": random.randint(1000, 1000000),
        "deaths": random.randint(10, 20000),
        "recovered": random.randint(500, 800000),
        "region": random.choice(regions),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    producer.send('covid_data', value=data)
    print(f"Enviado: {data}")
    time.sleep(2)
