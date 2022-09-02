# from fastapi import FastAPI, WebSocket

# app = FastAPI()


# @app.get("/")
# async def root():
#     i = 0
#     for i in range(1000):
#         return {"message": i}

#     # uvicorn python.main:app --reload


# from fastapi import FastAPI, WebSocket
# import random

# # Create application
# app = FastAPI(title='WebSocket Example')

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     print('Accepting client connection...')
#     await websocket.accept()
#     while True:
#         try:
#             # Wait for any message from the client
#             await websocket.receive_text()
#             # Send message to the client
#             resp = {'value': random.uniform(0, 1)}
#             await websocket.send_json(resp)
#         except Exception as e:
#             print('error:', e)
#             break
#     print('Bye..')

from fastapi import FastAPI, WebSocket
import random
from fastapi.responses import HTMLResponse
from fastapi_mqtt import FastMQTT, MQTTConfig

app = FastAPI()


mqtt_config = MQTTConfig(host = "broker.hivemq.com",
    port= 1883,
    keepalive = 60,)

mqtt = FastMQTT(
    config=mqtt_config
)

mqtt.init_app(app)

import json
import asyncio
from fastapi import FastAPI
from fastapi import Request
from fastapi import WebSocket
import uvicorn
import time

from paho.mqtt import client as mqtt_client
# broker = 'broker.hivemq.com'
# port = 1883
# topic = "/mqtt"
# # generate client ID with pub prefix randomly
# client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'
from firebase import Auth, Firebase


config = {
    "apiKey": "AIzaSyA6u82Q7e8v3rmuxYEPx70s7HgDayx_1mw",
    "authDomain": "asap-core.firebaseapp.com",
    "databaseURL": "https://asap-core-default-rtdb.firebaseio.com",
    "projectId": "asap-core",
    "storageBucket": "asap-core.appspot.com",
    "messagingSenderId": "181896432952",
    "appId": "1:181896432952:web:b16e4239e18a5d533005cd",
    "measurementId": "G-ENE3E2S2VZ"

}

firebase = Firebase(config)

db = firebase.database()

# time.sleep(1000)

# app = FastAPI()


@app.get("/")
async def func():
    # client = connect_mqtt()
    # client.loop_start()
    
    # subscribe(client)
    # publish(client)
    # while True:
    for i in range(50):
    
        mqtt.publish("/mqtt2","2") 
        mqtt.publish("/mqtt","1") 
        time.sleep(1)
   

    
    # return {"result": True,"message":"Published" }
#     # for i in range(10):

        # time.sleep(1)
   

    # return {"result": True,"message":"Published" }
    

import time



# @mqtt.on_connect()
# def connect(client, flags, rc, properties):
#     mqtt.client.subscribe("/mqtt") #subscribing mqtt topic
#     print("Connected: ", client, flags, rc, properties)

# @mqtt.on_subscribe()
# def subscribe(client, mid, qos, properties):
#     print("subscribed", client, mid, qos, properties)

@mqtt.on_connect()
def connect(client, flags, rc, properties):
    mqtt.client.subscribe("/mqtt") #subscribing mqtt topic
    mqtt.client.subscribe("/mqtt2") #subscribing mqtt topic
    print("Connected: ", client, flags, rc, properties)


@mqtt.on_message()
def message(client, topic, payload, qos, properties):
    print("Received message: ",topic, payload.decode(), qos, properties)

    
@mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)


def publish():
    print("PUBLISH")
    # msg_count = 0
    data = random.gauss(90,30.0)
        # msg = f"messages: {msg_count}"
        # result = client.publish(topic, msg)
    mqtt.publish("/mqtt",data) 
    db.child("HealthData/").push(round(data,0))
    topic = "mqtt"
    return {"data":data, "topic":topic}

def publish2():
    print("PUBLISH2")
    # msg_count = 0
    data = random.gauss(10,1.0)
        # msg = f"messages: {msg_count}"
        # result = client.publish(topic, msg)
    mqtt.publish("/mqtt2",data) 
    db.child("HealthData/").push(round(data,0))
    topic = "mqtt2"
    return {"data":data, "topic":topic}
        # db.child("HealthData/").push(10)
        # db.child("HealthData/").push(13)
        # db.child("HealthData/").push(100)
        # db.child("HealthData/").push(14)
        # db.child("HealthData/").push(15)



# def connect(client, flags, rc, properties):
#     mqtt.client.subscribe("/mqtt") #subscribing mqtt topic
#     print("Connected to: ", client, flags, rc, properties)


# @mqtt.on_message()
# async def message(client, topic, payload, qos, properties):
#     print("Received message: ",topic, payload.decode(), qos, properties)

# @mqtt.on_message()
# async def message(client, topic, payload, qos, properties):
#     print("Received message: ",topic, payload.decode(), qos, properties)

#     return payload.decode()


# @mqtt.on_connect()
# @mqtt.on_message() #on_message gör att funktionen körs automatiskt när ett medelande kommer in 


# def subscribe(client: mqtt_client):
# # @mqtt.on_message()
#     def on_message(client, userdata, msg):
#          print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
#         #  WebSocket.send_json( self=None, data={"value":msg.payload.decode()})

#     client.subscribe(topic)
#     client.on_message = on_message
        



# @mqtt.on_message()
# @mqtt.on_message()
@app.websocket("/bpm")
async def websocket_endpoint(websocket:WebSocket):
  await websocket.accept()
 
  while True:
    

    data = publish()
    print("data",data)
    await websocket.send_json({"value":round(data["data"],0),
                               "topic":data["topic"]})
    data2 = publish2()
    # data2 = publish()
    # for data in health_data_db.each():
    await websocket.send_json({"value":round(data2["data"],0),
                               "topic":data2["topic"]})

    # 
    #     print(data.val())
    #     await websocket.send_json({"value":data.val()})
    time.sleep(1)
    
# @app.websocket("/bpm2")
# async def websocket_endpoint2(websocket2:WebSocket):
#   await websocket2.accept()
 
#   while True:
#     data = publish2()
#     # for data in health_data_db.each():
#     await websocket2.send_json({"value":round((data),0)})
#     # 
#     #     print(data.val())
#     #     await websocket.send_json({"value":data.val()})
#     time.sleep(1)



# @app.websocket("/pressure")

# async def websocket_endpoint(websocket: WebSocket):
#     print("HEJ")
#     await websocket.accept()
#     while True:
        
#         # while data["data"] == "start":
#         #     data = await websocket.receive_json()
#         for i in range(30):
#             print(i)

#             if i > 10:
#                  await websocket.send_json({"value":random.gauss(90,30.0)})
           
#             else:
#                 print(i)
#                 await websocket.send_json({"value":random.gauss(60,20.0)})
            
#             time.sleep(1)
            
                
        # for i in range(100000):
        #     await asyncio.sleep(1)
        #     payload = next(i)
        #     await websocket.send_json(i)

    #   # uvicorn python.main:app --reload
