/*
 * script.js
 * Date: 6-29-16
 */

$(document).ready(function() {

    // Get all elements with the button class
    var button = $('.button');

    $('.button').mouseover(function () {
        // Change the button's content
        $('.button').html('Fine... Click me');
    });

    $('.button').mouseleave(function () {
        // Change the button's content
        $('.button').html('Do not click me');
    });

    // Change the click event for the
    button.click(function() {
        console.log(randomColor());

        // Generate the color
        var colorString = randomColor();

        // Set color
        $('.flash-wrapper').attr('style', 'background-color:' + colorString);
        $('.button').attr('style', 'color:' + colorString);
    });
});

function randomColor() {

    // Generate the random color
    var r = Math.floor(Math.random() * 256);
    var g = Math.floor(Math.random() * 256);
    var b = Math.floor(Math.random() * 256);

    // Format color
    var colorString = 'rgb(';
    colorString += r.toString() + ',';
    colorString += g.toString() + ',';
    colorString += b.toString() + ')';

    return colorString;
}
