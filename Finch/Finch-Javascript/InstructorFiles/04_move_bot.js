// 04_move_bot.js

// Necessary files
load("readline.js");
load("Finch.js");
load("sleep.js");

// Initialize the finch
var myFinch = new Finch();

// All commands go here
myFinch.setWheelPower(255,255); // Move the finch forward
sleep(1000);

myFinch.setWheelPower(-255,-255); // Move the finch backward
sleep(1000);

// Close the connection with the finch
myFinch.reset();
