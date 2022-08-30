
<h1 style="text-align: center;"><u><strong>Automated Plant Watering System 2022</strong></u></h1>
<h2 style="text-align: left;"><u style="font-size: 20.0px;letter-spacing: -0.008em;text-align: left;"><strong>Introduction</strong></u></h2>
<h3><u><strong>Context of our project</strong></u></h3>
<p>Plants are essential resource. They are very important for the planet and for all the living things. We rely on them for food, water, medicine, the air we breath and the climate. Therefore, it is very important to take a proper care of the plants.&nbsp;</p>
<p>Whenever we go out of the city for several days, we always used to worry about our plants as there is no one to care of them and they need water on regular demand. So, in this course, we will develop a project where plant will be watered automatically by using Arduino. In this automated plant watering system, we will use different sensors like - Temperature, Humidity, Pressure and Gas sensor, LCD display, water flow sensor, Capacitive plant moisture sensor. The data of the sensor devices are sent to the internet through the LoRaWAN network server. From this network server user can get the updated information of the pump, sensor readings.&nbsp;</p>
<p>As the system is automated, there is no need for the human help. So, this system can be very helpful for agricultural industry where less human will be required to monitor the plants.&nbsp;</p>
<h3><u><span style="color: rgb(0,51,102);"><strong>What is an automated watering system?</strong></span></u></h3>
<p>An &quot;automated watering system&quot; is a computer/timer-based method of providing water to crops, limiting human involvement to only supervision. Sprinklers, drip irrigation, and other water distribution methods may all be automated.&nbsp;</p>
<h4>Benefits of an automated watering system</h4>
<ul>
<li>Can save water</li>
<li>Will save time</li>
<li>Will save gardener's effort</li>
<li>Water can be delivered at optimal levels for plant growth</li>
<li>Can protect the soil ecosystem</li>
<li>Reduce labor cost in exchange for an efficient water supply system</li></ul>
<h4><u>Application of Automated watering system</u></h4>
<ul>
<li>Small-scale application, such as gardening.</li></ul>
<p><a href="https://www.amazon.co.uk/Garden-Gear-Irrigation-Greenhouse-Conservatory/dp/B07B4C627D"><ac:image ac:queryparams="effects=drop-shadow" ac:height="400"><ri:attachment ri:filename="garden.jpg" /></ac:image></a></p>
<ul>
<li>Large-scale application, such as agriculture.</li></ul>
<p><a href="http://www.cyulin.net/china/used-center-pivot-irrigation-system"><ac:image ac:title="Agriculture" ac:queryparams="effects=drop-shadow" ac:alt="Agriculture" ac:height="400"><ri:attachment ri:filename="agriculture.jpg" /></ac:image></a></p>
<h3><u><strong>Objectives</strong></u></h3>
<ul>
<li>Implement an irrigation control regulation including local monitoring data and public weather data</li>
<li>Explore the different <a href="https://wiki.tum.de/display/geosensorweb/Data+Downlink">LoRaWAN data downlink</a>/uplink capabilities and implement one of them</li></ul>
<h3><u><strong>Existing literature</strong></u></h3>
<p>Automated plant watering system experiments have already been concluded. In particular, two different experiments used respectively Arduino microcontroller, MySQL database and a PHP server [1], and a local server with Arduino Nano [2]. Both experiments used a threshold value for soil moisture content, and as soon the moisture was dropping below this value, the plant was supplied with water in order for the soil moisture to be higher than the threshold.</p>
<p>In our project, we propose to go further, and to use some weather data to forecast the soil moisture, and to prevent the soil moisture to drop below the threshold value. Moreover, the precipitation forecasts will allow our system to prevent useless watering and to spare some water.</p>
<h2><u><strong>Hardware description</strong></u></h2>
<h3><u><strong>Required hardware</strong></u></h3>
<ul>
<li>Flower box, rack for box, soil, plant</li>
<li>Pump, flexible tube, water storage bucket</li>
<li>Water-proof case for MC, if required</li>
<li>Seeeduino LoRaWAN: <a href="http://wiki.seeedstudio.com/Seeeduino_LoRAWAN/">http://wiki.seeedstudio.com/Seeeduino_LoRAWAN/</a></li>
<li>Grove Smart Plant Care Kit:&nbsp;<a href="http://wiki.seeedstudio.com/Grove_Smart_Plant_Care_Kit/">wiki.seeedstudio.com/Grove_Smart_Plant_Care_Kit/</a></li>
<li>Capacitive soil moisture sensor:&nbsp;<a href="http://wiki.seeedstudio.com/Grove-Capacitive_Moisture_Sensor-Corrosion-Resistant/">http://wiki.seeedstudio.com/Grove-Capacitive_Moisture_Sensor-Corrosion-Resistant/</a></li>
<li>Power supply for pump and MC
<ul>
<li>&nbsp;Voltcraft SNG-600-OW: <a href="https://www.amazon.de/Voltcraft-SNG-600-OW-STECKERNETZTEIL/dp/B008H3G6B4">https://www.amazon.de/Voltcraft-SNG-600-OW-STECKERNETZTEIL/dp/B008H3G6B4</a></li></ul></li></ul>
<h3><u><a href="https://wiki.seeedstudio.com/Seeeduino_LoRAWAN/">Seeeduino LoraWAN</a></u></h3>
<p>Using Seeeduino LoRaWAN, we can quickly experience LoRa's advantages in IoT with an Arduino development board embedded with LoRaWAN. In this project, we have used Seeeduino LoraWAN version 1.0&nbsp;</p>
<h5>Specification</h5>
<table class="wrapped"><colgroup><col /><col /></colgroup>
<tbody>
<tr>
<th style="text-align: left;">Item</th>
<th style="text-align: left;">Value</th></tr>
<tr>
<td style="text-align: left;">Microcontroller</td>
<td style="text-align: left;">ATSAMD21G18, 32-Bit ARM Cortex M0+</td></tr>
<tr>
<td style="text-align: left;">Operating Voltage</td>
<td style="text-align: left;">3.3V</td></tr>
<tr>
<td style="text-align: left;">Digital I/O Pins</td>
<td style="text-align: left;">20</td></tr>
<tr>
<td style="text-align: left;">PWM Pins</td>
<td style="text-align: left;">All but pins 2 and 7</td></tr>
<tr>
<td style="text-align: left;">UART</td>
<td style="text-align: left;">2 (Native and Programming)</td></tr>
<tr>
<td style="text-align: left;">Analog Input Pins</td>
<td style="text-align: left;">6, 12-bit ADC channels</td></tr>
<tr>
<td style="text-align: left;">Analog Output Pins</td>
<td style="text-align: left;">1, 10-bit DAC</td></tr>
<tr>
<td style="text-align: left;">External Interrupts</td>
<td style="text-align: left;">All pins except pin 4</td></tr>
<tr>
<td style="text-align: left;">DC Current per I/O Pin</td>
<td style="text-align: left;">7 mA</td></tr>
<tr>
<td style="text-align: left;">Flash Memory</td>
<td style="text-align: left;">256 KB</td></tr>
<tr>
<td style="text-align: left;">SRAM</td>
<td style="text-align: left;">32 KB</td></tr>
<tr>
<td style="text-align: left;">EEPROM</td>
<td style="text-align: left;">None</td></tr>
<tr>
<td style="text-align: left;">Clock Speed</td>
<td style="text-align: left;">48 MHz</td></tr>
<tr>
<td style="text-align: left;">Lenght</td>
<td style="text-align: left;">68 mm</td></tr>
<tr>
<td style="text-align: left;">Width</td>
<td style="text-align: left;">53 mm</td></tr>
<tr>
<td style="text-align: left;">Weight</td>
<td style="text-align: left;">19.6g(without GPS), 19.9(with GPS)</td></tr></tbody></table>
<p><br /></p>
<h3><u><a href="https://wiki.seeedstudio.com/Grove-Temperature_Humidity_Pressure_Gas_Sensor_BME680/#:~:text=The%20Grove%2DTemperature%26Humidity%26Pressure%26Gas%20Sensor(BME680,which%20needs%20those%20four%20parameters.">Temperature, Humidity, Pressure and Gas Sensor (BME 680)</a></u></h3>
<p>In addition to measuring temperature, pressure, humidity and gas simultaneously, the Temperature, Humidity, Pressure and Gas Sensor which is based on the BME680 module and can be used in GPS units, IoT devices or any device with a need for these parameters.&nbsp;</p>
<h5>Specification&nbsp;</h5>
<table class="wrapped">
<thead>
<tr>
<th style="text-align: left;">Item</th>
<th style="text-align: left;">Value</th></tr></thead>
<tbody>
<tr>
<td style="text-align: left;">Version</td>
<td style="text-align: left;">1.0</td></tr>
<tr>
<td style="text-align: left;">Working voltage</td>
<td style="text-align: left;">3.3V/5V</td></tr>
<tr>
<td style="text-align: left;">Operating range</td>
<td style="text-align: left;">-40~+85℃; 0-100% r.H.; 300-1100hPa</td></tr>
<tr>
<td style="text-align: left;">Digital interface</td>
<td style="text-align: left;">I<sup style="margin-left: 0.07812em;">2</sup>C(up to 3.4MHZ)/ SPI(3 and 4 wire, up to 10MHz)</td></tr>
<tr>
<td style="text-align: left;">I<sup style="margin-left: 0.07812em;">2</sup>C address</td>
<td style="text-align: left;">0x76(default)/ 0x77(optional)</td></tr></tbody></table>
<h3><u><a href="https://wiki.seeedstudio.com/Grove-16x2_LCD_Series/">Grove - 16 x 2 LCD (Black on Red)</a></u></h3>
<p><span>I2C LCD display grove - 16x2 is a great solution for Arduino and Raspberry Pi with high contrast and easy development which comes with two lines, each of which has 16 clumns, 32 characters in total. With Grove I2C connector, it only takes two signal pins and two power pins for the Grove 16x2 LCD display to work.</span></p>
<h5>Specification</h5>
<table class="wrapped">
<thead>
<tr>
<th style="text-align: left;">Item</th>
<th style="text-align: left;">Value</th></tr></thead>
<tbody>
<tr>
<td style="text-align: left;">Version</td>
<td style="text-align: left;">1.0</td></tr>
<tr>
<td style="text-align: left;">Operating Voltage</td>
<td style="text-align: left;">3.3V / 5V</td></tr>
<tr>
<td style="text-align: left;">Operating temperature</td>
<td style="text-align: left;">0 to 50℃</td></tr>
<tr>
<td style="text-align: left;">Storage temperature</td>
<td style="text-align: left;">-10 to 60℃</td></tr>
<tr>
<td style="text-align: left;">Driving method</td>
<td style="text-align: left;">1/16 duty, ⅕ bias</td></tr>
<tr>
<td style="text-align: left;">Interface</td>
<td style="text-align: left;">I<sup style="margin-left: 0.0px;">2</sup>C</td></tr>
<tr>
<td style="text-align: left;">I<sup style="margin-left: 0.0px;">2</sup>C Address</td>
<td style="text-align: left;">0X3E</td></tr></tbody></table>
<h3>Capacitive moisture sensor</h3>
<h4>Moisture sensor description</h4>
<p>TO DO</p>
<h4>Sensor calibration</h4>
<p>Source&nbsp;: <a href="https://makersportal.com/blog/2020/5/26/capacitive-soil-moisture-calibration-with-arduino">https://makersportal.com/blog/2020/5/26/capacitive-soil-moisture-calibration-with-arduino</a></p>
<p>You can cite the source as [3]</p>
<p>- Why are the sensor measurements linear dependant to the soil moisture (measurements of Capacitance + The volumetric water content is related to the dielectric content of soil and water by partitioning them as follows :</p>
<p><ac:image ac:thumbnail="true" ac:height="31"><ri:attachment ri:filename="Picture70.png" /></ac:image></p>
<p>And so :&nbsp;</p>
<p><ac:image ac:height="129"><ri:attachment ri:filename="Picture80.png" /></ac:image></p>
<h2><u><strong>Software design</strong></u></h2>
<h3><u><strong>Architecture</strong></u></h3>
<p>The figure below represents the architecture of our project.</p>
<p><ac:image ac:height="250"><ri:attachment ri:filename="Picture60.png" /></ac:image></p>
<p>The soil moisture, but also the weather data are measured by our sensors and transmitted, via the microcontroller, to the Frost server via a Cayenne protocol encryption.</p>
<p>We used the TUM server as a virtual machine, which collects and centralises all our data via 6 Python files working together. Every 6 hours, the server will request the latest data from our sensors, as well as weather data. All this data allows our server to choose whether or not to ask our microcontroller to pump water for our plant.</p>
<h3><u><strong>Sending uplink data</strong></u></h3>
<p>The following steps are being done to bring sensors' data into the Internet:</p>
<h4><u>Create entities for the device in the FROST-Server</u>&nbsp;</h4>
<p>All required properties (Thing, Location, Sensor, ObservedProperties) of a Datastream are created as JSON objects according to the SensorThingsAPI specification, so that &nbsp;the sensor observations can be stored in the FROST-Server. T<span style="color: rgb(23,43,77);">he JSON objects of the required properties are shown below:</span></p>
<h5><u><strong><span style="color: rgb(23,43,77);">Thing</span></strong></u></h5>
<p><span style="color: rgb(23,43,77);">The thing of the Datastream is ceated using the following code.</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8fd0077d-92b9-4a0e-b619-6d462d9a3309"><ac:parameter ac:name="theme">Midnight</ac:parameter><ac:parameter ac:name="title">Thing</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[{
  "name": "Automated Plant Watering System Thing",
  "description": "I am for testing and create random data.",
  "properties": {
    "frequency": "30 s",
    "groupNo": 5,
    "DevEUI": "0068BFFC9C146D7F"
  },
  "Locations": [
    {
      "name": "TUM, Arcisstr. 21 - Testlocation",
      "description": "Test location",
      "encodingType": "application/vnd.geo+json",
      "location": {
        "type": "Point",
        "coordinates": [
          11.568654,
          48.148653
        ]
      }
    }
  ]
}]]></ac:plain-text-body></ac:structured-macro>
<p><span>A Thing ID is generated in FROST-server with the help of HTTP Tool and the ID is appeared at the bottom of the dialog.</span></p>
<p><span style="color: rgb(23,43,77);"><ac:image ac:height="250"><ri:attachment ri:filename="Thing HTTP.png" /></ac:image></span></p>
<p><span style="color: rgb(23,43,77);"><a href="https://gi3.gis.lrg.tum.de/frost/v1.1/Things(77)">https://gi3.gis.lrg.tum.de/frost/v1.1/Things(77)</a></span></p>
<h5><u><strong>Sensor</strong></u></h5>
<p>After creating Thing ID, <span style="color: rgb(23,43,77);">we created a Sensor entity for each sensor attached to our device in the FROST-Server.</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e68510c3-3981-419d-b0cc-a2c79e36f112"><ac:parameter ac:name="theme">Midnight</ac:parameter><ac:parameter ac:name="title">SensorThingsAPI JSON Object: Sensor</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[{
  "name": "Grove BME680",
  "description": "Grove Temperature, Humidity, Pressure and Gas Sensor v1.0",
  "encodingType": "text/html",
  "metadata": "https://wiki.seeedstudio.com/Grove-Temperature_and_Humidity_Sensor_Pro/"
}]]></ac:plain-text-body></ac:structured-macro>
<p><ac:image ac:height="150"><ri:attachment ri:filename="Sensors HTTP.png" /></ac:image></p>
<p><a href="https://gi3.gis.lrg.tum.de/frost/v1.1/Sensors(131)">https://gi3.gis.lrg.tum.de/frost/v1.1/Sensors(131)</a></p>
<h5><u><strong>ObservedProperty</strong></u></h5>
<p>A Datastream's ObservedProperty describes the<span style="color: rgb(51,51,51);"> phenomenon of an Observation, thus creating ObservedProperties only once which are used by many Datastreams at once.</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="4983a086-3ee8-4261-90e2-8f5e8f728c44"><ac:parameter ac:name="theme">Midnight</ac:parameter><ac:parameter ac:name="title">SensorThingsAPI JSON Object: ObservedProperty/Temperature</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[{
  "name": "Temperature",
  "definition": "http://www.qudt.org/qudt/owl/1.0.0/quantity/Instances.html#ThermodynamicTemperature",
  "description": "The temperature."
}        ]]></ac:plain-text-body></ac:structured-macro>
<p><span style="color: rgb(51,51,51);"><ac:image ac:height="150"><ri:attachment ri:filename="OPTemp.png" /></ac:image></span></p>
<p><span style="color: rgb(51,51,51);"><a href="https://gi3.gis.lrg.tum.de/frost/v1.1/ObservedProperties(59)">https://gi3.gis.lrg.tum.de/frost/v1.1/ObservedProperties(59)</a></span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="4e8c6ac1-c7a0-4969-a888-244016552c41"><ac:parameter ac:name="theme">Midnight</ac:parameter><ac:parameter ac:name="title">SensorThingsAPI JSON Object: ObservedProperty/Pressure</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[{
    "name": "Pressure",
    "definition": "https://en.wikipedia.org/wiki/Pressure",
    "description": "Air pressure."
  }        ]]></ac:plain-text-body></ac:structured-macro>
