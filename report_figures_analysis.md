# Figure-by-figure analysis of the student report

Source file: `Final Year Project Report_last.docx` (Aug 17 2025, 7.1 MB).
All 60 embedded images were extracted from `word/media/` and cross-referenced with the captions in `word/document.xml`. Images are grouped by role rather than by numeric order, with the caption used in the report and a short note on content and suitability for the CEUS version.

## 1. Front matter / branding

| File | Caption | Content | CEUS reuse |
|---|---|---|---|
| image1.png | (none) | AFEKA College logo | No — institutional branding, not part of the scientific content. |

## 2. Executive-summary figures (Chapter 2)

These are the four figures the student uses up front to announce the contribution. They are the strongest candidates for the paper's teaser figures and abstract graphic.

| File | Caption | Content | CEUS reuse |
|---|---|---|---|
| image2.png | Fig 2.1 — LPR for Oblique Camera Capture: Concept Illustration | Cartoon car with a sharp yellow plate "478501" and an inset showing the same plate heavily motion-blurred/rotated, labelling the problem. | **Keep as opening/"graphical abstract"** — it is the clearest one-glance statement of the reframing (non-LPR camera sees a severely projected plate). Consider relabelling the inset as "body-cam / ATM-cam view" to align with the opportunistic-sensing framing. |
| image3.png | Fig 2.2 — Synthetic license plate generation process | Three side-by-side tiles: clean plate "341672", a warped-and-occluded version, and the dewarped/blurred version. | **Keep** as the forward-model teaser. Small: move under the Data section. |
| image4.png | Fig 2.3 — Recoverability–Reliability Plot (AUC vs F) for all models and datasets | Scatter of Boundary-AUC (x) vs RMS hole-distance F (y) with colour = dataset (A/B/C) and marker = model; diffusion_sr3 is the single clear outlier at F ≈ 0.57–1.12°. | **Keep** — this is the best single summary of all five models × three datasets. Goes in Results. |
| image5.png | Fig 2.4 — Maximal recoverability boundary | The envelope formed by taking the pointwise max over all 5 models (AUC = 0.934). Shows the "knee" near α≈80° / β≈80°. | **Keep** — headline figure for the "angular recoverability envelope" primitive. |

## 3. Motivation / context (Chapter 5)

| File | Caption | Content | CEUS reuse |
|---|---|---|---|
| image6.jpeg | Fig 5.1 — Controlled environment LPR example | Parking-lot photo of a dark sedan, plate CB3652 with a bounding-box crop shown alongside. | **Drop or merge** — stock photo, watermark/source unclear; safer to replace with a figure we own. |
| image7.jpeg | Fig 5.1 — (same caption, reused) | Parking-lot photo of a grey BMW, plate BY 299 RG, with two callouts: a blurred far-away view and a sharp close-up. | **Keep at most one** of these two photos — this one is a cleaner illustration of the "non-LPR camera" failure mode than image6, but licensing must be verified before resubmission. Safer to redraw. |

## 4. Method background art (Chapter 5 — textbook figures)

These are reproductions of well-known architectures from prior work. For a journal submission they must either be redrawn in our own style or omitted (most can be cited in prose).

| File | Caption | Content | CEUS reuse |
|---|---|---|---|
| image8.png | Fig 5.4 — U-Net architecture | Classic Ronneberger U-Net diagram (572×572 input, skip connections). | **Drop** — redraw or cite (Ronneberger et al. 2015). Not our contribution. |
| image9.jpeg | Fig 5.5 — GANs conceptual overview | Generic GAN cartoon with MNIST digits, generator/discriminator trapezoids. | **Drop** — textbook figure. |
| image10.png | Fig 5.6 — Forward process illustration | Diffusion forward chain q(xₜ\|xₜ₋₁) noising a face image. | **Drop** — textbook figure; clearly reproduced from Ho et al. 2020 / Saharia et al. |
| image11.png | Fig 5.7 — Reverse process illustration | Reverse diffusion chain recovering the face. | **Drop** — same as above. |

## 5. Methodology — overview flowchart (Chapter 8)

| File | Caption | Content | CEUS reuse |
|---|---|---|---|
| image12.png | Fig 8.1 — Methodology Flowchart Diagram | Vertical pipeline: Prepare Data → Warp/Noise/Dewarp → Implement Models → Evaluate → Compare → Conclusions. | **Keep, redrawn** — this is a useful schematic but visually generic. Replace with a cleaner SVG in the paper's "System overview" section. |

## 6. Methodology — synthetic LP pipeline (Chapter 8.2–8.4)

