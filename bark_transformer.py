from transformers import AutoProcessor, BarkModel
import soundfile as sf

def main(text, song_name, i):
    
    processor = AutoProcessor.from_pretrained("./suno--bark-small")
    model = BarkModel.from_pretrained("./suno--bark-small")

    voice_preset = "v2/en_speaker_9"
    print(text)

    inputs = processor(
        text=[text],
        voice_preset=voice_preset,
        return_tensors="pt",
    )

    speech_values = model.generate(**inputs, do_sample=True)

    sample_rate = model.generation_config.sample_rate
    wave_data = speech_values.cpu().numpy().squeeze()
    sf.write(f"./{"Audio for " + song_name + "line " + str(i)}.wav", wave_data, sample_rate)


