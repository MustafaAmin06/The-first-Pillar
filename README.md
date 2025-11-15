# The First Pillar

"The First Pillar" is a calm, minimalist web app built with Python and Flet. Its sole purpose is to provide a focused, non-overwhelming guide for new Muslim reverts, helping them learn the absolute essentials of prayer and faith.

## ✨ The "Vibe"

The app is designed with a "Zen" aesthetic: lots of white space, crisp black text, and a soft gold accent color. It is intentionally simple.

* **Prayers Tab:** A step-by-step visual guide for Wudu (Ablution) and the five daily prayers. It features swipe-based navigation, clear illustrations, and audio recitations with speed control.
* **Info Tab:** A simple, scrollable text page (rendered from Markdown) that clearly explains the 5 Pillars of Islam and the 6 Articles of Faith.

## 🛠️ Tech Stack

* **Python 3**
* **Flet** (for the entire UI and web app framework)

## 🚀 How to Run This Project

Follow these steps to run the app on your local machine.

### 1. Prerequisites

* Make sure you have **Python 3.10** or newer installed.
* Make sure you have **Git** installed.

### 2. Setup the Environment

1.  **Open a terminal** in the project's root folder (`THE FIRST PILLAR`).

2.  **Create a virtual environment:**
    ```bash
    # On macOS/Linux
    python3 -m venv venv
    
    # On Windows
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    ```bash
    # On macOS/Linux
    source venv/bin/activate
    
    # On Windows (Command Prompt)
    .\venv\Scripts\activate.bat
    
    # On Windows (PowerShell)
    .\venv\Scripts\activate
    ```
    > **PowerShell Note:** If you get an error, you may need to run this command first to allow scripts:
    > `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

### 3. Install Dependencies

With your virtual environment `(venv)` active, install Flet:

```bash
pip install flet
