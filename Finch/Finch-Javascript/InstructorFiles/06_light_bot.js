// 06_light_bot.js

// Necessary files
load("readline.js");
load("Finch.js");
load("sleep.js");

// Initialize the finch
var myFinch = new Finch();

// All commands go here
while (!StdIn.isInputAvailable()) {

  var sensors = myFinch.getLightSensors()

  if (sensors.left > sensors.right) {
    myFinch.setWheelPower(64, 255);  // Move the finch left
  } else {
    myFinch.setWheelPower(255, 64); // Move the finch right
  }
}

// Close the connection with the finch
myFinch.reset();
