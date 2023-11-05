# File Extension Adder

This Python script `aggiungi_estensione_cartella.py` is a simple utility that adds file extensions to files in a specified directory based on their MIME types. It utilizes the `filetype` library to determine the MIME type of each file and then renames the files to have the appropriate file extension.

## Usage

1. First, make sure you have Python installed on your system.

2. Install the `filetype` library if you haven't already. You can install it using `pip`:

   ```
   pip install filetype
   ```

3. Download the `aggiungi_estensione_cartella.py` script to your computer.

4. Open a terminal or command prompt and navigate to the directory where you placed the script.

5. Run the script by executing the following command:

   ```
   python aggiungi_estensione_cartella.py
   ```

   This will process the current directory (the one where the script is located) and add the appropriate file extensions to files based on their MIME types.

6. You can also specify a different directory by providing its path as an argument to the script:

   ```
   python aggiungi_estensione_cartella.py /path/to/your/directory
   ```

   This will process the specified directory and add file extensions accordingly.

## How It Works

The script works as follows:

- It imports the necessary libraries, including `os` and `filetype`.

- The `aggiungi_estensione_cartella` function takes a root directory as an argument and iterates through all files within that directory and its subdirectories using `os.walk`.

- For each file, it uses the `filetype.guess` method to determine its MIME type.

- If the MIME type indicates the file is an image, it checks if the file already has a `.jpg` extension. If not, it renames the file with a `.jpg` extension.

- If the MIME type indicates the file is a video, it checks if the file already has a `.mp4` extension. If not, it renames the file with a `.mp4` extension.

- Finally, in the `if __name__ == "__main__":` block, the script gets the current working directory and calls the `aggiungi_estensione_cartella` function to process the files in that directory.
