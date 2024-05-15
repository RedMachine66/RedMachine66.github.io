let mover1;
let mover2;

function setup() {
    createCanvas(640, 240);
    mover1 = new Mover(200, 120, 1);
    mover2 = new Mover(400, 100, 3);
    createP('Click mouse to apply wind force')
}

function draw() {
    background(210);
    
    let gravity = createVector(0, 0.1);
    let gravity1 = p5.Vector.mult(gravity, mover1.mass);
    mover1.applyForce(gravity1);
    let gravity2 = p5.Vector.mult(gravity, mover2.mass);
    mover2.applyForce(gravity2);

    if (mouseIsPressed) {
        let wind = createVector(0.1, 0);
        mover1.applyForce(wind);
        mover2.applyForce(wind);
    }
    
    mover1.checkEdges();
    mover1.update();
    mover1.show();

    mover2.checkEdges();
    mover2.update();
    mover2.show();
}

class Mover {
    // creating the vectors of the object
    constructor(x, y, mass) {
        this.position = createVector(x, y);
        this.velocity = createVector(0,0);
        this.acceleration = createVector(0, 0);
        this.mass = mass
    }

    //apply a force to the object taking mass into consideration
    applyForce(force) {
        let f = p5.Vector.div(force, this.mass);
        this.acceleration.add(f);
    }

    // updating the position of the object
    update() {
        this.velocity.add(this.acceleration);
        this.velocity.limit(this.topSpeed);
        this.position.add(this.velocity);
        this.acceleration.mult(0);
    }

    // drawing the object at the new position
    show() {
        stroke(0);
        strokeWeight(2);
        fill(120);
        circle(this.position.x, this.position.y, 30);
    }
    // what happens when the object goes outside the canvas: it wraps around in this example.
    checkEdges() {
        if (this.position.x > width) {
          this.position.x = width;
          this.velocity.x *= -1;
        } else if (this.position.x < 0) {
            this.velocity.x *= -1;
            this.position.x = 0;
        }
    
        if (this.position.y > height) {
            this.velocity.y *= -1;
            this.position.y = height;
        }
    }
}