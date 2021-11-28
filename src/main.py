import color
import presets
import arduino_serial


# ==================================================================================================
# ================================== ARDUINO MUST BE RUNNING FIRST =================================
# ==================================================================================================


def main():
    preset = presets.SolidTwoColorPreset(color.RED, color.GREEN)
    arduino_serial.run(preset.get_animation())


if __name__ == "__main__":
    main()