# Convert Ambisonics A -> B Format

Tiny script that converts Ambisonics A format recordings made with the Sennheiser Ambeo VR to Ambisonics B format. Uses `pedalboard` to invoke the official [Sennhesier Ambeo A to B Format Converter VST](https://docs.cloud.sennheiser.com/en-us/ambeo-vr-mic/ambeo-vr-mic/manual-converter.html)

## Requirements

- Windows (sorry, I didn't want to mess around with WINE here...)
- Python 3.10+ (install dependencies with `pip install -r requirements.txt`)
- Sennhesier Ambeo A to B Format Converter VST (download from above)

## Usage

- Dump your A-format recordings inside `data/mic`
- Update the paths inside `convert.py` to point towards your `.vst3` file
  - (you can also change the `SAMPLE_RATE`, the default is 24000)
- Run `python convert.py`
- Files will be converted and stored inside `data/foa`