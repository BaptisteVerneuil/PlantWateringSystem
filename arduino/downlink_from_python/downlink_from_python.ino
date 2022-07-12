// Seeeduino LoRaWAN ------------------------------------------------------------
#define PIN_GROVE_POWER 38
#define SerialUSB Serial
 
// LoRaWAN -----------------------------------------------------------------------
#include <LoRaWan.h>

// LoRa keys
#define DevEUI "00B193384D6E47B8"
#define AppEUI "70B3D57ED002F952"
#define AppKey "D9902CCE630C3FA5591FE68A451140D9"
 
// SETUP -------------------------------------------------------------------------
// vars
char buffer[256];
void setup(void)
{
  // Setup Serial connection
  delay(5000);
 
  if (Serial) {
    Serial.begin(115200);
  }
 
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
 
  // void setId(char *DevAddr, char *DevEUI, char *AppEUI);
  // replace the xxxxxx and the yyyyyy below with the DevEUI and the
  // AppEUI obtained from your registered sensor node and application
  // in The Things Network (TTN). The numbers are hexadecimal strings
  // without any leading prefix like "0x" and must have exactly the
  // same number of characters as given below.
  // lora.setId(NULL, "xxxxxxxxxxxxxxxx", "yyyyyyyyyyyyyyyy");
  lora.setId(NULL, DevEUI, AppEUI);
 
  // setKey(char *NwkSKey, char *AppSKey, char *AppKey);
  // replace the zzzzzz below with the AppKey obtained from your registered
  // application in The Things Network (TTN). The numbers are hexadecimal
  // strings without any leading prefix like "0x" and must have exactly
  // the same number of characters as given below.
  // lora.setKey(NULL, NULL, "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz");
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
  unsigned char tx[1] = { 1 };
 
  // Transfer LoRa package
  result = lora.transferPacketWithConfirmed(tx, sizeof(tx), 5);
  //result = lora.transferPacket(lpp.getBuffer(), lpp.getSize(), 5);
 
  if (result) {
    short length;
    short rssi;
 
    // Receive LoRaWAN package (LoraWAN Class A)
    char rx[256];
    length = lora.receivePacket(rx, 256, &rssi);
    int rx_int[length];
 
    // Check, if a package was received
    if (length)
    {
      if (Serial) {
        Serial.print("Length is: ");
        Serial.println(length);
        Serial.print("RSSI is: ");
        Serial.println(rssi);
 
        // Convert received package to int
        int arrtoint = atoi(rx);
        Serial.println();
        Serial.println("Received data: " + String(arrtoint));
        Serial.println();
 
        // Print RX as hex
        for (unsigned char i = 0; i < length; i ++)
        {
          // Convert received package to int
          int rx_data_asInteger = rx[i];
          rx_int[i] = rx_data_asInteger;
 
          Serial.print("[" + String(i) + "]: ");
          Serial.print("0x");
          Serial.print(rx[i], HEX);
          Serial.print(" -> ");
          Serial.println(String(rx_int[i]));;
        }
        Serial.println();
      }
    }
  }
 
  if (Serial) {
    Serial.println((String)"Loop " + nloops + "...done!\n");
  }
  delay(60000);
}
