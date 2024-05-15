let mover;

function setup() {
    createCanvas(640, 240);
    mover = new Mover();
}

function draw() {
    background(210);
    mover.update();
    mover.checkEdges();
    mover.show();
}

class Mover {
    // creating the vectors of the object
    constructor() {
        this.position = createVector(random(width), random(height));
        this.velocity = createVector(0,0);
        this.acceleration = createVector(0, 0);
        this.topSpeed = 10;
    }

    // updating the position of the object
    update() {
        // Using the random2D() method, which returns a unit vector pointing in a random direction.
        this.acceleration = p5.Vector.random2D();
        this.acceleration.mult(random(2));
        this.velocity.add(this.acceleration);
        this.velocity.limit(this.topSpeed);
        this.position.add(this.velocity);
    }

    // drawing the object at the new position
    show() {
        stroke(0);
        strokeWeight(2);
        fill(120);
        circle(this.position.x, this.position.y, 48);
    }
    // what happens when the object goes outside the canvas: it wraps around in this example.
    checkEdges() {
        if (this.position.x > width) {
          this.position.x = 0;
        } else if (this.position.x < 0) {
          this.position.x = width;
        }
    
        if (this.position.y > height) {
          this.position.y = 0;
        } else if (this.position.y < 0) {
          this.position.y = height;
        }
    }
}