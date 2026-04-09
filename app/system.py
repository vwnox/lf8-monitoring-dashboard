import psutil

def get_system_data():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    # ➕ NEU: CPU Warnung
    if cpu > 80:
        warning = "❗ CPU ÜBERLASTET"
    elif cpu > 40:
        warning = "⚠️ CPU hoch"
    else:
        warning = "✅ CPU normal"

    system_data = {
        "cpu_usage": cpu,
        "memory_usage": memory,
        "cpu_warning": warning   # ➕ NEU
    }

    return system_data


if __name__ == "__main__":
     print(get_system_data())