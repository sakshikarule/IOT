
# import paho mqtt client
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"message payload = {message.payload}")

# create a client for subscribing
subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# add on message callback function in client
subscriber.on_message = on_message

# connect with broker
subscriber.connect(host='localhost')

# subscribe for a topic
subscriber.subscribe(topic='sensor/ldr')

# keep subscriber running
subscriber.loop_forever()