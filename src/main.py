import color
import presets
import arduino_serial


def main():
    preset = presets.SolidColorPreset(color.RED)
    arduino_serial.run(preset.get_animation())


if __name__ == "__main__":
    main()