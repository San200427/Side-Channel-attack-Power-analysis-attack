import random
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to simulate power consumption based on Hamming weight
def simulate_power_consumption(data, key):
    power_trace = []
    for i in range(len(data)):
        encrypted_value = data[i] ^ key[i % len(key)]
        power_consumption = bin(encrypted_value).count('1')
        power_trace.append(power_consumption)
    return power_trace

# Generate power traces based on the secret key
def generate_power_traces(num_traces, key):
    power_traces = []
    for _ in range(num_traces):
        data = [random.randint(0, 255) for _ in range(len(key))]
        power_trace = simulate_power_consumption(data, key)
        power_traces.append(power_trace)
    return power_traces

# Function to plot power traces using Matplotlib and return as image
def plot_power_traces(power_traces, key):
    fig, ax = plt.subplots(figsize=(8, 4))
    for i in range(min(5, len(power_traces))):  # Plot up to 5 traces
        ax.plot(range(len(key)), power_traces[i], label=f"Trace {i + 1}")
    ax.set_xlabel("Byte Position in Key")
    ax.set_ylabel("Simulated Power Consumption (Hamming Weight)")
    ax.set_title("Power Analysis Attack Simulation - Power Traces")
    ax.legend()

    # Save the plot to a BytesIO object
    img_stream = BytesIO()
    fig.savefig(img_stream, format='png')
    img_stream.seek(0)

    # Encode the image to base64
    img_base64 = base64.b64encode(img_stream.read()).decode('utf-8')
    return img_base64

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Retrieve user input for key or generate a random one
        key_input = request.form.get("key")
        if key_input:
            key = [int(byte) for byte in key_input.split()]
        else:
            key = [random.randint(0, 255) for _ in range(8)]
        
        # Number of traces to generate
        num_traces = int(request.form.get("num_traces", 100))

        # Generate power traces
        power_traces = generate_power_traces(num_traces, key)

        # Generate the plot image and base64 encode it
        plot_img_base64 = plot_power_traces(power_traces, key)

        # Compute average power consumption per byte position
        average_consumption = np.mean(power_traces, axis=0)

        return render_template(
            "index.html",
            key=key_input,
            num_traces=num_traces,
            average_consumption=average_consumption,
            plot_img=plot_img_base64
        )

    return render_template("index.html", plot_img=None)

if __name__ == "__main__":
    app.run(debug=True)
