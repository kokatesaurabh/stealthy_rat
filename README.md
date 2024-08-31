# Stealthy RAT Project

## Overview
This project demonstrates a basic Remote Access Trojan (RAT) for educational purposes. The RAT is capable of collecting system information, logging keystrokes, capturing screenshots, and persisting on the target machine.

**WARNING**: This code is for educational purposes only. Unauthorized deployment or use of this code is illegal and unethical.

## Project Structure
- `C2_Server/`: Contains the Command and Control (C2) server code.
- `RAT_Client/`: Contains the RAT client code.
- `README.md`: This documentation file.

## Setup Instructions

### C2 Server Setup
1. Navigate to the `C2_Server/` directory:
    ```bash
    cd C2_Server
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the server:
    ```bash
    python server.py
    ```

### RAT Client Setup
1. Navigate to the `RAT_Client/` directory:
    ```bash
    cd RAT_Client
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Modify `main.py` to include your C2 server URL.
4. Run the RAT script:
    ```bash
    python main.py
    ```

## Ethical Considerations
- Use this project only in a legal, ethical, and controlled environment.
- Always obtain proper authorization before deploying any kind of RAT.
