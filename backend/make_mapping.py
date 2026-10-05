"""Create data/leaf_sensor_map.csv - assigns every leaf image a start row in cpdata.csv.

IMPORTANT: this is a DEMO PAIRING. The leaf photos and the sensor CSV were not recorded
together, so the assignment is random (fixed seed -> repeatable). Nothing here implies
that a leaf "caused" or "experienced" those readings.

Run from the backend folder:   python make_mapping.py
To use real pairings later, just edit/replace data/leaf_sensor_map.csv (columns below).
"""
import numpy as np
import pandas as pd
import config

WINDOW = 512   # largest window the UI can request (Samples N slider max)
SEED = 42      # change the seed to get a different (but still repeatable) assignment

rows = len(pd.read_csv(config.CSV_PATH))
images = sorted(p.name for p in config.IMAGE_DIR.iterdir() if p.suffix.lower() in (".jpg", ".jpeg", ".png"))
starts = np.random.default_rng(SEED).integers(0, rows - WINDOW, size=len(images))

pd.DataFrame({"image": images, "sensor_start_row": starts, "pairing": f"demo-random-seed{SEED}"}) \
  .to_csv(config.MAP_PATH, index=False)
print(f"Wrote {len(images)} pairings to {config.MAP_PATH}")
