# Reviewer Report, Round 2

**Manuscript:** Mapping License Plate Recoverability Under Extreme Viewing Angles for Opportunistic Urban Sensing
**Venues considered:** MDPI *AI* (primary), *Computers, Environment and Urban Systems* (CEUS, secondary).

---

## 1. Headline verdict

- **MDPI *AI*:** Minor revision; the methodology-first reframe plus the adapted (rather than novel) metric framing now fit the journal's scope, but the absence of multi-seed statistics and any real-data anchor still blocks a clean accept.
- **CEUS:** Major revision (borderline reject); the urban-sensing wrapper is more substantive than round 1 but is still rhetorical rather than modelled, and without a sensor-geometry overlay on the recoverability map the paper remains a CV benchmark dressed in smart-city language.

## 2. What improved since round 1

The paper is materially stronger than the CEUS round-1 submission. The title and abstract (lines 342-380) now foreground *recoverability maps* as a task-agnostic methodology with LPR as a showcase, matching the repositioning requested in round 1 weakness #3 and #5. The Contributions paragraph (lines 451-465) explicitly adapts boundary-AUC from Martin et al.'s DET-curve literature, softening the "novel metric" overclaim. The dataset inconsistency (old round 1 weakness #2: three datasets in the experiment log vs. two in the paper) is resolved: Section 4.1 and Table 1 now consistently describe DS-S and DS-E, and Section 6.3 no longer references a 20,000-sample dataset. A Notation block (lines 613-631) disambiguates the overloaded $\beta$ symbol between viewing angle and diffusion schedule. The task-agnostic framing paragraph before Eq. 2 (lines 665-671) makes the generalisation beyond LPR concrete. Section 5.2 no longer references dropped heatmaps. Fig. 8's caption (lines 1220-1231) now names the three angle regimes. Table 4 bolding is internally consistent. The related-work section added Laroca (both), Silva-Jung WPOD-NET, Xu perspective rectification, Zou, Hamdi, Zhang camera calibration, and Frome Street View privacy, and the bibliography now carries 36 entries. End-matter (Author Contributions through Conflicts, lines 1405-1454) is present. Limitations (Section 6.4) now state the 93.4% figure is benchmark-bounded.

## 3. Top 10 remaining improvements (priority order)

1. **No statistical uncertainty on any headline number.** *(Both, high impact.)* Tables 3 and 4 are single-run point estimates; the Restormer-vs-U-Net AUC gap on DS-S is 0.005, well inside typical seed variance. Section 7 (line 1401) now acknowledges this as future work, but MDPI *AI* and CEUS reviewers in 2026 will not accept architecture-ranking claims without at least bootstrap CIs over the 8,100-pair grid (cheap, no retraining needed) and ideally 3-seed retraining for the top three models. Add 95% CIs to Table 4 and a significance statement next to the $\Delta < 0.002$ claim (line 1267).

2. **No real-data sanity check.** *(CEUS high, AI medium.)* Section 6.4 (lines 1340-1358) continues to flag synthetic-only as a limitation without doing anything about it. Running the best discriminative checkpoint, zero-shot, on a public oblique dataset (UFPR-ALPR, RodoSol-ALPR, or CCPD-Tilt) and reporting whether recoverable angle pairs remain recoverable would convert the 93.4% figure from a benchmark artefact into something transferable. Even a single figure showing "synthetic boundary vs. CCPD-Tilt boundary overlay" would materially change the CEUS verdict.

3. **Urban-sensing framing is still rhetorical rather than quantitative.** *(CEUS high.)* Section 6.3 (lines 1293-1337) names ATMs, body-worn, and streetlight cameras but never assigns a plausible $(\alpha, \beta)$ distribution to any of them. The round-1 report asked for exactly this overlay. Add a small table in Section 6.3 mapping each sensor class to a nominal mount-geometry prior (citing, e.g., dashcam mount-height surveys, pole-CCTV deployment manuals) and compute the expected fraction of recoverable captures per class. Without this, the "quantitative planning guideline" claim on line 1295 is unsupported.

4. **OCR choice remains load-bearing and weak.** *(AI high, CEUS high.)* Tesseract v4 is acknowledged as a limitation (lines 1354-1358) but the R^2 = 0.99 PSNR-OCR claim, the 93.4% figure, and the discriminative-vs-generative ranking all depend on it. For MDPI *AI* specifically, running PaddleOCR or a CRNN on one model-dataset cell and reporting how AUC shifts would quiet the most predictable reviewer complaint. Current text only *promises* that "the relative ranking of architectures is expected to remain stable", which is an assertion, not a finding.

