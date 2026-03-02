from pathlib import Path

import librosa
import soundfile as sf
from pedalboard import load_plugin
from tqdm import tqdm

# Download from https://plugins.iem.at/docs/plugindescriptions/#binauraldecoder
PATH_TO_FOABIN_VST = r"C:\Program Files\Common Files\VST3\IEM\BinauralDecoder.vst3\Contents\x86_64-win\BinauralDecoder.vst3"
SAMPLE_RATE = 24000

PARAMETERS = dict(
    bypass=False,
    input_ambisonic_order="1st",
    input_normalization="N3D",
)
PLUGIN = load_plugin(PATH_TO_FOABIN_VST, parameter_values=PARAMETERS)

INPUT_DIR = Path("data/foa")
OUTPUT_DIR = Path("data/binaural")


def main():
    files = [f for f in INPUT_DIR.rglob("**/*.wav")]

    for full_path in tqdm(files, desc="Processing files..."):
        # Get the file paths
        out_path = Path(OUTPUT_DIR) / full_path.name

        # Create folder if not existing
        if not out_path.parent.exists():
            out_path.parent.mkdir(parents=True, exist_ok=True)

        # Silently skip over files that already exist
        if out_path.exists():
            continue

        # Load the audio, process with the plugin, and dump the output audio
        loaded, _ = librosa.load(full_path, mono=False, sr=SAMPLE_RATE)
        out = PLUGIN.process(loaded, sample_rate=SAMPLE_RATE)

        # Last two channels are silent
        sf.write(out_path, out[:2, :].T, SAMPLE_RATE)


if __name__ == "__main__":
    main()
