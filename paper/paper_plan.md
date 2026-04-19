# Paper Plan: Computers, Environment and Urban Systems (CEUS)

**Target journal:** Computers, Environment and Urban Systems (Elsevier)
**CiteScore:** 16.6 | **Impact Factor:** 8.3
**Word limit:** 8,000 words | **Abstract:** max 250 words | **References:** APA 7th Edition
**Review:** Double-blind

---

## Title

**Primary:**
> Opportunistic License Plate Recognition from Smart City Fixed Sensors: Quantifying Recoverability Limits Under Extreme Viewing Angles

**Alternative:**
> When You Cannot Reposition the Camera: Deep Learning Recoverability Boundaries for License Plate Recognition in Urban Opportunistic Sensing

**Rationale:** CEUS audience is urban systems researchers, not computer vision specialists. "Smart city fixed sensors," "opportunistic," and "urban" must appear in the title. The framing is the sensor infrastructure problem, not the image restoration problem.

---

## Highlights (max 85 characters each)

- Fixed urban sensors enable LPR without hardware changes in 93% of angle space
- Five deep learning architectures benchmarked on oblique license plate recovery
- Novel boundary-AUC and reliability-F metrics quantify recoverability coverage
- PSNR predicts OCR accuracy linearly (R2 = 0.99); SSIM is unreliable below 0.92
- Alpha-axis rotations degrade LPR more than beta-axis at equivalent angles

---

## Keywords (1-7)

opportunistic sensing, license plate recognition, smart city cameras, oblique-view restoration, deep learning, recoverability boundary, urban surveillance infrastructure

---

## Abstract (target: 220 words, max 250)

**Draft:**

Fixed cameras deployed in smart cities for purposes other than traffic enforcement (ATM units, body-worn cameras, pole-mounted security sensors) frequently capture vehicles at severe oblique angles, making automated license plate recognition (LPR) unreliable. We term this scenario opportunistic sensing: extracting vehicle identity from sensors not designed or positioned for that task. Despite the proliferation of such sensors in urban environments, no prior work has quantified the fundamental recoverability limit — the maximum viewing angles at which a license plate number can still be reconstructed and read automatically.

We address this gap through a controlled synthetic benchmark spanning the full oblique-angle space. Clean license plate images are geometrically distorted across all integer rotation pairs (alpha, beta) in [0, 89]^2 degrees, with realistic camera artifacts applied, and paired with their clean originals. Five deep-learning restoration architectures are trained and compared: three discriminative (U-Net, angle-conditioned U-Net, Restormer) and two generative (Pix2Pix GAN, diffusion SR3). All models are evaluated on a shared full-angle grid using a plate-level OCR accuracy threshold of 90%.

We introduce two complementary metrics: boundary-AUC, measuring the fraction of the angle grid where recovery succeeds, and a reliability score F, measuring the depth and frequency of failures within that region. Our results show that approximately 93.4% of the full angle grid is recoverable. Recovery fails beyond approximately 80 degrees in both axes simultaneously, with alpha rotations consistently harder to reconstruct than beta rotations. Discriminative architectures outperform generative ones in accuracy, training efficiency, and stability, with PSNR serving as a reliable OCR proxy (R2 = 0.99) during model development.

---

## Paper Structure and Section Plan

### 1. Introduction (target: ~900 words)

**Narrative arc:**
Smart cities are densely instrumented with cameras deployed for purposes far beyond traffic management. ATM cameras, body-worn law enforcement cameras, doorbell cameras, retail security sensors, and streetlight-mounted units collectively form a vast, underutilized sensor network. When a vehicle of interest passes within view of any of these cameras, the captured image may be the only available record. Yet these cameras were positioned without any consideration of license plate readability: the vehicle may appear at steep angles, with the plate partially foreshortened, noisy, and blurred.