These illustrate the image-formation model and are all original to the project.

| File | Caption | Content | CEUS reuse |
|---|---|---|---|
| image13.png | Fig 8.2 — Generated license plate on a black canvas example | Clean synthetic plate "104332" centred on a black canvas. | **Keep** (combine with image14 and image16/image17/image18 into a single multi-panel "forward model" figure). |
| image14.png | Fig 8.3 — License plate with bounding boxes example | Same plate with per-digit red bounding boxes. | **Keep** — useful for the digit-level OCR evaluation. |
| image15.png | Fig 8.4 — Demonstration of 3D rotation and projection to the 2D plane | Matplotlib 3D axes showing the original rectangle, rotated rectangle, focal length, viewpoint and projected quadrilateral. | **Keep if redrawn cleanly** — explains the (α, β) viewing geometry. Current render is a bit cluttered; a cleaner 2D diagram would communicate the same idea for the paper. |
| image16.png | Fig 8.5 — Warped License plate example (alpha: 80, beta: 20) | The yellow plate after perspective warp; most of the canvas is black. | Combine into the forward-model strip. |
| image17.png | Fig 8.6 — Warped License plate with noise example | Same plate after Gaussian blur + JPEG compression on a grey background. | Combine into the forward-model strip. |
| image18.jpeg | Fig 8.7 — Realigned License Plate Example | The dewarped plate in the canonical 1:3 crop, highly degraded. | **Keep** — shows the network's actual input (post-dewarp). |

## 7. Methodology — sampling machinery (Chapter 8.5)

This is the most technically distinctive part of the thesis and will be important when editors ask "why don't you just grid-sample?". Tight visual story here helps.

| File | Caption | Content | CEUS reuse |
|---|---|---|---|
| image19.png | Fig 8.8 — Hard mask | 2D heatmap over (α, β) ∈ [0°, 90°]² showing the binary admissible region (inside l_max/u_max bounds). | **Keep one of {hard mask, smoothed PDF}** — image21 (logistic smoothing) or image23 (sampling PDF) is more informative. |
| image20.png | Fig 8.8 — Hard mask (duplicate) | Same as image19, reinserted later in the chapter. | Drop the duplicate. |
| image21.png | Fig 8.10 — Logistic smoothing | Heatmap of the logistic smoothing weights with the hard-mask contour overlaid. | **Keep** — best single visualisation of the density trick. |
| image22.png | Fig 8.10 — Logistic smoothing (duplicate) | Same content. | Drop the duplicate. |
| image23.png | Fig 8.12 — Sampling PDF | Full final PDF with k_suppression = 25 — density concentrates near the knee. | **Keep** — shows where samples are spent. |
| image24.png | Fig 8.13 — Uniform vs Sobol comparison | Two scatter panels (N=2048) over the admissible region. | **Keep** — this is the argument for quasi-MC. |
| image25.png | Fig 8.14 — Scrambled Sobol triples example | 3D scatter of (u₀, u₁, u₂) triples. | Optional — more pedagogical than evidentiary; can go in supplementary. |
| image26.png | Fig 8.15 — Projected Sobol triples onto (u₀, u₁) | 2D projection of the same triples. | Optional — same as image25. |
| image27.png | Fig 8.16 — Sobol samples over [−90,90]² | Small thumbnail showing the full symmetric range. | Low-resolution; drop or re-render. |
| image28.png | Fig 8.17 — Sobol samples for A and C datasets | Two scatter panels comparing Dataset A's and Dataset C's sample masks. | **Keep** — best evidence for "Dataset C has wider high-angle coverage." |

## 8. Methodology — model architectures & scoring (Chapter 8.6–8.8)

| File | Caption | Content | CEUS reuse |
|---|---|---|---|
| image29.png | Fig 8.18 — Architecture of Restormer | Dense block-level diagram of Restormer (MDTA, GDFN, encoder/decoder). | **Drop** — reproduced from Zamir et al. 2022; cite instead and keep only if we can redraw. |
| image30.png | Fig 8.19 — Discriminator's predictions | Classic Pix2Pix shoe-sketch illustration (G, D, fake/real). | **Drop** — textbook figure from Isola et al. 2017. |
| image31.png | Fig 8.20 — Boundary-AUC measure illustration | Two panels: T=0 (trivial AUC = 1.0) vs T=90% (AUC = 0.920) with the boundary drawn in red. | **Keep** — this is the single most useful figure for defining Boundary-AUC; put it in the conceptual-framing section. |

## 9. Results — aggregate performance (Chapter 9.1–9.3)

