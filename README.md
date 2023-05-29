# pi-battery-widget

<b>** Our Kickstarter campaign has now finished, and we have completed shipping nearly a thousand units to all our backers! We are live with a pre-order form in case you missed our campaign or would like to order more units, please check our website at https://www.theredreactor.com/ - and check out our reviews page at https://www.theredreactor.com/reviews/ **</b>

But you can still see the story of our campaign journey on our <a href="https://www.kickstarter.com/projects/pascal-h/the-red-reactor-when-power-really-matters">Kickstarter page</a>, which also shows customer comments and our technology updates.

The Red Reactor is designed to fit underneath your Raspberry Pi, leaving the 40-pin header free for all the sensors, displays and other gadgets that you want to use in your projects. With ultra-low stand-by power, and seamless transition even at high currents between the battery and external power, it ensures your data is safe and your design just keeps on working. A wide range of features enable you to quickly create a robust system, including accurate access to the battery voltage and current, simple ON button integration and RUN/RESET support, battery protection and carefully managed charging circuitry to maximise battery life.

This code has been forked from the pi-battery-widget status icon widget, with major design changes
to support The Red Reactor Raspberry Pi UPS, including accurate battery life modelling for charging
and discharging profiles.<br>

<b>Now features Battery LOW warning and Battery EMPTY Auto-shutdown</b>

Please visit https://github.com/Scally-H/RedReactor for more technical details and code examples.

Please visit https://www.theredreactor.com for Info, News and <a href="https://www.theredreactor.com/reviews/">Reviews</a> from our Kickstarter and pre-order backers!

The C code executes the python code to configure and the read the battery voltage and current via
the INA219 I2C device, also allowing for the detection of charging, charging complete and no battery states.

Python code output format is 
```
voltage(float) | current(float) 

4.142 | 1088.98
```

**Features**
- <b> Updated for Bullseye</b>
- <b>NEW: Battery LOW Warning Pop-up at 10%</b>
- <b>NEW: Auto shutdown 30 seconds after Battery EMPTY Warning Pop-up at 0% (2.9v)</b>
- Displays a battery widget on the desktop panel of the general Raspberry LXDE at the right side
in the System Tray section.
- The green bar turns red if the battery charge left is below 10%, and yellow if the
battery is charging.
- The time remaining is displayed as a tooltip (both for charging and discharging!)
- The display is updated every 5 seconds
- Logs all activities in ~/RedReactor_batteryLog.txt
- Log File shows instant and averaged readings, battery life and status<br>
   chargingState = -1 is "no battery"<br>
   chargingState = 0 is "discharging"<br>
   chargingState = 1 is "charging"<br>
   chargingState = 2 is "externally powered "<br>
 
- Actual battery reading code is done in python script based on The Red Reactor configuration

![Alt text](icon.png?raw=true "panel with battery widget")

The Red Reactor UPS for Raspberry Pi zero, Pi Model 2/3 and Pi Model 4!
<img src="UPS-18650.png" width="50%"  alt="The Red Reactor Raspberry Pi 18650 UPS">


**Installation**

The application assumes you already have python3 installed (usually the case on Raspberry Pi OS).  
However, you also need to install the python INA219 library, as follows from a terminal window:

```
sudo pip3 install pi-ina219
```
Please remember to enable the I2C bus under the Advanced Options of raspi-config or via the GUI, as documented in the Red Reactor instruction manual (you will need to reboot the Pi for this to take effect).

Then, type the following

```
  cd
  cd Downloads
  git clone https://github.com/Scally-H/pi-battery-widget
  cd pi-battery-widget
```

Make sure GTK3.0 library is installed:
```
sudo apt install libgtk-3-dev
```


Compile the code with the following commands:
```
  make
```

Finally install the widget with the following commands:
```
  chmod +x install
  ./install 
```

Please check the install script output for errors. It has been tested on Raspberry Pi with Buster,
and creates or updates the ~/.config/lxsession/LXDE-pi/autostart file.

Please adjust your chosen battery capacity by editing ~/.config/lxpanel/LXDE-pi/panels/redreactor.conf
(given in mAh for total capacity)

When the widget is running, you can check for startup errors and battery information at ~/RedReactor_batterylog.txt

You can also run the python code directly to verify reading the battery info:
```
  python3 pi-battery-reader.py
```

Reboot your pi.


**To update the widget to the latest version**

Open a terminal and type

```
  cd
  cd Downloads/pi-battery-widget
  git pull
  make
```
Now install the updated widget
```
  chmod +x install
  ./install
```


**To uninstall the widget**

Open a terminal and type

```
  cd
  cd Downloads/pi-battery-widget
  chmod +x uninstall
  ./uninstall
```

Please open an issue in this repository or write to hello@theredreactor if you have any feedback
or problem with this repository. Your input is appreciated.


**Reference**

https://www.theredreactor.com  
https://github.com/Scally-H/RedReactor  
https://github.com/mezl/pi-battery-widget  
https://github.com/linshuqin329/UPS-18650  
https://github.com/rricharz/pi-top-battery-widget  

