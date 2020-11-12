from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import random, time
import json

SHADOW_CLIENT = "myShadowClient"

HOST_NAME = "amfljaaucfldu-ats.iot.ap-south-1.amazonaws.com"

ROOT_CA = "AmazonRootCA1.pem"

PRIVATE_KEY = "2806411728-private.pem.key"


CERT_FILE = "2806411728-certificate.pem.crt"

SHADOW_HANDLER = "MyRPi"

def myShadowUpdateCallback(payload, responseStatus, token):
  print()
  print('UPDATE: $aws/things/' + SHADOW_HANDLER + 
    '/shadow/update/#')
  print("payload = " + payload)
  print("responseStatus = " + responseStatus)
  print("token = " + token)

myShadowClient = AWSIoTMQTTShadowClient(SHADOW_CLIENT)
myShadowClient.configureEndpoint(HOST_NAME, 8883)
myShadowClient.configureCredentials(ROOT_CA, PRIVATE_KEY,
  CERT_FILE)
myShadowClient.configureConnectDisconnectTimeout(10)
myShadowClient.configureMQTTOperationTimeout(5)
myShadowClient.connect()

myDeviceShadow = myShadowClient.createShadowHandlerWithName(
  SHADOW_HANDLER, True)


lh = []
while True:
  #temperature and humidity of candy factory
  temperature = random.randrange(22,28)
  humidity = random.randrange(75,100)
  lh.append(humidity)
  if len(lh) > 5:
    sum = 0
    for i in range(-1,-6,-1):
      sum += lh[i]
    avghumidity = sum // 5
    if avghumidity > 80:
      payload = {"state":{"reported":{"humidity":str(humidity),"temperature":str(temperature),"alerting":"yes"}}}
    else:
      payload = {"state":{"reported":{"humidity":str(humidity),"temperature":str(temperature),"alerting":"no"}}}

  else:
    payload = {"state":{"reported":{"humidity":str(humidity),"temperature":str(temperature),"alerting":"no"}}}



  
  myDeviceShadow.shadowUpdate(json.dumps(payload),
      myShadowUpdateCallback, 5)
  

 


  
  time.sleep(30)

