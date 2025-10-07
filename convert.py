import os

import librosa
import soundfile as sf
from pedalboard import load_plugin
from tqdm import tqdm

# Yes you have to use windows, no i am not sorry
PATH_TO_AB_VST = r"C:\Program Files\Common Files\VST3\Sennheiser AMBEO A-B format converter.vst3"
SAMPLE_RATE = 24000

# Most important here is output format, needs to be WXYZ
PARAMETERS = dict(
    high_pass=False,
    coincidence_filter=True,
    position="Upright",
    output_format="FuMa",
    rotation_degree=0.,
    bypass=False
)
PLUGIN = load_plugin(PATH_TO_AB_VST, parameter_values=PARAMETERS)

MIC_DIR = "data/mic"
OUTPUT_DIR = "data/foa"


def main():
    files = [f for f in os.listdir(MIC_DIR) if f != ".gitkeep"]

    for f in tqdm(files, desc="Processing files..."):
        # Get the file paths
        full_path = os.path.join(MIC_DIR, f)
        out_path = os.path.join(OUTPUT_DIR, f)

        # Silently skip over files that already exist
        if os.path.isfile(out_path):
            continue

        # Load the audio, process with the plugin, and dump the output audio
        loaded, _ = librosa.load(full_path, mono=False, sr=SAMPLE_RATE)
        out = PLUGIN.process(loaded, sample_rate=SAMPLE_RATE)
        sf.write(os.path.join(OUTPUT_DIR, f), out.T, SAMPLE_RATE)


if __name__ == "__main__":
    main()
