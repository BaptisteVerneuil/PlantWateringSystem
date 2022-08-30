/////////////////////////////////////////////////////////////////
// Author: Md Ashiqur Rahman, Shota Yamamoto, Baptiste Verneuil
// Group number: 9
// Last date of change: 30/08/2022
/////////////////////////////////////////////////////////////////


// Seeeduino LoRaWAN ------------------------------------------------------------
#define PIN_GROVE_POWER 38
#define SerialUSB Serial

// LoRaWAN -----------------------------------------------------------------------
#include <LoRaWan.h>
 
// Put your LoRa keys here
#define DevEUI "XXXXXXXXXXXXXXXX"
#define AppEUI "XXXXXXXXXXXXXXXX"
#define AppKey "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

// CayenneLPP --------------------------------------------------------------------
#include <CayenneLPP.h>  // Include Cayenne Library
CayenneLPP lpp(51);      // Define the buffer size: Keep as small as possible
 
// SETUP -------------------------------------------------------------------------
// vars
char buffer[256];

int sensorPin = A0;
const int airValue = 1043; //Sensor value in the Air
const int waterValue = 805; //Sensor value in the water
int soilMoisturePercent=0;
int sensorValue = 0;

double flow; //Liters of passing water volume
unsigned long pulse_freq;

void setup(void)
{
  // Setup Serial connection
  delay(5000);
  if (Serial) {
    Serial.begin(115200);
  }
 
  // Powerup Seeeduino LoRaWAN Grove connectors
  pinMode(PIN_GROVE_POWER, OUTPUT);
  digitalWrite(PIN_GROVE_POWER, 1);
  pinMode(2, INPUT);
  attachInterrupt(0, pulse, RISING); // Setup Interrupt
  pinMode(7, OUTPUT);
 
  // Config LoRaWAN
  lora.init();
 
  memset(buffer, 0, 256);
  lora.getVersion(buffer, 256, 1);
  if (Serial) {
    Serial.print(buffer);
  }
 
  memset(buffer, 0, 256);
  lora.getId(buffer, 256, 1);
  if (Serial) {
    Serial.print(buffer);
  }
 
  lora.setId(NULL, DevEUI, AppEUI);
  lora.setKey(NULL, NULL, AppKey);
 
  lora.setDeciveMode(LWOTAA);
  lora.setDataRate(DR0, EU868);      // DR5 = SF7, DR0 = SF 12
  lora.setAdaptiveDataRate(true);
 
  lora.setChannel(0, 868.1);
  lora.setChannel(1, 868.3);
  lora.setChannel(2, 868.5);
  lora.setChannel(3, 867.1);
  lora.setChannel(4, 867.3);
  lora.setChannel(5, 867.5);
  lora.setChannel(6, 867.7);
  lora.setChannel(7, 867.9);
 
  lora.setDutyCycle(false);
  lora.setJoinDutyCycle(false);
 
  lora.setPower(14);
  lora.setPort(33);
 
  unsigned int nretries;
  nretries = 0;
  while (!lora.setOTAAJoin(JOIN, 20)) {
    nretries++;
    if (Serial) {
      Serial.println((String)"Join failed, retry: " + nretries);
    }
  }
  Serial.println("Join successful!");
}
 
// LOOP --------------------------------------------------------------------
unsigned int nloops = 0;
void loop(void) {
  
  nloops++;
  if (Serial) {
    Serial.println((String)"Loop " + nloops + "...");
  }
  bool result = false;

  // Moisture sensor
  // read the value from the sensor 100 times and averaging
  for (int i = 0; i <= 100; i++) 
  { 
    sensorValue = sensorValue + analogRead(sensorPin); 
    delay(1); 
  } 
  sensorValue = sensorValue/100.0; 

  // Converting sensor result into percentage
  soilMoisturePercent = map(sensorValue, airValue, waterValue, 0, 100);
  if(soilMoisturePercent >= 100){
    soilMoisturePercent = 100;
  }
  else if(soilMoisturePercent <=0){      
    soilMoisturePercent = 0;
  }
  Serial.print("Soil Moisture = " );
  Serial.print(soilMoisturePercent);
  Serial.println("%");

  // Sending data to Frost Server
  // Reset Cayenne buffer and add new data
  lpp.reset();                             // Resets the Cayenne buffer
  lpp.addAnalogOutput(1, soilMoisturePercent);  // encodes the sensor value on channel 1 in Cayenne format
 
  // Transfer LoRa package
  result = lora.transferPacket(lpp.getBuffer(), lpp.getSize(), 5);                  // sends the Cayenne encoded data packet (n bytes) with a default timeout of 5 secs

  // Receiving data
  if (result) {
    short length;
    short rssi;
    // Receive LoRaWAN package (LoraWAN Class A)
    char rx[256];
    length = lora.receivePacket(rx, 256, &rssi);
    float timeSeconds;
    // Check, if a package was received
    if (length)
    {
      if (Serial) {
        // Convert received package to float
        int rx_data_asInteger = rx[0];
        timeSeconds = rx_data_asInteger;
        // Adding water with the pump
        int timeMilliseconds = int(((1000*timeSeconds/255.0)*20.0));

        Serial.print("Activating pump for : ");
        Serial.print(String(timeMilliseconds));
        Serial.println(" milliseconds");

        digitalWrite(7, HIGH);
        delay(timeMilliseconds); // Waiting timeMilliseconds before switching off the pump
        digitalWrite(7, LOW);
        delay(5000);
      }
    }
  }
   
  if (Serial) {
    Serial.println((String)"Loop " + nloops + "...done!\n");
  }
  delay(600000); // 10 Minutes
 
}

void pulse () // Interrupt function

{
  pulse_freq++;
}
