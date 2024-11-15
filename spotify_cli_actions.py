import subprocess
import argparse

def send_method(dbus_method: str):
    command=["dbus-send",
             "--print-reply",
             "--dest=org.mpris.MediaPlayer2.spotify",
             "/org/mpris/MediaPlayer2",
             f"org.mpris.MediaPlayer2.Player.{dbus_method}"]
    subprocess.run(command, check=False)

def send_set(dbus_property: str, dbus_property_type: str, dbus_property_value: str) -> str:
    command=["dbus-send",
             "--print-reply", 
             "--session", 
             "--dest=org.mpris.MediaPlayer2.spotify", 
             "/org/mpris/MediaPlayer2", 
             "org.freedesktop.DBus.Properties.Set",
             "string:org.mpris.MediaPlayer2.Player",
             f"string:{dbus_property}",
             f"variant:{dbus_property_type}:{dbus_property_value}"]
    process=subprocess.run(command,
                           check=False, text=True, stdout=subprocess.PIPE)
    return process.stdout

def send_get(dbus_property: str) -> str:
    command=["dbus-send",
             "--print-reply", 
             "--session", 
             "--dest=org.mpris.MediaPlayer2.spotify", 
             "/org/mpris/MediaPlayer2", 
             "org.freedesktop.DBus.Properties.Get",
             "string:org.mpris.MediaPlayer2.Player",
             f"string:{dbus_property}"]
    process=subprocess.run(command,
                           check=False, text=True, stdout=subprocess.PIPE)
    return process.stdout

def action_play_pause():
    print("Toggle play/pause")
    send_method("PlayPause")

def action_previous():
    print("Previous")
    send_method("Previous")

def action_next():
    print("Next")
    send_method("Next")

def action_shuffle():
    print("Toggle Shuffle")
    get_value=send_get("Shuffle")
    if "boolean true" in get_value:
        send_set("Shuffle", "boolean", "false")
        print("Toggled off")
    else:
        send_set("Shuffle", "boolean", "true")
        print("Toggled on")

def action_volume_up():
    print("Volume up")
    get_value=send_get("Volume")
    volume=get_value.split()[-1]
    print(f"Volume is currently at {volume}")
    if float(volume) == 1.0:
        print("Volume is already maxed")
        return
    volume=round(min(float(volume)+0.1, 1.0), 1)
    print(f"Setting volume to {volume}")
    send_set("Volume", "double", str(volume))

def action_volume_down():
    print("Volume down")
    get_value=send_get("Volume")
    volume=get_value.split()[-1]
    print(f"Volume is currently at {volume}")
    if float(volume) == 0.0:
        print("Volume is already muted")
        return
    volume=round(max(float(volume)-0.1, 0.0), 1)
    print(f"Setting volume to {volume}")
    send_set("Volume", "double", str(volume))

def main():
    parser = argparse.ArgumentParser(prog="spotify_cli_actions",
                                     description="Spotify control commands")

    subparsers = parser.add_subparsers(dest="command",
                                       required=True,
                                       help="Command to send to Spotify")

    subparsers.add_parser("playpause", help="Toggle Play/Pause")
    subparsers.add_parser("previous", help="Play previous, or go back to beggining of the song")
    subparsers.add_parser("next", help="Play next song")
    subparsers.add_parser("shuffle", help="Toggle shuffle")
    subparsers.add_parser("volumedown", help=r"Decrease volume by 10%%")
    subparsers.add_parser("volumeup", help=r"Increase volume by 10%%")

    args = parser.parse_args()

    match args.command.lower():
        case "playpause":
            return action_play_pause()
        case "previous":
            return action_previous()
        case "next":
            return action_next()
        case "shuffle":
            return action_shuffle()
        case "volumeup":
            return action_volume_up()
        case "volumedown":
            return action_volume_down()
        case _:
            print(f"Invalid command {args.command}")

if __name__ == "__main__":
    main()
