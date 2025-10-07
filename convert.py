from pathlib import Path

import librosa
import soundfile as sf
from pedalboard import load_plugin
from tqdm import tqdm

# Yes you have to use windows, no I am not sorry
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

MIC_DIR = Path("data/mic")
OUTPUT_DIR = Path("data/foa")


def main():
    files = [f for f in MIC_DIR.rglob("*.wav")]

    for full_path in tqdm(files, desc="Processing files..."):
        # Get the file paths
        out_path = Path(OUTPUT_DIR) / full_path.name

        # Silently skip over files that already exist
        if out_path.exists():
            continue

        # Load the audio, process with the plugin, and dump the output audio
        loaded, _ = librosa.load(full_path, mono=False, sr=SAMPLE_RATE)
        out = PLUGIN.process(loaded, sample_rate=SAMPLE_RATE)
        sf.write(out_path, out.T, SAMPLE_RATE)


if __name__ == "__main__":
    main()
