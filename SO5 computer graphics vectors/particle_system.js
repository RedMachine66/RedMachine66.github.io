let emitter;

function setup() {
    createCanvas(640, 240);
    emitter = new Emitter(width / 2, 50);
}

function draw() {
    background(255);
    emitter.addParticle();
    emitter.run();
}

class Emitter {
    constructor(x, y) {
        this.origin = createVector(x, y);
        this.particles = [];
    }

    addParticle() {
        this.particles.push(new Particle(this.origin.x, this.origin.y));
    }

    run() {
        let length = this.particles.length -1;
        for (let i = length; i >= 0; i--) {
            let particle = this.particles[i];
            particle.run();
            if (particle.isDead()) {
                this.particles.splice(i, 1);
            }
        }
    }
}

class Particle {
    constructor(x, y) {
        this.position = createVector(x, y);
        this.acceleration = createVector(0, 0);
        this.velocity = createVector(random(-1, 1), random(-2, 0));
        this.lifespan = 255;
    }

    update() {
        this.velocity.add(this.acceleration);
        this.position.add(this.velocity);
        this.acceleration.mult(0);
        this.lifespan -= 2.0;
    }

    show() {
        stroke(0, this.lifespan);
        fill(175, this.lifespan);
        circle(this.position.x, this.position.y, 8);
    }

    applyForce(force) {
        this.acceleration.add(force);
    }

    isDead() {
        return (this.lifespan < 0.0);
    }

    run() {
        let gravity = createVector(0, 0.05);
        this.applyForce(gravity);
        this.update();
        this.show();
    }
}