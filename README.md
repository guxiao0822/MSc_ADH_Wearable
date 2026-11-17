# Wearable Lab — MSc Applied Digital Health (2026/27)

This lab introduces the use of wearables and AI in digital health. You will classify single-lead wearable ECG
recordings (normal, atrial fibrillation, other rhythm, noise) with a conventional feature-based pipeline and with
a deep learning pipeline, and then apply your model to an ECG exported from an Apple Watch.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/guxiao0822/MSc_ADH_Wearable/blob/cohort_26/27/Wearable_Lab.ipynb)

The lab instructions are in `Wearable_Lab_Note.pdf`.

## Running the lab

**On Colab (recommended):** click the badge above and run the cells from top to bottom. The notebook downloads the
helper scripts and the data by itself. For the deep learning section, a GPU runtime
(*Runtime → Change runtime type → T4 GPU*, selected before you start) makes training much faster.

**On your own machine:**

```bash
git clone -b cohort_26/27 https://github.com/guxiao0822/MSc_ADH_Wearable.git
cd MSc_ADH_Wearable
conda create --name lab3wearableEnv2627 python=3.11 -y
conda activate lab3wearableEnv2627
pip install numpy matplotlib neurokit2 scikit-learn torch tqdm PyPDF2 pillow jupyter
jupyter notebook Wearable_Lab.ipynb
```

## Data

The model development data (`data/ECG.pkl`, and the pre-computed features `data/ECG_feature.pkl`) is a 2,000-recording
subset of the [PhysioNet/CinC Challenge 2017](https://physionet.org/content/challenge-2017/1.0.0/) dataset. It is not
stored in this repository; the notebook downloads it into `./data` the first time it is run.

## Contact

Dr Xiao Gu — xiao.gu@eng.ox.ac.uk
