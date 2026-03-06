.. _electrochemical_imaging:

Electrochemical Imaging
=======================

This section provides an overview of the microscopy and imaging
techniques commonly used in electrochemical materials research, the
typical characteristics of the resulting images, and the challenges that
motivate the use of machine-learning-based image processing.

What Is Electrochemical Imaging?
---------------------------------

Electrochemical materials — such as battery electrodes, fuel-cell
catalysts, corrosion layers, and electrolytic coatings — are
characterized by their micro- and nano-scale structure. Understanding
this structure is crucial for explaining macroscopic performance metrics
such as capacity, efficiency, and lifetime.

**Electrochemical imaging** refers to the acquisition and analysis of
microscopy images of these materials to extract quantitative structural
information: particle size distributions, phase fractions, porosity,
tortuosity, connectivity, and surface chemistry.

Key Imaging Techniques
----------------------

Scanning Electron Microscopy (SEM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SEM rasters a focused electron beam over the sample surface and
detects secondary or backscattered electrons.

- **Resolution**: 1–20 nm, depending on instrument and sample.
- **Contrast mechanisms**:

  - *Secondary electron (SE)* images show surface topography.
  - *Backscattered electron (BSE)* images show compositional (atomic
    number) contrast — heavier elements appear brighter.

- **Applications**: particle morphology, grain structure, electrode
  cross-sections, coating thickness.
- **Typical artifacts**: charging effects (non-conductive samples),
  curtaining (FIB cross-sections), beam damage, low signal-to-noise at
  high magnification.

Transmission Electron Microscopy (TEM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TEM transmits a high-energy electron beam through a thin sample (< 100 nm).

- **Resolution**: sub-ångström with aberration-corrected instruments.
- **Contrast mechanisms**: mass-thickness contrast, diffraction contrast,
  phase contrast (HRTEM).
- **Applications**: atomic-resolution structure, lattice defects, grain
  boundaries, interface chemistry.
- **Challenges**: laborious sample preparation (FIB lamella), beam
  sensitivity of battery materials (e.g., lithium compounds), small
  field of view.

Atomic Force Microscopy (AFM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AFM rasters a sharp tip over the surface and measures tip–sample forces.

- **Resolution**: sub-nanometre in height; lateral resolution depends on
  tip radius (typically 5–30 nm).
- **Imaging modes**:

  - *Contact mode*: constant force; risk of sample damage.
  - *Tapping/AC mode*: oscillating tip; gentler; most common.
  - *Peak-force QNM*: maps mechanical properties simultaneously.

- **Applications**: solid-electrolyte-interphase (SEI) layer growth,
  surface roughness, particle deformation, in-situ/operando
  measurements.
- **Challenges**: slow scan speed, tip convolution artifacts, drift,
  vibration sensitivity.

Other Techniques
~~~~~~~~~~~~~~~~

- **Energy-dispersive X-ray spectroscopy (EDX/EDS)**: elemental mapping
  alongside SEM/TEM.
- **Electron backscatter diffraction (EBSD)**: crystallographic
  orientation mapping.
- **X-ray tomography (µCT)**: 3-D reconstruction of electrode
  microstructure at micron resolution.
- **Focused ion beam (FIB) tomography**: serial sectioning for 3-D
  reconstruction at nanometre resolution.

Typical Image Characteristics
------------------------------

Images from electrochemical imaging workflows share several features
that distinguish them from natural photographs:

**Grayscale**
   Most SEM, TEM, and AFM images are single-channel grayscale,
   though pseudo-colour is often applied for visualization.

**High dynamic range**
   16-bit acquisition is common; BSE images may span a small fraction
   of the available range due to a narrow compositional spread.

**Noise**
   - *Shot noise* (Poisson): dominant at low beam currents / short
     dwell times in SEM.
   - *Gaussian read noise*: detector electronics.
   - *Streak / scan noise*: mechanical vibration or electromagnetic
     interference during line scanning.

**Artifacts**
   - *Charging*: bright halos and bright spots in non-conductive
     regions.
   - *Curtaining*: parallel vertical streaks in FIB cross-sections
     from differential milling rates.
   - *Drift*: image shear from thermal or mechanical drift during
     long acquisitions.
   - *Beam damage*: progressive structural changes under the electron
     beam.

**Scale and magnification variation**
   A dataset may contain images acquired at different magnifications,
   requiring normalization of the physical scale before training ML
   models.

**Class imbalance**
   In electrode cross-sections, one phase (e.g., carbon black binder)
   may occupy only a few percent of the image area, creating severe
   class imbalance for segmentation models.

Why Machine Learning?
---------------------

Manual segmentation of large microscopy datasets is prohibitively
slow and introduces inter-analyst variability. Rule-based image
processing (thresholding, watershed) performs well only when imaging
conditions are uniform. Machine-learning approaches offer:

- **Generalization**: learned features adapt to varying contrast,
  noise, and morphology.
- **Scalability**: inference on thousands of images in minutes once
  a model is trained.
- **Reproducibility**: deterministic predictions from a fixed model.
- **Transfer learning**: foundation models trained on large generic
  datasets (SAM, NASA MicroNet) can be adapted to new domains with
  few or no labeled examples.

The primary challenge in applying ML to electrochemical imaging is
the **scarcity of labeled data**: pixel-level annotation of
microscopy images is extremely time-consuming. This motivates the
synthetic-data generation approaches covered in :doc:`synthetic_data`.
