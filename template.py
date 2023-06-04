import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')




list_of_files=[
    "src/__init__.py",
    "src/constant/__init__.py",
    "src/database/mongodb.py",
    "src/entity/__init__.py",
    "src/entity/generic.py",
    "src/kafka_config/__init__.py",
    "src/kafka_consumer/__init__.py",
    "src/kafka_consumer/json_consumer.py",
    "src/kafka_logger/__init__.py",
    "src/kafka_producer/__init__.py",
    "src/kafka_producer/json_producer.py",
    "producer_main.py",
    "consumer_main.py",
    "sample_data/kafka-sensor-topic"

]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"File already exists: {filename}")