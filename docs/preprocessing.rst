.. _preprocessing:

Image Preprocessing
===================

Preprocessing is the first and often most critical step in any
image-analysis pipeline. Its goal is to enhance image quality, reduce
noise and artifacts, and bring images into a consistent format before
feeding them to downstream algorithms or machine-learning models.

Why Preprocess?
---------------

Raw microscopy images suffer from a range of degradations:

- **Non-uniform illumination**: the background intensity varies across
  the field of view due to shadowing, beam profile, or detector
  inhomogeneity.
- **Noise**: shot noise at low beam currents, detector read noise, and
  scan noise all reduce image quality.
- **Low contrast**: compositionally similar phases may differ by only a
  few grey levels.
- **Scale inconsistency**: images from different sessions may be
  acquired at different magnifications and with different intensity
  calibrations.

Effective preprocessing mitigates these issues and ensures that
subsequent algorithms see consistent, well-conditioned data.

Key Preprocessing Operations
-----------------------------

Normalization and Standardization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Min-max normalization** rescales intensities to [0, 1]:

.. math::

   f_{\text{norm}}(x,y) = \frac{f(x,y) - f_{\min}}{f_{\max} - f_{\min}}

**Z-score standardization** removes the mean and scales to unit variance:

.. math::

   f_{\text{std}}(x,y) = \frac{f(x,y) - \mu}{\sigma}

Both operations are essential when combining images from different
acquisition sessions or instruments.

Denoising
~~~~~~~~~

- **Gaussian smoothing**: fast and simple; blurs both noise and edges.
  Appropriate when spatial resolution is not critical.
- **Median filtering**: preserves edges while removing impulsive
  (salt-and-pepper) noise.
- **Bilateral filtering**: edge-preserving smoothing; useful when
  structural boundaries must be maintained.
- **Non-local means (NLM)**: exploits self-similarity across the image;
  particularly effective for Gaussian noise in microscopy images at the
  cost of higher computation.

Contrast Enhancement
~~~~~~~~~~~~~~~~~~~~

- **Histogram equalization**: redistributes intensities globally for
  uniform contrast.
- **CLAHE** (Contrast Limited Adaptive Histogram Equalization): applies
  local equalization with histogram clipping to avoid noise
  amplification. Preferred for SEM/TEM images with non-uniform
  illumination.
- **Gamma correction**: non-linear brightness adjustment.

Background Correction
~~~~~~~~~~~~~~~~~~~~~

- **Rolling-ball / top-hat transform**: estimates and subtracts a
  slowly varying background using morphological operations.
- **Flat-field correction**: divides by a reference image acquired
  under the same conditions without the sample.

Edge Detection and Gradient Images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edge images highlight structural boundaries and are useful as auxiliary
inputs to segmentation models or for quality-control inspection.
Common operators: Sobel, Prewitt, Scharr, Canny (see
:doc:`image_processing_basics`).

Binarization and Thresholding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Converting a grayscale image to a binary mask separates foreground
(particles, pores) from background. Otsu's method automatically
selects the optimal global threshold; adaptive thresholding handles
non-uniform illumination.

Morphological Post-Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After binarization, morphological operations clean up the mask:

- **Opening**: removes small foreground fragments (noise).
- **Closing**: fills small holes in particles.
- **Fill holes**: fills enclosed background regions.
- **Remove small objects**: discards connected components below a
  minimum area threshold.

Preprocessing Notebook
-----------------------

The following Jupyter notebook demonstrates all of these operations on
real electrochemical microscopy images using OpenCV, scikit-image,
and NumPy:

- `Preprocessing basics (notebook) <notebooks/preprocess/preprocessing_basics.html>`_
