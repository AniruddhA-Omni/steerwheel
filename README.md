# Steerwheel
***
## <u>Dependencies and Installation</u>

- Python >= 3.7 (Recommend to use [Anaconda](https://www.anaconda.com/download/#linux))

- Optional: NVIDIA GPU + [CUDA](https://developer.nvidia.com/cuda-downloads)


### Installation

1. Clone repo

    ```bash
    git clone https://github.com/AniruddhA-Omni/steerwheel.git
    cd SteerWheel
    ```
2. Install dependent packages
    ```bash
    pip install -r requirements.txt
   ```

### Run the program
   ```
   python main.py
   ```

## <u>Instructions</u>

1. Selecting Colours
   - **Run** _color_select.py_
   - Adjust the trackbars to select the desired colour
   - Note the values
   - **Update colour_low** array in _main.py_
2. Adding or Removing Keys
   - Refer _key_code.txt_ to know the keycode of a specific key
   - **Add/Delete** the keycode in _directkeys.py_ in a mentioned area
   - **Import** the Variable for that key in _main.py_
3. Running main program
   - Keep the steering wheel <i>50cm - 60cm</i> away from Camera
   - Press ESC to quit from the program