<p><a href="https://gi3.gis.lrg.tum.de/frost/v1.1/ObservedProperties(60)">https://gi3.gis.lrg.tum.de/frost/v1.1/ObservedProperties(60)</a></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="3d83eda8-6479-4dc7-bce8-5771dd10d9f4"><ac:parameter ac:name="theme">Midnight</ac:parameter><ac:parameter ac:name="title">SensorThingsAPI JSON Object: ObservedProperty/Relative Humidity</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[{
    "name": "Relative Humidity",
    "definition": 	"https://en.wikipedia.org/wiki/Relative_humidity",
    "description": "The Relative Humidity."
  }        ]]></ac:plain-text-body></ac:structured-macro>
<p><a href="https://gi3.gis.lrg.tum.de/frost/v1.1/ObservedProperties(61)">https://gi3.gis.lrg.tum.de/frost/v1.1/ObservedProperties(61)</a></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="186eb22b-42a0-4231-bb6d-aef2ee51697e"><ac:parameter ac:name="theme">Midnight</ac:parameter><ac:parameter ac:name="title">SensorThingsAPI JSON Object: ObservedProperty/Soil Moisture</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[{
  "name":	"Soil Moisture",
  "definition":	"https://www.metergroup.com/crops/articles/what-is-soil-moisture-science-behind-the-measurement/",
  "description":	"Capacitive soil moisture measurement."
}]]></ac:plain-text-body></ac:structured-macro>
<p><a href="https://gi3.gis.lrg.tum.de/frost/v1.1/ObservedProperties(62)">https://gi3.gis.lrg.tum.de/frost/v1.1/ObservedProperties(62)</a></p>
<h5><u><strong>Datastream</strong></u></h5>
<p>Using the Thing, Sensor and ObservedProperty IDs from the previous steps, Datastreams are created for each sensor reading.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="70ed5fd9-9878-438b-9daf-e3f96f70a1cc"><ac:parameter ac:name="theme">Midnight</ac:parameter><ac:parameter ac:name="title">SensorThingsAPI JSON Object: Datastream/Temperature</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[{
  "name": "Room_temperature",
  "description": "The temperature inside Room.",
  "observationType": "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement",
  "unitOfMeasurement": {
    "name": "Centigrade",
    "symbol": "C",
    "definition": "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#DegreeCentigrade"
  },
  "Thing": {
    "@iot.id": 77
  },
  "ObservedProperty": {
    "@iot.id": 59
  },
  "Sensor": {
    "@iot.id": 131
  }
}]]></ac:plain-text-body></ac:structured-macro>
<p><ac:image ac:height="250"><ri:attachment ri:filename="DSTemp.png" /></ac:image></p>
<p><a href="https://gi3.gis.lrg.tum.de/frost/v1.1/Datastreams(253)">https://gi3.gis.lrg.tum.de/frost/v1.1/Datastreams(253)</a></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="cd56b942-aa7d-4fd7-b4ac-e04a9d0f5379"><ac:parameter ac:name="theme">Midnight</ac:parameter><ac:parameter ac:name="title">SensorThingsAPI JSON Object: Datastream/Pressure</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[{
    "name": "Room_pressure",
    "description": "The Air pressure inside Room.",
    "observationType": 	"http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement",
    "unitOfMeasurement": {
      "name": "Hecto Pascal",
      "symbol": "hPa",
      "definition": "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Pascal"
    },
    "Thing": {
      "@iot.id": 77
    },
    "ObservedProperty": {
      "@iot.id": 60
    },
    "Sensor": {
      "@iot.id": 131
    }
  }]]></ac:plain-text-body></ac:structured-macro>