5. **Reproducibility artefacts are still deferred.** *(AI high, CEUS high.)* Code Availability (lines 1442-1449) says "will be released upon acceptance". Both venues now routinely require a code URL (anonymised if needed) at submission, and CEUS in particular will bounce this. Deposit an anonymous GitHub link with the generation pipeline, Sobol seeds, and one trained checkpoint before resubmission; cite the Zenodo DOI in Data Availability.

6. **Boundary-AUC definition still reduces to a 1-D quantity.** *(AI medium.)* Eq. 5 (line 707) averages two marginal envelopes and divides by $89^2$. If the recoverable region is non-convex (an interior hole), this formula does not penalise it; $F$ is meant to, but the two metrics are defined on different axes (enclosed area vs. distance). Add one sentence between Eqs. 5 and 7 explaining what AUC does and does not capture, and reference erosion/opening measures from mathematical morphology as the conceptual ancestor of $F$. This costs one sentence and closes round-1 weakness #3 cleanly.

7. **Eq. 3 edge case handling is still ambiguous.** *(AI low, technical.)* Lines 687-689 say the convention is $\max\varnothing = -1$, but Eq. 3 itself writes $\max(\{0\} \cup \{\beta : r_T = 1\})$, which returns 0 on an empty recoverable slice, collapsing "boundary at zero" with "never recoverable". The prose and the formula disagree. Either change the formula to $\max(\{-1\} \cup \dots)$ or drop the prose sentence. Round-1 weakness addressed but not cleanly.

8. **$\alpha/\beta$ asymmetry claim is pipeline-specific but stated as physical.** *(Both, medium.)* Abstract lines 374-376 and Conclusion lines 1375-1378 present "lateral rotations are consistently harder than elevational ones" as a structural finding. It is, within this homography + fixed-focal-length + fixed-distance setting, but the same plate under a rolling-shutter dashcam with motion blur along the direction of travel would likely show the opposite asymmetry. Qualify with a phrase such as "under the fixed-distance central-projection model used here" on first mention in the Abstract.

9. **Fig. 5 and Section 5.3 do not show the central visual.** *(AI medium, reader-facing.)* The paper promises a "maximal recoverability boundary" (lines 1076-1088) but the only figure of boundaries themselves was removed (HTML comment at line 1092: "removed Fig 6 recoverability boundary schematic"). Readers have to parse Table 4 to reconstruct what the paper is fundamentally about. Add a single 2-panel figure (DS-S / DS-E) showing the $r_T = 1$ region per model as a thin contour, and the pooled boundary as a thick one. This is the paper's one pictorial argument and it is currently missing.

10. **Some residual overclaims about deployment.** *(CEUS high.)* Line 1297 says "software restoration pipeline is capable of recovering legible plates without hardware modification" for the majority of ATM/body-worn/streetlight geometries; this is an inference from the synthetic envelope, not a deployment-validated result, and it restates (in softened form) the line that drew round-1 CEUS weakness #5. Reword to "software restoration pipelines appear capable, under the assumptions of this benchmark, of covering..." and add one sentence restating that this conjecture requires the real-data validation of item 2.

## 4. Acceptance probability (current state)

| Venue | Estimated accept probability | Dominant blocker |
|---|---|---|
| MDPI *AI* | ~45% | Single-seed results; OCR-choice sensitivity |
| MDPI *Applied Sciences* | ~60% | Looser methodology bar; same single-seed concern but smaller weight |
| EAAI (Engineering Applications of AI) | ~35% | Reviewers expect either a novel architecture or a real-data application; paper now offers a framework but no real-data anchor |
| CEUS | ~15% | Still reads as CV benchmark; urban-sensor overlay not quantitative; missing real-data sanity check; artefacts deferred |

## 5. Net effect if all 10 improvements are applied

Executing items 1, 2, 3, 5, and 10 (the five highest-leverage items) is sufficient to move the paper into clear accept territory at MDPI *AI* (~75-80%) and MDPI *Applied Sciences* (~85%), and raises CEUS to a plausible major-revision-to-accept trajectory (~45-55%). EAAI would move to ~55-60%. The remaining items (6, 7, 8, 9) are polish that each adds a few percentage points and, collectively, remove the most reviewer-friction-inducing passages without new experiments. The critical path is items 1, 2, 5: multi-seed CIs, one real-data overlay figure, and an anonymous code repository. If only one thing is done before resubmission, it should be item 2, because it unblocks both the CEUS urban-sensing story and the AI generalisation question simultaneously.
