let x = 100;
let y = 100;
let xspeed = 2.5;
let yspeed = 2;

function setup() {
    createCanvas(640, 240);
  }

  function draw() {
    background(255);
    // moving the ball according to its speed
    x = x + xspeed;
    y = y + yspeed;
    // Check for boundcing
    if (x > width || x < 0) {
        xspeed = xspeed * -1;
    }
    if (y > height || y < 0) {
        yspeed = yspeed * -1;
    }
    // draw the ball at the postition (x,y).
    stroke(0);
    fill(127)
    circle(x, y, 48)
  }