<p><a href="https://gi3.gis.lrg.tum.de/frost/v1.1/Datastreams(254)">https://gi3.gis.lrg.tum.de/frost/v1.1/Datastreams(254)</a></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="48b3a33d-3e51-49db-a0ff-4af78d72aeb8"><ac:parameter ac:name="theme">Midnight</ac:parameter><ac:parameter ac:name="title">SensorThingsAPI JSON Object: Datastream/Relative Humidity</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[{
    "name": "Ashiq_room_humidity",
    "description": "The humidity inside Ashiq's room.",
    "observationType": 	"http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement",
    "unitOfMeasurement": {
      "name": "percentage",
      "symbol": "%",
      "definition": "https://en.wikipedia.org/wiki/Percentage""
    },
    "Thing": {
      "@iot.id": 67
    },
    "ObservedProperty": {
      "@iot.id": 53
    },
    "Sensor": {
      "@iot.id": 115
    }
  }]]></ac:plain-text-body></ac:structured-macro>
<p><a href="https://gi3.gis.lrg.tum.de/frost/v1.1/Datastreams(255)">https://gi3.gis.lrg.tum.de/frost/v1.1/Datastreams(255)</a></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="302fe332-2237-483f-9910-95ad16d2e719"><ac:parameter ac:name="theme">Midnight</ac:parameter><ac:parameter ac:name="title">SensorThingsAPI JSON Object: Datastream/Soil Moisture</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[{
    "name": "Soil_Moisture",
    "description": "The soil moisture around the plant.",
    "observationType": 	"https://defs.opengis.net/vocprez/object?uri=http%3A//www.opengis.net/def/sensor-model-param/xdomes/moisture_content_of_soil_layer",
    "unitOfMeasurement": {
      "name": "percentage",
      "symbol": "%"
     
    },
    "Thing": {
      "@iot.id": 77
    },
    "ObservedProperty": {
      "@iot.id": 62
    },
    "Sensor": {
      "@iot.id": 131
    }
  }]]></ac:plain-text-body></ac:structured-macro>
