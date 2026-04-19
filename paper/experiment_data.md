# Experiment Data

All quantitative results extracted from the Final Year Project Report.

---

## Table 1: Training Results (Test Split) - PSNR and SSIM per Model per Dataset

Source: Table 9.1

| Model | Dataset A PSNR (dB) | Dataset A SSIM | Dataset B PSNR (dB) | Dataset B SSIM | Dataset C PSNR (dB) | Dataset C SSIM |
|---|---|---|---|---|---|---|
| U-Net (baseline) | 23.66 | 0.9705 | 24.45 | 0.9762 | 20.96 | 0.9464 |
| U-Net Conditional | 24.18 | 0.9743 | 24.70 | 0.9773 | 21.35 | 0.9508 |
| Restormer | 24.71 | 0.9762 | 25.34 | 0.9777 | 21.67 | 0.9563 |
| GAN-pix2pix | 23.21 | 0.9672 | 23.48 | 0.9708 | 19.97 | 0.9177 |
| Diffusion-SR3 | 21.74 | 0.9315 | 21.74 | 0.9407 | 19.34 | 0.9052 |

---

## Table 2: Efficiency - Training Time and Inference Latency

Source: Table 9.1

| Model | Normalized Training Time | Latency (ms) |
|---|---|---|
| U-Net (baseline) | 1.00 | 11.75 |
| U-Net Conditional | 1.19 | 7.50 |
| Restormer | 14.87 | 14.01 |
| GAN-pix2pix | 1.23 | 7.34 |
| Diffusion-SR3 | 4.69 | 21.81 |

Notes: Latency measured on RTX 3090. Diffusion-SR3 latency reflects multi-step DDIM sampling.

---

## Table 3: Boundary-AUC and Reliability F Score per Model per Dataset

Source: Table 9.2. Evaluation on full [0, 89]^2 angle grid with T = 0.9 OCR threshold.

AUC: boundary area under curve (higher = wider recoverable coverage, max 1.0).
F: RMS distance of interior failures from the boundary in degrees (lower = more consistent, 0 = no interior failures).

| Model | Dataset A AUC | Dataset A F | Dataset B AUC | Dataset B F | Dataset C AUC | Dataset C F |
|---|---|---|---|---|---|---|
| U-Net (baseline) | 0.915 | 0.103 | 0.923 | 0.138 | 0.915 | 0.146 |
| U-Net Conditional | 0.916 | 0.145 | 0.924 | 0.137 | 0.917 | 0.115 |
| Restormer | 0.920 | 0.095 | 0.922 | 0.133 | 0.921 | 0.209 |
| GAN-pix2pix | 0.909 | 0.168 | 0.913 | 0.145 | 0.899 | 0.173 |
| Diffusion-SR3 | 0.889 | 0.572 | 0.887 | 0.100 | 0.886 | 1.124 |

---

## Table 4: Maximal Recoverability Boundary

The union boundary (pointwise maximum over all models and datasets):

| Metric | Value |
|---|---|
| Maximal boundary AUC | 0.934 |
| Recoverable fraction of [0, 89]^2 grid | 93.4% |
| OCR success threshold (T) | 0.90 (>= 9/10 plates recognized) |
| Beyond-limit region | Both alpha > ~80 deg AND beta > ~80 deg |

---

## Table 5: Per-Dataset Relative Performance vs U-Net Baseline (Test Split)

### Dataset A

| Model | PSNR change vs baseline | SSIM change vs baseline |
|---|---|---|
| U-Net Conditional | +2.2% | +0.4% |
| Restormer | +4.5% | +0.6% |
| GAN-pix2pix | -2.0% | -0.4% |
| Diffusion-SR3 | -8.0% | -4.0% |

### Dataset B

| Model | PSNR change vs baseline | SSIM change vs baseline |
|---|---|---|
| U-Net Conditional | +1.0% | +0.1% |
| Restormer | +3.6% | +0.15% |
| GAN-pix2pix | -4.0% | -0.4% |
| Diffusion-SR3 | -11.0% | -3.5% |

### Dataset C

