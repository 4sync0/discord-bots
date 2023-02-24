#output
import producer
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("fedora")) #"#game6.falixserver.net:23939"
channelmq = connection.channel()

channelmq.queue_declare("started")

def callback(ch, method, properties, body):
    global callback_checkpoint
    callback_checkpoint = True
    print(bytes(body))
channelmq.basic_consume(queue="started", auto_ack=True, on_message_callback=callback)

channelmq.start_consuming()
connection.close()