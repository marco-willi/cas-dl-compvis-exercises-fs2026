"""Canonical dataset source registry.

Single source of truth for all dataset archives used by the exercise notebooks.
Notebooks inline a copy of these dicts (notebooks are self-contained for Colab)
— keep this module and the inline copies in sync.

Each dataset may have two sources:
    * GDRIVE_IDS  — primary, public Drive file IDs fetched via ``gdown``
    * HF_REPOS    — fallback, Hugging Face Hub dataset repos fetched via
                    ``huggingface_hub.hf_hub_download``

Both are configured to require no authentication.

Optional alternative datasets (cats_vs_dogs, concrete_cracks, eurosat) have
GDrive entries only — no HF mirror due to licensing restrictions.
"""

GDRIVE_IDS = {
    "ser_balanced.tar.gz": "1iRlZue4-Udg_lA9RCYtg3zhctqbbPhX7",
    "abo_furniture.tar.gz": "1ClnTzR1plXXzKQslsK4YaQzzxCHU44cK",
    "deepfashion_classroom_v1_internal.zip": "1ImwlWDEpqK1q_KMGcjSSX557CRtSFWbN",
    "cct20.tar.gz": "105DkEQcFhgWsQEzKh6p-u2QMMuUc2yt2",
    "kgalagadi.tar.gz": "129vX_GF4vUgwRlyLpx5BNPf6lI2n89Wp",
    "ser_sampled.tar.gz": "",  # TODO: fill after GDrive upload
    "ser_sampled_cropped.tar.gz": "",  # TODO: fill after GDrive upload
    # Optional alternative datasets — fill IDs after uploading to GDrive
    "cats_vs_dogs.tar.gz": "",  # TODO: fill after GDrive upload
    "concrete_cracks.tar.gz": "",  # TODO: fill after GDrive upload
    "eurosat.tar.gz": "",  # TODO: fill after GDrive upload
}

HF_REPOS = {
    "ser_balanced.tar.gz": "marco-willi/ser_balanced",
    "abo_furniture.tar.gz": "marco-willi/abo_furniture",
    "cct20.tar.gz": "marco-willi/camera-trap-cct20",
    "ser_sampled.tar.gz": "marco-willi/ser_sampled",
    "ser_sampled_cropped.tar.gz": "marco-willi/ser_sampled_cropped",
}
