// 05_obstacle_bot.js

// Necessary files
load("readline.js");
load("Finch.js");
load("sleep.js");

// Initialize the finch
var myFinch = new Finch();

// All commands go here
while (!StdIn.isInputAvailable()) {

  var sensors = myFinch.getObstacleSensors()

  if (sensors.left || sensors.right) {
    myFinch.setWheelPower(-255,-255);
  } else {
    myFinch.setWheelPower(255,255);
  }
}

// Close the connection with the finch
myFinch.reset();