| File | Caption | Content | CEUS reuse |
|---|---|---|---|
| image32.png | Fig 9.1 — Models Performance on Dataset A | Two bar plots: PSNR (dB) and SSIM, five models on Dataset A. | **Merge into one 3-panel figure** (A/B/C) instead of three separate figures — cleaner and saves space. |
| image33.png | Fig 9.2 — Model Performance on Dataset B | Same design, Dataset B. | Merge as above. |
| image34.png | Fig 9.3 — Model Performance on Dataset C | Same design, Dataset C. | Merge as above. |
| image35.png | Fig 9.4 — Efficiency | Normalized training time and inference latency bar charts per model. | **Keep** — directly answers the "is diffusion worth it?" question: Restormer is 14.8× slower to train, diffusion_sr3 is 22 ms/image at inference vs 7–12 ms for the others. |

## 10. Results — qualitative reconstructions (Chapter 9.4)

| File | Caption | Content | CEUS reuse |
|---|---|---|---|
| image36.png | Fig 9.5 — Reconstructions per model (α=85, β=65) | Seven stacked panels: distorted input, ground truth "091984", then each of five models' reconstructions. unet_base mis-reads "491984", conditional "391984", restormer "691984", pix2pix "091984" ✓, diffusion_sr3 "691984". | **Keep one representative panel** — combine with 37 and 38 into a 3-column figure (one example per increasing difficulty). |
| image37.png | Fig 9.5 — Reconstructions (another example) | Same layout, different (α, β). | Merge. |
| image38.png | Fig 9.5 — Reconstructions (another example) | Same layout, another (α, β). | Merge. |

## 11. Results — angular envelope & OCR (Chapter 9.5–9.6)

| File | Caption | Content | CEUS reuse |
|---|---|---|---|
| image39.png | Fig 9.6 — Model-specific plate-level OCR accuracy on Dataset B | 2×3 grid of plate-pass-rate heatmaps (Restormer on top, then the other four in a 2×2 arrangement). Yellow = recoverable, purple = not. Shows the characteristic L-shaped envelope with a sharp drop past α≈80°. | **Keep — make this the hero figure** of the Results section. It is the single strongest argument of the thesis and maps directly onto the envelope framing. |
| image40.png | Fig 9.7 — Recoverability boundaries for all models and datasets | All 15 (5 models × 3 datasets) boundary curves overlaid; legend lists per-curve AUC values (0.886–0.924). | **Keep** — supports the "different architectures, same envelope" point. Consider splitting into three small subpanels (one per dataset) for readability. |
| image41.png | Fig 9.9 — Recoverability–Reliability (AUC vs F) | Same content as image4 (Fig 2.3) but appears in the results chapter. | Drop the duplicate; cite back to the executive-summary version. |
| image42.png | Fig 9.10 — Mean Performance in High-Angle Region (α ≥ 80° or β ≥ 80°) | 2×3 grid: PSNR / SSIM / OCR-plate (row 1) and PSNR-worst / SSIM-worst / OCR-digit (row 2), by model and dataset. | **Keep** — quantifies the practical cost of operating near the envelope. Numbers here (plate OCR in high-angle region drops to 0.54 for diffusion_sr3 vs 0.67 for the best CNNs) are the ones we'll cite in the abstract. |

## 12. Results — PSNR/SSIM ↔ OCR scaling (Chapter 9.7)

Note: the caption numbering in the docx is slightly off because the four figures are close together and my extractor took the nearest following caption. I report the actual image content below.

| File | Docx caption | Actual plot content | CEUS reuse |
|---|---|---|---|
| image43.png | Fig 9.11 Restormer OCR vs PSNR | OCR Plate Accuracy vs PSNR for **restormer (B)** — R² = 0.991. | **Keep one "best model" scatter.** Restormer is the strongest R², so this is a good candidate. |
| image44.png | Fig 9.12 Restormer OCR vs SSIM | Actually shows OCR vs PSNR for **diffusion_sr3 (B)** — R² = 0.979. | Use in Supplementary alongside 43. |
| image45.png | Fig 9.13 Diffusion-SR3 OCR vs PSNR | Actually shows OCR vs SSIM for **restormer (B)** — R² = 0.777. | Keep as the SSIM companion to image43. |
| image46.png | Fig 9.14 Diffusion-SR3 OCR vs SSIM | OCR vs SSIM for **diffusion_sr3 (B)** — R² = 0.739. | Supplementary. |

Caption/content mismatch above is a **defect in the original report** that should be fixed before resubmission. For the CEUS paper I recommend collapsing all four to a single 2×2 figure (rows = model, cols = {PSNR, SSIM}) with the R² values in the panel titles.

