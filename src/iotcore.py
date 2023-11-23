import time,json, ssl
import paho.mqtt.client as mqtt

ENDPOINT = "aaemtshrmuhgj-ats.iot.ap-northeast-2.amazonaws.com"
THING_NAME = 'raspberrypi'
CERTPATH = "/home/user/raspberrypi.cert.pem"
KEYPATH = "/home/user/raspberrypi.private.key"
CAROOTPATH = "/home/user/root-CA.crt"
TOPIC = 'farminfo'

def on_connect(mqttc, obj, flags, rc):
    if rc ==0:
        print('connected!!')

try:
    mqtt_client = mqtt.Client(client_id=THING_NAME)
    mqtt_client.on_connect = on_connect
    mqtt_client.tls_set(CAROOTPATH, certfile= CERTPATH, keyfile =KEYPATH, 
            tls_version = ssl.PROTOCOL_TLSv1_2, ciphers=None)
    mqtt_client.connect(ENDPOINT, port=8883)
    mqtt_client.loop_start()

    count =0
    i=0
    while True:
        if count==12:
            exec(open('water.py').read())
            exec(open('pump.py').read())
            count = 0
        else:
            time.sleep(300)
        exec(open('final.py').read())
        with open('data.json', 'r') as json_file:
            loaded_data = json.load(json_file)
        payload = json.dumps({'temp':loaded_data['temp'],
            'humi' : loaded_data['humi'], 'CO2' : loaded_data['CO2']})
        mqtt_client.publish(TOPIC, payload, qos=1)
        i=i+1
        count=count+1

except KeyboardInterrupt:
    pass

mqtt_client.disconnect()
print('\n')