<p><a href="https://gi3.gis.lrg.tum.de/frost/v1.1/Datastreams(256)">https://gi3.gis.lrg.tum.de/frost/v1.1/Datastreams(256)</a></p>
<h4><u><strong>Query data stream IDs</strong></u></h4>
<p>We can query the datastream IDs from the server using this following query after having all the ID of the Thing.</p>
<p><a href="https://gi3.gis.lrg.tum.de/frost/v1.1/Things(77)?$expand=Datastreams($select=@iot.id,name,description)">https://gi3.gis.lrg.tum.de/frost/v1.1/Things(77)?$expand=Datastreams($select=@iot.id,name,description)</a></p>
<h4><u><strong>Create a sensor data planning table</strong></u></h4>
<table class="wrapped"><colgroup><col /><col /><col /><col /><col /><col /><col /><col /></colgroup>
<tbody>
<tr>
<th>Name</th>
<th>GroupNo</th>
<th>Thing</th>
<th>DevEUI</th>
<th>Sensor</th>
<th>ObservedProperty</th>
<th>&nbsp;LppChannelNr</th>
<th><span style="color: rgb(23,43,77);">FROST Datastream IDs</span></th></tr>
<tr>
<td rowspan="4">Md Ashiqur Rahman</td>
<td rowspan="4">9</td>
<td rowspan="4">SeeeduinoLoRaWAN, Indoor, TUM, Arcisstr. 21</td>
<td rowspan="2">SWM: 003579593BE50175</td>
<td rowspan="2">Grove - BME680</td>
<td>Temperature [&deg;C]</td>
<td>1</td>
<td>253</td></tr>
<tr>
<td><span style="color: rgb(23,43,77);">Humidity [%H]</span></td>
<td>2</td>
<td>255</td></tr>
<tr>
<td rowspan="2">TTN: 8765182202E81E12</td>
<td rowspan="2">Grove Soil Moisture Sensor</td>
<td>Pressure (kPa)</td>
<td>3</td>
<td>254</td></tr>
<tr>
<td><span style="color: rgb(23,43,77);">Voltage [V]</span></td>
<td>4</td>
<td>256</td></tr></tbody></table>
<h4><u><strong>Cayenne LPP</strong></u></h4>
<p>Sensor readings are encoded according to the Cayenne Low Power Payload (Cayenne LPP) protocol.