**Key points to make:**
1. Scale of the smart city sensor problem: hundreds of millions of fixed cameras globally; LPR is one of the highest-value secondary applications.
2. The "opportunistic sensing" concept: a sensor is opportunistically useful for a task it was not designed for. This is established in mobile and IoT sensing literature but rarely applied to urban camera infrastructure for LPR.
3. The specific technical problem: oblique-angle capture causes geometric distortion (foreshortening, perspective skew) and amplifies noise. Standard LPR systems assume near-frontal, controlled angles and fail on these inputs.
4. The gap: no prior work characterizes *at what angles* recovery is still possible. Practitioners do not know whether investing in software restoration pipelines will work for their deployed sensor geometry.
5. Our contribution: we provide that characterization through a systematic benchmark and introduce a recoverability boundary framework that is directly actionable for urban planners and system integrators.

**Contributions box (4 items):**
1. A synthetic benchmark with low-dispersion Sobol-sampled angles and realistic camera artifact simulation, spanning the full oblique-angle space.
2. A head-to-head comparison of five restoration architectures (three discriminative, two generative) evaluated on a common full-angle grid.
3. Two novel evaluation metrics: boundary-AUC (coverage extent) and reliability-F (interior failure depth), together forming the first recoverability characterization for opportunistic LPR.
4. Practical limits: 93.4% of angle space is recoverable; beyond ~80 degrees in both axes, no current architecture succeeds; alpha rotations are harder; PSNR is a reliable training proxy (R2 = 0.99).

---

### 2. Related Work (target: ~900 words)

#### 2.1 Opportunistic and Repurposed Sensing in Urban Environments

Position our work relative to the broader opportunistic sensing literature:
- Opportunistic sensing in mobile computing: using smartphone sensors for unintended tasks (activity recognition from accelerometers, ambient audio for place recognition).
- Urban sensing literature: repurposing traffic loop detectors, parking sensors, utility meters for secondary analytics.
- The specific gap: fixed camera repurposing for vehicle identity extraction has not been systematically characterized for oblique geometries.
- Key contrast: most urban camera repurposing work assumes near-frontal vehicle capture or uses PTZ cameras that can reposition. We address the more common fixed-sensor case.

#### 2.2 License Plate Recognition Systems and Their Assumptions

- Survey-level positioning: LPR is mature for controlled conditions (Shashirangana et al., 2020; Anagnostopoulos et al., 2008).
- The controlled-camera assumption: most LPR literature requires alpha < 30 degrees and beta < 30 degrees.
- Existing oblique LPR approaches: detection-then-deskew pipelines exist but do not characterize the recovery limit; they assume the plate is still roughly readable before processing.
- Our distinction: we address the regime where the plate is *not* readable without deep restoration, and we ask how far into that regime restoration can reach.

#### 2.3 Deep Learning for Image Restoration Under Geometric Degradation

- U-Net and encoder-decoder architectures for image-to-image translation (Ronneberger et al., 2015).
- Transformer-based restoration: Restormer (Zamir et al., 2022) and related Uformer/SUNet approaches.
- GAN-based restoration: Pix2Pix (Isola et al., 2017) for paired image translation.
- Diffusion models for image restoration: SR3 (Saharia et al., 2022); velocity prediction for low-SNR regions (Salimans & Ho, 2022).
- Gap: these models have been benchmarked on natural image degradations (noise, blur, rain) but not on the systematic oblique-angle regime relevant to urban sensing.

#### 2.4 Low-Discrepancy Sampling for Synthetic Benchmark Design

- Monte Carlo vs. quasi-Monte Carlo: Sobol sequences provide better coverage of high-dimensional spaces with fewer samples (Burhenne et al., 2011).
- Importance for benchmark validity: uniform coverage of the angle space ensures evaluation conclusions generalize across the full operating range of a deployed sensor.
- Parametric PDF design: flexible emphasis on extreme angles allows dataset difficulty tuning.

#### 2.5 Evaluation Frameworks for Recognition Under Degradation

- PSNR and SSIM as standard image quality proxies: widely used but critiqued for not predicting downstream task performance.
- OCR accuracy as the ground-truth evaluation signal for LPR.
- Area-under-curve approaches for characterizing performance across a parameter space: related to ROC analysis but applied spatially over angle pairs.
- Gap: no prior work defines a recoverability boundary in the (alpha, beta) space or measures interior failure reliability.

---

### 3. Problem Formulation (target: ~400 words)

