import psutil

def get_system_data():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    system_data = {
        "cpu_usage": cpu,
        "memory_usage": memory
    }

    return system_data


if __name__ == "__main__":
    print(get_system_data())
    