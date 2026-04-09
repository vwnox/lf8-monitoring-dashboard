from flask import Flask
from app.api import get_weather
from app.system import get_system_data

app = Flask(__name__)

@app.route("/")
def index():
    weather = get_weather()
    system = get_system_data()

    cpu = int(system["cpu_usage"])
    ram = int(system["memory_usage"])

    condition = weather["weather"].lower()

    # 🌈 Hintergrund je nach Wetter
    if "sun" in condition:
        bg = "#0f172a"
        animation = '<div class="sun"></div>'
    elif "cloud" in condition:
        bg = "#1e293b"
        animation = '<div class="cloud"></div>'
    elif "rain" in condition:
        bg = "#020617"
        animation = "".join([f'<div class="rain" style="left:{i*3}%"></div>' for i in range(30)])
    else:
        bg = "#0f172a"
        animation = ""

    return f"""
<!DOCTYPE html>
<html>
<head>
<title>Smart Dashboard</title>

<style>
body {{
    margin:0;
    font-family:Arial;
    background:{bg};
    color:white;
    overflow:hidden;
}}

h1 {{
    text-align:center;
    padding:20px;
}}

.container {{
    display:flex;
    justify-content:center;
    gap:80px;
    margin-top:40px;
}}

.card {{
    text-align:center;
}}

.tacho {{
    width:220px;
    height:220px;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:28px;
    background:#111;
    box-shadow:0 0 20px rgba(0,255,200,0.2);
    transition:0.5s;
}}

.weather {{
    text-align:center;
    margin-top:60px;
    font-size:30px;
}}

.sun {{
    position:absolute;
    top:40px;
    right:40px;
    width:80px;
    height:80px;
    background:yellow;
    border-radius:50%;
    box-shadow:0 0 50px orange;
    animation: pulse 2s infinite alternate;
}}

@keyframes pulse {{
    from {{ transform:scale(1); }}
    to {{ transform:scale(1.2); }}
}}

.cloud {{
    position:absolute;
    top:40px;
    right:40px;
    font-size:60px;
    animation: moveCloud 20s linear infinite;
}}

@keyframes moveCloud {{
    from {{ transform:translateX(-100px); }}
    to {{ transform:translateX(100vw); }}
}}

.rain {{
    position:absolute;
    width:2px;
    height:20px;
    background:lightblue;
    animation: rain 1s linear infinite;
}}

@keyframes rain {{
    from {{ transform:translateY(-100px); }}
    to {{ transform:translateY(100vh); }}
}}
</style>

</head>

<body>

{animation}

<h1>Smart Monitoring Dashboard</h1>

<div class="container">

    <div class="card">
        <h2>CPU</h2>
        <div id="cpu" class="tacho">0%</div>
        <p>{system['cpu_warning']}</p>
    </div>

    <div class="card">
        <h2>RAM</h2>
        <div id="ram" class="tacho">0%</div>
    </div>

</div>

<div class="weather">
    🌤 {weather['temperature']}°C <br>
    {weather['weather']} <br>
    {weather['warning']}
</div>

<script>

// 🔥 Smooth Animation
function animateValue(id, value) {{
    let el = document.getElementById(id);
    let start = 0;

    let interval = setInterval(() => {{
        start++;
        el.innerText = start + "%";

        let deg = start * 3.6;

        let color = "#00ffcc";
        if(start > 70) color = "red";
        else if(start > 40) color = "orange";

        el.style.background = `
            radial-gradient(circle, #111 60%, transparent 61%),
            conic-gradient(${{color}} ${{deg}}deg, #222 ${{deg}}deg)
        `;

        if(start >= value) clearInterval(interval);

    }}, 10);
}}

// Start Animation
animateValue("cpu", {cpu});
animateValue("ram", {ram});

// Auto refresh (ruhiger)
setTimeout(() => location.reload(), 8000);

</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)