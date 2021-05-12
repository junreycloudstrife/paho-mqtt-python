import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect

# client.connect("mqtt.eclipse.org", 1883, 60)
client.connect("mqtt.eclipseprojects.io", 1883, 60)

time.sleep(1)
# count = 0
while True:
    client.loop()
    message = input(str('Enter message: '))
    client.publish("junrey/sample", message)
    # print(count)
    time.sleep(1)
    # count += 1