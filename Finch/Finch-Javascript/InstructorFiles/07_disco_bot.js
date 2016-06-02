// 07_disco_bot.js

// Necessary files
load("readline.js");
load("Finch.js");
load("sleep.js");

// Initialize the finch
var myFinch = new Finch();

// All commands go here
while (!StdIn.isInputAvailable()) {

  var sensors = myFinch.getAccelerations();

  myFinch.setLED(100 * sensors.x, 100 * sensors.y, 100 * sensors.z);

}

// Close the connection with the finch
myFinch.reset();