Formal setup — written accessibly for CEUS audience:

- Define the opportunistic LPR scenario: a camera at fixed position p observes a vehicle whose license plate undergoes rotation (alpha, beta) relative to the camera optical axis.
- Define the forward model: 3D rotation + perspective projection to 2D + additive sensor degradation (blur, noise, compression). Result: distorted image x_d from clean image x_0.
- Define the restoration goal: find model f such that f(x_d) approximates x_0 sufficiently for OCR to succeed.
- Define the recoverability function: r(alpha, beta) = 1 if plate-level OCR accuracy >= T (e.g., T = 0.9), 0 otherwise.
- Define the recoverability boundary B_T and the boundary-AUC metric.
- State the research question formally: what is the shape of B_T and its AUC for current deep-learning restoration models?

---

### 4. Methodology (target: ~1,800 words)

#### 4.1 Synthetic Dataset Construction

- Plate generation: random 6-digit strings on yellow background, standard Israeli plate font and dimensions, 256x64 pixels output.
- 3D rotation model: homogeneous coordinates, rotation matrices R(alpha) and R(beta), perspective projection to 2D plane.
- Distortion pipeline (in order): geometric warp -> edge blending with soft mask (SDF + logistic smoothing) -> color jitter -> Gaussian blur -> JPEG compression -> de-warp -> downscale.
- Angle sampling: Scrambled Sobol sequences mapped through a parametric PDF over [-90, 90]^2. Two PDF variants: moderate (Datasets A, B) and strong emphasis on extreme angles (Dataset C).
- Three datasets: A (10,240 pairs), B (20,480 pairs), C (10,240 pairs). 80/10/10 split.
- Why synthetic: enables ground truth at every angle pair; no ethical issues with real plate data; full control over the angle distribution.

#### 4.2 Restoration Architectures

Brief (2-3 sentences each), table summary for quick comparison:

| Model | Type | Key feature | Loss |
|---|---|---|---|
| U-Net | Discriminative | Skip connections, encoder-decoder | L1 + SSIM |
| U-Net Conditional | Discriminative | FiLM layers conditioned on (alpha, beta) | L1 + SSIM |
| Restormer | Discriminative | Multi-Dconv head transposed attention | L1 |
| GAN Pix2Pix | Generative | Patch discriminator, adversarial + L1 | Adversarial + L1 |
| Diffusion SR3 | Generative | DDPM with velocity prediction, DDIM inference | Velocity MSE |

#### 4.3 Training Protocol

- Hardware: NVIDIA RTX 3090.
- Optimizer: Adam/AdamW with learning rate schedules per model.
- Validation: PSNR and SSIM on validation split, best checkpoint saved.
- Diffusion: velocity prediction target to stabilize low-SNR regions; DDIM with 10-20 steps at inference.
- Hyperparameter tuning: see Appendix A (tuning tables).

#### 4.4 Full-Grid Evaluation Design

- Grid: all integer (alpha, beta) pairs in [0, 89]^2 = 8,100 angle pairs.
- Sampling density: 2 images per pair for alpha <= 60 AND beta <= 60; 10 images per pair otherwise.
- OCR pipeline: Tesseract v4 LSTM, digits-only filter, multi-strategy fallback thresholding.
- Metrics per pair: plate-level OCR, digit-level OCR, plate-level PSNR, plate-level SSIM, worst-case digit PSNR, worst-case digit SSIM.

#### 4.5 Recoverability Metrics

Present the boundary-AUC and reliability-F formulas with KaTeX math (in the HTML paper).

---

### 5. Results (target: ~1,400 words)

#### 5.1 Training Performance

- Table: PSNR, SSIM, normalized training time, latency per model per dataset.
- Key takeaway: Restormer best accuracy; Diffusion-SR3 worst by large margin; U-Net Conditional best efficiency-accuracy tradeoff.

#### 5.2 Full-Grid Recoverability Heatmaps

- Present OCR heatmaps for Dataset B (all 5 models).
- Describe spatial patterns: near-perfect below 70-75 deg; failure above 80 deg in both axes; asymmetry between alpha and beta axes.

