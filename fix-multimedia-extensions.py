import os
import filetype

def aggiungi_estensione_cartella(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            filepath = os.path.join(root, file)
            tipo = filetype.guess(filepath)
            
            if tipo is None:
                continue

            if "image" in tipo.mime: # immagine
                if not filepath.endswith(".jpg"):
                    os.rename(filepath, filepath + ".jpg")
            
            elif "video" in tipo.mime: # video
                if not filepath.endswith(".mp4"):
                    os.rename(filepath, filepath + ".mp4")

if __name__ == "__main__":
    current_directory = os.getcwd()
    aggiungi_estensione_cartella(current_directory)
