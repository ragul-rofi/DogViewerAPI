
# Random Dog Viewer

**Random Dog Viewer** is a Python application that displays a random dog image fetched from the [Dog CEO API](https://dog.ceo/dog-api/). The app provides an easy way to view a random dog picture each time you click the "Get Random Dog" button.

## Features

- Fetches a random dog image from the Dog CEO API.
- Displays the image in a GUI window using Tkinter.
- Resizes images to a standard size (300x300 pixels) for better visibility.
- Simple, clean, and interactive design.

## Requirements

To run this application, you need the following Python libraries:

- `requests` (for fetching data from the API)
- `Pillow` (for handling image data)
- `tkinter` (for the graphical user interface, pre-installed with Python)

You can install the required libraries by running:

```bash
pip install requests Pillow
```

## How to Run

1. Clone the repository or download the Python script.

2. Install the required dependencies:

   ```bash
   pip install requests Pillow
   ```

3. Run the `random_dog_viewer.py` script:

   ```bash
   python random_dog_viewer.py
   ```

4. Click the "Get Random Dog" button to fetch and display a random dog image.


## API Used

This app uses the [Dog CEO API](https://dog.ceo/dog-api/) to fetch random dog images.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
