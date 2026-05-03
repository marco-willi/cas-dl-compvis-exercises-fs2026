# Datasets

This document lists every dataset used by the exercises, with a short description
of its origin, content, and the exercise(s) it appears in. Curation details and
licensing for the course-curated subsets live in their dataset cards under
[scripts/prepare_datasets/](../scripts/prepare_datasets/).

## MNIST

The classic dataset of 28×28 grayscale handwritten digits (0–9), 60k train
and 10k test images. Used in [exercises/00_pytorch](../exercises/00_pytorch)
as a small, fast-loading dataset for first contact with PyTorch tensors,
`Dataset`, and `DataLoader`. Loaded directly from `torchvision.datasets.MNIST`.

![MNIST samples](mnist_samples.png)

## Snapshot Safari SER (Serengeti)

A balanced subset of camera-trap images from Serengeti National Park
(Snapshot Safari 2024 Expansion), curated to ten species classes plus an
`empty` class (~1850 images total). Used as the
**default** camera-trap dataset in
[01_image_data](../exercises/01_image_data),
[02_classification](../exercises/02_classification),
[04_adaptation](../exercises/04_adaptation), and
[05_backbones](../exercises/05_backbones).

![SER elephant — night IR camera-trap frame](ser_elephant.jpg)

## Caltech Camera Traps (CCT20)

A balanced 8-class subset of the CCT20 benchmark (200 images per class:
bobcat, cat, coyote, empty, opossum, rabbit, raccoon, squirrel). Sourced
from LILA Science. Offered as an **alternative** camera-trap dataset in
exercises 02, 04, and 05. When a
North-American species mix is preferred.

![CCT20 bobcat crossing a road at night](cct20_bobcat.jpg)

## Snapshot Kgalagadi

A subset of Snapshot Kgalagadi Season 1 (Kalahari camera traps) covering
six classes: empty, gemsbokoryx, birdother, steenbok, ostrich,
jackalblackbacked. Heavily imbalanced — `empty` accounts for ~78% of the
~3400 images, which makes it the **alternative of choice for dealing with
class imbalance** in exercises 02, 04, and 05.

![Kgalagadi gemsbok at a Kalahari camera trap](kgalagadi_gemsbok.jpg)

## Amazon Berkeley Objects (ABO) Furniture

A curated subset of the Amazon Berkeley Objects dataset, restricted to six
furniture categories (bed, chair, lamp, sofa, storage, table) with multiple
views per item, ~25k centre-cropped 224×224 JPEGs. The multi-view structure
(via `retrieval_groups.json`) makes it well-suited for image retrieval.
Used as the **default** dataset in
[03_retrieval](../exercises/03_retrieval).

![ABO chair — e-commerce product photo](abo_chair.jpg)

## DeepFashion (In-Shop Retrieval)

A 5-class coarse-label subset (dresses, outerwear, pants, skirts, tops) of
the DeepFashion In-Shop Clothes Retrieval Benchmark from MMLAB/CUHK, ~3300
images split by item ID so all views of one product stay in the same split.
Offered as the **alternative** to ABO in
[03_retrieval](../exercises/03_retrieval). **Internal use only — do not
redistribute** (see the dataset card for license details).

![DeepFashion dress — in-shop catalogue photo](deepfashion_dress.jpg)

## AMI-Br (Atypical Mitotic Figures — Breast)

128×128 histopathology patches of mitotic figures from human breast cancer
slides (subset of TUPAC16 + MIDOG21), with binary labels for normal vs.
atypical mitoses. Used in
[04_adaptation_lora](../exercises/04_adaptation_lora) as a small,
domain-shifted target task for parameter-efficient fine-tuning (LoRA).

![AMI-Br normal mitotic figure patch](ami_br_normal.png)

______________________________________________________________________

## Optional Alternative Datasets

The three datasets below are available as **alternatives** for any non-retrieval
exercise. They can replace the default camera-trap datasets in
[01_image_data](../exercises/01_image_data),
[02_classification](../exercises/02_classification),
[04_adaptation](../exercises/04_adaptation),
[04_adaptation_lora](../exercises/04_adaptation_lora), and
[05_backbones](../exercises/05_backbones).

They are **not suitable for [03_retrieval](../exercises/03_retrieval)**, which
requires a multi-view item structure (like ABO/DeepFashion).

All three are hosted on Google Drive only — no Hugging Face mirror due to
licensing restrictions. Download them with `ensure_dataset(..., hf_repo=None)`.

______________________________________________________________________

## Microsoft Cats vs Dogs

The full Microsoft/Kaggle Cats and Dogs dataset (~25,000 colour photos of cats
and dogs). Two corrupt source images (`Cat/666.jpg`, `Dog/11702.jpg`) are
removed during preparation. Classes are balanced (50/50). Images are
variable-size JPEGs, typically 150–500 px on the longer side.

- **Source:** Microsoft (https://www.microsoft.com/en-us/download/details.aspx?id=54765)
- **License:** Microsoft Terms of Use (educational/non-commercial)
- **Split:** stratified 70/15/15, seed 42
- **Classes:** Cat, Dog (~12,500 each)
- **Total:** ~25,000 images

```python
dataset_dir = ensure_dataset(
    DATA_PATH, "cats_vs_dogs.tar.gz", "cats_vs_dogs",
    gdrive_id=GDRIVE_IDS["cats_vs_dogs.tar.gz"],
)
```

Apply `transforms.Resize(256)` + `CenterCrop(224)` — images are variable size.

______________________________________________________________________

## Concrete Cracks

The Özgenel et al. Concrete Crack Images dataset (~40,000 227×227 JPEG images
of concrete surfaces), with binary labels for intact (Negative) vs. cracked
(Positive) surfaces. Well suited for teaching binary classification and
industrial defect detection.

- **Source:** Mendeley Data, doi: 10.17632/5y9wdsg2zt.2
- **License:** Creative Commons Attribution 4.0 (CC BY 4.0)
- **Split:** stratified 70/15/15, seed 42
- **Classes:** Negative (~20,000), Positive (~20,000)
- **Total:** ~40,000 images, 227×227 px

```python
dataset_dir = ensure_dataset(
    DATA_PATH, "concrete_cracks.tar.gz", "concrete_cracks",
    gdrive_id=GDRIVE_IDS["concrete_cracks.tar.gz"],
)
```

Images are 227×227 px — `transforms.Resize(224)` or `CenterCrop(224)` suffices.

______________________________________________________________________

## EuroSAT RGB

The EuroSAT land-use classification dataset (RGB variant, ~27,000 images across
10 classes from Sentinel-2 satellite imagery). Images are 64×64 px, making
this an interesting case for discussing domain shift from ImageNet pretraining.

- **Source:** Zenodo record 7711810 (https://zenodo.org/records/7711810)
- **License:** MIT License
- **Attribution:** Helber et al. (2019), IEEE JSTARS, doi: 10.1109/JSTARS.2019.2918242
- **Split:** stratified 70/15/15, seed 42
- **Classes (10):** AnnualCrop, Forest, HerbaceousVegetation, Highway, Industrial,
  Pasture, PermanentCrop, Residential, River, SeaLake (~1,900–3,000 each)
- **Total:** ~27,000 images, 64×64 px

```python
dataset_dir = ensure_dataset(
    DATA_PATH, "eurosat.tar.gz", "eurosat",
    gdrive_id=GDRIVE_IDS["eurosat.tar.gz"],
)
```

**Important:** EuroSAT images are 64×64 px. Apply `transforms.Resize(224)` (or
`Resize(256)` + `CenterCrop(224)`) so ImageNet-pretrained models receive the
expected input size.