<h4><u><strong>LoRaWAN connection</strong></u></h4>
<p>We used the SWM network to setup our LoRaWAN connection using the SWM <span style="color: rgb(23,43,77);">DevEUI.</span></p>
<h4><u><strong>Setup mapping from Cayenne to FROST-Server</strong></u></h4>
<p>A mapping JSON document is created in MongoDB containing the routing information to provide mapping information to allow package routing from your Cayenne Lpp Channel numbers to FROST-Server Datastream IDs. The image belows gives on overview on the mapping document and the tools, that store and use it:</p>
<p><br /></p>

<h5><u><strong>Mapping LPP channels to FROST Datastreams</strong></u></h5>
<p>A mapping document is created using the information from the sensor data planning table.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="94d63130-5c75-4107-85fd-34f85a61429f"><ac:parameter ac:name="theme">Midnight</ac:parameter><ac:parameter ac:name="title">SensorThingsAPI JSON Object: Datastream</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[{
    _id: '003579593BE50175',
    name: 'Automated-Plant-Watering-Device',
    group_id: 9,
    dev_eui: '003579593BE50175',
    datastreams: [
        {
            lpp_id: 1,
            sta_servers: [
                {
                    sta_url: 'https://gi3.gis.lrg.tum.de/frost/v1.1',
                    datastream_iot_id: 253
                }
            ]
        },
        {
            lpp_id: 2,
            sta_servers: [
                {
                    sta_url: 'https://gi3.gis.lrg.tum.de/frost/v1.1',
                    datastream_iot_id: 255
                }
            ]
        },
        {
            lpp_id: 3,
            sta_servers: [
                {
                    sta_url: 'https://gi3.gis.lrg.tum.de/frost/v1.1',
                    datastream_iot_id: 254
                }
            ]
        },
        {
            lpp_id: 4,
            sta_servers: [
                {
                    sta_url: 'https://gi3.gis.lrg.tum.de/frost/v1.1',
                    datastream_iot_id: 256
                }
            ]
        }   
    ]
}]]></ac:plain-text-body></ac:structured-macro>
<h5><u><strong>Post mappings document to MongoDB</strong></u></h5>
<p><a href="https://gi3.gis.lrg.tum.de/mongo-student/db/geosensorweb/student"><ac:image ac:height="250"><ri:attachment ri:filename="Mongo.png" /></ac:image></a></p>
<p><br /></p>
<p><ac:image ac:height="400"><ri:attachment ri:filename="MongoCode.png" /></ac:image></p>
<h3><u><strong>Decision-making process</strong></u></h3>
<h4>Retrieving the sensor data</h4>
<p>Every 6 hours, the server will request the latest data from our sensors. To do this, we send a request to the url of the Frost server of our project. In particular, the requests states that:</p>
<ul>
<li>The measurements have to by ordered by their respective <em>phenomenonTime</em>, from to the most to the least recent.</li>
<li>The number of measurements to retrieve is flexible, through the variable <em>nb_entries</em>.</li>
<li>As the moisture sensor wasn&rsquo;t calibrated before July, 10<sup>th</sup> 2022, the request only retrieve the measurements after this date.</li></ul><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8ba400bd-95d6-4d6b-9eaf-3ec9d7a1fba7"><ac:parameter ac:name="language">py</ac:parameter><ac:parameter ac:name="title">Function to get the data from the moisture sensor</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[####################################
## Author: Baptiste Verneuil
## Group number: 9
## Last date of change: 30/08/2022
####################################


import requests
import datetime

def get_sensor_data(thing_id=80, datastream_id=269, nb_entries = 1):
    """
    Return the list of the hourly precipitation (in mm)
    ---------------------
    parameters:
    lat: str
        latitude of the selected location
    lon: str
        longitude of the selected location
    date: str
        selected date, in the format yyyy-mm-dd
    """

    # We remove data before 10/07/2022 (uncalibrated sensor)
    url = "https://gi3.gis.lrg.tum.de/frost/v1.1/Things({thing_id})/Datastreams({datastream_id})/Observations?$orderby=phenomenonTime%20desc&$top={nb_entries}&$select=result,phenomenonTime&$filter=phenomenonTime ge 2022-07-10T00:00:00Z"
    
    resp = requests.get(url=url.format(thing_id=str(thing_id), datastream_id=str(datastream_id), nb_entries = str(nb_entries)))
    data = resp.json() # Check the JSON Response Content documentation below

    sensor_values = [data["value"][i]["result"] for i in range(len(data["value"]))]
    dates = [datetime.datetime.strptime(data["value"][i]["phenomenonTime"], "%Y-%m-%dT%H:%M:%S.%fZ") for i in range(len(data["value"]))]
    
    # Chronological order
    sensor_values.reverse()
    dates.reverse()

    return sensor_values, dates]]></ac:plain-text-body></ac:structured-macro>