#### 5.3 Recoverability Boundaries and Maximal Boundary

- Overlay plot of all 15 model-dataset boundaries.
- Maximal (union) boundary: AUC = 0.934.
- Interpretation for urban practitioners: 93.4% of fixed-camera angle space is serviceable for opportunistic LPR.

#### 5.4 Recoverability-Reliability Tradeoff

- Table: AUC and F per model per dataset.
- Scatter plot: AUC vs F.
- Discriminative cluster: AUC 0.915-0.924, F 0.095-0.209.
- Generative: AUC 0.886-0.913, F 0.100-1.124.
- Diffusion-SR3's dataset sensitivity: F = 0.10 on B vs. 1.124 on C.

#### 5.5 High-Angle Region Analysis

- Bar plots: mean PSNR, SSIM, OCR in the region {alpha >= 80 OR beta >= 80}.
- Restormer: ~40 dB, ~0.97 SSIM, ~0.67 OCR — stable across datasets.
- Diffusion-SR3: ~30 dB, ~0.92 SSIM, ~0.55 OCR — no improvement with dataset choice.

#### 5.6 Metric Proxy Validity

- PSNR-OCR: Restormer R2 = 0.991, slope 3%/dB. Diffusion-SR3 R2 = 0.979, slope 4%/dB.
- SSIM-OCR: R2 = 0.74-0.78; threshold-like at SSIM = 0.92; high variance in transition zone.
- Implication: PSNR is the reliable training signal for opportunistic LPR development.

---

### 6. Discussion (target: ~900 words)

#### 6.1 Implications for Smart City Sensor Deployment

- The 93.4% recoverable region translates directly to camera placement guidelines: if the worst-case angle for a fixed sensor is bounded by alpha < 80 AND beta < 80, software restoration alone is sufficient for LPR — no hardware upgrade needed.
- Urban planners can use the recoverability boundary as a coverage map: given a known camera mounting angle and typical vehicle trajectories, the boundary determines whether LPR is viable.
- The alpha > beta asymmetry in difficulty: cameras mounted high on poles (large alpha) are harder to recover from than cameras offset laterally (large beta). This suggests vertical mounting height is a more critical variable than horizontal offset when positioning sensors for opportunistic LPR.

#### 6.2 Architecture Choice for Urban Deployment

- Discriminative models are the practical choice: easier to validate, more stable, lower latency.
- U-Net Conditional (7.5ms latency) offers near-Restormer accuracy at 1/15 the training cost: the best candidate for real deployment.
- Generative models hallucinate plausible but incorrect plates when signal is too weak: dangerous for law enforcement applications where a false plate reading has serious consequences.

#### 6.3 Data Distribution vs. Data Volume

- Doubling sample size (A to B) yields AUC gain < 0.01: once coverage of the angle space is adequate, more data does not meaningfully extend the recoverability boundary.
- The angle sampling PDF matters more: Dataset C's stronger emphasis on extreme angles shifts model behavior at the boundary.
- Implication for practitioners building datasets: invest in angle diversity, not volume.

#### 6.4 Limitations and Boundary Conditions

- Synthetic only: constant focal length, constant camera-plate distance, uniform plate font. Real-world sensors add viewpoint-dependent scale variation, varying illumination, plate occlusion.
- Fixed plate size: does not simulate the scale reduction seen when vehicles are far from the camera.
- Binary success/failure OCR threshold: real use cases may accept partial plate reads (e.g., 4-of-6 digits match).

---

### 7. Conclusion (target: ~300 words)

- Restate the opportunistic sensing framing: smart city infrastructure can serve LPR without new hardware across 93.4% of the oblique angle space.
- Restate the hard limit: beyond ~80 degrees in both axes, residual signal is too weak for any current architecture.
- Restate the practical recommendations: discriminative architectures for deployment; PSNR as training proxy; camera height more critical than horizontal offset.
- Future work: real sensor data validation; variable distance and scale; domain adaptation from synthetic to real.

---

## Literature to Acquire and Cite

