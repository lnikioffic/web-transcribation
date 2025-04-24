import os
import whisper

_model = whisper.load_model('small', download_root='.')


def get_audio_text(file_path: str) -> str:
    if os.path.exists(file_path):
        audio = whisper.load_audio(file_path)
        audio = whisper.pad_or_trim(audio)
        result = _model.transcribe(audio)
        return result['text'].strip()
    return ''
