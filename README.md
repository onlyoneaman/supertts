## SuperTTS

#### Star the repository if this was useful. ⭐️

[![PyPI version](https://badge.fury.io/py/supertts.svg)](https://badge.fury.io/py/supertts)
[![Downloads](https://pepy.tech/badge/supertts)](https://pepy.tech/project/supertts)
[![Downloads](https://pepy.tech/badge/supertts/month)](https://pepy.tech/project/supertts/month)
[![Downloads](https://pepy.tech/badge/supertts/week)](https://pepy.tech/project/supertts/week)

![GitHub license](https://img.shields.io/github/license/onlyoneaman/supertts)

Single TTS Package to use multiple TTS engines.

## Installation

```bash
pip install supertts
```

## Usage

TTS
```python
from supertts import SuperTTS

supertts = SuperTTS()
supertts.tts("Hello World")
```

Voices
```python
from supertts import SuperTTS

supertts = SuperTTS()
supertts.voices()
```

### Configuration

#### tts

Openai TTS
- voice: Voice to use for TTS (Default: "alloy"
- model: Model to use for TTS (Default: "tts-1")

```python
from supertts import SuperTTS

supertts = SuperTTS()

supertts.tts("Hello World", model="tts-1-hd")

supertts.tts("Hello World", voice="nova")

supertts.tts("Hello World", model="tts-1-hd", voice="nova")
```


## Supported TTS Engines

- Openai
- Azure

### Upcoming TTS Engines

- Google

## License

MIT

## Author

[Aman](https://amankumar.ai) | [X (Twitter)](https://twitter.com/onlyoneaman)

Enjoy using SuperTTS! 🚀
