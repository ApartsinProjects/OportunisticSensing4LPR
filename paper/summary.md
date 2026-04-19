# Project Report Summary

**Title:** Generative Image Models for Enhancing License Plate Images Captured at Extreme Viewing Angles

**Authors:** Igor Adamenko, Orpaz Ben Aharon

**Supervisor:** Dr. Sasha Apartsin

**Department:** Electrical Engineering

**Submission Date:** 06/08/2025

---

## Project Overview

License plate recognition (LPR) engines perform reliably when cameras face vehicles directly. However, street, security, and ATM cameras often capture vehicles at steep angles with low image quality. This project defines a quantitative recoverability boundary: the maximum viewing angles at which deep-learning models can still reconstruct distorted license plate images well enough for automated recognition.

---

## Objectives

- Compare five deep-learning models (discriminative and generative) on synthetic clean-distorted license plate pairs.
- Identify the maximum (alpha, beta) rotation angles at which models can restore plates to OCR-readable quality.
- Quantify recoverability by mapping plate-level OCR accuracy >= 90% across the full angle grid [0, 89]^2.

---

## Methodology

### Data Generation

- Synthetic clean plates: random 6-digit numbers on a yellow background.
- Three datasets created with different angle distributions and sizes:
  - **Dataset A:** 10,240 samples, moderate emphasis on extreme angles.
  - **Dataset B:** 20,480 samples, moderate emphasis (doubled from A).
  - **Dataset C:** 10,240 samples, stronger emphasis on extreme angles.
- Angle pairs (alpha, beta) sampled using low-dispersion Scrambled Sobol sequences to ensure uniform coverage across the [-90, 90]^2 space.
- Distortion pipeline per image:
  1. 3D rotation by sampled (alpha, beta) angles and projection to 2D plane.
  2. Camera artifact simulation: edge blending, color jitter, Gaussian blur, JPEG compression.
  3. De-warping and downscale to 256x64 pixels.
- Train / validation / test split: 80% / 10% / 10%.

### Models Compared

| Model | Type |
|---|---|
| U-Net | Discriminative (baseline) |
| U-Net Conditional (FiLM-conditioned on angle) | Discriminative |
| Restormer | Discriminative (Transformer-based) |
| GAN Pix2Pix | Generative (adversarial) |
| Diffusion SR3 (velocity prediction, DDIM sampling) | Generative (diffusion) |

### Evaluation Protocol

- **Training metrics:** PSNR and SSIM on the validation split.
- **Full-grid evaluation:** All models tested on a shared grid of all integer (alpha, beta) pairs in [0, 89]^2.
  - 2 images per pair for alpha <= 60 AND beta <= 60.
  - 10 images per pair for the high-angle region (alpha > 60 OR beta > 60).
- **Metrics collected per angle pair:** plate-level PSNR, SSIM, OCR accuracy; digit-level PSNR, SSIM, OCR accuracy.
- **Recoverability boundary:** traced as the outer edge of the region where plate-level OCR >= 90%.
- **Boundary-AUC:** normalized area enclosed by the recoverability boundary (higher = wider coverage).
- **Reliability score F:** RMS distance of interior failures from the boundary (lower = more consistent).
- **OCR engine:** Tesseract v4 (LSTM mode), digits-only filter, with fallback thresholding strategies.

---

## Key Findings

### Training Results (Test Split)

- **Restormer** achieves the best PSNR and SSIM on all three datasets.
- **U-Net Conditional** is second, outperforming the U-Net baseline by ~2% PSNR.
- **GAN-pix2pix** slightly underperforms the U-Net baseline.
- **Diffusion-SR3** is the weakest, underperforming by 7-11% PSNR.

### Efficiency

- U-Net is the fastest to train (normalized time = 1.00) with 11.75ms latency.
- U-Net Conditional: 1.19x training time, 7.50ms latency (most efficient per accuracy).
- GAN-pix2pix: 1.23x training time, 7.34ms latency.
- Restormer: 14.87x training time, 14.01ms latency.
- Diffusion-SR3: 4.69x training time, 21.81ms latency (multi-step sampling).

### Full-Grid Evaluation (Recoverability)

- All discriminative models cluster tightly: boundary AUC 0.915-0.924, F scores 0.095-0.209.
- Generative models are 1-3% lower in AUC; Diffusion-SR3 shows unstable reliability (F up to 1.124 on Dataset C).
- The **maximal recoverability boundary** (union of all models) achieves AUC = 0.934, meaning 93.4% of the angle grid is recoverable at >= 90% plate-level OCR.
- No model achieves >= 90% OCR when both alpha AND beta exceed ~80 degrees.
- Alpha rotations are generally harder to reconstruct than beta rotations.
- Doubling training data (A to B) yields marginal AUC gain (< 0.01); angle distribution matters more than size.

