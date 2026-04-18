# Cindy Surprise 💌

An animated love surprise built with Python and Flask.

## What it does

Opens with a surprise intro screen addressed to Cindy, then reveals a beautiful animated heart after she taps the button. Features include:

- Surprise intro with a floating love letter envelope and animated text
- Heart outline that draws itself stroke by stroke before filling with colour
- Pulsing heartbeat animation with glowing drop shadow
- Orbiting glowing dots around the heart
- Floating heart particles rising from the bottom
- Twinkling star field in the background
- Smooth mouse / touch / gyroscope parallax
- Fully responsive — works on phones, tablets, and desktops
- No horizontal scrolling or pinch-zoom on mobile

## How it works

Python generates the heart shape using the parametric heart equation:

```
x = 16 · sin³(t)
y = 13cos(t) − 5cos(2t) − 2cos(3t) − cos(4t)
```

300 coordinate points are computed server-side and injected into the SVG path. Floating heart particle positions and animation timing are also seeded by Python's `random` module.

## Setup

```bash
pip install -r requirements.txt
python main.py
```

Then open `http://localhost:5000` in your browser.

## Project structure

```
cindy-surprise/
├── main.py              # Flask app — generates heart data and serves the page
├── templates/
│   └── index.html       # Full page template (HTML, CSS, JS)
├── requirements.txt
└── README.md
```
