# Spotify CLI Actions
A python script to send actions to Spotify in Linux using dbus, thanks to Spotify mpris implementation.

# List of supported actions (WIP)
Since Spotify uses the standard mpris for MediaPlayer2, you can get a list of the different possible actions [here](https://specifications.freedesktop.org/mpris-spec/latest/Player_Interface.html)

This script currently only handles the main actions, more could be added in the future, but to get a list simply run the script with -h

```bash
python3 spotify_cli_actions.py -h

usage: spotify_cli_actions [-h] {playpause,previous,next,shuffle,volumedown,volumeup} ...

Spotify control commands

positional arguments:
  {playpause,previous,next,shuffle,volumedown,volumeup}
                        Command to send to Spotify
    playpause           Toggle Play/Pause
    previous            Play previous, or go back to beggining of the song
    next                Play next song
    shuffle             Toggle shuffle
    volumedown          Decrease volume by 10%
    volumeup            Increase volume by 10%

options:
  -h, --help            show this help message and exit
```

# How to use
You can use it directly as is manually in the commandline, but I'd reccommend at least using one or multiple alias.
The main use case was to be used through a Stream Deck or other similar shortcuts.
