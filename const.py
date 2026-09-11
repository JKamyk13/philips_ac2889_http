"""Constants for the Philips AC2889 HTTP integration."""

DOMAIN = "philips_ac2889_http"
DEFAULT_NAME = "Philips AC2889"
DEFAULT_SCAN_INTERVAL = 30

FAN_SPEEDS = ("s", "1", "2", "3", "t", "a")
SPEED_NAMES = {
	"s": "Sleep",
	"1": "Speed 1",
	"2": "Speed 2",
	"3": "Speed 3",
	"t": "Turbo",
	"a": "Auto",
}

MODES = ("P", "A", "B")
MODE_NAMES = {
	"P": "Tryb ogólny",
	"A": "Tryb antyalerg",
	"B": "Tryb usuw. bakt. i wir.",
}
