# SPAYOLO Conda Environment

This repository provides an Anaconda environment (`yolo_env.yaml`) tailored for YOLO and general deep learning, computer vision, and scientific research. The environment is suitable for Windows, supports full GPU acceleration (CUDA 11.8), and includes most popular libraries for PyTorch, visualization, and more.

## Environment Highlights

- **Python 3.12.7**
- **PyTorch 2.5.1** (with CUDA 11.8 and GPU support)
- torchvision, timm, scikit-learn, matplotlib, OpenCV and other essentials for deep learning and data science
- Supports both pip and Conda channels (including popular mirrors), suitable for both domestic (China) and international users
- Out-of-the-box for YOLO, segmentation, vision transformers, and common research

## Quick Start

### 1. Install Anaconda/Miniconda

Visit the [Anaconda official site](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) to download and install.

### 2. Create the Environment from `yolo_env.yaml`

In your terminal (Anaconda Prompt, PowerShell, or cmd), execute:

```bash
conda env create -f yolo_env.yaml
```

The first creation may take some time. Please be patient.

If you've already created the environment and want to update it:

```bash
conda env update -f yolo_env.yaml --prune
```

### 3. Activate the Environment

```bash
conda activate yolo
```

### 4. Test PyTorch GPU/CUDA Support

```bash
python -c "import torch; print(torch.cuda.is_available())"
# Should print True if GPU is available
```

### 5. Continue with Your Research/Development

- You can now run `train.py`, `val.py`, etc. directly
- Fully compatible with Jupyter, notebooks, Spyder, and standard Python IDEs
- Includes visualization and model tuning tools used in research

## Dataset Preparation (FER13 & AffectNet)

Before training/validation, preprocess datasets into a standard image-classification directory layout: per-class subfolders under `train/`, `val/`, and optionally `test/`. For example:

```text
e:/Github/YoloV8/data/fer13/
├─ train/
│  ├─ angry/
│  ├─ disgust/
│  ├─ fear/
│  ├─ happy/
│  ├─ neutral/
│  ├─ sad/
│  └─ surprise/
├─ val/
│  ├─ angry/
│  └─ ...
├─ test/               # optional
│  ├─ angry/
│  └─ ...
├─ train.cache         # optional, auto-generated after first run
├─ val.cache           # optional, auto-generated after first run
└─ test.cache          # optional, auto-generated after first run
```

```text
e:/Github/YoloV8/data/affectnet/
├─ train/
│  ├─ neutral/
│  ├─ happy/
│  ├─ sad/
│  ├─ surprise/
│  ├─ fear/
│  ├─ disgust/
│  └─ anger/
├─ val/
│  ├─ neutral/
│  └─ ...
├─ train.cache         # optional, auto-generated after first run
└─ val.cache           # optional, auto-generated after first run
```

Notes:
- Place images of each class into its corresponding subfolder (folder name = class label).
- `*.cache` files are dataset index caches auto-generated on first run to speed up loading; you may delete them to rebuild.
- If your task is not classification (e.g., detection/segmentation), use YOLO annotation format and directory structure instead; this repo reads classification-style datasets by default.

If you need any assistance with datasets, please contact me: 4472472@gmail.com
## Dependency Notes

Notable environment components:

- pytorch, torchvision, torchaudio, timm (core vision & training packages)
- numpy, pandas, scikit-learn (data science basics)
- matplotlib, seaborn, plotly (visualization)
- opencv, Pillow (image processing), thop (model profiling)
- Extra pip-installed packages as needed (see end of `yolo_env.yaml`)

If you need additional libraries, modify `yolo_env.yaml` and rerun:

```bash
conda env update -f yolo_env.yaml
```

## Troubleshooting

1. **Package version conflicts**  
   If you see version conflicts, carefully check the conflicting packages in the error log and try fixing their versions in the yaml file.

2. **Slow or failed downloads**  
   The yaml uses several common mirrors (e.g. Tsinghua/Alibaba for China). International users can switch to other channels if needed.

3. **CUDA/cuDNN Issues**  
   Make sure your GPU drivers and CUDA toolkit are properly installed and compatible with PyTorch (see [PyTorch Getting Started](https://pytorch.org/get-started/locally/)).

## References & Credits

- [PyTorch Home](https://pytorch.org/)
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- [Anaconda Home](https://www.anaconda.com/)

---

Feel free to open an Issue if you encounter problems, and welcome to Star or Fork this repo!
