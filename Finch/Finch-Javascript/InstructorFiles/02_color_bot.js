// 02_color_bot.js

// Necessary files
load("readline.js");
load("Finch.js");
load("sleep.js");

// Initialize the finch
var myFinch = new Finch();

// All commands go here
myFinch.setLED(255,0,0);  // Changes color to red (R, G, B)
sleep(2000);              // Pauses the program for X milliseconds

// Close the connection with the finch
myFinch.reset();
