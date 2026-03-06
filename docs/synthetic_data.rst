.. _synthetic_data:

Synthetic Data Generation
=========================

A fundamental challenge in applying supervised machine learning to
scientific microscopy is the **scarcity of labeled data**. Pixel-level
annotation (semantic segmentation masks) of microscopy images requires
expert knowledge and is extremely time-consuming. Synthetic data
generation offers strategies to produce large annotated datasets
efficiently.

Why Synthetic Data?
-------------------

Training robust segmentation models typically requires hundreds or
thousands of annotated images. Several strategies exist to meet this
requirement:

1. **Classical augmentation**: apply label-preserving transformations to
   existing annotated images to artificially expand the dataset.
2. **Physics-based synthesis**: build a computational model of the
   imaging process and generate images analytically, with ground-truth
   masks known by construction.
3. **Generative models (GANs)**: train a neural network to learn the
   distribution of real images and sample new synthetic examples.
4. **Diffusion-based synthesis**: use large pretrained text-to-image or
   image-to-image diffusion models to generate realistic variations.

Each approach has different trade-offs between realism, diversity,
computational cost, and annotation effort.

Classical Augmentation
-----------------------

Data augmentation applies deterministic or random transformations to
each training image and its corresponding mask :cite:`shorten2019survey`.
Because the transformations are applied equally to both image and mask,
no new annotation is required.

**Geometric transforms**:

- Random horizontal / vertical flip
- Random rotation (arbitrary angle or restricted to multiples of 90°)
- Random scaling (zoom in / out)
- Random translation (shift)
- Elastic deformation: locally random displacement fields that simulate
  tissue or material deformation
- Perspective / affine warping

**Intensity transforms**:

- Random brightness and contrast adjustment
- Random gamma correction
- Gaussian noise addition
- Random blur (Gaussian, motion)
- Cutout / random erasing: randomly masking rectangular regions to
  simulate occlusion

Libraries such as ``albumentations`` and ``torchvision.transforms``
provide high-performance, composable augmentation pipelines.

Physics-Based Synthesis
------------------------

Physics-based synthesis places parameterized particle models onto real
or procedurally generated backgrounds. Because the object positions and
shapes are known by construction, ground-truth segmentation masks are
automatically available.

Typical workflow:

1. Acquire a set of representative background images (empty substrate,
   binder phase, etc.).
2. Define a particle model: shape (circle, ellipse, polygon), size
   distribution, contrast, edge-blur radius.
3. Randomly sample particle parameters from the defined distributions.
4. Composite particles onto backgrounds using alpha blending.
5. Record the binary mask of each particle.

This approach is related to **domain randomization**
:cite:`tobin2017domain`, which deliberately over-randomizes simulation
parameters to force the trained model to generalize across a broad
range of conditions.

Deep Convolutional GAN (DCGAN)
--------------------------------

Generative Adversarial Networks (GANs) :cite:`goodfellow2014gan`
train a **generator** network :math:`G` and a **discriminator**
network :math:`D` in an adversarial game:

.. math::

   \min_G \max_D \; \mathbb{E}_{x \sim p_{\text{data}}}[\log D(x)]
   + \mathbb{E}_{z \sim p_z}[\log(1 - D(G(z)))]

The DCGAN architecture :cite:`radford2015dcgan` uses convolutional
layers in both networks, enabling high-quality image synthesis.
Once trained, the generator can sample arbitrarily many synthetic
images by feeding random noise vectors :math:`z \sim p_z`.

**Limitations**: GAN training is notoriously unstable (mode collapse,
vanishing gradients); the generated images may not be paired with
segmentation masks without additional work (e.g., paired cGAN).

Stable Diffusion Image-to-Image
---------------------------------

Diffusion models :cite:`vonplaten2022diffusers` learn to reverse a
gradual noising process, iteratively denoising a Gaussian noise sample
into a high-fidelity image.

**Image-to-image synthesis** conditions the denoising on an existing
input image and a text prompt:

1. Encode the input image into a latent representation.
2. Add a controlled amount of Gaussian noise (strength parameter).
3. Run the denoising diffusion process conditioned on text and the
   noisy latent.
4. Decode the resulting latent to image space.

This produces a new image that retains the overall structure of the
input while incorporating diversity specified by the prompt and
strength parameter. In the context of microscopy, this can be used to
generate stylistic variants of real images.

Synthetic Data Notebooks
-------------------------

The following Jupyter notebooks demonstrate each synthetic data
generation strategy:

- `Classical augmentation (Aug) <https://github.com/omidvarnia/DPG2026_release>`_
- `Physics-based synthesis (PB) <https://github.com/omidvarnia/DPG2026_release>`_
- `DCGAN-based synthesis <https://github.com/omidvarnia/DPG2026_release>`_
- `Stable Diffusion image-to-image <https://github.com/omidvarnia/DPG2026_release>`_
