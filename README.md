# Spatial Audio Conversion Scripts

This repo contains a few helper scripts for converting between different spatial audio formats. Currently available:

- First-order Ambisonics A- (sometimes called `mic` format) to Ambisonics B-format
- First-order Ambisonics B-format to binaural

These scripts work by invoking different VST plugins using the `pedalboard` library. Check each script to find out which VST files you need.

## Requirements

- Windows (sorry, I didn't want to mess around with WINE here...)
- Python 3.10+ (install dependencies with `pip install -r requirements.txt`)
- Individual VST files (check the script to find out what you need, and where)

## Usage

- Dump your recordings inside `data/***`
  - E.g., for `foa2binaural.py`, dump into `data/foa`
- Update the paths inside `convert.py` to point towards your `.vst3` file
  - (you can also change the `SAMPLE_RATE`, the default is 24000)
- Run `python <script>.py`
- Files will be converted and stored inside `data/***`
  - E.g., for `foa2binaural.py`, files will be saved into `data/binaural`