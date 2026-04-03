"""Different Util Functions"""

from pathlib import Path

from sklearn.model_selection import train_test_split


def download_and_extract_zip(url: str, save_path: Path, extract_path: Path):
    """
    Downloads a ZIP file from a given URL and extracts its contents to a specified directory.

    Args:
        url (str): The URL of the ZIP file to download.
        save_path (Path): The path where the downloaded ZIP file will be saved.
        extract_path (Path): The directory where the ZIP file will be extracted.
    """
    import zipfile

    import requests

    # Make sure the directory exists
    save_path.parent.mkdir(parents=True, exist_ok=True)

    if not save_path.exists():
        print(f"Starting download from {url}")
        # Download the file
        response = requests.get(url, stream=True)
        with save_path.open("wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                _ = file.write(chunk)

        print(f"File downloaded and saved to {save_path}")
    else:
        print(f"File {save_path} exists already - not overwriting")

    if not extract_path.exists():
        print(f"Starting extracting {extract_path}")
        # Unzip the file
        with zipfile.ZipFile(save_path, "r") as zip_ref:
            zip_ref.extractall(extract_path)

        print(f"File extracted to {extract_path}")
    else:
        print(f"File {extract_path} exists already - not overwriting")


def download_from_gdrive_and_extract_zip(
    file_id: str, save_path: Path, extract_path: Path
):
    """
    Downloads a ZIP file from Google Drive using its file ID and extracts its contents to a specified directory.

    Args:
        file_id (str): The Google Drive file ID of the ZIP file to download.
        save_path (Path): The path where the downloaded ZIP file will be saved.
        extract_path (Path): The directory where the ZIP file will be extracted.
    """
    import zipfile

    import gdown

    url = f"https://drive.google.com/uc?id={file_id}"
    if not save_path.exists():
        gdown.download(url, str(save_path), quiet=False)
        print(f"File downloaded and saved to {save_path}")

    if not extract_path.exists():
        print(f"Starting to extract... {extract_path}")
        # Unzip the file
        with zipfile.ZipFile(save_path, "r") as zip_ref:
            zip_ref.extractall(extract_path)

        print(f"File extracted to {extract_path}")


def delete_bad_file(file_path: Path):
    """
    Deletes a specified file if it exists.

    Args:
        file_path (Path): The path of the file to be deleted.
    """
    # Check if file exists before trying to delete it
    if file_path.exists():
        file_path.unlink()
        print(f"{file_path} has been deleted")
    else:
        print(f"{file_path} does not exist")


def find_all_imges_and_their_labels(image_dir: str | Path) -> list[dict]:
    """
    Load image paths and corresponding labels.

    Args:
        image_dir: Directory with all the images.

    Returns:
        A list of dicts, one for each obsevation
    """
    image_dir = Path(image_dir)
    observations = []
    image_extensions = {".jpg", ".jpeg", ".png"}

    for class_dir in image_dir.iterdir():
        if not class_dir.is_dir():
            continue

        label = class_dir.name
        for img_path in class_dir.iterdir():
            if img_path.suffix.lower() in image_extensions:
                observation = {"image_path": str(img_path), "label": label}
                observations.append(observation)
    return observations


def create_train_test_split(
    ids: list[int],
    labels: list[int | str],
    random_state: int = 123,
    test_size: float = 0.2,
    val_size: float = 0.1,
) -> tuple[list[dict], list[dict], list[dict]]:
    train_ids, test_ids = train_test_split(
        ids,
        stratify=labels,
        test_size=test_size,
        random_state=random_state,
    )

    train_ids, val_ids = train_test_split(
        train_ids,
        stratify=[labels[i] for i in train_ids],
        test_size=val_size,
        random_state=random_state,
    )

    return train_ids, val_ids, test_ids
