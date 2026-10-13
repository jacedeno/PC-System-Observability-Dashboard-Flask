<h1 align="center">PC System Observability Dashboard</h1>
<p align="center"><em>Real-time CPU, memory, network and disk I/O metrics in the browser, built with Flask and psutil.</em></p>

<p align="center">
  <a href="#prerequisites"><img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-6e7781?style=flat-square" alt="Platform: Windows | macOS | Linux"></a>
  <a href="#dashboard-features"><img src="https://img.shields.io/badge/updates-every%20second-2ea44f?style=flat-square" alt="Updates: every second"></a>
  <a href="#available-endpoints"><img src="https://img.shields.io/badge/stream-Server--Sent%20Events-1f6feb?style=flat-square" alt="Stream: Server-Sent Events"></a>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776ab?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Flask-backend-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/psutil-system%20metrics-4b8bbe?style=flat-square" alt="psutil">
  <img src="https://img.shields.io/badge/Chart.js-frontend-ff6384?style=flat-square&logo=chartdotjs&logoColor=white" alt="Chart.js">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/jacedeno/PC-System-Observability-Dashboard-Flask?style=flat-square" alt="License"></a>
  <img src="https://img.shields.io/github/last-commit/jacedeno/PC-System-Observability-Dashboard-Flask?style=flat-square" alt="Last commit">
</p>

## Overview

A comprehensive PC system observability dashboard built with Python (Flask) providing real-time system metrics and performance insights for Windows, macOS, and Linux.

## Features

- Real-time system metrics visualization
- CPU, Memory, Network, and Disk I/O tracking
- Process monitoring
- Lightweight and extensible observability solution
- Web-based dashboard with real-time updates

### Dashboard features

- **Real-time Updates**: Metrics update every second
- **Interactive Charts**: Visual representation of system metrics
- **Responsive Design**: Works on desktop and mobile devices
- **Clean Interface**: Easy to read and understand metrics

<details>
<summary><b>Feature details</b></summary>

### Real-time Metrics
- **CPU Usage**: Real-time CPU utilization percentage
- **Memory Usage**: RAM usage statistics and availability
- **Network I/O**: Network bytes sent/received and packet counts
- **Disk I/O**: Disk read/write operations and data transfer

### System Information
- Platform details (OS, version, architecture)
- CPU core count (physical and logical)
- Total system memory
- System uptime

### Process Monitoring
- Top 10 processes by CPU usage
- Memory usage per process
- Process IDs and names

### Network Monitoring
- Active network connections
- Connection states and addresses
- Network interface statistics

### Disk Monitoring
- Disk usage by partition
- Available and used space
- File system types

</details>

### Available endpoints

- `/` - Main dashboard with real-time metrics
- `/system-info` - Detailed system information
- `/process-metrics` - Top resource-consuming processes
- `/disk-usage` - Disk usage statistics
- `/network-connections` - Active network connections
- `/metrics-stream` - Real-time metrics stream (Server-Sent Events)
- `/metrics-overview` - Overview of all available endpoints

## Tech stack

- **Backend**: Flask
- **System Metrics**: psutil
- **Frontend**: Chart.js
- **Visualization**: Real-time web dashboard

## Getting started

### Prerequisites

- Python 3.10+
- Windows, macOS, or Linux

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Python-Observability-Dashboard
```

### 2. Create Virtual Environment

```bash
# Using built-in venv
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Flask Application

```bash
python app.py
```

### 6. Access the Dashboard

Open your web browser and navigate to: **http://localhost:5000**

### Usage

1. Start the application with `python app.py`
2. Open your browser to `http://localhost:5000`
3. View real-time system metrics on the dashboard
4. Use the API endpoints to get specific metric data
5. Monitor system performance and resource usage

<details>
<summary><b>Troubleshooting</b></summary>

**Issue: `ModuleNotFoundError`**
- Solution: Make sure you've activated the virtual environment and installed dependencies with `pip install -r requirements.txt`

**Issue: Permission errors on network connections**
- Solution: Some network monitoring features may require elevated privileges on certain systems

**Issue: Application not starting**
- Solution: Check that port 5000 is not in use by another application

</details>

## Development

To extend the dashboard:

1. Add new metrics collection in `system_metrics.py`
2. Create new API endpoints in `app.py`
3. Update the frontend templates in `templates/`
4. Add styling in `static/css/`
5. Enhance JavaScript functionality in `static/js/`

## License

MIT — see [LICENSE](LICENSE).

---

<p align="center">
  Built by <b>Jose Cedeno</b> ·
  <a href="https://geekendzone.com">geekendzone.com</a> ·
  <a href="https://www.linkedin.com/in/joseangelcedeno/">LinkedIn</a>
</p>
