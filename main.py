from flask import Flask, render_template
import math
import json
import random

app = Flask(__name__)


def generate_heart_points(steps=300):
    points = []
    for i in range(steps):
        t = 2 * math.pi * i / steps
        x = 16 * (math.sin(t) ** 3)
        y = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
        points.append({"x": round(x, 3), "y": round(y, 3)})
    return points


def generate_particles(count=50):
    particles = []
    for _ in range(count):
        particles.append({
            "x": random.uniform(2, 98),
            "size": random.uniform(8, 20),
            "speed": random.uniform(0.35, 1.1),
            "delay": random.uniform(0, 7),
            "opacity": random.uniform(0.3, 0.8),
            "drift": random.uniform(-20, 20),
        })
    return particles


@app.route("/")
def index():
    pts = generate_heart_points(steps=300)
    heart_d = "M " + " L ".join(f"{p['x']},{p['y']}" for p in pts) + " Z"
    particles = generate_particles(50)
    return render_template(
        "index.html",
        heart_d=heart_d,
        particles_json=json.dumps(particles),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
