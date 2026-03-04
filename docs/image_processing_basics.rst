.. _image_processing_basics:

Digital Image Processing Basics
================================

This section introduces the fundamental concepts of digital image
processing that underpin all the methods used throughout this tutorial.
For comprehensive treatments, see :cite:`gonzalez2018digital` and the
`OpenCV documentation <https://docs.opencv.org/>`_ :cite:`bradski2000opencv`.

What Is a Digital Image?
-------------------------

A **digital image** is a discrete, two-dimensional representation of a
continuous scene, stored as a rectangular array of numerical values
called **pixels** (picture elements).

Formally, a grayscale image is a function:

.. math::

   f: \{0, 1, \ldots, M-1\} \times \{0, 1, \ldots, N-1\} \to \{0, 1, \ldots, L-1\}

where :math:`M \times N` is the **spatial resolution** (height × width)
and :math:`L` is the number of discrete intensity levels (e.g.,
:math:`L = 256` for 8-bit images).

Key Concepts
~~~~~~~~~~~~

**Resolution**
   The number of pixels in each spatial dimension. Higher resolution
   captures finer detail but requires more storage and computation.
   Common resolutions in microscopy range from 512×512 to 4096×4096.

**Bit Depth**
   The number of bits used to represent each pixel value. Common depths:

   - *8-bit*: 256 levels (0–255), standard for display.
   - *16-bit*: 65 536 levels, common in scientific microscopy for
     preserving dynamic range.
   - *32-bit float*: used after processing operations that may produce
     fractional values.

**Color Spaces**
   - *Grayscale*: single channel; most scientific microscopy images.
   - *RGB*: three channels (red, green, blue); standard for color images.
   - *HSV / HSL*: hue–saturation–value/lightness; useful for
     color-based segmentation.
   - *Lab*: perceptually uniform; useful for color-difference metrics.

Histograms
----------

The **intensity histogram** :math:`h(r_k)` counts the number of pixels
with intensity level :math:`r_k`:

.. math::

   h(r_k) = \sum_{i=0}^{M-1} \sum_{j=0}^{N-1} \delta(f(i,j) - r_k), \quad k = 0, 1, \ldots, L-1

Histograms reveal the tonal distribution of an image and are the basis
for several enhancement techniques.

**Histogram equalization** redistributes pixel intensities to achieve a
roughly uniform histogram, enhancing global contrast:

.. math::

   s_k = (L-1) \sum_{j=0}^{k} p_r(r_j)

where :math:`p_r(r_j) = h(r_j) / (MN)` is the normalized histogram.

**Contrast Limited Adaptive Histogram Equalization (CLAHE)** applies
equalization locally within tiles and clips the histogram to avoid
over-amplifying noise, making it well suited for microscopy images.

Spatial Filtering
-----------------

Spatial filters operate on a neighborhood of each pixel using a
**convolution kernel** :math:`w`:

.. math::

   g(x, y) = (f * w)(x, y) = \sum_{s=-a}^{a} \sum_{t=-b}^{b} w(s, t)\, f(x+s, y+t)

Smoothing (Low-Pass) Filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Box (mean) filter**: replaces each pixel with the average of its
  neighborhood. Simple but blurs edges.
- **Gaussian filter**: weights neighbors by a Gaussian function,
  providing smoother results with less ringing.
- **Median filter**: replaces each pixel with the median of its
  neighborhood. Highly effective for salt-and-pepper noise while
  preserving edges.
- **Bilateral filter**: edge-preserving smoothing that weights neighbors
  by both spatial distance and intensity similarity.
- **Non-local means (NLM)**: exploits self-similarity across the whole
  image; excellent for Gaussian noise in microscopy
  :cite:`vanderwalt2014scikit`.

Edge Detection
--------------

Edges correspond to regions of rapid intensity change. Common operators:

- **Sobel / Prewitt**: first-order derivative filters for gradient
  magnitude and direction.
- **Laplacian of Gaussian (LoG)**: second-order operator; detects
  zero-crossings.
- **Canny edge detector**: multi-stage pipeline (Gaussian smoothing →
  gradient → non-maximum suppression → hysteresis thresholding);
  widely regarded as optimal for general use.

Image Transformations
---------------------

**Geometric transformations** map pixel coordinates from one space to
another:

.. math::

   \begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix}
   = \mathbf{T}
   \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}

Common transformations include translation, rotation, scaling, shearing,
and affine/perspective warping. These are used extensively in data
augmentation (see :doc:`synthetic_data`).

**Intensity transformations** operate point-wise:

- *Normalization*: rescale intensities to a fixed range, e.g., [0, 1].
- *Standardization* (z-score): subtract mean and divide by standard
  deviation.
- *Gamma correction*: :math:`s = r^\gamma` adjusts brightness.
- *Log transform*: :math:`s = c \log(1 + r)` compresses dynamic range.

Thresholding and Binarization
------------------------------

**Thresholding** converts a grayscale image to binary:

.. math::

   g(x, y) = \begin{cases} 1 & \text{if } f(x,y) \geq T \\ 0 & \text{otherwise} \end{cases}

- **Global (Otsu's method)**: automatically finds :math:`T` by
  maximizing inter-class variance.
- **Adaptive thresholding**: computes :math:`T` locally in each region,
  handling non-uniform illumination.

Morphological Operations
------------------------

Morphological operations process binary (or grayscale) images using a
**structuring element** :math:`B`:

- **Erosion**: removes small protrusions; shrinks foreground.
- **Dilation**: fills small holes; expands foreground.
- **Opening** (erosion then dilation): removes small objects.
- **Closing** (dilation then erosion): fills small holes.
- **Watershed**: topology-based algorithm for separating touching objects
  by treating the intensity surface as a landscape and flooding from
  seed points.

Connected Components
--------------------

After binarization, **connected-component labeling** assigns a unique
integer label to each connected foreground region. This is the standard
way to count and characterize individual particles or cells in a
segmented image.

Libraries and Tools
-------------------

This tutorial uses the following Python libraries for image processing:

- **OpenCV** :cite:`bradski2000opencv` — comprehensive computer-vision
  library with highly optimized C++ back-end.
- **scikit-image** :cite:`vanderwalt2014scikit` — Pythonic, NumPy-based
  image processing; excellent for scientific applications.
- **Pillow** — basic image I/O and transformations.
- **NumPy** / **SciPy** — array operations and signal-processing
  utilities.

References
----------

.. bibliography::
   :filter: False
   :list: bullet

   gonzalez2018digital
   bradski2000opencv
   vanderwalt2014scikit
