# Power Analysis Attack Simulation

This project simulates a **power analysis attack** to demonstrate how an attacker can exploit patterns in power consumption to infer sensitive information, such as cryptographic keys. The attack uses the **Hamming Weight model**, which assumes that the power consumed by a device is related to the number of `1` bits in the data being processed.

## Overview

Side-channel attacks, like **power analysis attacks**, are a class of attacks where an attacker gathers information from physical emanations such as timing, electromagnetic radiation, or power consumption. In this project, we simulate the process of generating power consumption traces and visualizing these traces in order to understand how attackers can use this information to deduce the secret key in a cryptographic system.

### Key Concepts:

- **Hamming Weight**: The number of `1` bits in a binary number. This is used as a proxy for power consumption.
- **Power Trace**: A time series representing the power consumption of a device during cryptographic operations.
- **Side-Channel Attack**: An attack that uses information gained from the physical implementation of a system (e.g., power consumption) to break cryptographic algorithms.

## How it Works

The simulation consists of the following main steps:

1. **Simulating Power Consumption**:  
   The core of the attack involves calculating the **Hamming weight** of the data during encryption. Each time the device performs an encryption operation, the result is analyzed by counting the number of `1` bits in the binary representation of the data. This count is used as a proxy for the power consumption during that operation.

2. **Generating Power Traces**:  
   The attacker collects multiple power traces while a cryptographic operation is being performed. For each encryption operation, a power trace is recorded based on the Hamming weight of the result. The attacker assumes that they do not know the key but can infer patterns from these traces.

3. **Visualizing Power Traces**:  
   The power traces are visualized in a plot. Each trace represents the power consumption over time, and patterns can emerge that might correlate with specific bits of the secret key, allowing the attacker to gradually deduce the key.

4. **Using the Attack**:  
   In the real world, the attacker could gather power traces by monitoring a device during encryption operations (e.g., via electromagnetic leaks or by physically attaching to the device). By analyzing these traces and comparing them to known patterns, the attacker can deduce the secret key bit by bit.

---

## Technology Used

This project is created using **Flask** for the web interface to simulate and visualize the power analysis attack.

---


