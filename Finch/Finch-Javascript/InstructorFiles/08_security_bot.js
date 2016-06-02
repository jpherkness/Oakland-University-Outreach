// 08_security_bot.js

// Necessary files
load("readline.js");
load("Finch.js");
load("sleep.js");

// Initialize the finch
var myFinch = new Finch();

// All commands go here
var allSensors = myFinch.getAllSensors();
while (allSensors.accelerometer.x > -0.5) {
  allSensors = myFinch.getAllSensors();  // Update the sensor values

}

// Close the connection with the finch
myFinch.reset();