## 13. Appendix / operational artifacts (end-of-document)

The final 14 images (47–60) are not numbered figures — no captions are associated with them in the docx. They are operational artifacts from the project-management and supervisor-facing parts of the report.

| File | Content | CEUS reuse |
|---|---|---|
| image47.png | Full-project Gantt chart (MS Project) with all tasks and % completion. | **Drop** — PM artefact, irrelevant to a journal paper. |
| image48.png | AFEKA Electrical Engineering conference poster ("Generative AI Models for License Plate Restoration at Extreme Viewing Angles" — Igor Adamenko & Orpaz Ben Aharon, advisor Dr. Sasha Apartsin). Summarises background/objective/methods/results on a single panel. | **Drop from paper**, but **keep the source** — this is a useful starting point for the SI one-pager and for the eventual CEUS graphical abstract. |
| image49.png | MLflow UI screenshot — U-Net Optuna sweep, ~50 trials, val_loss/val_psnr/val_ssim columns. | **Drop** from main paper; optionally mention in Methods appendix as evidence of systematic hyperparameter tuning. |
| image50.png – image53.png | More MLflow screenshots, one per model (U-Net Conditional, Restormer, Pix2Pix, Diffusion-SR3 sweeps). | Same as above — drop or collapse to a single supplementary table of best hyperparameters. |
| image54.png | A thumbnail reprising the recoverability-boundary panels for Datasets A/B/C in one 3-panel view. | **Candidate for the final paper** — cleaner than image40 (all datasets overlaid). Re-render at higher resolution. |
| image55.png – image59.png | Per-model OCR-vs-PSNR scatter plots for the remaining (model × dataset) combinations that didn't make it into §9.7. | Candidates for Supplementary. |
| image60.png | OCR Plate Accuracy vs SSIM for **pix2pix (B)** — R² = 0.755. | Keep in Supplementary alongside 43–46 when building the full 5-model × 2-metric grid. |

## 14. Summary of recommendations

Proposed figure budget for the CEUS paper (Elsevier soft cap ≈ 8 figures in the main text; supplementary is unlimited):

**Main text (8 figures)**

1. Graphical abstract / teaser = image2 (Fig 2.1), relabelled to make "non-LPR camera" explicit.
2. Forward model strip = image13 + image14 + image16 + image17 + image18 merged into a 5-panel strip.
3. Sampling — image21 (logistic smoothing) + image28 (dataset-specific Sobol) as a 2-panel figure.
4. Boundary-AUC definition = image31 (Fig 8.20).
5. Per-dataset aggregate performance = image32–34 merged as a 3-subplot figure.
6. Efficiency = image35 (Fig 9.4).
7. Hero envelope figure = image39 (Fig 9.6) — plate-pass-rate heatmaps.
8. Headline scatter = image4 (Fig 2.3 / 9.9) — Boundary-AUC vs Reliability F.

**Supplementary**

- image5 (maximal envelope), image40/54 (per-dataset boundaries), image42 (high-angle bar grid), image36–38 (reconstruction examples), image43–46 + image55–60 (full OCR-vs-PSNR/SSIM grid), image49–53 (hyperparameter sweeps as a table), image25–27 (Sobol construction), image15 (3D projection diagram).

**Drop**

- image1 (logo), image6/image7 (stock photos, licensing), image8–image11 (textbook reproductions), image20/image22 (duplicates), image29/image30 (textbook architecture/Pix2Pix), image41 (duplicate of image4), image47/image48 (PM/poster artefacts).

## 15. Defects to fix before resubmission

- Figure 9.11–9.14 captions are **swapped with their contents**. The correct mapping is:
  - "Restormer vs PSNR" → image43 ✓, image44 is actually diffusion_sr3 vs PSNR.
  - "Diffusion vs PSNR" → image44 (label it 9.13), not image45.
  - "Restormer vs SSIM" → image45 (label it 9.12), not image44.
  - "Diffusion vs SSIM" → image46 ✓.
- image8–image11, image29, image30 reproduce third-party figures without visible attribution — a potential **desk-reject trigger** at Elsevier. Either redraw or remove.
- image6/image7 appear to be stock/automotive photos — licence must be confirmed before any external publication.
- image19/image20 and image21/image22 are duplicated; reduce to one each.
- image27 is too small to read; re-render.

All 60 original images remain available at `/sessions/affectionate-dazzling-noether/report_imgs/report_unzipped/word/media/` if we need to revisit any of them.
