// Seeeduino LoRaWAN ------------------------------------------------------------
#define PIN_GROVE_POWER 38
#define SerialUSB Serial
 
// LoRaWAN -----------------------------------------------------------------------
#include <LoRaWan.h>
 
// Put your LoRa keys here
#define DevEUI "00B193384D6E47B8"
#define AppEUI "70B3D57ED002F952"
#define AppKey "D9902CCE630C3FA5591FE68A451140D9"
 
// CayenneLPP --------------------------------------------------------------------
#include <CayenneLPP.h>  // Include Cayenne Library
CayenneLPP lpp(51);      // Define the buffer size: Keep as small as possible
 
// SETUP -------------------------------------------------------------------------
// vars
char buffer[256];

int sensorPin = A0;
const int airValue = 640;   //Sensor value in the Air
const int waterValue = 400;  //Sensor value in the water
int soilMoisturePercent=0;
int sensorValue = 0;
 
void setup() {
  // Setup Serial connection
  delay(5000);
  Serial.begin(115200);
 
  // Powerup Seeeduino LoRaWAN Grove connectors
  pinMode(PIN_GROVE_POWER, OUTPUT);
  digitalWrite(PIN_GROVE_POWER, HIGH);
 
  // Config LoRaWAN
  lora.init();
}
void loop() {

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
    delay(10000);
}