### Opportunistic Sensing (Urban/IoT context)
- Campbell et al. (2008) "The Rise of People-Centric Sensing" — foundational opportunistic sensing paper.
- Ganti et al. (2011) "Mobile Crowdsensing: Current State and Future Challenges" — IEEE Communications.
- Ratti et al. — urban sensing with existing infrastructure.
- Batty (2013) "The New Science of Cities" — smart city sensor proliferation.
- Kitchin (2014) "The Real-Time City? Big Data and Smart Urbanism" — GeoJournal.

### Smart City Camera Infrastructure and LPR
- Shashirangana et al. (2020) "Automated License Plate Recognition: A Survey" — already in report.
- Anagnostopoulos et al. (2008) "License Plate Recognition from Still Images and Video Sequences" — already in report.
- Studies on oblique-angle LPR in deployed CCTV systems.

### Deep Learning Restoration
- Ronneberger et al. (2015) U-Net — already in report.
- Zamir et al. (2022) Restormer — already in report.
- Isola et al. (2017) "Image-to-Image Translation with Conditional Adversarial Networks" (Pix2Pix).
- Ho et al. (2020) DDPM — already in report.
- Salimans & Ho (2022) "Progressive Distillation for Fast Sampling of Diffusion Models" (velocity prediction).
- Song et al. (2020) DDIM.

### Sampling and Benchmark Design
- Burhenne et al. (2011) Sobol sequences — already in report.
- Joe & Kuo (2008) "Constructing Sobol Sequences with Better Two-Dimensional Projections."

### Urban Geospatial / CEUS-compatible framing references
- Goodchild (2007) "Citizens as Sensors: The World of Volunteered Geographic Information" — GeoJournal.
- Townsend (2013) "Smart Cities: Big Data, Civic Hackers, and the Quest for a New Utopia."

---

## Writing Guidelines for This Paper

### Voice and Audience
- Primary reader: urban systems researcher or smart city planner, not a computer vision specialist.
- Explain deep learning concepts in 1-2 sentences before using them; do not assume familiarity with PSNR/SSIM.
- Lead every section with the urban systems implication, then the technical detail.
- All figures must be self-contained with thorough captions.

### CEUS-Specific Framing Rules
- The word "urban" must appear in every major section's opening paragraph.
- Quantify practical implications: e.g., "a camera mounted at 75 degrees elevation would remain in the recoverable region."
- Connect to policy: what does a city infrastructure manager do with this finding?

### Math
- Use KaTeX in HTML version. Every equation must be numbered.
- Equations: 3D rotation model, distortion pipeline, boundary-AUC, reliability-F, recoverability boundary definition, PSNR formula, R2 formula.

### Figures to Include (from report/figures/)
1. figure_03 — concept illustration (oblique LPR)
2. figure_13 — methodology flowchart
3. figure_16 — 3D rotation and projection diagram
4. figure_06 or figure_41 — maximal recoverability boundary
5. figure_39 — OCR heatmaps Dataset B
6. figure_40 or figure_05 — recoverability-reliability scatter
7. figure_35 — efficiency comparison
8. figure_43 or figure_44 — PSNR vs OCR scatter

Target: 7-8 figures total (CEUS norm for this length paper).

---

## Estimated Word Budget

| Section | Target words |
|---|---|
| Abstract | 220 |
| Introduction | 900 |
| Related Work | 900 |
| Problem Formulation | 400 |
| Methodology | 1,800 |
| Results | 1,400 |
| Discussion | 900 |
| Conclusion | 300 |
| References | ~400 (not counted in body) |
| **Total body** | **6,820** |
| Margin for captions, tables | ~600 |
| **Grand total** | **~7,400** |

This keeps us safely under the 8,000-word limit while leaving room for revisions.

---

## Next Steps

1. Write HTML paper skeleton with KaTeX math engine, CEUS-style CSS.
2. Draft Introduction and Problem Formulation first (set the urban framing).
3. Draft Related Work (need to find and cite opportunistic sensing papers).
4. Port Methodology from the FYP report, rewriting for CEUS audience.
5. Port Results tables and figures, adding urban-systems interpretation.
6. Write Discussion and Conclusion with policy angle.
7. Final APA 7th Edition reference list.
