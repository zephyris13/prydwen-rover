# omega-eyes
A WiFi camera unit that can pan and tilt based on the commands from a device on the same WiFi network

# Physical setup

## Controller

Plug in the Arduino Dock device. Wait for 2 min for it to fully boot.

## Actuator

* Connect the servo with the **yellow** tape on the lead to Channel 0 on the PWM Expansion.
  * Note that the orange wire is the signal wire and the brown wire is ground
* Connect the servo with the **green** tape on the lead to Channel 1 on the PWM Expansion
  * Note that the orange wire is the signal wire and the brown wire is ground
* Connect the DC Adapter to the Servo Expansion Barrel Jack
* Power on the Actuator Omega
* Wait for about two minutes

* Now try moving the joystick on the Controller, the webcam should move
  * If it doesn't move, try rebooting the Actuator Omega by unplugging the MicroUSB adapter and plugging it back in
  * If that still doesn't work, try rebooting the Controller Omega, and then the Actuator Omega


## The Webcam Stream

* Connect to the `Omega-Eyes-Controller` WiFi network, the password is `12345678`
* Navigate to `http://omega-29e4.local/` to get to the console of the Actuator Omega
* Open the Webcam App and start streaming
