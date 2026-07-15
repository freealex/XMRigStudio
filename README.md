# XMRigStudio

XMRigStudio is a cross-platform graphical interface for managing and monitoring the XMRig cryptocurrency miner. It is designed to make configuring, starting, stopping, and monitoring XMRig easier without requiring users to edit configuration files or use the command line for everyday tasks.

> **Disclaimer:** XMRigStudio is a management interface. It does **not** include or modify XMRig itself. Users are responsible for complying with all applicable laws, mining pool terms of service, and the licenses of any software they use.

---

# Features

* 🖥️ Modern graphical interface
* ⚡ Start and stop XMRig with a single click
* 📊 View mining status and performance
* ⚙️ Manage XMRig configuration
* 📝 Display miner output and logs
* 🌐 Connect to the mining pool of your choice
* 🔄 Cross-platform support (Windows, macOS, and Linux)
* 🔓 Open source

---

# Requirements

* Python 3.10 or newer (when running from source)
* XMRig installed separately
* A Monero-compatible mining pool (optional but recommended)
* A Monero wallet address

---

# Installation

## Windows

### Option 1 – Installer (Recommended)

1. Download the latest **XMRigStudio-Setup.exe** from the Releases page.
2. Run the installer.
3. Follow the installation wizard.
4. Launch XMRigStudio from the Start Menu or Desktop.

### Option 2 – Run from Source

```bash
git clone https://github.com/freealex/XMRigStudio.git
cd XMRigStudio
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

---

## macOS

Install Python (if necessary):

```bash
brew install python
```

Clone the repository:

```bash
git clone https://github.com/freealex/XMRigStudio.git
cd XMRigStudio
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python3 main.py
```

If macOS blocks execution because the application is from an unidentified developer, remove the quarantine attribute or allow it in **System Settings → Privacy & Security**.

---

## Linux

Ubuntu/Debian example:

```bash
sudo apt update
sudo apt install python3 python3-venv git
```

Clone the repository:

```bash
git clone https://github.com/freealex/XMRigStudio.git
cd XMRigStudio
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch:

```bash
python3 main.py
```

---

# Installing XMRig

XMRigStudio requires an existing XMRig installation.

## Windows

1. Download XMRig.
2. Extract it to a folder such as:

```
C:\xmrig
```

3. Point XMRigStudio to the location of `xmrig.exe`.

---

## macOS

Using Homebrew:

```bash
brew install xmrig
```

Or build from source following the XMRig documentation.

---

## Linux

Ubuntu example:

```bash
sudo apt install xmrig
```

Or build the latest version from source if desired.

---

# Configuration

Configure the following before mining:

* Monero wallet address
* Mining pool hostname
* Pool port
* Worker name (optional)
* CPU thread settings
* TLS options (if supported)

Save your configuration and start the miner from within XMRigStudio.

---

# Building from Source

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

# Building a Windows Executable

PyInstaller example:

```bash
pyinstaller --onefile --windowed main.py --name XMRigStudio
```

The executable will be created in:

```
dist/
```

---

# Building the Windows Installer

This repository includes an Inno Setup script (`installer.iss`) that packages the PyInstaller executable into a Windows installer.

Compile using:

```text
ISCC installer.iss
```

The installer will be generated in:

```
installer/
```

---

# GitHub Actions

The included GitHub Actions workflow can automatically:

* Install dependencies
* Build the Windows executable
* Compile the installer
* Upload the finished installer as a downloadable artifact

This allows Windows installers to be built automatically without requiring a Windows development machine.

---

# Troubleshooting

## XMRig not found

Verify the path to the XMRig executable in the application settings.

## Miner immediately exits

Check:

* Wallet address
* Mining pool hostname
* Port number
* Internet connection
* Antivirus software

## Firewall

Some firewalls or antivirus products may block mining software. You may need to create an exception for XMRig.

---

# Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a Pull Request.

Bug reports, feature requests, and documentation improvements are appreciated.

---

# License

This project is released under the MIT License unless otherwise specified.

---

# Acknowledgements

* The XMRig project and its contributors
* The Python open-source community
* Everyone who contributes to improving XMRigStudio
* contact Alex with questions at mitchconners576@gmail.com