### Metric Correlation

- **PSNR vs OCR:** Strong linear relationship. Restormer: R^2 = 0.991, slope ~3% OCR per dB. Diffusion-SR3: R^2 = 0.979, slope ~4% OCR per dB. PSNR is a reliable proxy for OCR during training.
- **SSIM vs OCR:** Weaker and threshold-like. R^2 = 0.777 (Restormer), 0.739 (Diffusion-SR3). OCR near zero below SSIM 0.92, then rises sharply with high variance.

### Failure Patterns by Model Type

- **Discriminative models:** produce blurred or ambiguous digits under low signal; digits may merge features of multiple characters.
- **GAN-pix2pix:** fewer blurry digits but more hybrid or incomplete digits; occasional color artifacts.
- **Diffusion-SR3:** always generates visually clean plates, but hallucinates digits when signal is too weak.

---

## Conclusions

Discriminative architectures (especially Restormer) outperform generative models by a small but consistent margin and are easier to train, tune, and validate due to explicit loss functions. Generative models (GAN and diffusion) lack clear quantitative validation signals; diffusion adds further complexity through multi-step inference. All models converge on the same ~93% recoverable region, confirming a hard physical limit set by the residual signal in the distorted images. Beyond ~80 degrees in both angles, further improvement is unlikely regardless of architecture.

---

## Future Work

- Extend data generation to include varying plate distances and focal lengths (simulating real static cameras).
- Build a real-data pipeline using fixed cameras with sensors to record actual images and angle metadata.
- Adapt the synthetic-data and low-dispersion sampling framework to other oblique-view restoration tasks (signage, document imaging).

---

## Figures Index

| Figure | Description |
|---|---|
| [figure_03](figures/figure_03_lpr_oblique_concept.png) | LPR for Oblique Camera Capture: Concept Illustration |
| [figure_04](figures/figure_04_synthetic_plate_generation_strip.png) | Synthetic License Plate Generation Process |
| [figure_05](figures/figure_05_recoverability_reliability_plot_auc_vs_f.png) | Recoverability-Reliability Plot (AUC vs F) for All Models and Datasets |
| [figure_06](figures/figure_06_maximal_recoverability_boundary.png) | Maximal Recoverability Boundary |
| [figure_13](figures/figure_13_methodology_flowchart.png) | Methodology Flowchart Diagram |
| [figure_16](figures/figure_16_3d_rotation_projection_2d_plane.png) | 3D Rotation and Projection to the 2D Plane |
| [figure_30](figures/figure_30_restormer_architecture.png) | Architecture of Restormer |
| [figure_31](figures/figure_31_boundary_auc_measure_illustration.png) | Boundary-AUC Measure Illustration |
| [figure_32](figures/figure_32_model_performance_dataset_a.png) | Models Performance on Dataset A |
| [figure_33](figures/figure_33_model_performance_dataset_b.png) | Model Performance on Dataset B |
| [figure_34](figures/figure_34_model_performance_dataset_c.png) | Model Performance on Dataset C |
| [figure_35](figures/figure_35_efficiency_train_time_latency.png) | Efficiency (Train Time and Latency) |
| [figure_39](figures/figure_39_ocr_accuracy_heatmaps_dataset_b.png) | Model-Specific Plate-Level OCR Accuracy on Dataset B (Heatmaps) |
| [figure_40](figures/figure_40_recoverability_boundaries_all_models_datasets.png) | Recoverability Boundaries for All Models and Datasets |
| [figure_41](figures/figure_41_recoverability_reliability_scatter_auc_vs_f.png) | Recoverability-Reliability Scatter Plot (AUC vs F) |
| [figure_42](figures/figure_42_mean_performance_high_angle_region.png) | Mean Performance in High-Angle Region |
| [figure_43](figures/figure_43_restormer_ocr_vs_psnr.png) | Restormer OCR Accuracy vs PSNR |
| [figure_44](figures/figure_44_diffusion_sr3_ocr_vs_psnr.png) | Diffusion-SR3 OCR Accuracy vs PSNR |
| [figure_45](figures/figure_45_restormer_ocr_vs_ssim.png) | Restormer OCR Accuracy vs SSIM |
| [figure_46](figures/figure_46_diffusion_sr3_ocr_vs_ssim.png) | Diffusion-SR3 OCR Accuracy vs SSIM |
