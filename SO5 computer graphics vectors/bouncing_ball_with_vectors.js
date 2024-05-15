let position;
let velocity;

function setup() {
    createCanvas(600,200)
    
    position = createVector(100,100);
    velocity = createVector(2, 4.3);
}

function draw() {
    background(255);

    // add the vectors together using the p5.Vector class's add() method
    position.add(velocity);

    // to refer to individual coordinates, use the dot syntax: position.x etc.
    if (position.x > width || position.x < 0) {
        velocity.x = velocity.x * -1;
    }
    if (position.y > height || position.y < 0) {
        velocity.y = velocity.y * -1;
    }

    // draw the ball at the postition (x,y).
    stroke(0);
    fill(127);
    circle(position.x, position.y, 48);
 }