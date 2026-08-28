<img width="428" height="157" alt="Snímka obrazovky 2026-08-28 105432" src="https://github.com/user-attachments/assets/d3dc1c56-c2a8-4adb-808d-bea9868667de" />
# angeldust-multitool
A lightweight terminal-based system diagnostics, network &amp; utility toolkit.
# `ANGELDUST`

### `SYSTEM DIAGNOSTICS // NETWORK HUD // UTILITIES`

> **A lightweight Python multi-tool built for terminal-based system diagnostics, network utilities and everyday tools.**

```text
        ANGELDUST MULTI-TOOL v1.0
        ──────────────────────────
        SYSTEM       [ ONLINE ]
        NETWORK      [ ONLINE ]
        UTILITIES    [ ONLINE ]
```

---

## `// FEATURES`

### `01` — SYSTEM

- System information
- Hardware telemetry
- CPU & RAM monitoring
- Disk partition usage
- Top 10 memory-consuming processes
- Battery & power status

### `02` — NETWORK

- Public & local IP lookup
- Host latency testing
- DNS resolution
- IP geolocation
- Common port checker

### `03` — UTILITIES

- Password generator
- Base64 encoder / decoder
- Temporary file cleaner
- MD5 / SHA-1 / SHA-256 hash generator

---

## `// INTERFACE`

ANGELDUST uses a dark terminal-style interface with a red → purple visual theme.

```text
╭──────────────── SYSTEM TOOLS ────────────────╮
│ [01] System Summary                           │
│ [02] Hardware Telemetry                       │
│ [03] Disk Partition Usage                     │
│ [04] Active Processes Top 10                  │
│ [05] Battery & Power Status                   │
╰───────────────────────────────────────────────╯

╭──────────────── NETWORK TOOLS ────────────────╮
│ [06] Show Public & Local IP                   │
│ [07] Host Latency Ping                        │
│ [08] DNS Lookup                               │
│ [09] IP Geolocation Lookup                    │
│ [10] Local Port Checker                       │
╰───────────────────────────────────────────────╯

╭────────────────── UTILITIES ──────────────────╮
│ [11] Secure Password Gen                      │
│ [12] Base64 Encoder/Decoder                   │
│ [13] Flush Temp Files                         │
│ [14] Hash Generator                           │
│ [15] Exit Multi-Tool                          │
╰───────────────────────────────────────────────╯
```

---

## `// INSTALLATION`

### Requirements

- Python 3.9+
- Windows / Linux
- Internet connection for IP-related features

### Install dependencies

```bash
pip install requests psutil pystyle rich
```

### Run

```bash
python angeldust.py
```

---

## `// WINDOWS QUICK START`

If you're using the included Windows launcher:

```text
install_and_run_angeldust.cmd
```

Run the `.cmd` file and let it handle the setup/startup process.

---

## `// PROJECT STRUCTURE`

```text
ANGELDUST/
│
├── angeldust.py
├── install_and_run_angeldust.cmd
├── README.md
└── requirements.txt
```

---

## `// DISCLAIMER`

ANGELDUST is intended for **personal system diagnostics, learning and legitimate network testing**.

Only use network-related features on systems and networks you own or have permission to test.

---

## `// STATUS`

```text
VERSION     : 1.0
PLATFORM    : Windows / Linux
LANGUAGE    : Python
STATUS      : ACTIVE
```

### `ANGELDUST // END OF LINE`