<p><br /></p>
<p><span style="font-weight: 600;letter-spacing: -0.003em;">Retrieving the weather data</span></p>
<p>The weather data comes from the Deutscher Wetterdienst (DWD), the German public weather service, via the open-source API <a href="https://brightsky.dev/docs/">Brightsky</a>. Thus, we can get the temperature, the humidity, the wind speed and especially the precipitation for the next 24 hours.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="87ee2652-14a5-46e0-8858-a1c55f554e3a"><ac:parameter ac:name="language">py</ac:parameter><ac:parameter ac:name="title">Function to get the precipitation using the Brightsky API</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[####################################
## Author: Baptiste Verneuil
## Group number: 9
## Last date of change: 30/08/2022
####################################


import requests
from datetime import datetime, timedelta

def get_precipitation(lat, lon, first_date, last_date):
    """
    Return the list of the hourly precipitation (in mm)
    ---------------------
    parameters:
    lat: str
        latitude of the selected location
    lon: str
        longitude of the selected location
    date: str
        selected date, in the format yyyy-mm-dd
    """
    url = "https://api.brightsky.dev/weather?lat={lat}&lon={lon}&date={first_date}&last_date={last_date}"

    resp = requests.get(url=url.format(lat=lat, lon=lon, first_date=first_date, last_date=last_date))
    data = resp.json() # Check the JSON Response Content documentation below

    list_precipitation = [data["weather"][i]["precipitation"] for i in range(len(data["weather"]))]
    list_date = [datetime.strptime(data["weather"][i]["timestamp"], "%Y-%m-%dT%H:%M:%S%z") for i in range(len(data["weather"]))] # We convert the string dates to datetime/datetime objects

    return list_precipitation, list_date]]></ac:plain-text-body></ac:structured-macro>
<h4>Forecasting the soil moisture</h4>
<p>In order to decide when to water the plant, we decided to make soil moisture predictions from a linear regression. However, we want to give more importance to the most recent values: this is why we have performed a weighted linear regression, with decreasing weights for more distant values. Thus processes such as a rapid water spreading in the plant pot of the last watering will not be taken into account.</p>
<p><ac:image ac:height="250"><ri:attachment ri:filename="Picture50.png" /></ac:image></p>
<p>Hence, the participation to the linear regression of the first points in the figure above remains very low, while the regression is giving more credit to the last point which could be more representative of a current trend.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="f2db6d11-2601-4432-b3d1-4521b847a043"><ac:parameter ac:name="language">py</ac:parameter><ac:parameter ac:name="title">Functions used for doing the weighted linear regression</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[####################################
## Author: Baptiste Verneuil
## Group number: 9
## Last date of change: 30/08/2022
####################################


def multiply_matrix(x, y):
    return [x[i] * y[i] for i in range(len(x))]

def estimate_coef(x, y):
    """
    Return the coefficients of the linear regression fitting the points listed int he lists x and y
    Inspired from https://github.com/OpenGenus/quark/blob/master/code/code/artificial_intelligence/src/Linear_Regression/linear_regression.py
    ---------------------
    parameters:
    x: list of floats
        list of the points x-axis
    y: list of floats
        list of the points y-axis
    """
    # number of observations/points
    n = len(x)
  
    # mean of x and y vector
    m_x = sum(x) / len(x)
    m_y = sum(y) / len(y)
  
    # calculating cross-deviation and deviation about x
    SS_xy = sum(multiply_matrix(y, x)) - n*m_y*m_x
    SS_xx = sum(multiply_matrix(x, x)) - n*m_x*m_x
  
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
  
    return (b_0, b_1)

def update_x_y_weight(x, y, w):
    """
    Function to convert a weighted linear regression problem into a classical linear regression problem
    Return the new lists of describing the points taking into account the weight of each point
    ---------------------
    parameters:
    x: list of floats
        list of the points x-axis
    y: list of floats
        list of the points y-axis
    w: list of floats
        list of the points weight
    """
    # turning weights into integers between 0 and 1000
    max_w = max(w)
    w = [int((w[i]*1000)/max_w) for i in range(len(w))]

    # We add in the new list new_x the x[i] value w[i] times (resp. new_y and y[i])
    new_x, new_y = [], []
    for i in range(len(x)):
        for j in range(w[i]):
            new_x.append(x[i])
            new_y.append(y[i])
    return new_x, new_y

def weighted_linear_regression(x, y, w):
    return estimate_coef(*update_x_y_weight(x, y, w))]]></ac:plain-text-body></ac:structured-macro>
<p>It is then possible to extrapolate a rate of decrease in soil moisture for the next 24 hours; to this we can add the collected rainfall data. The precipitation is converted into a percentage of soil moisture using parameters specific to our plant, such as the surface area reached by the rain and the volume of soil in the pot.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ba6687b8-1d9e-4e6b-bf7a-b19bf7aeb72d"><ac:parameter ac:name="language">py</ac:parameter><ac:parameter ac:name="title">Function for forecasting the soil moisture</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[####################################
## Author: Baptiste Verneuil
## Group number: 9
## Last date of change: 30/08/2022
####################################


def forecast_moisture(moisture_past, date_moisture_past, weights, precipitation_forecast, dates_forecast, plot=False):
    """
    Function for forecasting the soil moisture, taken into account the precipitation forecast, using a weighted linear regression
    Return the list of the future moisture, as well as the coefficient of the weitghed linear regression
    ---------------------
    parameters:
    moisture_past: list of floats
        list of the moisture measurements
    date_moisture_past: list of floats
        list of the dates asociated with each moisture measurement
    weights: list of floats
        list of the points weight
    precipitation_forecast: list of floats
        list of precipitation forecast
    dates_forecast: list of floats
        list of the dates of the precipitation forecast
    plot: boolean
        Boolean set to True if we want to plot the linear regression
    """

    b = weighted_linear_regression(date_moisture_past, moisture_past, weights)

    # Used for plotting the weighted regression
    if plot==True : 
        y_pred = [b[1]*date_moisture_past[i]+b[0] for i in range(len(date_moisture_past))]
        import matplotlib.pyplot as plt
        plt.scatter(date_moisture_past, moisture_past, s=weights, c='grey', edgecolor='black')
        plt.plot(date_moisture_past, y_pred, color='blue', linewidth=3, label='Weighted model')
        plt.legend()
        plt.show()

    # returning predicted moisture
    future_moisture = [b[1]*dates_forecast[i]+b[0] for i in range(len(dates_forecast))]

    # Adding the precipitation
    for i,p in enumerate(precipitation_forecast):
        if p!=0:
            for j in range(i, len(future_moisture)):
                future_moisture[j]+=p*config.area_plant*config.conversion_moisture_volume

    return future_moisture, b]]></ac:plain-text-body></ac:structured-macro>
