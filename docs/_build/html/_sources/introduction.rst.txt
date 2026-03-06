.. _introduction:

Introduction
============

Overview
--------

This tutorial provides a comprehensive, hands-on introduction to
**machine-learning-based image processing** for electrochemical and
scientific microscopy data. It was developed for the
**DPG 2026, AKPIK session** in Dresden, March 2026

Developer
---------

**Amir Omidvarnia** — `Institute of energy Technologies (IET-1), Forschungszentrum Jülich <https://www.fz-juelich.de/de/iet>`_,
`a.omidvarnia@fz-juelich.de <mailto:a.omidvarnia@fz-juelich.de>`_

The tutorial walks through different classical and machine-learning pipelines for
scientific image analysis — from through image preprocessing and synthetic 
data generation, to segmentation and
tracking of structures of interest.

Tutorial Goals
--------------

By the end of this tutorial, participants will be able to:

- Apply standard image-processing techniques (normalization, denoising,
  contrast enhancement, morphological operations) to microscopy images.
- Generate synthetic training data using classical augmentation,
  physics-based simulation, GANs, and Stable Diffusion.
- Train and apply deep-learning segmentation models (U-Net) to
  electrochemical microscopy data.
- Use foundation models (SAM v1 & v2, NASA MicroNet) for zero-shot and
  few-shot segmentation.
- Perform particle detection, tracking, and motion analysis with TrackPy.

Target Audience
---------------

The tutorial targets researchers and students in physics, materials
science, electrochemistry, and related fields who have a basic
familiarity with Python and want to apply modern machine-learning tools
to their imaging data. Prior deep-learning experience is helpful but
not required.

Tutorial Structure
------------------

The tutorial is organized into three main themes, presented in the
following order:

1. **Image Preprocessing** — Fundamental operations on digital images:
   normalization, denoising, contrast enhancement, edge detection,
   binarization, and morphological analysis.
   See :doc:`preprocessing`.

2. **Synthetic Data Generation** — Techniques for creating training
   data when labeled real images are scarce: classical augmentation,
   physics-based synthesis, deep convolutional GANs (DCGAN), and
   Stable Diffusion image-to-image synthesis.
   See :doc:`synthetic_data`.

3. **Image Segmentation & Tracking** — Supervised and foundation-model
   approaches: U-Net training, SAM v1 & v2, NASA MicroNet pretrained
   models, and TrackPy particle tracking.
   See :doc:`segmentation`.

Each theme is accompanied by one or more Jupyter notebooks that can be
run interactively. The notebooks demonstrate the concepts on
electrochemical microscopy images, but the methods apply broadly to any
scientific imaging domain.

How to Use This Tutorial
------------------------

All interactive content is provided as Jupyter notebooks. To run the
notebooks, follow the setup instructions in the repository README:

1. Create a Python 3.11 virtual environment (using `uv <https://docs.astral.sh/uv/>` or
   `pyenv <https://github.com/pyenv/pyenv>`_).
2. Install dependencies from ``requirements.txt``.
3. Open the notebooks in VS Code or JupyterLab and select the
   appropriate kernel.

Alternatively, the notebooks can be read statically in this
documentation without executing them.

Repository
----------

The source code and notebooks are available at:
`https://github.com/omidvarnia/dpg2026_mlip_tutorial

<https://github.com/omidvarnia/dpg2026_mlip_tutorial
>`_