| Model | PSNR change vs baseline | SSIM change vs baseline |
|---|---|---|
| U-Net Conditional | +1.9% | +0.5% |
| Restormer | +3.4% | +1.0% |
| GAN-pix2pix | -4.8% | -2.1% |
| Diffusion-SR3 | -7.8% | -4.3% |

---

## Table 6: PSNR vs OCR Accuracy Linear Regression

Full-grid evaluation. y = plate-level OCR accuracy, x = plate-level PSNR.

| Model | Slope (% OCR per dB) | Intercept | R^2 |
|---|---|---|---|
| Restormer | ~3.2% | -0.55 | 0.991 |
| Diffusion-SR3 | ~4.3% | -0.74 | 0.979 |

Interpretation: Each additional 1 dB of PSNR yields approximately 3% OCR gain for Restormer and 4% for Diffusion-SR3. PSNR explains nearly all variance in OCR accuracy.

---

## Table 7: SSIM vs OCR Accuracy Linear Regression

| Model | R^2 |
|---|---|
| Restormer | 0.777 |
| Diffusion-SR3 | 0.739 |

Interpretation: SSIM has a threshold-like relationship with OCR. OCR stays near zero below SSIM ~0.92, then rises sharply. High variance at similar SSIM values makes it an unreliable proxy for OCR during training.

---

## Table 8: High-Angle Region Mean Performance

Region R = {(alpha, beta) | alpha >= 80 OR beta >= 80}.
Values are approximate from bar plots (Figure 9.10).

| Model | Approx. Mean PSNR (dB) | Approx. Mean SSIM | Approx. Mean Plate OCR |
|---|---|---|---|
| Restormer | ~40 | ~0.97 | ~0.67 |
| U-Net Conditional | ~37 | ~0.97 | ~0.67 |
| U-Net (baseline) | ~36-37 (best on B) | ~0.96 | ~0.65 |
| GAN-pix2pix | ~35 (A, B) / lower (C) | ~0.95 | ~0.63 |
| Diffusion-SR3 | ~30 | ~0.92 | ~0.55 |

---

## Table 9: Dataset Specifications

| Dataset | Samples | Angle PDF type | Train set | Val set | Test set |
|---|---|---|---|---|---|
| A | 10,240 | Moderate emphasis on extreme angles | 80% | 10% | 10% |
| B | 20,480 | Same as A (doubled) | 80% | 10% | 10% |
| C | 10,240 | Stronger emphasis on extreme angles | 80% | 10% | 10% |

Angle space sampled: (alpha, beta) in [-90, 90]^2 using Scrambled Sobol sequences.
Image resolution: 256x64 pixels after de-warping and downscaling.

---

## Table 10: Full-Grid Evaluation Sampling Density

| Angle region | Samples per (alpha, beta) pair |
|---|---|
| alpha <= 60 AND beta <= 60 | 2 |
| alpha > 60 OR beta > 60 | 10 |

Grid covers all integer pairs in [0, 89]^2 = 8,100 angle pairs total.

---

## Key Numerical Findings Summary

| Finding | Value |
|---|---|
| Maximal recoverable fraction of angle grid | 93.4% |
| Hard unrecoverable region | alpha > ~80 deg AND beta > ~80 deg |
| Best discriminative boundary AUC range | 0.915 - 0.924 |
| Best discriminative reliability F range | 0.095 - 0.209 |
| Generative AUC deficit vs discriminative | 1 - 3% lower |
| Diffusion-SR3 worst-case F (Dataset C) | 1.124 |
| PSNR-OCR R^2 (Restormer) | 0.991 |
| PSNR-OCR R^2 (Diffusion-SR3) | 0.979 |
| SSIM-OCR R^2 (Restormer) | 0.777 |
| SSIM-OCR R^2 (Diffusion-SR3) | 0.739 |
| SSIM threshold below which OCR ~= 0 | ~0.92 |
| AUC gain from doubling data (A to B) | < 0.01 |
| Restormer training time vs U-Net | 14.87x |
| Diffusion-SR3 training time vs U-Net | 4.69x |
| Restormer latency | 14.01 ms |
| Diffusion-SR3 latency | 21.81 ms |
| U-Net Conditional latency | 7.50 ms |
| GAN-pix2pix latency | 7.34 ms |
