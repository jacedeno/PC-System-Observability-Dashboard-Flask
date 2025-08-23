# PC System Observability Dashboard

## 🌟 Overview

A comprehensive PC system observability dashboard built with Python (Flask) providing real-time system metrics and performance insights for Windows, macOS, and Linux.

## ✨ Features

- Real-time system metrics visualization
- CPU, Memory, Network, and Disk I/O tracking
- Process monitoring
- Lightweight and extensible observability solution
- Web-based dashboard with real-time updates

## Prerequisites

- Python 3.10+
- Windows, macOS, or Linux

## Technology Stack

- **Backend**: Flask
- **System Metrics**: psutil
- **Frontend**: Chart.js
- **Visualization**: Real-time web dashboard

## 🛠 Setup, Install & Run

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

## 📊 Available Endpoints

- `/` - Main dashboard with real-time metrics
- `/system-info` - Detailed system information
- `/process-metrics` - Top resource-consuming processes
- `/disk-usage` - Disk usage statistics
- `/network-connections` - Active network connections
- `/metrics-stream` - Real-time metrics stream (Server-Sent Events)
- `/metrics-overview` - Overview of all available endpoints

## 🔧 Features Details

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

## 🚀 Usage

1. Start the application with `python app.py`
2. Open your browser to `http://localhost:5000`
3. View real-time system metrics on the dashboard
4. Use the API endpoints to get specific metric data
5. Monitor system performance and resource usage

## 📱 Dashboard Features

- **Real-time Updates**: Metrics update every second
- **Interactive Charts**: Visual representation of system metrics
- **Responsive Design**: Works on desktop and mobile devices
- **Clean Interface**: Easy to read and understand metrics

## 🔧 Troubleshooting

**Issue: `ModuleNotFoundError`**
- Solution: Make sure you've activated the virtual environment and installed dependencies with `pip install -r requirements.txt`

**Issue: Permission errors on network connections**
- Solution: Some network monitoring features may require elevated privileges on certain systems

**Issue: Application not starting**
- Solution: Check that port 5000 is not in use by another application

## 🛠 Development

To extend the dashboard:

1. Add new metrics collection in `system_metrics.py`
2. Create new API endpoints in `app.py`
3. Update the frontend templates in `templates/`
4. Add styling in `static/css/`
5. Enhance JavaScript functionality in `static/js/`
