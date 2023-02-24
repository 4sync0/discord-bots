#poner:
#./bootproducer.sh para el setup automatico de la script en server
#y autohandler.sh para que la script se ejecute automaticamente cada vez que el server se enciende




#input
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("fedora")) #server host
#"#game6.falixserver.net:23939"
channel = connection.channel()

channel.queue_declare(queue="started")
channel.basic_publish(exchange="",
                        routing_key="started",
                        body="server started"
                          )

connection.close()
