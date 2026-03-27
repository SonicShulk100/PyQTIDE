# PyQt IDE - An IDE made in Python (Specifically PyQt6)

> [!WARNING]
> It's still in WIP. Do not use it until it is fully functional.

Summary:
1) What is it?
2) Why?
3) How to install?

## What is it?

PyQt IDE, as the title suggest, is an IDE that is made in Python, specifically using PyQt6 as the base of it.

## Why?

Honestly? My first IDE for Python is Pycharm. Because of JetBrains making the community edition I relied on as part of the unified professionnal version of Python, I choose to make it my own, open-source and handled everything an IDE could have.

## How to install?

> [!IMPORTANT]
> In order to use it, you need the following tools:
> - Git (Obviously)
> - Python (Also Obviously)

### Step 1
Install it using Git (I don't have the capability to write a proper release yet.)
```shell
git clone https://github.com/SonicShulk100/PyQTIDE.git
```

### Step 2

Head to the directory and make the virtual environment.

```shell
cd PyQTIDE
python -m venv .venv #Reason why ".venv" is the default name for it
source .venv/bin/activate #<= ONLY if you use bash
```

### Step 3

Install the packages in the `requirements.txt` file.

```shell
pip install -r requirements.txt
```

### Final Step

Once you've done that, run the `main.py` file.

```shell
python main.py
```