<h4>The decision-making algorithm</h4>
<p>In order to determine when to water the plant, we have defined critical moisture thresholds. These thresholds are specific to each type of plant, and it is often possible to find these values online.</p>
<p><ac:image ac:height="400"><ri:attachment ri:filename="Picture40.png" /></ac:image></p>
<p>There are two criteria for watering the plant. Firstly, the soil moisture must be below the maximum soil moisture limit; secondly, the soil moisture is expected to exceed the recommended minimum soil moisture limit within 24 hours. If these two criteria are met, then the pump is instructed to compensate for the drop in moisture to remain at an optimal soil moisture level.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="5f5e68a6-4091-450a-9ec0-d85f11cfc440"><ac:parameter ac:name="language">py</ac:parameter><ac:parameter ac:name="title">Criteria for watering (part of the file main.py)</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[	####################################
	## Author: Baptiste Verneuil
	## Group number: 9
	## Last date of change: 30/08/2022
	####################################
 	
	
	# Giving order to the pump if needed, 2 criteria for watering the plant : 
    # 1) Current moisture is not too wet
    # 2) in the next 24H, soil moisture will be too dry

    current_moisture = past_moisture[-1] # current value = last value of the past

    if current_moisture < config.moisture_too_wet and min(moisture_future)[0] < config.moisture_too_dry:
        logger.info("Some pumping is required !")

        # We set the moisture the the target moisture
        moisture_to_add = config.target_moisture - min(moisture_future)

        # Sending the information to the pump
        success = send_info_pump(moisture_to_add)
        if success == 0 :
            logger.info("Successful sending of data to the pump")
        else :
            logger.info('\nSometing went wrong: HTTP Status: %s: %s' % (success[0], success[1]))
    else :
        logger.info("No pumping required")]]></ac:plain-text-body></ac:structured-macro>
<p>All the parameters specific to the plant (including the moisture thresholds and the parameters to convert the precipitation data into soil moisture) are stored in the file <em>config.py</em></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="4fd3dc84-84cf-452a-83d1-21ef7a4584c9"><ac:parameter ac:name="language">py</ac:parameter><ac:parameter ac:name="title"> Parameters depending on the plant</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[####################################
## Author: Baptiste Verneuil
## Group number: 9
## Last date of change: 30/08/2022
####################################


lat="48.121842"
lon="11.600352"
moisture_too_wet = 80
moisture_too_dry = 40
target_moisture = 65
area_plant = 0.01 # in m^2 (10cm*10cm)
conversion_moisture_volume = 400 # 1L of water = +400% of soil moisture
flow_rate_pump = 38 #mL/s]]></ac:plain-text-body></ac:structured-macro>
<p><br /></p>
<h3><span style="font-size: 16.0px;font-weight: bold;letter-spacing: -0.006em;">Sending downlink data</span></h3>
<h4>Sending data from the TUM server to the pump</h4>
<p>In the case where we want to water the plant, we have to send data downlink back to the microcontroller. This data is sent through a Python file, which sends - through the Frost server - a data in hexadecimal format. This data represents the percentage of moisture to be added for our plant. This data is then converted into milliseconds of pumping, thanks to the volume of soil in the pot and the flow rate of the pump that we have previously measured with the Flow Rate Sensor. Finally, we convert the milliseconds of pumping into an integer between 0 and 255 (u_int8 format).</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8454b81c-302a-4208-a6bc-6e8abc1f2ded"><ac:parameter ac:name="language">py</ac:parameter><ac:parameter ac:name="title">downlink_swm.py</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[####################################
## Author: Baptiste Verneuil
## Group number: 9
## Last date of change: 30/08/2022
####################################


import requests
import binascii
import config
 
def send_info_pump(moisture_to_add):
  """
    Send the moisture to our microcontroller (through the Frost sever) the number of milliseconds of pumping for the plant
    Return 0 if success, else return the response
    ---------------------
    parameters:
    moisture_to_add: float
        moisture we want to add to the plant (in percent)
    """

  # SWM LoRaWAN config ----------------------------------------------------------
  url = 'https://iot-lns.swm.de/1/rest'
  token = 'Bearer vgEAGAAAAA5pb3QtbG5zLnN3bS5kZbtqvQH--h5qpruoSK4aJBo='
  
  eui = '00B193384D6E47B8'
  port = 33
  confirmed = 'false'
  appid = 'BE01000A'
  
  # LoRaWAN payload -------------------------------------------------------------
  size = 1                    # Length of the byte array
  arr = bytearray(size)       # Init byte array
  
  # convert moisture in percent to milliseconds of pumping
  time_second = moisture_to_add *(1000/config.conversion_moisture_volume)*(1/config.flow_rate_pump)
   # Set values (converted in u_int8) to array positions
  arr[0] = int((time_second/20)*255)

  # Convert bytearray to UTF-8 HEX String
  hex = binascii.hexlify(bytearray(arr))
  hex_string = hex.decode('utf-8')
  
  # Build HTTP header
  headers = {
      'Authorization': token,
      'Cache-Control': 'no-cache',
      'Content-Type': 'application/json',
  }

  # Build HTTP body
  data = '{\n"cmd": "tx",\n"EUI": "' + eui + '",\n"port": ' + str(port) + ',\n"confirmed": '+ confirmed + ',\n"data": "' + hex_string +  '",\n"appid": "' + appid + '"\n}'
  
  # Send HTTP POST
  response = requests.post(url, headers=headers, data=data)
  
  # Check request response for errors
  if response.status_code < 300:
    return 0
  else:
    return [response.status_code, response.reason]]]></ac:plain-text-body></ac:structured-macro>
