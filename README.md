# ASCII Art

Convert a YouTube video into a colorful ASCII-art animation directly in your terminal.

![ASCII Art example](img.jpg)

## Features

- Downloads a YouTube video and audio
- Plays the audio while rendering the frame-by-frame ASCII animation
- Uses color output in the terminal for a more vivid effect
- Works from a simple Python script or the Windows batch installer

## Requirements
python
The project uses:

- numpy
- opencv-python
- termcolor
- pytubefix
- pydub

## Installation on Windows

You can use the provided batch script:

```bat
install.bat
```

## Usage

Run the script:

```bash
AsciiArt.bat
```

Then enter a YouTube video URL when prompted. Press `q` to exit.

## Notes

- The script downloads the video and audio temporarily while rendering.
- The output is displayed in the terminal, so a terminal with color support is recommended.
- ffmpeg is often required by audio processing libraries, so make sure it is available on your system if you run into audio issues.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
