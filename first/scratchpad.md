# Scratchpad for Hello World and Page Views Examples 

### Set up your envirnoment
Execute these commands before executing the rest of the commands for the two examples below.  
1. git clone https://github.com/InfluxCommunity/kafka_faust_examples.git
2. cd first 
   docker compose up -d
3. pipenv install
   pipenv shell

Make sure to setup two virtuan env shells so that you can start a fuast app, and send messages to topics. 

### Hello World Example Commands 
4. faust -A hello_world worker -l info
5. faust -A hello_world send greetings "Hello Kafka" 
6. docker exec -it first-kafka-1 /bin/sh
7. /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --
topic greetings --from-beginning

### InfluxDB Resources Placeholder
<!-- Use as a placeholder for your credintials  -->
Org ID = 
Views token = 
CSTR token = 

### Page Views Example Commands 
1. faust -A page_views  worker -l info
2. faust -A page_views send page_views '{"id": "foo", "user": "bar"}'
3. docker exec -it first-kafka-1 /bin/sh
   /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic page_view_counts --from-begin
ning
4. telegraf --config telegraf.conf

### Additional Helpful Commands 
To manually create topics: 
`/opt/kafka/bin/kafka-topics.sh --create --topic example --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1`
To manually delete topics: 
`/opt/kafka/bin/kafka-topics.sh --delete --topic example --bootstrap-server kafka:9092`
Monitor Processes 
`lsof -i :6066`
Kill Processes 
`kill <PID>`

