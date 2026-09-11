"""Fan entity."""

from __future__ import annotations

from homeassistant.components.fan import FanEntity, FanEntityFeature
from homeassistant.const import PERCENTAGE
from homeassistant.helpers.entity import EntityCategory

from .const import FAN_SPEEDS, SPEED_NAMES
from .entity import PhilipsEntity

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data["philips_ac2889_http"][entry.entry_id]
    async_add_entities([PhilipsAC2889Fan(coordinator)])


class PhilipsAC2889Fan(PhilipsEntity, FanEntity):
    """Philips AC2889 fan."""

    _attr_name = "Oczyszczacz"
    _attr_supported_features = (
        FanEntityFeature.TURN_ON
        | FanEntityFeature.TURN_OFF
        | FanEntityFeature.SET_SPEED
    )
    _attr_percentage_step = 25

    def __init__(self, coordinator):
        super().__init__(coordinator, "fan")
        self._attr_icon = "mdi:air-purifier"

    @property
    def is_on(self):
        return str(self.coordinator.data.get("pwr", "0")) == "1"

    @property
    def percentage(self):
        value = str(self.coordinator.data.get("om", "a"))
        mapping = {"1": 33, "2": 50, "3": 75, "s": 25, "t": 100, "a": 0}
        return mapping.get(value, 0)

    @property
    def preset_mode(self):
        return str(self.coordinator.data.get("om", "a"))

    @property
    def preset_modes(self):
        return list(FAN_SPEEDS)

    async def async_turn_on(self, *args, **kwargs):
        await self.coordinator.async_set_values({"pwr": "1"})

    async def async_turn_off(self, **kwargs):
        await self.coordinator.async_set_values({"pwr": "0"})

    async def async_set_percentage(self, percentage):
        if percentage == 0:
            await self.async_turn_off()
            return

        speed = "1" if percentage <= 33 else "2" if percentage <= 66 else "3"
        await self.coordinator.async_set_values({
            "pwr": "1",
            "mode": "M",
            "om": speed,
        })

    async def async_set_preset_mode(self, preset_mode):
        if preset_mode not in FAN_SPEEDS:
            return
        values = {"pwr": "1", "om": preset_mode}
        if preset_mode in {"1", "2", "3"}:
            values["mode"] = "M"
        await self.coordinator.async_set_values(values)
