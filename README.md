# control-api
A flask based API for controlling the system.

## Requirements
* Docker
* RabbitMQ Docker image
  * `docker run -d --hostname <hostname> --name <imagename> -p 5672:5672 -p 15672:15672 rabbitmq:3.5-management`
* Cassandra Docker image
  * `docker run -d --name <imagename> -p 9042:9042 -p 9160:9160 cassandra:2.1`