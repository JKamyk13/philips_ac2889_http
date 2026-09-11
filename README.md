# philips_ac2889_http
# Philips AC2889 HTTP

Home Assistant custom integration for controlling the **Philips AC2889/10 air purifier** over HTTP.

This integration is based on the [`py-air-control`](https://github.com/rgerganov/py-air-control) Python library and communicates with the air purifier directly over the local network.

## Features

* Control the Philips AC2889/10 over HTTP
* Local network communication
* No cloud connection required
* Integration with Home Assistant
* Device configuration through the Home Assistant UI

## Supported Device

Currently supported:

* **Philips AC2889/10**

Other Philips air purifier models may work with `py-air-control`, but they have not been tested with this integration.

## Installation

### Manual installation

1. Download the repository as a ZIP file.

2. Extract the downloaded ZIP file.

3. Open the extracted repository folder.

4. Inside it, you will find the `philips_ac2889_http` folder.

5. Copy the **`philips_ac2889_http`** folder.

6. Open your Home Assistant configuration directory:

```text
/config/custom_components/
```

For example, on a typical Home Assistant installation:

```text
homeassistant/config/custom_components/
```

7. Paste the `philips_ac2889_http` folder into the `custom_components` directory.

The final directory structure should look like this:

```text
config/
└── custom_components/
    └── philips_ac2889_http/
        ├── __init__.py
        ├── manifest.json
        ├── config_flow.py
        └── ...
```

8. Restart Home Assistant.

9. Go to:

**Settings → Devices & services → Add Integration**

10. Search for:

**Philips AC2889 HTTP**

11. Follow the configuration steps and enter the IP address of your Philips AC2889/10.

## Requirements

* Home Assistant
* Philips AC2889/10
* The air purifier and Home Assistant must be connected to the same local network
* A stable IP address for the air purifier is recommended

## Communication

The integration communicates directly with the purifier over the local network using HTTP.

No Philips cloud account or cloud service is required for the communication between Home Assistant and the purifier.

## Credits

This project uses code and functionality from:

* [`py-air-control`](https://github.com/rgerganov/py-air-control) by **rgerganov**

Many thanks to the developers and contributors of `py-air-control` for their work on reverse-engineering and controlling Philips air purifiers.

## Disclaimer

This is an unofficial Home Assistant custom integration and is **not affiliated with or endorsed by Philips**.

Use it at your own risk.

## License

See the `LICENSE` file included in this repository.
