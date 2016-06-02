// 02_buzz_bot.js

// Necessary files
load("readline.js");
load("Finch.js");
load("sleep.js");

// Initialize the finch
var myFinch = new Finch();

// All commands go here
myFinch.playTone(440, 500); //Plays the not 'A' for 0.5 seconds
sleep(500);

// Close the connection with the finch
myFinch.reset();
