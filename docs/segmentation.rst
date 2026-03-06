.. _segmentation:

Image Segmentation
==================

Image segmentation assigns a class label to every pixel in an image,
partitioning it into meaningful regions. In electrochemical microscopy,
segmentation is used to identify and quantify phases, particles, pores,
and other structural features.

Classical vs. ML-Based Approaches
------------------------------------

**Classical approaches**:

- *Thresholding* (Otsu, adaptive): effective for bimodal histograms.
- *Watershed transform*: separates touching objects using topological
  flooding; sensitive to over-segmentation.
- *Active contours / level sets*: iteratively deform a contour to
  minimize an energy functional.
- *Graph-cut methods*: formulate segmentation as a min-cut problem on
  a pixel graph.

**Machine-learning approaches**:

- *Random forests on handcrafted features*: fast and interpretable;
  used in tools such as ilastik.
- *Convolutional neural networks (CNNs)*: learn hierarchical features
  end-to-end from annotated data; far more powerful than handcrafted
  features for complex textures and shapes.
- *Foundation models*: large models pretrained on web-scale or
  domain-specific data; applicable with zero or very few labels.

U-Net
-----

U-Net :cite:`ronneberger2015unet` is the dominant architecture for
biomedical and scientific image segmentation. Its defining feature is
a **symmetric encoder–decoder** structure with **skip connections**:

- **Encoder** (contracting path): a stack of convolutional blocks with
  max-pooling that progressively reduces spatial resolution while
  increasing feature dimensionality.
- **Decoder** (expanding path): transposed convolutions or bilinear
  upsampling restore spatial resolution, with skip connections
  concatenating high-resolution encoder features at each scale.
- **Output**: a :math:`1 \times 1` convolution producing per-pixel
  class logits.

The skip connections allow the decoder to recover fine spatial detail
that would otherwise be lost in the bottleneck, which is critical for
precise boundary localization.

The ``segmentation_models_pytorch`` library :cite:`yakubovskiy2020smp`
provides a high-level API for U-Net and many other architectures with
a choice of encoder backbones (ResNet, EfficientNet, etc.) pretrained
on ImageNet.

Segment Anything Model (SAM v1)
---------------------------------

SAM :cite:`kirillov2023sam` is a large-scale segmentation foundation
model trained by Meta AI on over 1 billion masks from 11 million
images. It supports three prompting modes:

- *Point prompts*: one or more foreground/background point clicks.
- *Box prompts*: a bounding box around the target object.
- *Automatic mask generation*: dense grid of point prompts to
  segment everything in the image.

SAM uses a large Vision Transformer (ViT) image encoder, a lightweight
prompt encoder, and a fast mask decoder. The image embeddings are
computed once per image and cached, enabling interactive prompting at
near-real-time speeds.

SAM 2
------

SAM 2 :cite:`ravi2024sam2` extends SAM to video segmentation by
introducing a **memory mechanism** that propagates object masks
across frames. For image segmentation, SAM 2 retains the prompting
interface of SAM v1 while offering improved mask quality and a
streaming architecture.

NASA MicroNet
--------------

NASA's pretrained microscopy models (MicroNet) provide convolutional
neural networks trained on a diverse collection of materials
microscopy images. The pretrained features transfer well to new
microscopy domains, often outperforming ImageNet-pretrained
initializations when fine-tuned on domain-specific data.

Reference:
`https://github.com/nasa/pretrained-microscopy-models
<https://github.com/nasa/pretrained-microscopy-models>`_

TrackPy
-------

TrackPy :cite:`allan2021trackpy` is a Python library for
**particle tracking** in image sequences. It implements the
Crocker–Grier tracking algorithm:

1. **Particle detection**: locate bright spots (or dark spots on a
   bright background) by bandpass filtering and local maxima detection.
2. **Subpixel refinement**: estimate particle centroid positions with
   sub-pixel accuracy.
3. **Trajectory linking**: connect particle positions across frames
   into trajectories by solving an assignment problem that minimizes
   total displacement.
4. **Drift correction**: subtract ensemble-average motion to isolate
   individual particle dynamics.
5. **Motion analysis**: mean-squared displacement (MSD), diffusion
   coefficients, velocity statistics.

TrackPy is well suited for tracking colloidal particles, bubbles,
and other small objects in electrochemical or fluid-dynamics imaging
experiments.

Segmentation Notebooks
-----------------------

The following Jupyter notebooks demonstrate each segmentation and
tracking approach:

- :doc:`Binary segmentation with U-Net <notebooks/segmentation/example_unet>`
- :doc:`Segment Anything Model (SAM v1) <notebooks/segmentation/example_sam1>`
- :doc:`Segment Anything Model 2 (SAM 2) <notebooks/segmentation/example_sam2>`
- :doc:`NASA MicroNet segmentation <notebooks/segmentation/example_nasa_micronet>`
- :doc:`Particle tracking with TrackPy <notebooks/segmentation/example_trackpy>`
