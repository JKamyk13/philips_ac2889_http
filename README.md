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

### HACS

This integration can be installed through **HACS** as a custom repository.

#### 1. Add the repository to HACS

Open **HACS → Integrations** and click the **three-dot menu** in the top-right corner.

Select **Custom repositories**.

Add the following repository:

```text
https://github.com/JKamyk13/philips_ac2889_http
```

Set the category to:

```text
Integration
```

Then click **Add**.

#### 2. Install the integration

After adding the repository, open it in HACS and click **Download**.

You can also use the button below to open the repository directly in HACS:

[![Open your Home Assistant instance and show the repository](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=JKamyk13&repository=philips_ac2889_http)

#### 3. Restart Home Assistant

After the installation is complete, restart Home Assistant.

Then go to:

**Settings → Devices & services → Add Integration**

Search for:

**Philips AC2889 HTTP**

Select the integration and follow the configuration steps.

### Manual installation
Download the repository as a ZIP file and extract it.
Open the extracted repository and copy:

custom_components/philips_ac2889_http/

Paste the folder into:

/config/custom_components/

The final structure should be:

config/
└── custom_components/
    └── philips_ac2889_http/
        ├── __init__.py
        ├── manifest.json
        ├── config_flow.py
        └── ...

Restart Home Assistant.
Go to Settings → Devices & services → Add Integration.
Search for Philips AC2889 HTTP and follow the configuration steps.


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
