let emitter;
let img;

function preload() {
    // img = loadImage("data/small_smoke_particle.png");
    // img = loadImage("data/IMG_3104.png");
    img = loadImage("data/IMG_3105.png");
}

function setup() {
    createCanvas(640, 300);
    emitter = new Emitter(width / 2, height / 2);
}

function draw() {
    background(10);
    // let gravity = createVector(0, 0.1);
    // emitter.applyForce(gravity);
    let dx = map(mouseX, 0, width, -0.2, 0.2);
    let wind = createVector(dx, 0);
    emitter.applyForce(wind);
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

    applyForce(force) {
        for (let particle of this.particles) {
            particle.applyForce(force)
        }
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
        let vx = randomGaussian(0, 0.46)
        let vy = randomGaussian(-1.8, 0.4)
        this.velocity = createVector(vx, vy);
        this.lifespan = 200.0;
        //this.mass = 1;
    }

    update() {
        this.velocity.add(this.acceleration);
        this.position.add(this.velocity);
        this.acceleration.mult(0);
        this.lifespan -= 4;
    }

    show() {
        imageMode(CENTER);
        tint(230, this.lifespan);
        let imageSize = 50
        image(img, this.position.x, this.position.y, imageSize, imageSize);
    }

    applyForce(force) {
        // let f = force.copy();
        // f.div(this.mass);
        // this.acceleration.add(f);
        // ignoring mass:
        this.acceleration.add(force);
    }

    isDead() {
        return (this.lifespan < 0.0);
    }

    run() {
        this.update();
        this.show();
    }
}