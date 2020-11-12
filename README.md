# ZenatixProject
 IoT device publishes data on  sensor_data and cloud server receives this data by subscribing to the topic MyRPi.Include alerting on simulating sensors of a candy factory.
 
 #ProjectInfo
 The script should simulate values between 22°C to 28°C. Similarly, to simulate humidity sensors, script should simulate values which are valid values of humidity.
 
 #Alerting 
 Email get sent on  if average of humidity values received is more than 80% for more than 5 minutes. Alerting module  receive data over a MQTT topic and then raise an alert via email
 #Plaform and features Used
 Aws IoT Core
 MQTT Protocol used to assign topic,getting suscribed and publishing.
 Aws IoT Act(assigned rule for that)
 Aws SNS for sending email
 
 #Info
 Dipanshu Sharma
 beingdipanshu@gmail.com
 Cont:7988378475


 
 
