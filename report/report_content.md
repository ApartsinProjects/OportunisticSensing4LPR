![](media/image1.png){width="3.1301202974628173in"
height="0.6458333333333334in"}

Department of Electrical Engineering

**Project Name:**

**Generative Image Models for Enhancing License Plate Images Captured at
Extreme Viewing Angles**

**Final Year Project Report**

**Student Name:** Igor Adamenko Orpaz Ben Aharon

**Supervisor\'s Name:** Dr. Sasha Apartsin

**Approved By: [ ]{dir="rtl"}** Dr. Sasha Apartsin

**Submission Date: []{dir="rtl"}**06/08/25

Mentor\'s Approval:

> ![](media/image2.png){width="6.758121172353456in"
> height="3.4672036307961505in"}

# Contents {#contents .TOC-Heading}

[2. Executive Summary [6](#executive-summary)](#executive-summary)

[3. Glossary [12](#glossary)](#glossary)

[4. Abstract [15](#abstract)](#abstract)

[5. Introduction [15](#introduction)](#introduction)

[6. Goals, Objectives, and Metrics
[17](#goals-objectives-and-metrics)](#goals-objectives-and-metrics)

[6.1. Goals [17](#goals)](#goals)

[6.2. Objectives [17](#objectives)](#objectives)

[6.3. Metrics [18](#metrics)](#metrics)

[7. Literature Review [19](#literature-review)](#literature-review)

[7.1. 3D Projective Geometry
[19](#d-projective-geometry)](#d-projective-geometry)

[7.2. Low Dispersion Sampling
[19](#low-dispersion-sampling)](#low-dispersion-sampling)

[7.3. LPR Systems [19](#lpr-systems)](#lpr-systems)

[7.4. Deep Learning-Based Restoration Approaches
[19](#deep-learning-based-restoration-approaches)](#deep-learning-based-restoration-approaches)

> [7.4.1. U-Net [19](#u-net)](#u-net)
>
> [7.4.2. GAN [19](#gan)](#gan)
>
> [7.4.3. Diffusion Models [20](#diffusion-models)](#diffusion-models)

[7.5. OCR [20](#ocr)](#ocr)

[8. Methods [21](#methods)](#methods)

[8.1. Block Diagram [21](#block-diagram)](#block-diagram)

[8.2. Phases Description [22](#phases-description)](#phases-description)

> [8.2.1. Data Preparation [22](#data-preparation)](#data-preparation)
>
> [8.2.2. Model Implementation
> [22](#model-implementation)](#model-implementation)
>
> [8.2.3. Model Evaluation [22](#model-evaluation)](#model-evaluation)
>
> [8.2.4. Model Comparison [22](#model-comparison)](#model-comparison)
>
> [8.2.5. Conclusion [22](#conclusion)](#conclusion)

[8.3. Detailed Description of Processing Steps
[23](#detailed-description-of-processing-steps)](#detailed-description-of-processing-steps)

> [8.3.1. Data Preparation
> [23](#data-preparation-1)](#data-preparation-1)
>
> [8.3.2. Model Implementation
> [32](#model-implementation-1)](#model-implementation-1)
>
> [8.3.3. Model Evaluation
> [36](#model-evaluation-1)](#model-evaluation-1)
>
> [8.3.4. Model Comparison
> [39](#model-comparison-1)](#model-comparison-1)
>
> [8.3.5. Conclusion [39](#conclusion-1)](#conclusion-1)

[9. Results [40](#results)](#results)

[9.1. Training Results [40](#training-results)](#training-results)

[9.2. Full Grid Evaluation Results
[43](#full-grid-evaluation-results)](#full-grid-evaluation-results)

[10. Discussion [50](#discussion)](#discussion)

[10.1. Data Preparation [50](#data-preparation-2)](#data-preparation-2)

[10.2. Evaluation [50](#evaluation)](#evaluation)

[10.3. Model Comparison [51](#model-comparison-2)](#model-comparison-2)

[11. Summary and Conclusions
[51](#summary-and-conclusions)](#summary-and-conclusions)

[11.1. Training Conclusion
[51](#training-conclusion)](#training-conclusion)

[11.2. Full Grid Evaluation Conclusion
[51](#full-grid-evaluation-conclusion)](#full-grid-evaluation-conclusion)

[12. References [52](#references)](#references)

[13. Appendices [54](#appendices)](#appendices)

[13.1. Deliverables, Work plan, Resources
[54](#deliverables-work-plan-resources)](#deliverables-work-plan-resources)

[13.2. Gantt Chart [56](#gantt-chart)](#gantt-chart)

[13.3. Project Poster [57](#project-poster)](#project-poster)

[13.4. Extensions [58](#extensions)](#extensions)

> [13.4.1. Tuning and Validation
> [58](#tuning-and-validation)](#tuning-and-validation)
>
> [13.4.2. Full Grid Heatmaps
> [60](#full-grid-heatmaps)](#full-grid-heatmaps)
>
> [13.4.3. Recoverability Boundaries Detailed
> [61](#recoverability-boundaries-detailed)](#recoverability-boundaries-detailed)
>
> [13.4.4. PSNR, SSIM vs OCR Correlation
> [62](#psnr-ssim-vs-ocr-correlation)](#psnr-ssim-vs-ocr-correlation)

[13.5. Project Framework Overview
[63](#project-framework-overview)](#project-framework-overview)

[13.6. Project Files [66](#project-files)](#project-files)

> **Table of Figures**

[Figure ‎2.1 LPR for Oblique Camera Capture: Concept Illustration
[6](#_Toc205224383)](#_Toc205224383)

[Figure ‎2.2 Synthetic License Plate Generation Process
[6](#_Toc205224384)](#_Toc205224384)

[Figure ‎2.3 Recoverability--Reliability Plot (AUC vs F) for All Models
and Datasets [7](#_Toc205224385)](#_Toc205224385)

[Figure ‎2.4 Maximal Recoverability Boundary
[8](#_Toc205224386)](#_Toc205224386)

[Figure ‎5.1 Controlled Environment LPR Example
[15](#_Toc205224387)](#_Toc205224387)

[Figure ‎5.2 Distorted License Plate Example
[15](#_Toc205224388)](#_Toc205224388)

[Figure ‎5.3 Synthetic license plate generation process
[15](#_Toc205224389)](#_Toc205224389)

[Figure ‎5.4 U-Net Architecture [16](#_Ref200906097)](#_Ref200906097)

[Figure ‎5.5 GANs Conceptual Overview
[16](#_Ref200906191)](#_Ref200906191)

[Figure ‎5.6 Forward Process Illustration
[17](#_Ref201854918)](#_Ref201854918)

[Figure ‎5.7 Reverse Process Illustration
[17](#_Ref201890980)](#_Ref201890980)

[Figure ‎8.1 Methodology Flowchart Diagram
[21](#_Toc205224394)](#_Toc205224394)

[Figure ‎8.2 Generated License Plate on a Black Canvas Example
[23](#_Ref201105317)](#_Ref201105317)

[Figure ‎8.3 License Plate with Bounding Boxes Example
[23](#_Ref201104870)](#_Ref201104870)

[Figure ‎8.4 Demonstration of 3D Rotation and Projection to the 2D Plane
[24](#_Ref185208026)](#_Ref185208026)

[Figure ‎8.5 Warped License Plate Example (alpha: 80, beta: 20)
[24](#_Ref201106780)](#_Ref201106780)

[Figure ‎8.6 Warped License Plate with Noise Example
[25](#_Ref201108934)](#_Ref201108934)

[Figure ‎8.7 Realigned License Plate Example
[26](#_Ref201110709)](#_Ref201110709)

[Figure ‎8.8 Hard Mask [27](#_Toc205224401)](#_Toc205224401)

[Figure ‎8.9 Signed Distance Field [27](#_Toc205224402)](#_Toc205224402)

[Figure ‎8.10 Logistic Smoothing [27](#_Toc205224403)](#_Toc205224403)

[Figure ‎8.11 Suppression [27](#_Toc205224404)](#_Toc205224404)

[Figure ‎8.12 Sampling PDF [28](#_Ref201196476)](#_Ref201196476)

[Figure ‎8.13 Uniform - Sobol Comparison
[28](#_Ref203494370)](#_Ref203494370)

[Figure ‎8.14 Scrambled Sobol Triples Example
[29](#_Ref201279401)](#_Ref201279401)

[Figure ‎8.15 Projected Sobol Triples Onto (u0, u1) Example
[29](#_Ref201280197)](#_Ref201280197)

[Figure ‎8.16 Sobol samples over the \[-90,90\]\^2 range
[30](#_Ref201281385)](#_Ref201281385)

[Figure ‎8.17 Sobol Samples for A and C Datasets Illustration
[31](#_Ref201341474)](#_Ref201341474)

[Figure ‎8.18 Architecture of Restormer
[34](#_Ref202064454)](#_Ref202064454)

[Figure ‎8.19 Discriminator\'s Predictions
[35](#_Ref186504632)](#_Ref186504632)

[Figure ‎8.20 Boundary-AUC Measure Illustration
[38](#_Ref202239423)](#_Ref202239423)

[Figure ‎9.1 Models Performance on Dataset A
[40](#_Ref203494458)](#_Ref203494458)

[Figure ‎9.2 Model Performance on Dataset B
[41](#_Ref203525600)](#_Ref203525600)

[Figure ‎9.3 Model Performance on Dataset C
[41](#_Ref203525515)](#_Ref203525515)

[Figure ‎9.4 Efficiency [42](#_Ref203525492)](#_Ref203525492)

[Figure ‎9.5 Reconstructions Per Model Example
[43](#_Ref202224922)](#_Ref202224922)

[Figure ‎9.6 Model-Specific Plate-Level OCR Accuracy on Dataset B
[44](#_Ref202742628)](#_Ref202742628)

[Figure ‎9.7 Recoverability Boundaries for All Models and Datasets
[45](#_Ref202799408)](#_Ref202799408)

[Figure ‎9.8 Maximal Recoverability Boundary
[46](#_Ref202748352)](#_Ref202748352)

[Figure ‎9.9 Recoverability--Reliability Plot (AUC vs F) for All Models
and Datasets [47](#_Ref202803516)](#_Ref202803516)

[Figure ‎9.10 Mean Performance in High-Angle Region
[48](#_Ref202921339)](#_Ref202921339)

[Figure ‎9.11 Restormer OCR Accuracy vs PSNR
[48](#_Ref203011624)](#_Ref203011624)

[Figure ‎9.12 Restormer OCR Accuracy vs SSIM
[49](#_Ref203011642)](#_Ref203011642)

[Figure ‎9.13 Diffusion-SR3 OCR Accuracy vs PSNR
[49](#_Ref203012003)](#_Ref203012003)

[Figure ‎9.14 Diffusion-SR3 OCR Accuracy vs SSIM
[50](#_Ref203012008)](#_Ref203012008)

> **Table of Tables**

[Table ‎9.1 Metrics Summary for Each Model and Dataset.
[40](#_Toc205219581)](#_Toc205219581)

[Table ‎9.2 Boundary-AUC and F Scores by Model and Dataset
[46](#_Ref202833285)](#_Ref202833285)

[Table ‎13.1 Outcomes/Deliverables [54](#_Toc205219583)](#_Toc205219583)

[Table ‎13.2 Work Plan [55](#_Toc205219584)](#_Toc205219584)

[Table ‎13.3 Technical Resources [55](#_Toc205219585)](#_Toc205219585)

**\
**

# Executive Summary

License plate recognition (LPR) engines perform reliably in controlled
scenes where the camera is oriented directly toward the vehicle.
However, street, security, and ATM cameras often capture vehicles so
that license plates are seen at an angle, and the plates appear noisy
due to low quality. In these situations, a clear, quantitative limit for
the extent to which license plate images can still be successfully
reconstructed has not been defined. To address this gap, we compare
deep-learning models for reconstructing synthetically distorted license
plate images and identify the maximum extent of viewing angles at which
recovery remains possible.

![](media/image3.png){width="4.16964457567804in" height="1.875in"}

**Objectives**

-   Compare discriminative models (U-Net, U-Net Conditional, Restormer)
    and generative models (GAN Pix2Pix, diffusion SR3) on synthetic
    clean-distorted plates.

-   Identify the maximum (α, β) rotation angles that deep-learning
    models can restore on synthetic license plate images.

-   Quantify recoverability by mapping plate OCR accuracy ≥ 90% on a
    full-grid $\lbrack 0{^\circ},\ 89{^\circ}\rbrack ²$.

**Methodology**

-   Generate clean synthetic plates by rendering random 6-digit numbers
    on a yellow background.

-   Define two smooth PDFs over (α, β) ∈ \[-90°, 90°\]²: one with
    moderate emphasis on extreme angles, one with stronger emphasis.

-   Draw 10,240 and 20,480 (α, β) samples from the moderate PDF to
    create Datasets A and B; draw 10,240 samples from the stronger PDF
    to create Dataset C.

-   Warp each plate using sampled (α, β) angles and simulate camera
    artifacts through edge blending, color jitter, Gaussian blur, and
    JPEG compression. De-warp each plate and downscale to 256×64 pixels.

-   Store each clean-distorted image pair with its (α, β) angle and
    plate number labels into the 80/10/10 train, validation, and test
    sets.

-   Train models and tune hyperparameters by tracking PSNR and SSIM on
    the validation sets.

-   Evaluate on a full-grid \[0°, 89°\]² of integer angle pairs; record
    plate-level OCR accuracy, trace the recoverability boundary, and
    compute boundary-AUC and reliability F.

> ![](media/image4.png){width="6.353606736657918in"
> height="0.7352099737532808in"}

**Key Findings**

-   Discriminative models exhibit tight clustering in full-grid
    coverage, with boundary AUCs ranging from 0.920 to 0.924 and
    reliability F values in the 0.1-0.15 range.

-   Generative models are lower by about 1-3% AUC; Pix2Pix shows F ≈
    0.15, while SR3 ranges from 0.10 on the best dataset to \> 0.50 on
    others, indicating deeper interior failures.

-   U-Net Conditional and Pix2Pix GAN train within 1-1.2×U-Net's
    (baseline) time, with latency of 7-12ms on an RTX 3090; Restormer
    requires 15 × training time and has 14ms latency; diffusion is
    4.7×slower to train and has 22ms latency due to multi-step sampling.

-   The maximal recoverability boundary shows that about 93.4% of the
    \[0°, 89°\]² full-grid contains recoverable signal. No model
    achieves ≥ 90 % OCR accuracy beyond 80° in both α and β, and α
    rotations are generally harder to reconstruct than β rotations.

-   PSNR correlates linearly with plate-level OCR accuracy (R² ≈ 0.98)
    and shows low variance at similar PSNR levels, confirming PSNR as a
    reliable validation indicator. SSIM is less effective (R² ≈ 0.74);
    values below 0.92 yield near-zero OCR, and OCR variance remains high
    at similar SSIM values.

-   Doubling training data from 10k to 20k yields a marginal AUC gain
    (\< 0.01); recoverability is influenced more by sample distribution.

![](media/image5.png){width="6.318695319335083in"
height="4.201492782152231in"}

![](media/image6.png){width="4.111090332458443in"
height="4.324251968503937in"}

**Impact**

-   This study identifies the boundary where license plate images can be
    restored and shows that recovery is harder when both angles are
    high, with α rotations generally more difficult than β rotations.

-   The project provides a framework to generate synthetic data, apply
    distortions, train models, and compare their results.

-   It introduces a method for low-dispersion angle sampling using a
    flexible, parametric PDF, which can be adapted for other tasks.

**Future Work & Extensions**

-   Extend data generation to include varying plate distances, better
    reflecting real-world static cameras viewing vehicles at different
    distances.

-   Build a real data pipeline using fixed cameras and sensors to record
    actual images and angle information, then test models on this data.

-   Adapt this synthetic-data framework to other domains requiring
    oblique-view restoration, such as signage or document imaging.

**Conclusion**

Discriminative architectures outperform their generative counterparts by
a small margin and are easier to adapt, train, and tune. Their explicit
loss functions make validation straightforward, whereas GANs and
diffusion models lack clear quantitative signals; diffusion adds further
complexity through multi-step sampling. Restormer delivers the best
accuracy, while diffusion-SR3 remains the hardest to stabilize and lags
under severe distortion. The maximal recoverability boundary traces the
outer envelope of usable signal, confirming that all models converge on
the same ≈93% recoverable region; once both angles exceed \~80°, the
residual information is too weak and further gains are unlikely.

[תקציר מנהלים]{dir="rtl"}

[מערכות לזיהוי לוחיות רישוי (]{dir="rtl"}LPR[) פועלות באופן מיטבי
כשהמצלמה מכוונת ישירות אל הלוחית. אולם, מצלמות רחוב, אבטחה וכספומטים
לוכדות לעיתים קרובות תמונות שבהן לוחית הזיהוי מופיעה בזווית או באיכות
ירודה. בסיטואציות אלו, לא הוגדר גבול כמותי ברור למידה שבה עדיין ניתן
לשחזר בהצלחה את תמונת הלוחית. כדי לטפל בפער זה, אנו משווים מודלים של
למידה עמוקה לשחזור תמונות לוחיות זיהוי מעוותות באופן סינתטי, על מנת
לזהות את היקף הזוויות המרבי שבו ניתן להצליח לשחזר תמונת לוחית
זיהוי.]{dir="rtl"}

![](media/image3.png){width="4.16964457567804in" height="1.875in"}

> *[איור]{dir="rtl"} ‎2.1 [המחשה עקרונית של זיהוי לוחית רישוי בתנאי צילום
> בזווית]{dir="rtl"}*

**[מטרות]{dir="rtl"}**

-   [השוואת מודלים דיסקרימינטיביים]{dir="rtl"} (U-Net, U-Net
    Сonditional, Restormer) [ומודלים גנרטיביים]{dir="rtl"}

> (GAN Pix2Pix, diffusion SR3) [המאומנים עם זוגות נקי-מעוות של לוחיות
> סינתטיות.]{dir="rtl"}

-   [זיהוי זוויות הסיבוב]{dir="rtl"} (α, β) [המקסימליות שמודלים של למידה
    עמוקה יכולים לשחזר בתמונות לוחיות רישוי סינתטיות.]{dir="rtl"}

-   [כימות יכולת השחזור על ידי מיפוי באמצעות]{dir="rtl"} OCR [כאשר
    הזיהוי הוא 90% ומעלה, על תחום זוויות מלא בטווח של]{dir="rtl"}
    $\lbrack 0{^\circ},\ 89{^\circ}\rbrack ²$[.]{dir="rtl"}

**[מתודולוגיה]{dir="rtl"}**

-   [יצירת לוחיות סינתטיות נקיות על ידי שיבוץ מספרים אקראיים בני 6 ספרות
    על גבי רקע צהוב.]{dir="rtl"}

-   [הגדרת שתי פונקציות צפיפות הסתברות (]{dir="rtl"}PDFs[) חלקות על
    פני]{dir="rtl"} (α, β) ∈ \[-90°, 90°\]²[: אחת עם דגש מתון על זוויות
    קיצוניות והשנייה עם דגש חזק יותר.]{dir="rtl"}

-   [לקיחת 10,240 ו-20,480 דגימות של]{dir="rtl"}(α, β) [מתוך
    ה-]{dir="rtl"}PDF [המתונה ליצירת מערכי נתונים]{dir="rtl"} A
    [ו-]{dir="rtl"}B[, ו- 10,240 דגימות מתוך ה-]{dir="rtl"}PDF [החזקה
    יותר ליצירת מערך נתונים]{dir="rtl"} C[.]{dir="rtl"}

-   [יצירת לוחיות מעוותות בתהליך הכולל: הפעלת עיוות גאומטרי באמצעות
    זוויות הדגימה]{dir="rtl"}(α, β) [, הוספת רעשי מצלמה באמצעות מיזוג
    קצוות, שינוי רנדומלי בצבעי התמונה (]{dir="rtl"}color jitter[), טשטוש
    גאוסי ודחיסת]{dir="rtl"} JPEG[, הסרת העיוות הגאומטרי והקטנת קנה
    המידה ל-]{dir="rtl"}256×64 [פיקסלים.]{dir="rtl"}

-   [יצירת מערך נתונים הכולל זוגות לוחיות (נקי-מעוות) ואת המידע הנלווה:
    זוויות הדגימה (]{dir="rtl"}α, β[) ומספר הלוחית. המערך מחולק לקבוצות
    אימון (80%), וולידציה (10%) ובדיקה (10%).]{dir="rtl"}

-   [אימון מודלים וכיול היפר-פרמטרים על ידי מעקב אחר מדדי]{dir="rtl"}
    PSNR [ו-]{dir="rtl"}SSIM [על קבוצת הוולידציה.]{dir="rtl"}

-   [הערכת המודלים על גבי תחום זוויות מלא בטווח של]{dir="rtl"}
    $\lbrack 0{^\circ},\ 89{^\circ}\rbrack ²$ [המכיל דגימות מרובות
    לכל]{dir="rtl"} (α, β)[; מיפוי באמצעות]{dir="rtl"} OCR [ברמת הלוחית,
    מציאת גבול השחזור, כימות יכולת השחזור באמצעות]{dir="rtl"}
    boundary-AUC [וציון \"אמינות\"]{dir="rtl"} F[.]{dir="rtl"}

![](media/image4.png){width="6.353606736657918in"
height="0.7352099737532808in"}

> *[איור]{dir="rtl"} ‎2.2 [המחשה עקרונית של זיהוי לוחית רישוי בתנאי צילום
> בזווית]{dir="rtl"}*

[\
]{dir="rtl"}

**[ממצאים עיקריים]{dir="rtl"}**

-   [במודלים דיסקרימינטיביים מיפוי]{dir="rtl"} OCR [מציג יכולת שחזור
    טובה, עם ערכי]{dir="rtl"} boundary AUC [הנעים בין 0.920 ל-0.924
    וציוני \"אמינות\"]{dir="rtl"} F [בטווח של 0.10-0.15.]{dir="rtl"}

-   [במודלים גנרטיביים, ה-]{dir="rtl"} boundary AUC [נמוך ב-1% עד
    3%]{dir="rtl"}; []{dir="rtl"}Pix2Pix [מציג]{dir="rtl"} F ≈ 0.1[,
    בעוד שב-]{dir="rtl"}SR3 [ערך ה-]{dir="rtl"}F [הוא 0.10 במערך הנתונים
    הטוב ביותר, הוא עולה מעל ל-0.5 במערכי הנתונים האחרים, מה שמצביע על
    כשלים פנימיים עמוקים.]{dir="rtl"}

-   [בהשוואה ל-]{dir="rtl"}U-Net [(עם כרטיס מסך]{dir="rtl"} RTX
    3090[)]{dir="rtl"}; [זמן האימון של]{dir="rtl"} U-Net Conditional
    [ו-]{dir="rtl"}Pix2Pix GAN [הוא פי 1-1.2, עם זמן היסק
    (]{dir="rtl"}latency[) של]{dir="rtl"} 7-12ms[. זמן האימון
    של]{dir="rtl"}Restormer [ארוך פי 15 וזמן היסק שלו הוא]{dir="rtl"}
    14ms[, ואילו זמן האימון של]{dir="rtl"}diffusion [ארוך פי 4.7 וזמן
    היסק שלו הוא]{dir="rtl"} 22ms[, בעקבות דגימה רב-שלבית.]{dir="rtl"}

-   [סף השחזור המקסימלי, המשותף לכל המודלים, מכסה 93.4% מתחום זוויות מלא
    בטווח של]{dir="rtl"} $\lbrack 0{^\circ},\ 89{^\circ}\rbrack ²$[. אף
    מודל לא השיג יכולת שיחזור כאשר זוויות הסיבוב]{dir="rtl"} α
    [ו-]{dir="rtl"}β [גבוהות מ-]{dir="rtl"}80°[. באופן כללי, השחזור נעשה
    קשה יותר עבור זוויות]{dir="rtl"} α [קיצוניות בהשוואה
    לזוויות]{dir="rtl"} β[.]{dir="rtl"}

-   [מדד ה]{dir="rtl"}PSNR [יכול לנבא את מדד ה-]{dir="rtl"}OCR [ברמת
    הלוחית (]{dir="rtl"}R² ≈ 0.98[), ומראה שונות נמוכה ברמות]{dir="rtl"}
    PSNR [דומות, מה שמאשר את]{dir="rtl"} PSNR [כמדד ולידציה אמין,
    מדד]{dir="rtl"} SSIM [פחות יעיל (]{dir="rtl"}R² ≈ 0.74[), ערכים מתחת
    ל-0.92 מניבים ערכי]{dir="rtl"} OCR [הקרובים לאפס, והשונות נשארת
    גבוהה בערכי]{dir="rtl"} SSIM [דומים.]{dir="rtl"}

-   [הכפלת נתוני האימון מ-]{dir="rtl"}10k [ל-]{dir="rtl"}20k [מניבה
    שיפור זניח ב-]{dir="rtl"}AUC [(פחות מ0.01)]{dir="rtl"}; [יכולת
    השחזור מושפעת יותר מהתפלגות הדגימות.]{dir="rtl"}

![A graph with numbers and a number of red and blue squares AI-generated
content may be incorrect.](media/image5.png){width="6.318695319335083in"
height="4.201492782152231in"}

> *[איור]{dir="rtl"} ‎2.3 [גרף יכולת שחזור ואמינות (]{dir="rtl"}AUC
> [מול]{dir="rtl"} F[)]{dir="rtl"} [עבור כל המודלים וכל מערכי
> הנתונים]{dir="rtl"}*

![A graph of a number of models AI-generated content may be
incorrect.](media/image6.png){width="4.111090332458443in"
height="4.324251968503937in"}

> *[איור]{dir="rtl"} ‎2.4 [גבול יכולת השחזור המרבית]{dir="rtl"}*
>
> **[השפעה]{dir="rtl"}**

-   [המחקר מזהה את סף ההצלחה שבו ניתן לשחזר תמונות של לוחיות רישוי ומראה
    כי השחזור קשה יותר כאשר שתי זוויות הסיבוב גבוהות, ובעיקר עבור
    זוויות]{dir="rtl"} α [קיצוניות.]{dir="rtl"}

-   [הפרויקט מספק תשתית ליצירת מערכי נתונים סינתטיים, יישום עיוותים,
    אימון מודלים והשוואת תוצאותיהם.]{dir="rtl"}

-   [הפרויקט מציג שיטה לדגימת הזוויות הממלאת את חלל האפשרויות בצורה
    אחידה יותר באמצעות]{dir="rtl"} PDF [גמישה ופרמטרית, הניתנת להתאמה
    למשימות שונות.]{dir="rtl"}

> **[עבודה עתידית והרחבות]{dir="rtl"}**

-   [הרחבת יצירת הנתונים כך שתכלול מרחקי צילום שונים, המדמים מצלמות
    סטטיות בעולם האמיתי הלוכדות כלי רכב ממרחקים שונים.]{dir="rtl"}

-   [איסוף נתונים מהעולם האמיתי באמצעות מצלמות וחיישנים לקביעת הזוויות,
    ולאחר מכן לבחון את המודלים על נתונים אלו.]{dir="rtl"}

-   [התאמת תשתית יצירת הנתונים הסינתטיים לתחומים אחרים הדורשים שחזור
    מתצוגה אלכסונית כמו שילוט או הדמיית מסמכים.]{dir="rtl"}

> **[מסקנות]{dir="rtl"}**

[ארכיטקטורות דיסקרימינטיביים מציגות ביצועים טובים יותר במעט ממקבילותיהן
הגנרטיביות והן קלות יותר להתאמה, אימון וכיול. הסיבה לכך היא שפונקציות
ההפסד המפורשות שלהן הופכות את תהליך הוולידציה לפשוט, בעוד שלמודלים
כמו]{dir="rtl"} GAN [ו-]{dir="rtl"}diffusion [חסרים מדדים כמותיים
ברורים, כאשר]{dir="rtl"} diffusion [מוסיף מורכבות נוספת באמצעות דגימה
רב-שלבית. בפועל, מודל]{dir="rtl"} Restormer [מספק את רמת הדיוק הגבוה
ביותר, בעוד שמודל]{dir="rtl"} diffusion-SR3 [הוא הקשה ביותר לייצוב ומפגר
בביצועיו תחת עיוותים קשים. גבול יכולת שחזור מרבי המשותף לכל המודלים מכסה
כ-93% מהתחום שנבדק, ומאשר כי ברגע ששתי הזוויות עולות על רף]{dir="rtl"}
80°[, המידע השיורי חלש מדי ושיפורים נוספים אינם סבירים.]{dir="rtl"}

# Glossary 

  -------------------- ----------------------------------------------------
  **Term**             **Explanation**

  **Camera Geometry &  
  Projection**         

  Perspective          Maps 3D points to 2D using a focal length and a
  Projection           camera principal point, as in a pin-hole camera
                       model.

  Perspective          The geometric warping that occurs when a planar
  Distortion           object is viewed from an oblique angle.

  Principal Point      The sensor location where the optical axis meets the
                       image plane; fixing it keeps synthetic warps
                       centered.

  Focal Length         Distance from the pinhole to the image sensor that
                       determines the field of view; held constant, so only
                       rotation alters appearance.

  Homography           A 3×3 projective matrix mapping one planar view to
                       another; its inverse realigns warped points to their
                       original positions.

  **Angle Space &      
  Sampling**           

  Angle Space          The domain of all possible angle pairs (α, β) in
                       \[-90,90\]² range.

  Full Grid            Exhaustive evaluation set containing every integer
                       angle pair (α, β) within \[0,89\]² for comprehensive
                       testing.

  Low Dispersion       Describes a sequence of points that fill a space as
                       evenly as possible, so no region is over- or under
                       sampled.

  Sobol Sequence       A method for generating a set of points that cover a
                       multi-dimensional space uniformly, using a base-2,
                       quasi-random pattern.

  Sobol Sampling       Uses points from a Sobol sequence, mapped through
                       the target PDF, to draw samples that fill the space
                       with low dispersion.

  PDF                  Probability Density Function: Defines the desired
                       sampling weight for each angle pair (α, β). It is
                       shaping how likely each distortion is during dataset
                       creation.

  CDF                  Cumulative Distribution Function: A non-decreasing
                       function giving, at each value, the probability that
                       a continuous random variable is less than or equal
                       to that value.

  Signed-Distance      A scalar function that assigns each point the
  Field                shortest distance to a reference surface, with the
                       sign indicating whether the point lies inside or
                       outside that region.

  **Model Architecture 
  Components &         
  Operations**         

  Generative Model     Learns the underlying data distribution, allowing it
                       to both classify inputs and synthesize new samples
                       that follow that distribution.

  Discriminative Model Learns a direct mapping from input features to class
                       labels, optimizing the decision boundary between
                       categories.

  Convolution &        Learned N×N filters used in standard, strided,
  Kernels              transposed, depth-wise, and point-wise forms for
                       feature extraction and resizing.

  CNN (Convolutional   Network built from convolution, pooling, and
  Neural Network)      activation layers; forms the backbone of our U-Net
                       and GAN generator.

  Receptive Field      Region of the input image that influences one output
                       pixel; a larger field lets the model consider wider
                       image context.

  Depth-Wise           Applies a separate spatial filter to each channel,
  Convolution          reducing parameter count before mixing or attention
                       layers.

  Point-Wise           1×1 convolution that mixes channel outputs after
  Convolution          depth-wise filtering.

  Pooling (Max         Down-samples by summarizing local windows; max
  Pooling)             pooling retains the strongest activation in each
                       region.

  Activation Function  Nonlinearities that enable networks to learn complex
                       mappings; ReLU is simple, efficient, and widely used
                       in standard networks. SiLU and GELU are used in
                       modern diffusion and transformer variants.

  Channel              Stacks multiple feature maps along the channel
  Concatenation        dimension to incorporate conditioning information.

  Skip Connection      In U-Net, transfers encoder activations to
                       corresponding decoder layers; preserves spatial
                       detail and aids gradient flow.

  Noise Encoder        Lightweight CNN that encodes input distortions into
                       a conditioning vector for FiLM layers.

  FiLM                 Feature-wise affine modulation that scales and
                       shifts activations based on an external conditioning
                       vector.

  Self-Attention       Computes interactions across all spatial positions,
                       capturing global context in feature maps.

  Cross-Attention      Queries from one feature map attend to keys and
                       values from another, enabling guided information
                       flow.

  Transformer          A network built from alternating attention and
                       feed-forward blocks

  MDTA                 Multi-Dconv Head Transposed Attention: applies
                       depth-wise convolution to each head before
                       self-attention to reduce parameters.

  GDFN                 Gated-Dconv Feed-Forward Network: mixes channels
                       using depth-wise convolutions and gating mechanisms
                       for efficiency.

  Residual Block       Adds the original input to the processed output,
                       making it easier to train deep networks and avoid
                       vanishing gradients.

  MLP                  Multi-Layer Perceptron: a feed-forward network
                       composed of stacked fully connected layers that
                       learns nonlinear mappings from input features to
                       target outputs.

  Generator            Produces synthetic samples by turning a random or
                       conditioned vector into data that resembles the
                       training set.

  Discriminator        Judges each sample as real or fake, providing
                       feedback that helps the generator improve its
                       synthetic outputs.

  **Training Process & 
  Hyperparameters**    

  Hyperparameter       Settings preselected before training, such as
                       learning rate, batch size, β-schedule, or network
                       depth.

  Epoch / Step         One full pass over the training data (epoch) or a
                       fixed number of update steps (step) for diffusion
                       models

  Batch Size           Number of samples processed in each gradient update.

  Data Loader          Iterator that shuffles data and forms batches for
                       GPU training.

  Optimizer            An algorithm that updates model weights based on
                       gradients to minimize the objective function. (SGD,
                       Adam, AdamW)

  Learning-Rate        Changes the learning rate during training by
  Scheduler            following a preset schedule, often reducing it over
                       time.

  Loss Function        The formula that measures how far model predictions
                       are from the target values; it is minimized during
                       training.

  Objective            The full expression that is being optimized during
                       training; combines all individual loss terms into a
                       single value.

  Number of Filters    Base channel count in convolutional layers,
  (kernels/features)   typically doubled after each down-sampling stage.

  Checkpoint           Saved model learned weights whenever validation
                       performance improves.

  **Metrics &          
  Evaluation**         

  Heatmap              A 2D colored grid that visualizes any metric's value
                       across the full grid.

  Recoverability       The curve on the full grid that marks the farthest
  boundary             point where the model still meets the plate OCR
                       accuracy threshold. It shows the edge of where plate
                       recognition is reliable.

  Mean interior        The average distance from each failure under the
  failure distance     recoverability boundary to the boundary. This value
                       shows how many errors occur in the reliable region
                       and how far they are.

  Boundary-AUC         Boundary area under curve: a measure that quantifies
                       the area under the recoverability boundary.

  Plate-Level Metric   Mean PSNR, SSIM, or OCR accuracy computed over the
                       entire region of the license plate image.

  Digit-Level Metric   Mean PSNR, SSIM, or OCR accuracy computed over a
                       subregion of the license plate image, capturing only
                       a single digit.

  Worst-Case Metric    The lowest PSNR or SSIM among subregions on a
                       license plate. Indicates the maximum local error for
                       a sample.

  Efficiency           Computed performance-per-time or per-resource ratio.

  Train Time Norm      Training duration normalized by the baseline U-Net's
                       time, allowing efficiency comparison.

  Latency              Average time, in milliseconds, to restore one image
                       on an RTX 3090 GPU.
  -------------------- ----------------------------------------------------

  : []{#_Toc205224383 .anchor}Figure ‎2.1 LPR for Oblique Camera Capture:
  Concept Illustration

# Abstract

**License Plate Recognition (LPR)** systems typically rely on
high-quality images captured under controlled conditions. Street,
security, and ATM cameras often capture vehicles so that license plates
are seen at an angle, and the plates appear noisy due to low quality.
This study investigates whether deep-learning image-restoration models
can reconstruct such plates and determines the maximum extent of viewing
angles at which recovery remains possible. We compare a classic
**U-Net** architecture with generative approaches such as **generative
adversarial networks (GANs)** and **diffusion models** for
reconstructing warped, noisy plates.

We create synthetic datasets that simulate a wide range of viewing
angles and noise levels to provide controlled test conditions. The study
highlights the strengths and limitations of each model and maps the
recoverability boundary beyond which models can no longer restore plate
images.

# Introduction

**License Plate Recognition (LPR)** systems support traffic control and
law enforcement. In controlled scenes (Figure ‎5.1) the cameras are
mounted at fixed angles, under steady **lighting, and at known
distances, so plate numbers are captured cleanly. These systems rely**
on clear images to extract characters accurately, and performance is
usually consistent when the environment is designed for this purpose.
Standard LPR setups are well-studied and often achieve high accuracy.

Outside these controlled scenes, however, ordinary cameras (Figure
‎5.2)---for example, those at ATMs or in street surveillance---record
plates at steep angles and with compression artifacts and noise. In
these settings, plate numbers often disappear entirely or become
difficult to recognize, even for human observers. We explore whether
deep-learning models can restore such images.

  ----------------------------------------------------------------------------------------------------------
  ![](media/image7.jpeg){width="1.9763779527559056in"   ![](media/image8.jpeg){width="2.467438757655293in"
  height="1.8515944881889763in"}                        height="1.851388888888889in"}
  ----------------------------------------------------- ----------------------------------------------------
                                                        

  ----------------------------------------------------------------------------------------------------------

  : []{#_Toc205224384 .anchor}Figure ‎2.2 Synthetic License Plate
  Generation Process

**Research Question:** At which viewing angles can different models
recover noisy plates that are unrecognizable to humans? This question
addresses the extent to which distortion can be tolerated before plate
information is lost and whether model choice affects this threshold.

To answer, we generate synthetic datasets that blend random plate
numbers, strong geometric warps, and realistic noise (Figure ‎5.3). This
data lets us test each model under controlled and repeatable
distortions.

> ![](media/image4.png){width="6.353606736657918in"
> height="0.7352099737532808in"}

+------------------------+----------------------+---------------------+
| *(a) Original license  | *(b) Warped and      | > *(c) De-warped    |
| plate*                 | noisy license plate* | > license plate*    |
+========================+======================+=====================+
|                        |                      |                     |
+------------------------+----------------------+---------------------+

: []{#_Toc205224385 .anchor}Figure ‎2.3 Recoverability--Reliability Plot
(AUC vs F) for All Models and Datasets

Recent advances in generative AI offer promising solutions for image
restoration. This study clarifies how generative and discriminative
models apply to LPR under extreme angles and noise.

While **U-Net** was initially designed for biomedical image segmentation
\[1\], it can be adapted for image restoration tasks. The network uses
an encoder to extract multi-scale features from the distorted input. A
decoder then reconstructs the image by merging encoder features at
corresponding scales via skip connections. (Figure ‎5.4), In practice,
this structure has shown robust and effective performance in recovering
details.

![](media/image9.png){width="5.409344925634295in"
height="3.588692038495188in"}

Generative Adversarial Networks (**GAN**s) \[2\](pages 331-335) consist
of two competing neural networks: a generator $G$ and a discriminator
$D$. The generator aims to generate realistic images from distorted
inputs, while the discriminator aims to distinguish generated images
from true, clean images (Figure ‎5.5). Training follows the minimax
objective (Equation ‎5.1)

$$\min_{G}{\max_{D}E_{x \sim p_{\text{data}}}}\left\lbrack \log D(x) \right\rbrack + E_{z \sim p_{z}}\left\lbrack \log\left( 1 - D\left( G(z) \right) \right) \right\rbrack$$

> ![GAN examples](media/image10.jpeg){width="4.662482502187227in"
> height="2.3541666666666665in"}

A **Diffusion model** \[3\] consists of a forward process and a reverse
process. In the forward process (Figure ‎5.6), the image is progressively
corrupted by adding Gaussian noise over many steps (Equation ‎5.2).

> $$q\left( x_{t}\  \right|x_{t - 1}\mathcal{)\  = \ N}\left( x_{t};\sqrt{\left( 1\  - \beta_{t} \right)}x_{t - 1}\ ,\ {\ \beta}_{t}I \right)$$

$x_{t - 1}$ is the previous image, and $\beta_{t}$ controls the amount
of noise added at each step. As $t$ increases, the image becomes less
like the original and more like random noise. After enough steps, all
the structure is lost and only noise remains.

![](media/image11.png){width="5.168919510061242in"
height="0.8382786526684165in"}

The reverse process (Figure ‎5.7) undoes this diffusion. We train a
neural network to predict and remove the noise at each step. The reverse
step is also Gaussian (Equation ‎5.3)

> $$p_{\theta}\left( x_{t - 1}\  \right|x_{t}\mathcal{)\  = N}\left( x_{t - 1};\mu_{\theta}\left( x_{t},\ t \right)\ ,\ {\ \sigma}_{\theta}^{2}I \right)$$

![](media/image12.png){width="4.981173447069116in"
height="0.8407250656167979in"}

The model predicts $\epsilon_{\theta}\left( x_{t},t \right)$ and
computes (Equation ‎5.4)

> $$\mu_{\theta}\left( x_{t},t \right) = \frac{1}{\sqrt{1 - \beta_{t}}}\left( x_{t} - \beta_{t}\epsilon_{\theta}\left( x_{t},t \right) \right)$$

Training minimizes the noise-prediction loss (Equation ‎5.5)

> $$L_{\theta} = \mathbb{E}_{t,\, x_{0},\,\epsilon}\left\lbrack \parallel \epsilon - \epsilon_{\theta}\left( x_{t},t \right) \parallel^{2} \right\rbrack$$

where $\epsilon$ is the true Gaussian noise from the forward step. Most
diffusion models use U-Net architecture for the noise-prediction network
because it preserves spatial details and maintains the same
input-to-output shape at each reverse step.

After training, we generate new images by sampling
$x_{T}\mathcal{\sim N}(0,I)$ and applying the learned reverse chain from
$t = T$ down to $t = 0$.

# Goals, Objectives, and Metrics

## Goals

1.  Reconstructed license plate images captured under extreme viewing
    angles and noise conditions using deep-learning models.

2.  Evaluate and compare the performance of U-Net, GANs, and diffusion
    models in handling image distortions and noise.

3.  Identify the limit of recoverable data present in the distorted
    license plate images.

## Objectives

4.  Create synthetic datasets simulating various distortion levels to
    train and test the models.

5.  Adapt and configure existing U-Net, GANs, and Diffusion Models for
    the image restoration task.

6.  Find optimal model settings through hyperparameter tuning and
    systematic validation.

7.  Measure image quality, recognition accuracy, and computational
    efficiency for each model.

8.  Analyze and compare model performance to identify strengths,
    weaknesses, and operational limits.

## Metrics

9.  **Mean Squared Error (MSE):** We use MSE as the loss function during
    training. MSE quantifies the average squared difference per pixel
    between two images, or, in the case of diffusion, reduces the
    difference between actual and predicted noise. It is widely used in
    image restoration because it penalizes large errors, is
    differentiable everywhere, and has stable gradients. (Equation ‎6.1)

> $$\text{MSE} = \frac{1}{N}\sum_{i = 1}^{N}\left( x_{i} - y_{i} \right)^{2}$$
>
> $N$ is the pixel count. $x_{i}$ and $y_{i}$ are original and restored
> pixel values.

10. **Peak Signal-to-Noise Ratio (PSNR):** PSNR is widely used for image
    evaluation and comparison. It converts MSE into a dB score. We use
    PSNR because it summarizes overall restoration quality in a way that
    is easy to interpret and compare between models. (Equation ‎6.2)

> $$PSNR = 10\log_{10}\left( \frac{MAX^{2}}{MSE} \right)$$
>
> $MAX$ is the maximum possible pixel value.

11. **Structural Similarity Index (SSIM):** SSIM evaluates perceptual
    similarity by comparing structure, brightness, and contrast. We
    select SSIM because it correlates more closely with human perception
    and emphasizes structural information critical for reading license
    plate digits. Higher SSIM values indicate better preservation of
    perceptual details. (Equation ‎6.3)

> $$SSIM\  = \frac{\left( 2\mu_{x}\mu_{y} + C_{1} \right)\left( 2\sigma_{xy} + C_{2} \right)}{\left( \mu_{x}^{2} + \mu_{y}^{2} + C_{1} \right)\left( \sigma_{x}^{2} + \sigma_{y}^{2} + C_{2} \right)}\ $$
>
> $\mu_{x},\mu_{y}$ are means; $\sigma_{x}^{2},\sigma_{y}^{2}$ are
> variances; $\sigma_{xy}$ is covariance; $C_{1},C_{2}$ are small
> constants to stabilize the division.

12. **Optical Character Recognition** **Accuracy (OCR):** **OCR**
    accuracy is our primary metric. It measures how well restored images
    support automated LPR. We report both plate-level OCR accuracy,
    which checks if the entire plate number is recognized, and per-digit
    OCR accuracy, which gives the percentage of correctly recognized
    digits for a single plate. OCR accuracy provides a direct measure of
    the practical effectiveness of each model. (Equation ‎6.4)

> $$\text{OCR Acc} = \frac{\text{K correct}}{\text{N total}}$$

13. **Computational Efficiency:** We record training time and latency
    for each model to assess practical usage.

# Literature Review

This literature review surveys methods that reconstruct license plates
that cannot be read directly. It considers image enhancement,
restoration, and super-resolution. It also explains how 3D projective
geometry supports the creation of synthetic training data. OCR is
discussed as a tool for evaluating restored images. 

##  3D Projective Geometry

3D Projections, rotations, and coordinate transforms from 3D projective
geometry let us render license plates at controlled angles. Python
Graphics \[4\] supplies practical routines for these transforms. By
sweeping through wide-angle ranges, we create images that resemble real,
distorted captures. Such datasets isolate perspective effects and guide
restoration model design.

##  Low Dispersion Sampling

Covering all projective distortions requires a sampling plan that avoids
dense clusters and empty gaps. Low-discrepancy Sobol sequences \[5\]
offer a nearly uniform, space-filling distribution, so both typical and
extreme tilt angles appear in the data. Using these sequences during
training and evaluation prevents bias toward any part of the distortion
space.

## LPR Systems

Early LPR systems relied on edge-based extraction and geometric
correction, but accuracy dropped at oblique views \[6\]. Surveys note
that many methods remain sensitive to uneven lighting, motion blur, and
extreme perspective distortions \[7\]. For many images, a separate
restoration or de-warping step is required before applying OCR.

## Deep Learning-Based Restoration Approaches

## U-Net

> U-Net was first designed for biomedical image segmentation \[1\]. Its
> encoder--decoder structure preserves fine spatial details. Researchers
> later adapted U-Net for denoising, deblurring, and geometric
> correction tasks \[8\] \[9\]. Newer variants target limitations of the
> standard U-Net when distortions are more complex. Uformer \[10\]
> replaces CNN blocks with a U-shaped Transformer, helping to recover
> features that conventional models may miss. Restormer \[11\] extends
> this for high-resolution inputs and outperforms Uformer in severe
> noise and blur \[12\]. Some models improve skip connections. Attention
> U-Net \[13\] adds gates to let the model focus on important features
> and reduce noise. UNet++ \[14\] uses a nested skip connection
> structure, improving how features are fused and helping restore fine
> details. For this project, we use U-Net as the baseline because it
> reliably preserves character structure. Restormer is selected as the
> advanced model. It is designed for strong noise and blur, which are
> typical for plates at extreme viewing angles.

## GAN

> GANs \[2\] are widely used for image-to-image restoration tasks
> because the adversarial loss encourages outputs with sharp and
> realistic detail. Pix2Pix \[15\] []{dir="rtl"}combines a U-Net
> generator with a PatchGAN discriminator to turn degraded images into
> clean ones; it produces clear edges and low L1 error across many
> tasks. SRGAN \[16\] and its improved version, ESRGAN \[17\], focus on
> super-resolution and raised perceptual quality by generating fine
> details at 4× upscaling; these models also won the PIRM challenge for
> image restoration. DeblurGAN \[18\] handles motion blur as a
> conditional image translation task, increasing SSIM by about 0.05 and
> working five times faster than earlier methods on the GoPro dataset.
> GANs can sometimes create artifacts under very strong distortions
> \[19\], but their strength is making crisp and readable features.
> Pix2Pix seems the best fit for our project because it learns directly
> from any pair of distorted and clean images, it\'s highly configurable
> with a straightforward architecture, and can be trained efficiently on
> ordinary hardware.

## Diffusion Models

> Diffusion models \[3\] are a newer approach to image restoration. They
> surpass GANs and are based on learning to undo a gradual noising
> process. The baseline DDPM method \[3\] removes noise in small steps,
> producing realistic images without adversarial training. SR3 \[20\]
> extends diffusion to super-resolution, achieving up to 8× scaling,
> halving FID compared to GAN baselines, and fooling human judges in
> half of the comparisons. DvD \[21\] uses diffusion for document
> dewarping and reports higher accuracy than earlier convolutional
> models on standard tests. I²SB \[22\] and DiffPIR \[23\], apply
> diffusion as a prior for deblurring and inpainting and reduce sampling
> time while preserving image quality. While these models are more
> computationally demanding, they reliably recover fine structure and
> complex textures. SR3 is most relevant to license plate restoration
> because it directly learns from paired low- and high-resolution
> images, allowing us to adapt the same conditional framework to restore
> distorted license plates.

## OCR

Tesseract \[24\] is an open-source OCR tool built on LSTM neural
networks. It has been integrated into license plate recognition
pipelines \[25\] \[26\], especially after preprocessing and cleaning
steps. It offers several operation modes, including settings for
digit-only or single-character recognition, which help improve results
on cropped digits. Tesseract is lightweight and handles large test sets
efficiently on ordinary hardware. PaddleOCR \[27\] uses deep CNN text
detectors and Transformer-based recognition to detect and read text in a
variety of images, but it is mainly designed for general text, and it
does not support different modes or settings for single, cropped digits.
It is also demanding to install. Since license plate images usually
require only digit or number recognition, Tesseract's focused modes and
light design are better matched to these needs​.

# Methods

The project consists of the following phases: Data preparation, Model
Implementation, Model Evaluation, Model Comparison, and Conclusion
Formulation.

## Block Diagram

> ![](media/image13.png){width="3.4040234033245844in"
> height="8.266055336832896in"}

## Phases Description

## Data Preparation

> In this phase, we create clean license plate images with random plate
> numbers. We define angles used to rotate the plates, and noise to
> simulate real camera distortions, such as JPEG artifacts, color
> variations, blur, etc. Then, we apply warping and the noise to clean
> images and realign them to their original orientation. This process
> generates pairs of clean and distorted license plates. Next, we
> generate a synthetic dataset that includes images with distortions
> ranging from moderate to severe. We split the data into training,
> validation, and test sets. For evaluation, we generate a full grid
> that covers every angle pair. A fixed random seed is used so that the
> dataset is always generated in the same way.

## Model Implementation

> In this phase, we implement or adapt three model types: U-Net
> (baseline), GANs, and diffusion models. Each model is set up to
> process license plate images of the same size and channel format. We
> tune key hyperparameters such as filter number, learning rate, batch
> size, and others by running several trials and choosing the values
> that give the best validation results. U-Net is trained to reduce the
> MSE between its output and the clean plate image. For GANs, we update
> the generator and discriminator in turns, aiming to make generated
> images look real. Diffusion models predict the noise added at each
> step and are trained to match this predicted noise to the true noise
> using MSE loss.\
> Data loaders supply shuffled training and validation batches. We
> periodically evaluate SSIM and PSNR on the validation set to monitor
> restoration quality. We do not perform OCR accuracy (the primary
> metric) validation during training because it is computationally heavy
> and needs preprocessing. It is only done in the final full grid test
> evaluation. We retain the checkpoint that achieves the highest
> validation metric score.

## Model Evaluation

> In this phase, we evaluate how effectively our trained models perform
> on the unseen test dataset. Then, we evaluate performance on the full
> grid, which contains multiple samples for each possible angle pair.
> Each model is applied to the full grid; we compute the digit-level and
> plate-level PSNR, SSIM, and OCR accuracy. Our main emphasis is on
> plate-level OCR accuracy, as it directly supports automatic LPR. These
> results are used directly in the model comparison phase.

## Model Comparison

> In this phase, we organize the collected metrics to compare models. We
> create tables from raw collected metrics. We use heatmaps to display
> how performance varies with different angles for comparison. We use
> box plots and scatter plots to compare mean results over different
> criteria. We examine the correlation between metrics to identify
> relationships and trends.

## Conclusion

> In this phase, we interpret results to derive conclusions. By
> examining the metrics and visual plots, we find which angles each
> model handles best and what the limit is. This lets us answer the main
> research questions. We determine maximum tolerable distortion and
> identify strengths and weaknesses in each model\'s design. Finally, we
> summarize the findings, suggest areas for improvement, and discuss
> practical insights.

## Detailed Description of Processing Steps

## Data Preparation 

1.  **Creation of Clean License Plate Images**

> Each synthetic license plate is initially generated at a base
> resolution of $w \times h$ pixels (e.g., 512×128). The plate number is
> a random 6-digit string, with each digit occupying a fixed equal-width
> cell on the plate. The plate image is then centered within a larger
> black canvas (Figure ‎8.2), enabling rotation of the plate without
> clipping it.

![](media/image14.png){width="4.97417760279965in"
height="1.725119203849519in"}

> The coordinates of the license plate corners within the larger canvas
> are calculated and stored as (Equation ‎8.1)

$$\text{S} = \text{\{}(x,y),(x + w,y),(x + w,y + h),(x,y + h)\text{\}}$$

> These source corner points are stored for later perspective
> transformations.
>
> The bounding box for each digit is computed based on its assigned cell
> (Figure ‎8.3), and saved in the metadata.
>
> ![](media/image15.png){width="3.591994750656168in"
> height="0.9515682414698162in"}

2.  **Perspective Warp Using Rotation Angles**

> To simulate viewpoint changes, we apply 3D rotations to the source
> corner points and project them to find the target points for the
> subsequent perspective warp (Figure ‎8.4).
>
> We rotate the corners first around the x-axis by $\beta$ and then the
> y-axis by $\alpha$ using 3D rotation matrices (Equation ‎8.2).

  ------------------------------------------------------------------------------
  Rotation around the x-axis:         Rotation around the y-axis:
  ----------------------------------- ------------------------------------------
  $$R_{x} = \begin{bmatrix}           $$R_{y} = \ \begin{bmatrix}
  1 & 0 & 0 \\                        \cos(\alpha) & \ 0\  & \sin(\alpha) \\
  0 & \cos(\beta) & - sin(\beta) \\   \ 0\  & \ 1\  & \ 0\  \\
  0 & sin(\beta) & \cos(\beta)        \  - \sin(\alpha) & \ 0\  & \cos(\alpha)
  \end{bmatrix}$$                     \end{bmatrix}$$

  The combined rotation matrix is     
  computed as:                        
  $R\  = \ R_{y} \cdot R_{x}$         
  ------------------------------------------------------------------------------

  : []{#_Toc205224386 .anchor}Figure ‎2.4 Maximal Recoverability Boundary

> Each corner $(x,y,0)$ is mapped to
> $\left( x^{'},y^{'},z^{'} \right)^{T} = R\,\left\lbrack x - c_{x},\ \ y - c_{y},\ \ 0 \right\rbrack^{T}$,
>
> where $c_{x} = x + \frac{w}{2}$, $c_{y} = \ y + \frac{h}{2}$ are the
> plate's center coordinates for rotation around the center. Then,
> rotated corners are projected back into a 2D plane via the perspective
> projection formula (Equation ‎8.3)

$$x_{p} = p_{x} + f \cdot \frac{x^{'}}{f + z^{'}}\ \ ,\quad y_{p} = p_{y} + f \cdot \frac{y^{'}}{f + z^{'}}$$

> Here, $(x',y',z')$ are the 3D coordinates and $(x_{p},\ y_{p},0)$ are
> the projected target coordinates.
>
> This is a pin-hole camera model with focal length $f$ and principal
> point $p$ \[2\](pages 33-66).

![](media/image16.png){width="4.6280686789151355in" height="4.25in"}

> With the source corners and the projected target corners, a
> perspective transform matrix $H$ is calculated using homography \[2\]
> (pages 66-88). (Equation ‎8.4)

$$\begin{bmatrix}
x^{'} \\
\ y^{'} \\
\ z^{'}
\end{bmatrix} = \ H\  \cdot \ \begin{bmatrix}
x \\
\ y\  \\
1
\end{bmatrix},\ \ H\  = \ \begin{bmatrix}
h_{11} & \ h_{12} & \ h_{13} \\
\ h_{21} & \ h_{22} & \ h_{23} \\
\ h_{31} & \ h_{32} & \ 1
\end{bmatrix}$$

> This matrix $H$ is then used to map the whole image to its projected
> version (Figure ‎8.5).
>
> ![](media/image17.png){width="4.984478346456693in"
> height="1.7286909448818897in"}

3.  **Noise Simulation**

> To mimic real-world camera captures, we apply a fixed sequence of
> synthetic noise effects to each warped image (Figure ‎8.6):
>
> **Double-edge blending:** Convolve the input $I_{0}$ with the
> Sobel-like kernel []{dir="rtl"}(Equation ‎8.5)
>
> $$S = \begin{bmatrix}
> 1 & 2 & 1 \\
> 0 & 0 & 0 \\
>  - 1 & - 2 & - 1
> \end{bmatrix}$$
>
> Then blend (Equation ‎8.6)
>
> $$I_{1} = 0.7\, I_{0} + 0.3\,\left( I_{0}*S \right)$$
>
> **White balance:** Split $I_{1}$ into channels
> $\left( I_{B},I_{G},I_{R} \right)$, draw scales
> $s_{R},\, s_{B} \sim U(0.8,1.2)$, and recombine (Equation ‎8.7)
>
> $$I_{2} = merge\left( s_{B}\, I_{B},\mspace{6mu} I_{G},\mspace{6mu} s_{R}\, I_{R} \right)$$
>
> **Gaussian blur:** Convolve $I_{2}$ with a 3×3 Gaussian kernel
> (Equation ‎8.8)
>
> $$G = \frac{1}{16}\begin{bmatrix}
> 1 & 2 & 1 \\
> 2 & 4 & 2 \\
> 1 & 2 & 1
> \end{bmatrix},\quad I_{3} = I_{2}*G$$
>
> **JPEG compression:** Simulate 8×8 block quantization with quality
> factor $Q = 20$ (Equation ‎8.9)
>
> $$I_{4} = JPEG\left( I_{3} \right)$$
>
> **Contrast and brightness adjustment:** Apply random $\alpha,\ \beta$
> (Equation ‎8.10)
>
> $$I_{5} = clip\left( \alpha\, I_{4} + \beta \right)$$
>
> **Additive Gaussian noise**: Sample
> $n \sim N\left( 0,\sigma^{2} \right)$ with $\sigma = 0.01 \times 255$
> and add to each channel (Equation ‎8.11)
>
> $$I_{6} = clip\left( I_{5} + n \right)$$
>
> ![](media/image18.png){width="5.271855861767279in"
> height="1.828358486439195in"}

4.  **Realignment and Downsampling**

> After noise injection, we apply the inverse homography $H^{- 1}$ to
> realign each warped image to its original orientation (Figure ‎8.7). We
> then crop the image to the base plate size (e.g., 512x128), apply a
> blur, and downsample it by a factor of two to obtain the final image
> with a smaller resolution, retaining most of the detail (256×64).
>
> We scale digit bounding boxes by the same factors to maintain the
> metadata aligned with the resized image.
>
> ![](media/image19.jpeg){width="3.805686789151356in"
> height="1.008180227471566in"}

5.  **Angles Sampling Strategy**

> Effective model training requires a dataset that emphasizes heavy
> perspective distortions. Uniformly sampling rotation angles
> $(\alpha,\beta)$ from the $\lbrack - 90,90\rbrack^{2}$ range would
> yield many images that are either nearly undistorted or excessively
> distorted, limiting their usefulness.
>
> Instead, we select angles primarily from a region where distortions
> provide the most useful training data for models to generalize well
> across all angle ranges, especially at extreme angles.
>
> First, we define two boundary curves to restrict rotation angles in
> the first quadrant $\lbrack 0,89\rbrack^{2}$ (Equation ‎8.12)
>
> (Superellipse function in the first quadrant:
> $ y(x) = b\lbrack 1 - (x/a)^{\, n}\rbrack^{1/n}$, $y,x \geq 0$)
>
> $$L(t) = l_{\max}\left( 1 - \left( \frac{t}{l_{\max}} \right)^{l} \right)^{\frac{1}{l}},\quad U(t) = u_{\max}\left( 1 - \left( \frac{t}{u_{\max}} \right)^{u} \right)^{\frac{1}{u}}$$
>
> where $l_{\max}$, $u_{\max}$, $l$, and $u$ control the curve shape.
> These curves establish the lower and upper limits of one angle for
> each value of the other.
>
> The hard mask $M(\alpha,\beta)$ is then constructed (Equation ‎8.13)
>
> $$M(\alpha,\beta) = \left\{ \begin{matrix}
> 1, & L(\alpha) \leq \beta \leq U(\alpha)\ ,\ L(\beta) \leq \alpha \leq U(\beta) \\
> 0, & \text{otherwise}
> \end{matrix} \right.\ $$
>
> (Figure ‎8.8) illustrates the curves (Equation ‎8.12) and the region
> $M(\alpha,\beta)$ (Equation ‎8.13).
>
> Next, we compute the signed-distance field by applying Euclidean
> distance transforms to the mask. $d_{in}$ is the distance to the
> nearest point where $M = 1$ and $d_{out}$ is the distance to the
> nearest point where $M = 0$, then (Equation ‎8.14)
>
> $$d(\alpha,\beta) = d_{in}(\alpha,\beta) - d_{out}(\alpha,\beta)$$
>
> produces positive values inside the mask and negative values outside.
> (Figure ‎8.9) displays this map.

  ----------------------------------------------------------------------------------------------------------
  ![](media/image20.png){width="2.967646544181977in"   ![](media/image21.png){width="3.0020286526684163in"
  height="2.5659339457567802in"}                       height="2.5652777777777778in"}
  ---------------------------------------------------- -----------------------------------------------------
                                                       

  ----------------------------------------------------------------------------------------------------------

  : []{#_Ref200906097 .anchor}Figure ‎5.4 U-Net Architecture

> To avoid a sharp transition at the mask boundary, we apply logistic
> smoothing (Equation ‎8.15)
>
> $$\Lambda(\alpha,\beta) = \frac{1}{\, 1 + e^{- d(\alpha,\beta)/s}}$$
>
> where $s$ is the smoothing scale. This yields a continuous weight
> between 0 and 1 across the edge. (Figure ‎8.10) shows the effect.
>
> Next, we apply a suppression factor to de-emphasize samples where only
> one angle is large. (Equation ‎8.16)
>
> $$\begin{matrix}
> a = \alpha/90 & b = \beta/90 \\
> m = \min(a,b) & M = \max(a,b)
> \end{matrix}$$
>
> $$S(\alpha,\beta) = m\mspace{6mu} + \mspace{6mu}(1 - m)\, M^{\, k}$$
>
> Large $k$ (e.g $25$) yields $S \approx 0$ when one angle is small and
> $S \approx m$ when both angles are moderately high, as shown in
> (Figure ‎8.11).

  --------------------------------------------------------------------------------------------------------
  ![](media/image22.png){width="2.967645450568679in"   ![](media/image23.png){width="2.96966426071741in"
  height="2.5659339457567802in"}                       height="2.567679352580927in"}
  ---------------------------------------------------- ---------------------------------------------------
                                                       

  --------------------------------------------------------------------------------------------------------

  : Equation ‎5.1

> We multiply smoothing and suppression to get the final weight
> (Equation ‎8.17)
>
> $$W(\alpha,\beta) = \Lambda(\alpha,\beta) \bullet S(\alpha,\beta)$$
>
> Finally, to get a PDF, this weight is normalized by integrating over
> the grid (Equation ‎8.18)
>
> $$p(\alpha,\beta) = \frac{W(\alpha,\beta)}{\iint W(\alpha,\beta)\, d\alpha\, d\beta}$$
>
> so that $\iint p\, d\alpha\, d\beta = 1$. (Figure ‎8.12) presents the
> resulting sampling distribution.
>
> ![](media/image24.png){width="3.9365168416447944in"
> height="3.27082895888014in"}
>
> To sample rotation angles $(\alpha,\beta)$ from the PDF (Figure ‎8.12),
> we employ a 3-dimensional Sobol sequence \[5\]. Sobol sampling ensures
> uniform coverage of the sampling region, with lower dispersion and
> fewer gaps than uniform random draws.
>
> ([]{dir="rtl"}Figure ‎8.13) shows a comparison between uniform random
> samples and Sobol samples drawn from $p(\alpha,\beta)$. As we can
> observe, the Sobol set exhibits visibly lower dispersion, which helps
> the models learn from a more balanced range of distortions.

![](media/image25.png){width="6.270357611548556in"
height="3.1908180227471568in"}

> To generate samples in the $\lbrack - 90,90\rbrack^{2}$ range, we
> first draw $N = 2^{m}$ scrambled Sobol triples
> $\left( u_{0},u_{1},u_{2} \right)$ in $\lbrack 0,1\rbrack^{3}$, see
> (Figure ‎8.14).
>
> The Sobol sequence is designed so that, when we generate exactly
> $2^{m}$ points, any equal partition of one coordinate contains the
> same number of samples. That is, splitting $u_{2}$ into four intervals
> of length 0.25 and projecting them to $\left( u_{0},u_{1} \right)$
> yields $N/4$ samples in each, see (Figure ‎8.15).
>
> ![](media/image26.png){width="5.210917541557305in"
> height="3.9081889763779527in"}
>
> ![](media/image27.png){width="4.997566710411198in"
> height="4.822864173228346in"}
>
> We map each $\left( u_{0},u_{1} \right)$ pair into
> $(\alpha,\beta) \in \lbrack 0,89\rbrack^{2}$ by inverting the CDFs of
> our target PDF (Equation ‎8.18). We define the marginal CDF of $\alpha$
> (Equation ‎8.19)
>
> $$F_{\alpha}(a) = \int_{0}^{a}\int_{0}^{89}p(\alpha',\beta')\, d\beta'\, d\alpha'$$
>
> compute $\alpha$ (Equation ‎8.20)
>
> $$\alpha = F_{\alpha}^{- 1}\left( u_{0} \right)$$
>
> Given $\alpha$, the conditional CDF of $\beta$ is (Equation ‎8.21)
>
> $$F_{\beta \mid \alpha}(b \mid \alpha) = \frac{\int_{0}^{b}p(\alpha,\beta')\, d\beta'}{\int_{0}^{89}p(\alpha,\beta')\, d\beta'}$$
>
> compute $\beta$ (Equation ‎8.22)
>
> $$\beta = F_{\beta \mid \alpha}^{- 1}\left( u_{1} \mid \alpha \right)$$
>
> Next, we fold each $(\alpha,\beta)$ into the
> $\lbrack - 90,90\rbrack^{2}$ range by partitioning $u_{2}$ into four
> equal intervals. Each interval assigns one sign combination
> $( \pm \alpha, \pm \beta)$, ensuring exactly one quarter of the
> samples lie in each quadrant. This folding produces a complete,
> balanced grid of angle pairs (Figure ‎8.16) to form our dataset.
>
> ![](media/image28.png){width="5.447755905511811in"
> height="5.427372047244094in"}
>
> Next, we construct three training sets to determine which provides the
> most beneficial data for models to generalize across the full-grid
> test set (or our region of interest), given that not all samples carry
> useful information.
>
> For each dataset, we independently generate Sobol samples for the
> training, validation, and test subsets in an 80/10/10 ratio, each with
> a size that is a power of two as required by Sobol sequences.
>
> **Dataset A** uses base parameters and has 10240 samples
> (8192/1024/1024 train/val/test).
>
> **Dataset B** retains the same parameters as **dataset A** but doubles
> the total number of samples to 20480 (16384/2048/2048 train/val/test.
> This allows us to test whether models perform better when given a
> larger dataset (diffusion commonly requires large datasets). The
> larger set may have additional information not included in dataset A.
>
> **Dataset C** applies a second parameter set that shifts the PDF
> toward higher $\alpha$ and $\beta$ values, emphasizing more extreme
> distortions. For this set, we generate 10240 samples (8192/1024/1024
> train/val/test)
>
> (Figure ‎8.17) illustrates the Sobol samples in the first quadrant of A
> and C datasets.
>
> ![](media/image29.png){width="6.202944006999125in" height="3.15625in"}

6.  **Algorithmic Workflow**

```{=html}
<!-- -->
```
a.  **Initialize execution:** seed RNGs; set plate dimensions, and other
    plate parameters.

b.  **Select dataset subset:** choose target split for train,
    validation, test subsets (e.g, 80/10/10) and its sample count.

c.  **Build data list:**

    -   **Train, validation, and test subsets**: draw Sobol samples in
        $(\alpha,\beta) \in \lbrack - 90,90\rbrack^{2}$ from the defined
        PDF.

    -   **Full-grid test set:** draw $N$ samples (e.g., $N = 5$) per
        integer pair $(\alpha,\beta) \in \lbrack 0,89\rbrack^{2}$.

d.  **Generate license plates:** create clean plates with a random
    6-digit number.

e.  **Warp plates**: apply a 3D perspective transform using the selected
    $(\alpha,\beta)$.

f.  **Inject noise**: edge blending, white balance, blur, JPEG,
    contrast/brightness adjustment, Gaussian noise

g.  **Dewarp plates:** apply inverse homography to realign to the
    original orientation.

h.  **Crop and Downsample:** realign to the desired dimension and
    resolution.

i.  **Create and split datasets:** partition the Sobol-sampled plates
    into training, validation, and test subsets; create the full grid
    for final evaluation.

j.  **Save and annotate** write clean/distorted PNGs and append metadata
    (index, plate number, $\alpha$, $\beta$, bounding boxes).

k.  **Repeat steps 2--10:** for every required subset; each subset is
    generated in its own directory with a metadata.json file.

## Model Implementation

1.  **Conditioning Mechanisms**

> Conditioning mechanisms enable image-to-image models to utilize
> external information, such as a distorted input, to inform
> restoration. We focus on three main strategies in our implementations:
> channel concatenation, feature-wise linear modulation (FiLM) \[28\],
> and cross-attention \[29\].
>
> In **channel concatenation**, the conditioning image is added by
> stacking its channels with the model's inputs. In Pix2Pix, the
> generator receives only the three-channel distorted plate, while the
> discriminator sees a six-channel tensor formed by concatenating the
> distorted and real (or generated) plates. In SR3 diffusion, we stack
> the three-channel distorted plate with its three-channel noisy latent
> to produce the U-Net's six-channel input.
>
> In **FiLM**, we encode the distorted plate into a vector $z$ of low
> dimension. Each FiLM block then computes learned parameters
> $\gamma(z),\beta(z)$, applying them via $h^{'}$ to feature map $h$.
> (Equation ‎8.23)
>
> $$\mathbf{h}^{\mathbf{'}}\mathbf{=}\mathbf{\gamma}\left( \mathbf{z} \right)\mathbf{\odot}\mathbf{h}\mathbf{+}\mathbf{\beta}\left( \mathbf{z} \right)$$
>
> $\odot$ denotes element-wise multiplication. This adaptive scaling and
> shifting help attend to distorted images and adjust feature maps
> according to specific distortion patterns. Our conditional U-Net
> implements FiLM blocks at each encoder and decoder stage. SR3
> diffusion uses FiLM for timestep embeddings.**\
> ** In **cross-attention**, the network first processes the distorted
> image into feature maps. Then, for each pixel it tries to reconstruct
> in the output, the model examines all regions of the distorted input
> and learns which areas to focus on most. This means each output pixel
> can selectively draw information from any part of the distorted plate.
> It is a powerful mechanism, but it is highly computationally
> expensive.**\
> Self-attention** enables each pixel in a feature map to compare itself
> with every other pixel in that map. This is like cross-attention but
> attends to internal features rather than the conditional image.
> Self-attention is used in Restormer, a transformer-based U-net.

2.  **U-Net**

> U-Net \[1\] is built with a contracting path and an expanding path. In
> the contracting path, each stage applies two 3×3 convolutions. The
> original U-Net employed valid (unpadded) convolutions without batch
> normalization, which necessitated cropping feature maps before
> concatenation in the decoder. It was designed for single-channel
> grayscale input and produced multi-channel segmentation maps, where
> each output channel represented a target class.\
> For restoration, we employ 3×3 padded convolutions to maintain spatial
> dimensions and add batch normalization after each convolution to
> stabilize training. Since our task is to reconstruct color images
> rather than predict class labels, we configure the network for
> three-channel RGB input and three-channel output. Each down-sampling
> step utilizes a 2×2 max pooling layer, which halves the spatial size
> and doubles the number of feature channels.\
> In the expanding path, each stage up-samples features with a 2×2
> transposed convolution and concatenates with encoder features via skip
> connections. Two more 3×3 padded convolutions with batch normalization
> and ReLU are then applied. A final 1×1 convolution projects features
> to the required output channels. See original architecture overview
> (Figure ‎5.4). The overall structure preserves the original U--Net\'s
> symmetric encoder--decoder design but adapts its components for image
> restoration.

3.  **U-Net Conditional**

> We extend the base U-Net by integrating FiLM at each convolutional
> block. A noise encoder processes the distorted plate into a compact
> latent vector $z$ that describes the distortion pattern. At every
> encoder and decoder stage, FiLM uses $z$ to produce channel-wise scale
> $\gamma(z)$ and shift $\beta(z).$ These parameters modulate each
> feature map, so that activations are dynamically scaled and shifted
> according to the input's distortion. This process is defined in
> (Equation ‎8.23).
>
> This way, the network can adapt its internal features to emphasize
> undistorted content and suppress artifacts specific to each image.
> Downsampling and upsampling remain unchanged from the base U-Net. FiLM
> conditioning is lightweight; it adds few parameters and keeps
> inference efficient, while potentially improving restoration.

4.  **Restormer**

> Another model is Restormer \[11\]. It is an encoder--decoder model
> designed for high-resolution image restoration. The model follows a
> U-Net--like structure but replaces standard convolutional blocks with
> Transformer blocks (Figure ‎8.18). They capture both local and global
> context and are much more precise than convolutions.
>
> At each stage, the model processes a layer-normalized feature tensor
> $Y \in \mathbb{R}^{H \times W \times C}$, where $H$ is the height, $W$
> is the width, and $C$ is the channel dimension. The Multi-Dconv Head
> Transposed Attention (MDTA) module computes queries, keys, and values
> by applying parallel $1 \times 1$ point-wise convolutions
> $W_{\cdot}^{p}$ and $3 \times 3$ depth-wise convolutions
> $W_{\cdot}^{d}$ (Equation ‎8.24)
>
> $Q = W_{Q}^{d}W_{Q}^{p}(Y),\ \ K = W_{K}^{d}W_{K}^{p}(Y),\ \ \ V = W_{V}^{d}W_{V}^{p}(Y),\ \ $​
>
> The resulting tensors are reshaped as
> $\widehat{Q},\widehat{V} \in \mathbb{R}^{HW \times C}$ and
> $\widehat{K} \in \mathbb{R}^{C \times HW}$. Attention is then
> calculated across channels (Equation ‎8.25)
>
> $$Attention\left( \widehat{Q},\widehat{K},\widehat{V} \right) = \widehat{V}\ Softmax\left( \frac{\widehat{K}\widehat{Q}}{\alpha} \right)$$
>
> where $\alpha$ is a learned scaling parameter. The attention output is
> projected back and added to the input through a residual connection.
>
> To complement this mechanism, the Gated-Dconv Feed-Forward Network
> (GDFN) extends the standard feed-forward module. For input
> $X \in \mathbb{R}^{H \times W \times C}$, the module applies two sets
> of $1 \times 1$ point-wise convolutions $W_{p}^{i}$ and $3 \times 3$
> depth-wise convolutions $W_{d}^{i}$, followed by a gating mechanism
> (Equation ‎8.26)
>
> $$Gating(X) = \phi\left( W_{d}^{1}W_{p}^{1}\left( LN(X) \right) \right)\bigodot\left( W_{d}^{2}W_{p}^{2}\left( LN(X) \right) \right)$$
>
> Where $\phi$ is the GELU activation, LN is layer normalization, and
> $\odot$ denotes element-wise multiplication. This design has been
> proven to perform well on denoising tasks.
>
> ![](media/image30.png){width="6.109090113735783in"
> height="2.3785859580052495in"}

5.  **GAN -- Pix2pix**

> **Pix2Pix** \[15\] is a Conditional GAN supervised image-to-image
> translation. In Pix2pix, the generator is a U-Net model that learns to
> map distorted images to their restored counterparts. The discriminator
> uses PatchGAN. Rather than evaluating the whole image, PatchGAN judges
> the realism of local patches. This enables the model to enforce local
> consistency and structure.
>
> The discriminator receives image pairs as input. Each pair consists of
> a distorted image and either the original or the generated image, both
> with three channels. These images are concatenated along the channel
> dimension to form a six-channel tensor. For real inputs, the pair is
> \[distorted image, original image\]. For fake inputs, the pair is
> \[distorted image, generated image\]. The PatchGAN discriminator
> predicts whether each local patch in a pair is real or fake.
>
> The generator is trained to minimize two losses: an adversarial loss
> (Equation ‎8.27), which measures how well the generated image fools the
> discriminator. A L1 loss (Equation ‎8.28), which measures the
> pixel-wise difference between the generated image and the ground
> truth.
>
> $$L_{cGAN}(G,D) = E_{x,y}\left\lbrack logD(x,y) \right\rbrack + E_{x,z}\left\lbrack \log\left( 1 - D\left( x,G(x,z) \right) \right) \right\rbrack$$
>
> $$L_{1}(G) = E_{x,y,z}\left\lbrack \left\| y - G(x,z) \right\| \right\rbrack\ $$
>
> where $x$ is the input, $y$ is the ground truth, and $G(x,z)$ is the
> generated image.
>
> $D(x,y)$ and $D(x,G(x,z))$ represent the discriminator\'s predictions
> for real and fake images (Figure ‎8.19), respectively.
>
> ![](media/image31.png){width="5.180608048993876in"
> height="1.7440376202974628in"}
>
> The final objective for Pix2Pix is a weighted combination of these two
> losses:
>
> $$G^{*} = arg\min_{G}{\max_{D}{L_{cGAN}(G,D) + {\lambda L}_{1}(G)}}$$
>
> $\lambda$ []{dir="rtl"}is a regularization hyperparameter balancing
> the losses.

6.  **Diffusion []{dir="rtl"}-- SR3**

> We adapt SR3 \[20\], a super-resolution diffusion model, but condition
> on the distorted plate instead of a low-resolution image. At each
> timestep, we concatenate the noisy plate $x_{t}$ and the distorted
> image $x_{d}$ as the condition. This forms a six-channel input.
>
> In standard DDPMs \[3\], the forward noising at timestep *t* is a
> Markovian process defined by (Equation ‎8.30)
>
> $$q\left( xₜ \middle| x_{t - 1} \right)\mathcal{= \ N}\left( xₜ;\sqrt{1 - \beta ₜ}\ x_{t - 1},\ \beta ₜI \right)\  \Rightarrow \ xₜ\  = \ \sqrt{{\bar{\alpha}}_{t}}x_{0} + \ \sqrt{1 - {\bar{\alpha}}_{t}}\,\epsilon$$
>
> where $\epsilon\mathcal{\sim N}(0,I)$ and
> ${\bar{\alpha}}_{t} = \prod_{i = 1}^{t}\left( 1 - \beta_{i} \right)$
> is the cumulative signal coefficient. The SNR at each step is the
> ratio of preserved signal energy ${\bar{\alpha}}_{t}$ to added noise
> $1 - {\bar{\alpha}}_{t}$, and it decreases over $t$.
>
> For uniform regions, such as the solid yellow plate background, black
> digits, the local signal variance is zero, so the SNR is also zero. In
> standard $\epsilon$-prediction, the network is trained to recover the
> added noise via (Equation ‎8.31)
>
> $$L_{\text{noise}}(\theta) = \mathbb{E}_{x_{0},t,\epsilon}\, \parallel \epsilon - \epsilon_{\theta}\left( x_{t},t,x_{d} \right) \parallel^{2}$$
>
> but in regions where $\epsilon_{t} \rightarrow 0$, the loss provides
> almost no gradient. This leaves residual speckle after denoising.
>
> To address this, we instead predict the velocity parameter $v_{t}$,
> following \[30\] (Equation ‎8.32)
>
> $$v_{t} = \sqrt{\alpha_{t}}\,\epsilon - \sqrt{1 - {\bar{\alpha}}_{t}}\, x_{0}$$
>
> This angular velocity remains nonzero even in low-SNR regions, so the
> model always has a meaningful learning target. (Equation ‎8.33)
>
> $$L_{\text{vel}}(\theta) = \mathbb{E}_{x_{0},t,\epsilon}\, \parallel v_{t} - v_{\theta}\left( x_{t},x_{d},\sqrt{{\bar{\alpha}}_{t}} \right) \parallel^{2}$$
>
> This loss leads to cleaner license plates.
>
> At each step, we encode the noise level $\sqrt{{\bar{\alpha}}_{t}}$
> into a sinusoidal embedding. This embedding utilizes sine and cosine
> functions at exponentially increasing frequencies, resulting in a
> continuous and unique code for each time step. The embedding is
> processed by a small MLP and injected into each residual block with
> FiLM conditioning. This lets the model adjust its activations in
> response to both the noise level and the distorted input.
>
> The U-Net backbone has five levels with paired residual blocks and
> self-attention at the bottleneck. Downsampling uses strided
> convolutions; upsampling uses nearest-neighbor interpolation and
> convolution. The activation is SiLU.
>
> During inference, we use DDIM sampling \[31\]. At each step, we first
> estimate the clean image (Equation ‎8.34)
>
> $${\widehat{x}}_{0} = \frac{x_{t} - \sqrt{1 - {\bar{\alpha}}_{t}}\,\epsilon_{\theta}\left( x_{t},t,x_{d} \right)}{\sqrt{{\bar{\alpha}}_{t}}}$$
>
> The next state is then computed (Equation ‎8.35)
>
> $$x_{t - 1} = \sqrt{{\bar{\alpha}}_{t - 1}}\,{\widehat{x}}_{0} + \sqrt{1 - {\bar{\alpha}}_{t - 1} - \sigma_{t}^{2}}\,\epsilon_{\theta}\left( x_{t},t,x_{d} \right) + \sigma_{t}\, z,\quad z\mathcal{\sim N}(0,I)$$
>
> Setting $\sigma_{t} = 0$ makes the update fully deterministic. This
> approach preserves fine details and reduces the number of required
> sampling steps from hundreds to as few as 10--20.

7.  **Algorithmic Workflow**

```{=html}
<!-- -->
```
a.  **Initialize Model**: set hyperparameters, initialize the Data
    Loader, and define necessary transforms.

b.  **Define Loss Function**: select appropriate loss functions (e.g.,
    MSELoss for U-Net, adversarial loss for GANs).

c.  **Set Optimizer**: configure the optimizer (e.g., SGD, Adam, AdamW)
    with selected hyperparameters.

d.  **Set Scheduler**: configure a learning rate scheduler (e.g.,
    ReduceLROnPlateau, CosineAnnealingLR) if needed.

e.  **Load data**: use the Data Loader to batch and feed training data.

f.  **Train**:

-   **Forward Pass**: compute model outputs for input batches.

-   **Compute Loss**: evaluate the discrepancy between outputs and
    ground truth.

-   **Backward Pass**: perform backpropagation to compute gradients.

-   **Parameter Update**: adjust model weights based on gradients.

g.  **Validation**: assess model performance on validation set,
    monitoring PSNR and SSIM metrics.

h.  **Checkpointing**: Save the model state whenever validation
    performance improves.

i.  **Iterate**: Continue training for the specified number of
    epochs/steps or until the convergence criteria are met.

## Model Evaluation

> We begin by loading the checkpoint that achieved the highest
> validation score. For each dataset, every model processes its held-out
> test split. We compute mean PSNR, SSIM, training time, and latency.
> Alongside, we examine the visual appearance of restored images to
> identify each model's typical patterns and artifacts.
>
> Next, we assess generalization on the common full grid of angle pairs.
> The grid spans all ($\alpha,\,\beta) \in \lbrack 0,89\rbrack ².$ For
> each angle pair where $\alpha \leq 60\  \cap \beta \leq 60$, we
> include 2 distinct plate images. For the complementary region where
> $\alpha > 60\  \cup \ \beta > 60$, we sample 10 plate images per
> ($\alpha,\,\beta)$. This sampling focuses on severe distortions. The
> lower-angle region is included for completeness, as all models
> reliably reconstruct these cases.
>
> We collect six metrics over the full grid of distortion angles. For
> each pair $(\alpha,\beta)$, we compute and store the worst digit-level
> PSNR and SSIM, the plate-level PSNR and SSIM, the digit-level OCR
> accuracy, and the plate-level OCR accuracy. Each metric forms a
> matrix. These matrices are visualized as heatmaps, which provide a
> spatial view of how model performance changes across different
> distortion levels. We primarily focus on plate-level OCR accuracy.
>
> From the plate-level OCR accuracy heatmap, we derive a single
> recoverability measure and compute its coverage. We define
> $f(\alpha,\beta) = \text{OCR}_{\text{plate}}(\alpha,\beta)\  \in \lbrack 0,1\rbrack$
>
> Choosing a success threshold $T \in \lbrack 0,1\rbrack$ (for example,
> $T = 0.9$), we identify the set of all angle pairs where recognition
> meets or exceeds this value. To describe the outer edge of this
> region, we define two functions (Equation ‎8.36)
>
> $$\beta_{\max}(\alpha) = \max\left( \left\{ 0 \right\} \cup \ \{\beta \in \lbrack 0,89\rbrack\ |\ f(\alpha,\beta) \geq T\} \right)$$
>
> $$\alpha_{\max}(\beta) = \max\left( \left\{ 0 \right\} \cup \ \{\alpha \in \lbrack 0,89\rbrack\ |\ f(\alpha,\beta) \geq T\} \right)$$
>
> These functions mark the outer edge of the region where the model
> meets the chosen threshold.
>
> The full recoverability boundary is given by the union of the two
> curves
>
> $$B_{T} = C1 \cup C2$$

$$C_{1} = \left\{ \left( \alpha,\mspace{6mu}\beta_{\max}(\alpha) \right)\  \middle| 0 \leq \alpha \leq 89 \right\},\quad C_{2} = \left\{ \left( \alpha_{\max}(\beta),\mspace{6mu}\beta \right)\  \right|\ 0 \leq \beta \leq 89\}$$

> Traversing $C_{1}$ from $\alpha = 0$ to $89$, then returning along
> $C_{2}$, creates a closed contour that encloses the region where
> $f(\alpha,\beta) \geq T$.
>
> We then compute the region area $E$ as a sum of two directional areas
> (Equation ‎8.38)
>
> $$E = \frac{1}{2}\left( \int_{0}^{89}\beta_{\max}(\alpha)\, d\alpha\  + \int_{0}^{89}\alpha_{\max}(\beta)\, d\beta \right)$$
>
> Averaging and normalizing by the total grid area $89^{2}$ yields the
> boundary-AUC (Equation ‎8.39)
>
> $$AUC = \frac{E}{89^{2}}\  \in \lbrack 0,1\rbrack$$
>
> The boundary-AUC measures the largest fraction of the $(\alpha,\beta)$
> grid enclosed by the recoverability boundary. A higher AUC indicates
> that a model can reconstruct license plates across a wider range of
> angle pairs. This approach reduces the two-dimensional heatmap to a
> single coverage metric for direct model comparison. (Figure ‎8.20)
> Illustrates the recoverability boundary and the area under it.
>
> ![](media/image32.png){width="6.376820866141732in"
> height="3.0318088363954505in"}
>
> Because scattered failures under the recoverability boundary occur, we
> also measure how often and how deeply these interior failures appear.
> For every failed angle pair $\left( \alpha_{h},\beta_{h} \right)$ that
> falls inside $B_{T}$, we compute its shortest Euclidean distance to
> the boundary (Equation ‎8.40)
>
> $$d_{h} = \min_{\left( \alpha_{b},\,\beta_{b} \right) \in B_{T}}\sqrt{\left( \alpha_{h} - \alpha_{b} \right)^{2} + \left( \beta_{h} - \beta_{b} \right)^{2}}$$
>
> For $N$ such failures, we aggregate those distances into a single
> "reliability" score $F$ by computing the root-mean-square (RMS) of all
> such distances, normalized by the total area enclosed by the
> recoverability boundary $E$ (Equation ‎8.41)
>
> $$F = \sqrt{\frac{1}{E}\sum_{h = 1}^{N}d_{h}^{2}}$$
>
> A value of $F = 0$ means there are no interior failures, while a
> larger $F$ indicates that failures are either more numerous, deeper,
> or both. In this way, $F$ captures the "variance" of recoverability in
> a single, interpretable metric that complements the boundary-AUC: one
> measures the **extent** of recoverability, the other its
> **consistency**.
>
> []{dir="rtl"}Finally, to analyze performance in a specific part of the
> angle grid, we define a region of interest
> $R \subseteq \lbrack 0,89\rbrack^{2}$. For example,
> $R = \{(\alpha,\beta) \mid \alpha \geq 80 \cup \beta \geq 80\}$.
>
> For each model, we calculate the mean of PSNR, worst-case PSNR, SSIM,
> worst-case SSIM, digit-level OCR, and plate-level OCR within $R$. We
> then display these mean scores as bar plots, where each bar represents
> the typical performance of a model under extreme distortions.
>
> Tesseract OCR (version 4, in LTSM mode) is used in digit-only mode as
> we use a 0-9 only symbols filter. Each restored plate image is
> converted to grayscale and contrast-normalized. Digit patches are
> upscaled by a factor of two. Then we binarize by simple fixed
> thresholding. If this produces a valid digit, the result is accepted.
> If the result is empty or not a digit, we continue to additional
> thresholding methods (e.g., Otsu, adaptive) and inverting the patch
> color. If a digit isn\'t recognized, we apply the same sequence of OCR
> steps to the whole plate region using single-line mode. The missing
> digit is then filled by taking the character at the corresponding
> position in the recognized plate string. We repeat this process until
> a digit is recognized; if not, we assign "0" as a placeholder. The
> final recognized string is compared to the ground truth to compute
> digit-level and plate-level OCR accuracy.

1.  **Algorithmic Workflow**

```{=html}
<!-- -->
```
a.  **Load Test Images:** load test dataset/full grid images.

b.  **Perform Inference:** reconstruct images by applying each trained
    model to the distorted inputs.

c.  **Compute Metrics:** for each reconstructed image, calculate
    metrics.

d.  **Collect Results:** organize and save metrics in a structured data
    frame.

e.  **Visualize Metrics:** produce metric tables, heatmaps,
    recoverability boundary curves, scatter plots, bar plots, and error
    bars.

## Model Comparison

> We compare every model using the metrics defined in Model Evaluation.
> First, we overlay the recoverability boundaries for all model-dataset
> pairs on one plot; this reveals which curves extend furthest and
> highlights their overlaps. We then compute each pair's boundary-AUC
> and RMS failure distance ($F$), and add the maximal recoverability
> curve, showing the best coverage any model achieves. Bar plots
> summarize mean metric values within high-distortion regions.
>
> Finally, to assess whether improvements in image-quality metrics lead
> to better recognition, we compare the mean plate-level OCR accuracy
> against a single quality metric $x$ (either PSNR or SSIM) for each
> angle pair $i$. We denote $y_{i} = OCR_{i}$ and plot the pairs and fit
> with a linear line (Equation ‎8.42):
>
> $${\widehat{y}}_{i} = mx_{i} + b$$
>
> We then compute the coefficient of determination $R^{2}$ (Equation
> ‎8.43)
>
> $$R^{2} = 1 - \frac{\sum_{i}^{}\left( y_{i} - {\widehat{y}}_{i} \right)^{2}}{\sum_{i}^{}\left( y_{i} - \overline{y} \right)^{2}}$$
>
> where ${\widehat{y}}_{i}$ is the value predicted by the line and
> $\overline{y}$ is the mean observed OCR accuracy. $R^{2}$ quantifies
> the fraction of the total variation in recognition that can be
> explained by changes in $q$.
>
> A High $R^{2}$ value indicates a strong linear relationship---most of
> the rise and fall in OCR can be predicted by proportional changes in
> x, so each unit increase in the metric results in a consistent gain in
> OCR accuracy. A lower $R^{2}$ suggests a weaker or non-linear
> relationship; in these cases, metric gains may not improve OCR until a
> threshold is reached or may not improve linearly. The $R^{2}$
> statistic and the scatter-fit plot help us judge whether PSNR or SSIM
> serves as a reliable proxy for OCR accuracy.
>
> This lets us optimize PSNR or SSIM during training and avoid costly
> OCR evaluations.

## Conclusion 

> We use the results from model comparison to answer the research
> question: at which viewing angles can different models reconstruct
> license plates that are unrecognizable to humans, and what is the
> limit of recoverable data in distorted images?
>
> By examining recoverability boundaries, AUC values, and bar plots, we
> identify the angles and conditions where plate information can be
> recovered and where it is lost. This phase clarifies how model choice
> and the training dataset affect the threshold for successful
> recognition and how much useful signal remains in the images under
> severe distortion.

# Results

## Training Results

We trained each model for a fixed number of epochs (or steps for
diffusion models) and ensured convergence without overfitting. Using a
validation set, we tuned hyperparameters for optimal performance.
Results are reported on each dataset's unseen 10% test split
[]{dir="rtl"}(Figure ‎9.1). For a detailed overview of hyperparameters,
see Appendix (‎13.4.1).

**Note**: At this stage, we do not compare models across datasets. Each
model is evaluated only on its own dataset's validation and test splits.
In section (‎9.2) we compare all models on a shared full grid set.

  -----------------------------------------------------------------------------------------------
                  Dataset A          Dataset B          Dataset C          Efficiency   
  --------------- --------- -------- --------- -------- --------- -------- ------------ ---------
  Model           PSNR      SSIM     PSNR      SSIM     PSNR      SSIM     Train Time   Latency
                                                                           Norm         (ms)

  U-Net           23.66     0.9705   24.45     0.9762   20.96     0.9464   1.00         11.75
  (baseline)                                                                            

  U-Net           24.18     0.9743   24.70     0.9773   21.35     0.9508   1.19         7.50
  Conditional                                                                           

  Restormer       24.71     0.9762   25.34     0.9777   21.67     0.9563   14.87        14.01

  GAN-pix2pix     23.21     0.9672   23.48     0.9708   19.97     0.9177   1.23         7.34

  Diffusion-SR3   21.74     0.9315   21.74     0.9407   19.34     0.9052   4.69         21.81
  -----------------------------------------------------------------------------------------------

  : []{#_Ref200906191 .anchor}Figure ‎5.5 GANs Conceptual Overview

Compared to the U-Net baseline,

On **Dataset A** (Figure ‎9.1), Restormer outperforms by 4.5% PSNR and
0.6% SSIM. U-Net Conditional outperforms by 2.2% PSNR and 0.4% SSIM.
GAN-pix2pix underperforms by 2% PSNR and 0.4% SSIM. Diffusion-SR3
underperforms by 8% PSNR and 4% SSIM.

> ![](media/image33.png){width="6.309581146106737in"
> height="2.855297462817148in"}

On **Dataset B** (Figure ‎9.2), Restormer outperforms by 3.6% PSNR and
0.15% SSIM. U-Net Conditional outperforms by 1% PSNR and 0.1% SSIM.
GAN-pix2pix underperforms by 4% PSNR and 0.4% SSIM. Diffusion-SR3
underperforms by 11% PSNR and 3.5% SSIM.

> ![](media/image34.png){width="6.223468941382327in"
> height="2.8159995625546808in"}

On **Dataset C** (Figure ‎9.3), Restormer outperforms by 3.4% PSNR and 1%
SSIM. U-Net Conditional outperforms by 1.9% PSNR and 0.5% SSIM.
GAN-pix2pix underperforms by 4.8% PSNR and 2.1% SSIM. Diffusion-SR3
underperforms by 7.8% PSNR and 4.3% SSIM.

> ![](media/image35.png){width="6.2402821522309715in"
> height="2.823611111111111in"}

Restormer consistently outperforms U-Net across all datasets.
Diffusion-SR3 shows the largest performance drop. U-Net Conditional and
GAN-pix2pix remain between these two in both metrics.

Efficiency (Figure ‎9.4) results show that U-Net training is fastest
(normalized time 1.00) with a latency of 11.75ms. U-Net Conditional
requires 1.18 times the training time but achieves a lower latency of
7.50ms. Restormer is the most computationally demanding, requiring 15
times the training time and exhibiting a latency of 14.01ms, which is
twice that of U-Net. GAN-pix2pix is like U-Net Conditional in training
time. Diffusion-SR3 requires 4.69 times the training time and, due to
its stepping denoising, exhibits the highest latency at 21.81ms.

> ![](media/image36.png){width="6.114856736657917in" height="2.52in"}

These results provide a general ranking, but the appearance of
reconstructed images and failure patterns varies across models, see
(Figure ‎9.5):

-   **Discriminative models** (U-Net, U-Net Conditional, Restormer)
    respond to low signal by producing blurred or ambiguous digits. In
    some cases, a digit region may merge features from several digits at
    once (for example, a blend of "8," "3," and "6") or display
    artifacts rather than a clear character.
-   **GAN-pix2pix** typically generates fewer blurry digits than U-Net
    variants but more often creates hybrid or incomplete digits. These
    may appear as digits with missing segments or as a composite of
    several digit shapes. Also, digits may appear with color artifacts.
-   **Diffusion models** always produce samples from the clean plate
    distribution, so the output visually resembles a clean license
    plate, even when the input is heavily distorted. However, in areas
    where a signal is too weak, diffusion models tend to hallucinate
    digits and generate plausible but incorrect plate numbers.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image37.png){width="2.1272779965004376in"   ![](media/image38.png){width="2.135022965879265in"   ![](media/image39.png){width="2.111750874890639in"
  height="5.345273403324584in"}                         height="5.376517935258093in"}                        height="5.30625in"}
  ----------------------------------------------------- ---------------------------------------------------- ----------------------------------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Equation ‎5.2

## Full Grid Evaluation Results

First, we present full-grid performance heatmaps. Since there are 15
models in total (five models evaluated on three datasets), we display
only the plate-level OCR accuracy heatmaps for Dataset B. See Appendix
(‎13.4.2) for results on the other datasets. All models perform
similarly, but visual inspection confirms that Restormer achieves the
best results.

Heatmaps (Figure ‎9.6) indicate that recognition is nearly perfect when
both $\alpha$ and $\beta$ are below $70 - 75{^\circ}$, whereas recovery
fails almost entirely once both exceed $80{^\circ}$, as shown in the
top-right corner. Along the extreme $\beta$ edge, accuracy stays high
for $\alpha$ up to about 60°, then declines steadily. In contrast, along
the extreme $\alpha$ edge, accuracy drops sooner, even at low $\beta$.
Notably, for $\alpha$ between $80{^\circ}$ and $89{^\circ}$, recognition
dips at low $(\beta \approx 0 - 8{^\circ})$ and moderate
$(\beta \approx 40 - 53{^\circ})$ $\beta$ values, with a partial
recovery in between. These patterns indicate the model handles high
$\beta$ better than high $\alpha$, and that certain $\alpha - \beta$
combinations consistently produce failures.

> ![](media/image40.png){width="6.025047025371829in"
> height="8.223412073490813in"}

Next, we overlay all recoverability boundaries for each model and
dataset (Figure ‎9.7). All boundaries are closely grouped, and the red
curves for Dataset B are either higher or match the other datasets over
most of the grid, indicating that models trained on Dataset B achieve
slightly greater angular coverage, although the improvement is not
large. The AUC values support this, with minor differences across
datasets.

![](media/image41.png){width="6.2947069116360455in"
height="6.39834208223972in"}

By taking the pointwise maximum over all models, we trace the
"best-possible" recoverability boundary (Figure ‎9.8). Beyond this
maximal contour, no model meets the $T = 0.9$ threshold. The
union-boundary AUC of 0.934 means that, even in the best case, only
93.4% of the full $\lbrack 0,89\rbrack^{2}$ angle grid can be recovered
at plate-level OCR accuracy ≥ 90% (9/10 fully recognized plates).

For detailed overlays of recoverability boundaries within each dataset,
or comparisons between datasets for a single model, see Appendix
(‎13.4.3).

![](media/image6.png){width="5.2483552055993in"
height="5.5204800962379705in"}

Then, we summarize each model--dataset pair by plotting its **extent**
(boundary-AUC) against its **reliability** (RMS failure distance $F$)
(Table ‎9.2). We present these results as a scatter plot, where the
x-axis shows the boundary-AUC (higher is better), the y-axis shows the
$F$ -- the amount of any interior failures and their depth in degrees
(lower is better). Each colored marker corresponds to one dataset, and
each shape to one model (Figure ‎9.9).

  ----------------------------------------------------------------------------
                   Dataset A           Dataset B           Dataset C 
  ---------------- --------- --------- --------- --------- --------- ---------
  Model            AUC       F         AUC       F         AUC       F

  U-Net (baseline) 0.915     0.103     0.923     0.138     0.915     0.146

  U-Net            0.916     0.145     0.924     0.137     0.917     0.115
  Conditional                                                        

  Restormer        0.920     0.095     0.922     0.133     0.921     0.209

  GAN-pix2pix      0.909     0.168     0.913     0.145     0.899     0.173

  Diffusion-SR3    0.889     0.572     0.887     0.100     0.886     1.124
  ----------------------------------------------------------------------------

  : []{#_Ref201854918 .anchor}Figure ‎5.6 Forward Process Illustration

![](media/image42.png){width="7.202189413823272in"
height="4.789335083114611in"}

On the scatter plot (Figure ‎9.9), we can observe that most models
cluster within an AUC range of 0.91 to 0.925 and maintain low RMS
failure distances ($F$) between $0.1{^\circ}$ and $0.2{^\circ}$,
indicating similar coverage and reliability. The U-Net base, U-Net
Conditional, and Restormer models, on Dataset B, lead in coverage, with
high AUC and strong reliability with low $F$. Restormer appears less
affected by the choice of dataset, as Restormer models are grouped
tightly in the high recoverability -- high reliability region. In
contrast, the reliability of diffusion-SR3 depends strongly on the
dataset: it achieves low $F \approx 0.1{^\circ}$ on Dataset B, and high
$F \approx 0.6{^\circ}$, $F \approx 1.1{^\circ}$ on Datasets A and C,
respectively, reflecting more frequent or deeper interior failures; its
AUC is consistently lower than for other models. U-Net Conditional on
Dataset B attains the highest AUC observed. Overall, results for Dataset
B are superior in both coverage and reliability.

Then, we report the mean values of all six metrics in the high-angle
region $R$. (Figure ‎9.10). Restormer is consistently the best, with
average clustering around $40$dB PSNR, 0.97 SSIM, and approximately
$0.67$ plate-level OCR accuracy. These numbers exhibit negligible
variations across Datasets A, B, and C, indicating that Restormer is
largely indifferent to the training-set choice. The conditional U-Net
trails by about 3dB in PSNR yet matches Restormer on OCR, making it the
strongest lightweight alternative. The U-Net base improves on Dataset B
as opposed to A and C, and reaches close to Restormer's score.
Diffusion-SR3 is lowest on every metric---about 30dB PSNR, 0.92 SSIM,
0.55 OCR---and shows no meaningful improvement with dataset choice.
Pix2pix performs a little better than Diffusion-SR3---about 35dB PSNR,
0.63 OCR on Datasets A and B---but drops on Dataset C.

![](media/image43.png){width="7.324642388451443in"
height="4.742077865266841in"}

Finally, we examine how image quality translates into recognition for
two contrasting architectures: Restormer and diffusion-SR3. In the
PSNR--OCR scatter, Restormer follows
$y = 0.032x - 0.55,\ \ R^{2} = 0.991$ (Figure ‎9.11) and diffusion-SR3
follows $y = 0.043x - 0.74,\ \ R^{2} = 0.979$ (Figure ‎9.12)$.$ Thus,
each extra 1dB of PSNR yields about a 3% OCR gain for Restormer and
about 4% for diffusion-SR3. In both cases, PSNR explains almost the
entire spread in recognition accuracy; nearly every change in OCR aligns
with a change in PSNR. The binned curves confirm this behavior: OCR
rises smoothly from zero at 15dB to near-perfect recognition above 40dB,
and the error bars (one-standard-deviation bands) remain short, showing
low within-bin variance. Short bars mean plates that share similar PSNR
values deliver almost identical OCR results.

![](media/image44.png){width="6.9721073928258965in"
height="2.9026017060367453in"}

![](media/image45.png){width="6.977293307086614in"
height="2.904760498687664in"}

By contrast, the SSIM--OCR plots display a threshold-like response. OCR
stays near zero until SSIM reaches about 0.92, then climbs sharply
toward 1. A linear fit yields $R^{2} = 0.777$ for Restormer (Figure
‎9.13) and $R^{2} = 0.739$ for Diffusion-SR3 (Figure ‎9.14). This
underscores that SSIM explains only part of the variance across its full
range. The binned SSIM curve stays flat at low values, surges within a
narrow band, and shows large error bars during that
transition---identical SSIM levels can produce divergent OCR until
perceptual similarity is already very high. Other models have similar
trends; See Appendix (‎13.4.4).

![](media/image46.png){width="6.984036526684164in"
height="2.91246719160105in"}

![](media/image47.png){width="7.0383180227471565in"
height="2.9301662292213475in"}

# Discussion

## Data Preparation

Our dataset is generated with a constant camera--plate distance and
focal length. This means all license plates appear at the same size in
the image, regardless of their orientation. This approach isolates the
effects of rotation; it does not account for the scale changes seen in
real scenarios, where vehicles move closer or farther from the camera.
To fully reflect real-world conditions, future work should introduce
variation in distance and focal length during data generation. However,
that would add more dimensions to the data and raise complexity.

## Evaluation

The size and range of the training data influence models' performance.
We treat the choice of dataset, including the angle distribution, as a
hyperparameter. We started with dataset A, then decided to explore more
variants. We doubled the sample size for dataset B and changed the
sampling distribution for dataset C. All models are trained and
validated on their own splits, but these results only show how well the
model fits that particular data.

For a complete evaluation, we test all models on a single, fixed full
grid of angle pairs. This full grid is the main benchmark. It allows a
fair comparison of models trained on different datasets, since every
model is tested on exactly the same set of distorted images. Different
datasets let us explore how increasing the dataset size or changing the
angle distribution affects recoverability. if we see no improvement, we
can assume we have reached the capacity limit of recoverable signal in
the data, regardless of the model architecture.

We train our models using the full angle space
$\lbrack - 90,90\rbrack^{2}$, but we evaluate performance only on a full
grid within the first quadrant, $\lbrack 0,89\rbrack^{2}$. This strategy
is justified by the symmetry of our data distribution and the linearity
of the projection transform. We sample rotation angles $(\alpha,\beta)$
with a Sobol sequence and fold them to ensure uniform coverage across
all quadrants, so each tilt direction is equally represented during
training. The homography and projection formulas depend only on the
magnitudes $|\alpha|$ and $|\beta|$; flipping the sign of either angle
simply mirrors the distortion pattern without changing its statistical
properties. As a result, geometric distortions and restoration
challenges remain consistent across quadrants, differing only by
direction. By evaluating in the first quadrant, we obtain a
representative assessment of model performance over the entire angle
space, since we expect models to reconstruct distorted license plates
equally well in all quadrants.

Distortion in license plate images is directional, so some digits become
harder to reconstruct depending on the viewing angle. Because the
distortion is mostly linear, less distorted digits may provide direct
spatial clues that help reconstruct heavily distorted digits. We assume
models use these spatial dependencies to recover information from areas
that seem unrecoverable. To test this idea and better capture such
dependencies, we extend the standard U-Net with FiLM layers that encode
distortion, and we also use Restormer, which applies cross-attention.
These methods capture spatial dependencies more strongly than CNN's
receptive fields.

We focus on our main metric, plate-level OCR accuracy, along with
plate-level PSNR and SSIM. Digit-level metrics are also collected.
Although they are not central to our evaluation, we include them in the
appendix for reference.

## Model Comparison

The ground truth data consists of clean license plate images with
uniform backgrounds, random digits, no lighting variation, and fixed
fonts and plate sizes. This means the targets in our dataset are highly
regular and lack the variability present in real-world examples. We
assume that discriminative models such as U-Net, U-Net Conditional, and
Restormer are well-suited for this scenario. When trained with mean
squared error, these models fit the clean targets closely and achieve
higher PSNR, SSIM, and OCR accuracy than GANs or diffusion models. In
this constrained setting, we do not observe an advantage for generative
models.

# Summary and Conclusions

## Training Conclusion 

Overall, the test results indicate that Restormer achieves the best
average restoration accuracy across each dataset. Diffusion-SR3 lags,
especially under extreme distortion.

In practice, diffusion models proved to be the most challenging to
adapt. It was challenging to make the model generate plausible samples
that matched the distribution of clean plates. At times, the diffusion
model produced noisy or inconsistent outputs. Achieving stable training
required substantial deviation from standard SR3 hyperparameters and
extensive testing of different training and sampling schedulers.
Validation was also demanding, since image generation required running
the sampling process for many steps---ranging from 10 up to 1,000 per
image---using the U-Net generator. With further tuning, it is possible
that performance could be improved.

GAN models were also difficult to tune. Training stability was a
frequent issue, and models could fail to reach equilibrium if
hyperparameters were not carefully selected. Occasionally, training
suffered from mode collapse, in which the generator and discriminator
converged to a local minimum and stopped making progress. As a result,
GANs required more careful tuning, and additional optimization could
likely yield better results.

In contrast, discriminative models such as U-Net, U-Net Conditional, and
Restormer were easier to validate and tune. Hyperparameter choices were
more robust, and established best practices from the literature
generally led to good results. This made hyperparameter search more
efficient, and in many cases, following published recommendations
produced strong performance.

## Full Grid Evaluation Conclusion

All models successfully reconstruct heavily distorted license plate
images in most cases. Their performance is mainly limited by the amount
of meaningful signal left in the distorted images. Our results suggest
that we have reached the practical limit of recoverability for these
methods, so major improvements appear unlikely. The maximal
recoverability boundary shows that even the strongest model, Restormer,
cannot exceed a specific extent. On Dataset B, other models approach
this same limit, further indicating that useful signal extraction is
nearly exhausted.

Generative models (GAN-pix2pix and diffusion-SR3) generally perform less
reliably than discriminative models (U-Net variants and Restormer). The
Diffusion-SR3 model struggles when the conditional input contains a low
signal and tends to produce samples from the learned distribution rather
than accurately reconstruct the plate\'s number. Still, the diffusion
model always generates visually clean and undistorted plates, even if
the digits are incorrect. Other models, in contrast, often produce
blurred or corrupted digits when the input is heavily degraded. Despite
these differences, both GAN and diffusion models provide acceptable
results.

We set the plate-level OCR accuracy threshold at 90%, requiring at least
9 out of 10 plates to be recognized at each angle pair. This allows for
occasional OCR errors. For each angle pair, we sampled 10 images to
balance computational and storage demands with statistical reliability.
Given the limited variation in the synthetic dataset, this sample size
provides a stable estimate of recoverability.

To answer the main research question, our results show that a meaningful
signal is present in approximately 93% of the angle grid, as defined by
the maximal recoverability boundary. The region beyond 80° for both
angles (the top-right corner) is unrecoverable. And alpha rotations are
generally harder to reconstruct than beta rotations, a difference that
is clear along the right and top sides of the heatmaps (Figure ‎9.6) or
recoverability plot (Figure ‎9.8).

Regarding metric correlation, PSNR and OCR maintain a strongly linear,
highly explanatory relationship, whereas SSIM influences recognition
only after reaching very high values and does so with greater scatter
and variance. Thus, PSNR can be reliably used as a proxy for OCR
accuracy. Models that improve PSNR also consistently improve OCR
accuracy. Maximizing PSNR during training serves as a reliable surrogate
for improving OCR performance.

# References

+---+-------------------------------------------------------------------+
| \ | > O. Ronneberger, P. Fischer and T. Brox, \"U-Net: Convolutional  |
| [ | > Networks for Biomedical Image Segmentation,\" 2015.             |
| 1 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+===+===================================================================+
| \ | > R. Szeliski, Computer Vision: Algorithms and Applications 2nd   |
| [ | > Edition, 2021.                                                  |
| 2 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > J. Ho, A. Jain and P. Abbeel, \"Denoising Diffusion             |
| [ | > Probabilistic Models,\" 26 August 2020.                         |
| 3 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > B. Korites, Python Graphics: A Reference for Creating 2D and 3D |
| [ | > Images, 2nd ed., APRESS, 2023.                                  |
| 4 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > S. Burhenne, D. Jacob and G. P. Henze, \"Sampling based on      |
| [ | > Sobol\' sequences for Monte Carlo techniques applied to         |
| 5 | > building simulations,\" 15 November 2011.                       |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > J. Shashirangana, h. Padmasiri and d. Meedeniya, \"Automated    |
| [ | > License Plate Recognition: A Survey,\" 29 December 2020.        |
| 6 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > C. N. E. Anagnostopoulos, I. E. Anagnostopoulos, I. D.          |
| [ | > Psoroulas and E. Kayafas, \"License Plate Recognition From      |
| 7 | > Still Images and Video Sequences: A Survey,\" 16 January 2008.  |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > K. H. Liu, C. M. Fan and T. J. Liu, \"SUNet: Swin Transformer   |
| [ | > UNet for Image Denoising,\" 28 February 2022.                   |
| 8 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > Z. Lian, H. Wang and Q. Zhang, \"An Image Deblurring Method     |
| [ | > Using Improved U-Net Model,\" 31 July 2022.                     |
| 9 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > Z. Wang, X. Cun, J. Bao, W. Zhou, J. Liu and H. Li, \"Uformer:  |
| [ | > A General U-Shaped Transformer for Image Restoration,\" 25      |
| 1 | > November 2021.                                                  |
| 0 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > S. W. Zamir, A. Arora, S. Khan, M. Hayat, F. S. Khan and M. H.  |
| [ | > Yang, \"Restormer: Efficient Transformer for High-Resolution    |
| 1 | > Image Restoration,\" 11 March 2022.                             |
| 1 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > X. Chen, Z. Li, Y. Pu, Y. Liu, J. Zhou, Y. Qiao and C. Dong,    |
| [ | > \"A Comparative Study of Image Restoration Networks for General |
| 1 | > Backbone Network Design,\" 16 July 2024.                        |
| 2 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > O. Oktay, J. Schlemper, L. L. Folgoc, M. Lee, M. Heinrich, K.   |
| [ | > Misawa, K. Mori, S. McDonagh, N. Y. Hammerla, B. Kainz, B.      |
| 1 | > Glocker and D. Rueckert, \"Attention U-Net: Learning Where to   |
| 3 | > Look for the Pancreas,\" 20 May 2018.                           |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > Z. Zhou, M. R. Siddiquee, N. Tajbakhsh and J. Liang, \"UNet++:  |
| [ | > A Nested U-Net Architecture for Medical Image Segmentation\" 01 |
| 1 | > July 2020.                                                      |
| 4 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > P. Isola, T. Zhou, A. A. Efros and J.-Y. Zhu, \"Image-to-Image  |
| [ | > Translation with Conditional Adversarial Networks,\" 26         |
| 1 | > November 2018.                                                  |
| 5 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > C. Ledig, L. Theis, F. Huszar, J. Caballero, A. Cunningham, A.  |
| [ | > Acosta, A. Aitken, A. Tejani, J. Totz, Z. Wang and W. Shi,      |
| 1 | > \"Photo-Realistic Single Image Super-Resolution Using a         |
| 6 | > Generative Adversarial Network\" 25 May 2025.                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > X. Wang, K. Yu, S. Wu, J. Gu, Y. Liu, C. Dong, C. C. Loy, Y.    |
| [ | > Qiao and X. Tang, \"ESRGAN: Enhanced Super-Resolution,\" 17     |
| 1 | > September 2018.                                                 |
| 7 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > O. Kupyn, V. Budzan, M. Mykhailych, D. Mishkin and J. Matas,    |
| [ | > \"DeblurGAN: Blind Motion Deblurring Using Conditional          |
| 1 | > Adversarial Networks,\" 3 April 2018.                           |
| 8 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > S. Saxena and M. N. Teli, \"Comparison and Analysis of          |
| [ | > Image-to-Image Generative Adversarial Networks: A Survey,\" 27  |
| 1 | > August 2022.                                                    |
| 9 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > C. Saharia, J. Ho, W. Chan, T. Salimans, D. J. Fleet and M.     |
| [ | > Norouzi, \"Image Super-Resolution via Iterative Refinement,\"   |
| 2 | > 30 Jun 2021.                                                    |
| 0 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > W. Zhang, H. Lu, M. Ning, X. Huang, W. Wang, K. Huang and Q.    |
| [ | > Wang, \"DvD: Unleashing a Generative Paradigm for Document      |
| 2 | > Dewarping via Coordinates-based Diffusion Model,\" 28 May 2025. |
| 1 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > G. H. Liu, A. Vahdat, D. A. Huang, E. . A. Theodorou, W. Nie    |
| [ | > and A. Anandkumar, \"IS2B: Image-to-Image Schrodinger Bridge,\" |
| 2 | > 26 May 2023.                                                    |
| 2 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > Y. Zhu, K. Zhang, J. Liang, J. Cao, B. Wen, R. Timofte and L.   |
| [ | > V. Gool, \"Denoising Diffusion Models for Plug-and-Play Image   |
| 2 | > Restoration,\" 15 May 2023.                                     |
| 3 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > \"Overview of the new neural network system in Tesseract        |
| [ | > 4.00,\" \[Online\]. Available:                                  |
| 2 | > https://tess                                                    |
| 4 | eract-ocr.github.io/tessdoc/tess4/NeuralNetsInTesseract4.00.html. |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > A. Y. Sugiyono, \"Extracting Information from Vehicle           |
| [ | > Registration Plate using OCR Tesseract,\" 2023.                 |
| 2 |                                                                   |
| 5 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > R. Ritika, S. Srushti, S. Pratiksha, S. Kaldhone and J. D.      |
| [ | > Jadhav, \"Automatic License Plate Recognition Using YOLOv4 and  |
| 2 | > Tesseract OCR,\" March 2022.                                    |
| 6 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > Y. Du, C. Li, R. Guo, X. Yin, W. Liu, J. Zhou, Y. Bai, Z. Yu,   |
| [ | > Y. Yang, Q. Dang and H. Wang, \"PP-OCR: A Practical Ultra       |
| 2 | > Lightweight OCR System,\" 15 October 2020.                      |
| 7 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > F. S. H. d. V. Ethan Perez, \"FiLM: Visual Reasoning with a     |
| [ | > General Conditioning Layer,\" 2017.                             |
| 2 |                                                                   |
| 8 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > N. S. N. P. Ashish Vaswani, \"Attention Is All You Need,\"      |
| [ | > 2017.                                                           |
| 2 |                                                                   |
| 9 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > B. L. J. L. Shanchuan Lin, \"Common Diffusion Noise Schedules   |
| [ | > and Sample Steps are Flawed,\" 2023.                            |
| 3 |                                                                   |
| 0 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+
| \ | > C. M. &. S. E. Jiaming Song, \"Denoising Diffusion Implicit     |
| [ | > Models,\" 2021.                                                 |
| 3 |                                                                   |
| 1 |                                                                   |
| \ |                                                                   |
| ] |                                                                   |
+---+-------------------------------------------------------------------+

: Equation ‎5.3

# Appendices

## Deliverables, Work plan, Resources

+---+---------------+------------+-----------+------------+-------------+
| I | Name of the   | Input      | Expected  | Quality    | Open Issues |
| D | Task          |            | Delivery  | Criteria   |             |
+===+===============+============+===========+============+=============+
| 1 | Define        | Initial    | Clear     | Concise,   | Keep scope  |
| . | Project Scope | re         | scope &   | actionable | realistic   |
|   |               | quirements | o         | statement  |             |
|   |               |            | bjectives |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 2 | Identify      | Project    | Tool &    | Covers all | Check tool  |
| . | Resources &   | needs      | resource  | tasks      | co          |
|   | Tools         |            | list      |            | mpatibility |
|   |               |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 3 | Create Goals, | Scope      | Goals &   | Measurable | Find most   |
| . | Objectives,   |            | metric    | & aligned  | applicable  |
|   | Metrics       |            | set       |            | metrics     |
|   |               |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 4 | Draft         | Goals,     | SOW       | Clear work | Balance     |
| . | Statement of  | scope      | pre       | plan       | scope &     |
|   | Work          |            | sentation |            | effort      |
|   |               |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 5 | Conduct       | Papers &   | Review    | Current &  | LPR related |
| . | Literature    | docs       | report    | relevant   |             |
|   | Review        |            |           |            |             |
|   |               |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 6 | Write Project | Scope,     | Charter   | Includes   | --          |
| . | Charte        | resources, | draft     | all        |             |
|   | r/Engineering | methods    |           | sections   |             |
|   | Report        |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 7 | Submit        | Revised    | Approved  | Meets      | Meet        |
| . | Project       | charter    | charter   | g          | deadline    |
|   | Charte        |            |           | uidelines, |             |
|   | r/Engineering |            |           | no errors  |             |
|   | Report        |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 8 | Prepare       | Specs      | Clean/    | Uniform    | Simulating  |
| . | Synthetic LP  |            | Distorted | res.,      | rotation    |
|   | Generation    |            | LP image  | correct    |             |
|   | Pipeline      |            | pairs     | labels     |             |
+---+---------------+------------+-----------+------------+-------------+
| 9 | Angle         | α--β range | Dis       | Ext        | Tune        |
| . | Sampling      |            | tribution | reme-angle | d           |
|   | Strategy      |            | for       | coverage   | istribution |
|   |               |            | sampling  |            | parameters  |
+---+---------------+------------+-----------+------------+-------------+
| 1 | Prepare       | Complete   | Train     | Non-o      | Storage     |
| 0 | Dataset       | set        | /val/test | verlapping | capacity    |
| . |               |            | 80/ 10/10 | splits     |             |
|   |               |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 1 | Adapt U-Net   | Plate      | U-Net     | Runs,      | --          |
| 1 | Baseline      | pairs      | code      | trains,    |             |
| . |               |            |           | correct    |             |
|   |               |            |           | outputs    |             |
+---+---------------+------------+-----------+------------+-------------+
| 1 | Adapt         | Plate      | F         | Runs,      | --          |
| 2 | FiLM-U-Net    | pairs      | iLM-U-Net | trains,    |             |
| . |               |            | code      | correct    |             |
|   |               |            |           | outputs    |             |
+---+---------------+------------+-----------+------------+-------------+
| 1 | Adapt         | Plate      | Restormer | Runs,      | High        |
| 3 | Restormer     | pairs      | code      | trains,    | co          |
| . |               |            |           | correct    | mputational |
|   |               |            |           | outputs    | demand      |
+---+---------------+------------+-----------+------------+-------------+
| 1 | Adapt Pix2Pix | Plate      | Pix2Pix   | Runs,      | Unstable    |
| 4 | GAN           | pairs      | code      | trains,    |             |
| . |               |            |           | correct    |             |
|   |               |            |           | outputs    |             |
+---+---------------+------------+-----------+------------+-------------+
| 1 | Adapt SR3     | Plate      | SR3 code  | Runs,      | Complex     |
| 5 | Diffusion     | pairs      |           | trains,    |             |
| . |               |            |           | correct    |             |
|   |               |            |           | outputs    |             |
+---+---------------+------------+-----------+------------+-------------+
| 1 | Train & Tune  | Data A/B/C | Trained   | Best       | Hyper-param |
| 6 | U-Net         |            | U-Net     | metrics    | sweep       |
| . |               |            |           |            |             |
|   |               |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 1 | Train & Tune  | Data A/B/C | Trained   | Best       | Hyper-param |
| 7 | FiLM-U-Net    |            | F         | metrics    | sweep       |
| . |               |            | iLM-U-Net |            |             |
|   |               |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 1 | Train & Tune  | Data A/B/C | Trained   | Best       | GPU budget  |
| 8 | Restormer     |            | Restormer | metrics    |             |
| . |               |            |           |            |             |
|   |               |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 1 | Train & Tune  | Data A/B/C | Trained   | Best       | G/ D        |
| 9 | Pix2Pix       |            | GAN       | metrics    | balance     |
| . |               |            |           |            |             |
|   |               |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 2 | Train & Tune  | Data A/B/C | Trained   | Best       | Long        |
| 0 | Diffusion     |            | SR3       | metrics    | sampling    |
| . |               |            |           |            | time        |
|   |               |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 2 | Full-Grid     | All models | OCR       | Re         | --          |
| 1 | Evaluation    |            | heatmaps, | producible |             |
| . |               |            | AUC, F    | coverage   |             |
|   |               |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 2 | Metric        | Heatmaps   | PSNR--OCR | R² values  | Confirm     |
| 2 | Correlation   |            | &         | logged     | thresholds  |
| . | Study         |            | SSIM--OCR |            |             |
|   |               |            | plots     |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 2 | Draft Final   | All        | Report    | Complete,  | Integrate   |
| 3 | Report        | results    | draft     | clear      | figures     |
| . |               |            |           |            |             |
|   |               |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 2 | Review &      | Draft      | Final     | Error-free | Apply       |
| 4 | Finalize      | report     | report    |            | feedback    |
| . | Report        |            |           |            |             |
|   |               |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 2 | Prepare       | Final      | Project   | Visual,    | Fit layout  |
| 5 | Poster        | report     | poster    | concise    | limits      |
| . |               |            |           |            |             |
|   |               |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 2 | Corrections & | Feedback   | Enhanced  | Issues     | Time        |
| 6 | Improvements  |            | report &  | resolved   | constraints |
| . |               |            | poster    |            |             |
|   |               |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+
| 2 | Submit Final  | Final      | S         | Meets      | Deadline    |
| 7 | Report        | report     | ubmission | guidelines | met         |
| . |               |            |           |            |             |
|   |               |            |           |            |             |
+---+---------------+------------+-----------+------------+-------------+

: []{#_Ref201890980 .anchor}Figure ‎5.7 Reverse Process Illustration

+---+---------------------+--------+--------+------------------+-------+
| * | **Task**            | **S    | *      | **               | **Res |
| * |                     | tart** | *End** | Deliverable(s)** | ponsi |
| I |                     |        |        |                  | ble** |
| D |                     |        |        |                  |       |
| * |                     |        |        |                  |       |
| * |                     |        |        |                  |       |
+===+=====================+========+========+==================+=======+
| 1 | Define Project      | 01-    | 10-    | Project scope &  | Igor, |
| . | Scope               | Apr-24 | May-24 | objectives       | Orpaz |
|   |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 2 | Identify Resources  | 01-    | 10-    | Tool & resource  | Igor, |
| . | & Tools             | Apr-24 | May-24 | list             | Orpaz |
|   |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 3 | Create Goals,       | 10-    | 24-    | Goals & metric   | Igor, |
| . | Objectives, Metrics | May-24 | May-24 | set              | Orpaz |
|   |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 4 | Draft Statement of  | 03-    | 24-    | SOW draft        | Igor, |
| . | Work                | Jun-24 | Jun-24 |                  | Orpaz |
|   |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 5 | Conduct Literature  | 03-    | 23-    | Literature       | Igor, |
| . | Review              | Jun-24 | Jul-24 | review report    | Orpaz |
|   |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 6 | Submit Project      | 01-    | 22-    | PDF file         | Igor, |
| . | Charter Report      | Apr-24 | Aug-24 |                  | Orpaz |
|   |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 7 | Submit Project      | 01-    | 16-    | PDF file         | Igor, |
| . | Engineering Report  | Nov-24 | Jan-25 |                  | Orpaz |
|   |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 8 | Prepare Synthetic   | 02-    | 09-    | Clean            | Igor, |
| . | LP Generation       | Sep-24 | Sep-24 | license-plate    | Orpaz |
|   | Pipeline            |        |        | images           |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 9 | Angle Sampling      | 09-    | 16-    | Distribution for | Igor  |
| . | Strategy            | Sep-24 | Sep-24 | sampling         |       |
|   |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 1 | Prepare Dataset     | 27-    | 01-    | 80/10/10         | Orpaz |
| 0 |                     | Sep-24 | Oct-24 | train/val/test   |       |
| . |                     |        |        | splits           |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 1 | Adapt U-Net         | 05-    | 25-    | U-Net            | Igor  |
| 1 | Baseline            | Sep-24 | Sep-24 | implementation   |       |
| . |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 1 | Adapt FiLM-U-Net    | 05-    | 13-    | Conditional      | Igor  |
| 2 |                     | Sep-24 | Nov-24 | U-Net code       |       |
| . |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 1 | Adapt Restormer     | 05-    | 13-    | Restormer        | Orpaz |
| 3 |                     | Sep-24 | Nov-24 | implementation   |       |
| . |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 1 | Adapt Pix2Pix GAN   | 20-    | 24-    | Pix2Pix GAN      | Orpaz |
| 4 |                     | Sep-24 | Oct-24 | implementation   |       |
| . |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 1 | Adapt SR3 Diffusion | 05-    | 13-    | SR3 diffusion    | Igor  |
| 5 |                     | Sep-24 | Nov-24 | implementation   |       |
| . |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 1 | Train & Tune U-Net  | 25-    | 22-    | Optimized U-Net  | Igor  |
| 6 |                     | Sep-24 | Oct-24 |                  |       |
| . |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 1 | Train & Tune        | 25-    | 10-    | Optimized        | Igor  |
| 7 | FiLM-U-Net          | Sep-24 | Dec-24 | FiLM-U-Net       |       |
| . |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 1 | Train & Tune        | 25-    | 10-    | Optimized        | Orpaz |
| 8 | Restormer           | Sep-24 | Dec-24 | Restormer        |       |
| . |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 1 | Train & Tune        | 20-    | 15-    | Optimized        | Orpaz |
| 9 | Pix2Pix             | Oct-24 | Nov-24 | Pix2Pix GAN      |       |
| . |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 2 | Train & Tune        | 13-    | 10-    | Optimized SR3    | Igor  |
| 0 | Diffusion           | Nov-24 | Dec-24 | diffusion        |       |
| . |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 2 | Full-Grid           | 25-    | 16-    | OCR heatmaps,    | Igor, |
| 1 | Evaluation          | Nov-24 | Dec-24 | recoverability   | Orpaz |
| . |                     |        |        | boundary, AUC, F |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 2 | Metric Correlation  | 25-    | 16-    | PSNR--OCR &      | Igor, |
| 2 | Study               | Nov-24 | Dec-24 | SSIM--OCR plots  | Orpaz |
| . |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 2 | Draft Final Report  | 01-    | 01-    | Initial report   | Igor, |
| 3 |                     | Apr-25 | Jul-25 | draft            | Orpaz |
| . |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 2 | Review & Finalize   | 01-    | 19-    | Final report     | Igor, |
| 4 | Report              | Jun-25 | Jul-25 |                  | Orpaz |
| . |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 2 | Prepare Poster      | 01-    | 22-    | Poster           | Igor, |
| 5 |                     | Apr-25 | Apr-25 |                  | Orpaz |
| . |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 2 | Corrections &       | 19-    | 24-    | Enhanced report  | Igor, |
| 6 | Improvements        | Jun-25 | Jul-25 |                  | Orpaz |
| . |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+
| 2 | Submit Final Report | 24-    | 24-    | Submitted report | Igor, |
| 7 |                     | Jul-25 | Jul-25 |                  | Orpaz |
| . |                     |        |        |                  |       |
|   |                     |        |        |                  |       |
+---+---------------------+--------+--------+------------------+-------+

: Equation ‎5.4

  -----------------------------------------------------------------------
  **Category**              **Resources / Tools**
  ------------------------- ---------------------------------------------
  Hardware                  GPU with CUDA, Google's Compute Engine

  Development               VS Code, Jupyter Notebooks, Anaconda, Google
                            Colab

  Frameworks                PyTorch

  Experiment Management     MLflow, Optuna, Comet ML

  Libraries                 OpenCV, NumPy, Pillow

  Visualization             Matplotlib, Pandas

  OCR                       Tesseract

  Version Control           Git, GitHub

  Docs / Reports            Google Docs, MS Word

  Slides & Posters          PowerPoint

  Project Management        MS Project
  -----------------------------------------------------------------------

  : Equation ‎5.5

## Gantt Chart

![](media/image48.png){width="8.065680227471566in"
height="5.776000656167979in"}

## Project Poster

![](media/image49.png){width="8.257828083989502in"
height="6.492361111111111in"}

## Extensions

## Tuning and Validation

> We only showcase a single example of tuning and the MLflow framework
> we worked with. We did not record all tuning steps, as they were
> performed both automatically and manually. Tuning took place on
> separate machines, on local hardware and Google Cloud. For some
> models, especially diffusion, tuning involved not only standard
> hyperparameters like learning rate and batch size. It also required
> changing other architectural parameters such as number of timesteps,
> beta schedule, prediction type, and sampler type. These could not be
> automated and had to be tuned manually.

![](media/image50.png){width="7.679000437445319in"
height="5.201492782152231in"}

![A screenshot of a graph AI-generated content may be
incorrect.](media/image51.png){width="6.491666666666666in"
height="3.6193613298337706in"}

![A screenshot of a graph AI-generated content may be
incorrect.](media/image52.png){width="6.495833333333334in"
height="2.4242891513560805in"}

![A screenshot of a graph AI-generated content may be
incorrect.](media/image53.png){width="6.495833333333334in"
height="3.6659317585301836in"}

## Full Grid Heatmaps

> These Heatmaps for Datasets A and C supplement the main report and
> visually confirm that Restormer achieves the best result among tested
> architectures:
>
> ![](media/image54.png){width="8.145833333333334in"
> height="6.108333333333333in"}

**\
**

## Recoverability Boundaries Detailed

![](media/image55.png){width="7.378494094488189in"
height="7.517323928258968in"}

**\
**

## PSNR, SSIM vs OCR Correlation

> The results align with those in the main report. PSNR correlates
> strongly with OCR accuracy, with R² values of 0.989 for U-Net, 0.961
> for U-Net Conditional, and 0.988 for Pix2Pix. SSIM shows a threshold
> effect. OCR accuracy remains near zero below about 0.85 SSIM, then
> rises sharply above this point. The R² values for SSIM are 0.725,
> 0.713, and 0.755 for the three models. This confirms that PSNR is a
> more reliable indicator of OCR accuracy than SSIM.

![](media/image56.png){width="6.4301093613298335in"
height="2.677165354330709in"}

![A graph and chart with numbers AI-generated content may be
incorrect.](media/image57.png){width="6.4301093613298335in"
height="2.677165354330709in"}

![A graph and diagram of a graph AI-generated content may be
incorrect.](media/image58.png){width="6.4301093613298335in"
height="2.677165354330709in"}

![A graph of a graph AI-generated content may be
incorrect.](media/image59.png){width="6.42055883639545in"
height="2.677165354330709in"}

![A graph of a graph and a graph of a graph AI-generated content may be
incorrect.](media/image60.png){width="6.420557742782152in"
height="2.677165354330709in"}

![A graph of a graph AI-generated content may be
incorrect.](media/image61.png){width="6.420557742782152in"
height="2.677165354330709in"}

## Project Framework Overview

All code is run in a dedicated Anaconda environment (**environment.yml**
file), which includes PyTorch, OpenCV, Tesseract OCR, MLflow, and other
required libraries. Installing and activating this environment ensures
all dependencies are available for every script. The project is
organized as follows:

-   **scripts/** -- **lp_processing.py** for data generation, splitting,
    and storing; **run_inference.py** for inference on the full grid and
    saving the resulting images; **compute_metrics.py** for evaluation.\
    **models**/ -- Contains model's code such as official PyTorch models
    from GitHub (e.g., Restormer), and adapted or custom models.

-   **src/** -- Contains training scripts for each model in the form
    **train\_{model_name}.py**, shared utility functions in
    **utils.py**, and a custom **lp_dataset.py** class used with data
    loaders to feed data into models during training.

-   **data/** -- Data folder containing datasets folders **A**, **B**,
    **C**, and a **full_grid** folder. Each dataset contains subfolders
    for train, validation, and test splits, with images and a metadata
    file. **full_grid** directly includes all images and metadata.

-   **Jupyter Notebooks** -- Notebooks at the project root for
    experimentation and analysis. **ocr_test.ipynb** used for testing
    OCR, **sampling.ipynb** for experimenting and visualizing PDF and
    sampling, **report_artifacts.ipynb** for report figures, and
    **results.ipynb** for organizing, analyzing, and making figures of
    raw results data from CSV files.

**Dataset Generation**

**lp_processing.py** -- This script runs the full dataset generation
pipeline, from creating clean plates to saving them in the data folder.
In the main, we can set all the related parameters of the clean plates'
dimensions, font, the sampling PDF, the number of samples, etc. By
default, three datasets are created and saved in
**data/{dataset}/split/** folders as paired **original\_{index}.png**
and **distorted\_{index}.png** images. Each split includes a
**metadata.json** file that records the plate text, distortion angles,
and bounding boxes for every digit, linking each distorted image with
its clean original. A fixed random seed is used for reproducibility.

**Models and Training Workflow**

The **models/** folder stores all our models: U-Net, Conditional U-Net,
Restormer, Pix2Pix GAN, diffusion SR3. Each model takes a distorted
plate image and returns a restored image of the same size.

Training scripts (**src/)** all follow the same steps:

-   **Configuration:** The script reads command-line arguments and
    builds a config with epochs, batch size, learning rate, weight
    decay, and any model-specific settings.

-   **Data loading:** The custom **LicensePlateDataset** class reads all
    image pairs into memory once and applies any necessary transforms
    (tensor conversion, normalization). **PyTorch DataLoaders** turns
    the dataset class into an iterable over batches, shuffles batches
    (only for training set), and delivers them to the model in the
    training loop.

-   **Model setup:** The selected model is moved to the GPU. The script
    defines a loss (e.g., MSE) and an optimizer (e.g., AdamW). It
    defines a learning rate scheduler (e.g, CosineAnnealingLR**).** A
    fixed seed fixes data order and weight initialization.

-   **MLflow tracking:** The script starts an MLflow run. It logs
    hyperparameters and copies the training script and model file as
    artifacts. Metrics and sample images are logged during training.
    Those artifacts are stored locally and can be accessed through the
    MLflow UI.

-   **Training loop:** For U-Net and GANs, each epoch shuffles batches,
    runs forward pass, computes loss, back-propagates, updates weights,
    then runs a no-gradient validation pass. Diffusion follows the same
    cycle, but first adds noise to each input and predicts that noise
    across scheduled timesteps. After validation, the script logs loss,
    MSE, SSIM, and PSNR to MLflow and keeps the model state with the
    best validation SSIM.

-   **Post-training.** After the final epoch or step, the best model
    weights are loaded. Evaluated on the unseen test set. Test MSE,
    SSIM, and PSNR are logged. The trained model is logged with an
    environment file for dependencies.

**Inference and Evaluation Scripts**

-   **run_inference.py** -- This script loads trained models from MLflow
    and applies them to the **data/full_grid/** set. It loads each model
    under the chosen dataset name, moves the model to the GPU, and
    enables evaluation mode. For U‑Net, U-Net Conditional, Restormer,
    and Pix2Pix, each distorted image is fed through the network, and
    the restored output is saved in **results/{dataset}/{model}/**. For
    the diffusion model, it performs the scheduled denoising loop before
    saving the image. The script measures the average inference time per
    image and writes it to **inference_times.csv**. Command‑line flags
    control parameters such as model names, batch size, and diffusion
    sampling steps.

-   **compute_metrics.py** -- script compares each reconstructed image
    with its clean original. It looks up the plate number, angle pair,
    and digit boxes in **metadata.json**. For each image, it reports
    plate‑level and digit-level metrics. It runs Tesseract in digit
    mode, extracts the digit patch, preprocesses it, and applies
    recognition. If recognition fails or is incomplete, the script tries
    alternative preprocessing or attempts to identify the digit from a
    full plate. All values (raw data) are saved to a CSV at
    **results/{dataset}/{model_name}.csv.**

-   **run_all.py** -- This script automates the workflow for any dataset
    **A**, **B**, or **C**. It activates the project's environment. It
    runs the training scripts for each model in sequence. After
    training, it calls **run_inference.py**. It then calls
    **compute_metrics.py**. The script can be configured to enable or
    skip specific models and steps. It uses subprocess to launch each
    script in the correct order. This allows running the entire pipeline
    with a single command once the data is available.

**Jupyter Notebooks for Testing and Analysis**

Several notebooks are included at the project root. These are not part
of the main pipeline, but are used for checking, validation, and making
figures.

-   **ocr_test.ipynb --** In this notebook, we test OCRs. We check that
    the OCR and preprocessing steps can read digits from distorted
    plates. Different preprocessing options are tried. The final
    approach is used in the main pipeline. This notebook confirms that
    OCR will work before it is used in **compute_metrics.py**.

-   **report_artifacts.ipynb** -- This notebook makes the figures and
    sample images used in the project report. Here, we break down our
    code and plot intermediate results and other relevant illustrations.

-   **sampling.ipynb** -- In this notebook, we test the sampling
    distribution for rotation angles. We select parameters and plot PDFs
    and how rotation angles are sampled from the PDF for each dataset.
    We compare sampling methods. This helps us visually verify
    correctness of our distribution and sampling. We use those figures
    in the report. It is an extension to **report_artifacts.ipynb**.

-   **results.ipynb** -- In this notebook, we load the CSV files (raw
    data) from **compute_metrics.py** for each model and dataset as
    pandas dataframes. We compute means over all samples for each angle
    pair to get a general overview of each model. We transform the
    dataframes to draw statistics and make different plots, such as
    heatmaps, bar charts, scatter plots, and tables. This notebook is
    used to prepare the main summary figures and tables for the final
    report.

## Project Files

GitHub Repository: <https://github.com/aiigoradam/LPR_Project>