<h4><span style="letter-spacing: 0.0px;">Process automation</span></h4>
<p>Our program is controlled by a cron job, presented here through a screenshot of the crontab. We can set some parameters, such as the number of data from our sensor to retrieve (with <em>- s 100</em>, for retrieving one hundred values), or the number of days of forecast to generate (with <em>-d 1</em>, for a one-day forecasting).</p>
<p><ac:image ac:width="400"><ri:attachment ri:filename="Picture1.png" /></ac:image></p><br />
<h2><u style="font-size: 20.0px;letter-spacing: -0.008em;"><strong>Results</strong></u></h2>
<h3>Visualization with Grafana</h3>
<p>We used Grafana to visualize our sensors' data. With its powerful plug-in system, Grafana provides charts, graphs and alerts for the web when connected to supported data sources.&nbsp;</p>
<p><ac:image ac:height="400"><ri:attachment ri:filename="Grafana.png" /></ac:image></p>
<h3>Visualization of the logs</h3>
<p>Each step of the automated process, as well as error messages, are documented in a custom log file; you can see an example of the log file rendering here.</p>
<p>This file allows us to have an overview of the functioning of each step of our process, and to identify easily the errors.</p>
<p><ac:image ac:height="250"><ri:attachment ri:filename="Picture2.png" /></ac:image></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="73a1462a-444b-4355-86f2-50f69b47d733"><ac:parameter ac:name="language">py</ac:parameter><ac:parameter ac:name="title">Use of a Python logger (part of the file main.py)</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[	####################################
	## Author: Baptiste Verneuil
	## Group number: 9
	## Last date of change: 30/08/2022
	####################################
	 
	
	# Setup logger
    config.setup_logger(logfile="pws.log", level=args.verbosity)
    logger.info("Using PlantWateringSystem version %s", config.__version__)

    # Getting past moisture
    past_moisture, dates_moisture = get_sensor_data(nb_entries=args.n_sensor)
    logger.info("Successful acquisition of sensor data")]]></ac:plain-text-body></ac:structured-macro>
<h3>Results of the algorithm</h3>
<p>To Do (Baptiste)</p>
<p>how to interpret the observed values ?</p>
<p>Were the results checked by the students and possibly compared with reference measurements?</p>
<h2>Conclusion</h2>
<h3>Objectives fulfilment</h3>
<p>Is there a discussion at the end of the report to which degree the objectives were met? Are the reasons discussed on objectives that were not met on why they were not met?</p>
<p><br /></p>
<p>What does our project bring to the table compared to the other projects of part 1.4?</p>
<ul>
<li>We used some weather data to forecast the soil moisture, and to prevent the soil moisture to drop below the threshold value. Moreover, the precipitation forecasts allowed our system to prevent useless watering and to spare some water.</li></ul>
<h3>Challenges and further improvements</h3>
<p>From Presentation</p>
<ul>
<li>The device fails to upload data when it gets disconnected from laptop and plug into the socket.</li>
<li>There&nbsp;is no defined&nbsp;Cayenne LPP data&nbsp;for&nbsp;soil moisture&nbsp;sensor.</li>
<li>Continuous measuring of water flow using water flow sensor</li>
<li>Use of&nbsp;FAO Penman Monteith equations not necessarily applicable to a pot plant</li></ul>
<p>Text of the presentation (Baptiste)</p>
<p>To create the decision-making algorithm, we faced several challenges. Firstly, collecting data a long process: the typical drying time for a plant pot is up to one week. That is the reason why this project was very challenging, because a lot of experimental data was needed for validating the choice of algorithm.</p>
<p>Moreover, we first wanted to use precise equations for determining the water balance of the plant which could have included radiation, heat flux, temperature, wind speed and vapour pressure. But these equations not necessarily applicable to a pot plant. Collecting a lot of data would allow us to analyse it and to build our own water balance equations with our own parameters: it would be a good way of improving our project, making it more precise and taking into account key parameters <span style="letter-spacing: 0.0px;">such as sunlight levels.</span></p>
<p><span style="letter-spacing: 0.0px;"><ac:image ac:height="150"><ri:attachment ri:filename="Picture3.png" /></ac:image><br /></span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell>
<h2><span>Annexes</span></h2>
<h3>Supervisor</h3>
<p>Bruno Willenborg</p>
<h3>Arduino code snippet</h3><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="2049e24c-323c-4e30-8ff0-6d484dc71df5"><ac:parameter ac:name="language">cpp</ac:parameter><ac:parameter ac:name="title">Main arduino code</ac:parameter><ac:parameter ac:name="collapse">true</ac:parameter><ac:plain-text-body><![CDATA[/////////////////////////////////////////////////////////////////
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
}]]></ac:plain-text-body></ac:structured-macro>
<h3>Github link</h3>
<p><a href="https://github.com/BaptisteVerneuil/PlantWateringSystem">https://github.com/BaptisteVerneuil/PlantWateringSystem</a></p>
<h3>References</h3>
<p>[1] Shah, Kritika and Pawar, Saylee and Prajapati, Gaurav and Upadhyay, Shivam and Hegde, Gayatri, 2019. , Proposed Automated Plant Watering System Using IoT.&nbsp; [Online]. Available at&nbsp;<a href="https://dx.doi.org/10.2139/ssrn.3360353">http://dx.doi.org/10.2139/ssrn.3360353</a></p>
<p>[2] Đuzić, Nermin &amp; Đumić, Dalibor, 2017. Automatic Plant Watering System via Soil Moisture Sensing by means of Suitable Electronics and its Applications for Anthropological and Medical Purposes. Collegium Antropologicum. 41. 169-172. [Online]. Available at <a href="https://hrcak.srce.hr/file/295019">https://hrcak.srce.hr/file/295019</a></p>
<p>[3] Joshua Hrisko, 2020. Capacitive Soil Moisture Sensor Calibration with Arduino. [Online]. Maker Portal. Available at : <a href="https://makersportal.com/blog/2020/5/26/capacitive-soil-moisture-calibration-with-arduino">https://makersportal.com/blog/2020/5/26/capacitive-soil-moisture-calibration-with-arduino</a></p></ac:layout-cell></ac:layout-section></ac:layout>