# NeuroSignal-QC

## Interpretable Power-Line Interference Screening in Intracranial EEG

An exploratory neuroengineering research project investigating
power-line interference detection in intracranial EEG recordings
using interpretable spectral features and cross-hospital evaluation.

## Research Question

Can simple frequency-domain measurements identify power-line
interference across recording institutions while minimizing
unnecessary flags on pathological-labeled neural recordings?

## Dataset

This project uses the multicenter intracranial EEG dataset
published by Nejedly et al. (2020).

Institutions:
- Mayo Clinic, United States
- St. Anne's University Hospital (FNUSA), Czech Republic

Public NEMAR datasets:
- Mayo: https://www.nemar.org/dataset/nm000182
- FNUSA: https://www.nemar.org/dataset/nm000183

Original publication:
https://doi.org/10.1038/s41597-020-0532-5

The published collection contains 348,300 annotated clips
from 38 participants.

The final detector analysis uses 225 selected three-second
intracranial EEG clips representing all 38 participants.

Signals were accessed remotely through NEMAR's Zarr
representation at a sampling frequency of 1,000 Hz.

The analyzed clips appear standardized. Signal amplitudes
should not be treated as calibrated absolute microvolt values.

## Methodology

### Signal Processing

Power spectral density was estimated using Welch's method.

Configuration:
- Sampling frequency: 1,000 Hz
- Window: Hann
- Segment length: 2,048 samples
- Overlap: 1,024 samples
- Spectral analysis range: 1-150 Hz

### Feature 1: Relative Mains-Frequency Power

Percentage of spectral power concentrated within
2 Hz of the hospital's expected mains frequency.

- Mayo Clinic: 60 Hz
- FNUSA: 50 Hz

### Feature 2: Local Spectral Prominence

Decibel ratio between the strongest spectral peak
near the expected mains frequency and the median
power spectral density in neighboring frequency bands.

### Detection Framework

The detector uses a conservative two-feature AND rule.

A recording is flagged only when:

1. Relative mains-frequency power exceeds its threshold.
2. Local spectral prominence exceeds its threshold.

Thresholds are derived from the 95th percentile
of non-power-line-labeled calibration recordings.

No machine-learning classifier is required.

## Evaluation Design

The investigation includes:

- Exploratory EEG waveform and spectral inspection
- Signal-integrity and flatline analysis
- Participant-disjoint development and evaluation
- Retrospective cross-hospital threshold transfer
- Recording-level sensitivity and specificity
- Pathological-annotation false-positive analysis
- Participant-level reliability assessment
- Statistical uncertainty analysis

## Main Results

### Mayo to FNUSA

- Target recordings: 105
- Target participants: 14
- Sensitivity: 100%
- Specificity: 100%
- Pathological recordings flagged: 0/30
- Complete power-line detection: 3/3 participants

### FNUSA to Mayo

- Target recordings: 120
- Target participants: 24
- Sensitivity: 90%
- Specificity: 95.56%
- Pathological recordings flagged: 0/30
- Complete power-line detection: 6/8 participants

Cross-hospital transfer was asymmetric, suggesting
that detector performance depends on calibration conditions.

The results are exploratory and should not be interpreted
as prospective or independent clinical validation.

## Research Limitations

- Selectively sampled subset of the original dataset
- Exploratory feature analysis preceded evaluation splitting
- Retrospective evaluation rather than prospective validation
- Multiple recordings from some participants
- Only three FNUSA participants with power-line recordings
- Standardized and resampled signal representation
- Wide uncertainty intervals for participant-level outcomes
- Different electrical mains frequencies between hospitals
- Detection restricted to power-line interference
- No actual EEG artifact removal or waveform restoration
- No demonstrated preservation of pathological waveforms
- No clinical deployment or safety validation

A pathological-labeled recording that is not flagged
cannot automatically be considered free of interference.

## Repository Structure

NeuroSignal-QC/

    README.md
    requirements.txt
    results/
    figures/
    metadata/
    notebooks/

## Reproducibility

The analysis notebook documents data retrieval, signal
processing, spectral feature extraction, detector
calibration, and evaluation.

The research is organized into five phase notebooks under the notebooks/ directory.

Raw EEG recordings are accessed through the public
NEMAR datasets and are not redistributed.

## Intended Use

This project is an exploratory computational
neuroscience and signal-processing investigation.

It is not a clinical diagnostic, monitoring,
or treatment system.

## Reference

Nejedly, P. et al. (2020).
Multicenter intracranial EEG dataset for classification
of graphoelements and artifactual signals.
Scientific Data.

https://doi.org/10.1038/s41597-020-0532-5

## Phase-Based Research Notebooks

The project contains five documented notebooks:

1. Data acquisition and signal inspection
2. Signal quality and spectral analysis
3. Detector development and evaluation
4. Cross-hospital generalization
5. Final research results

All notebooks preserve their scientific code
and execution outputs.

See `docs/NOTEBOOK_INDEX.md` for details.

To reproduce the full workflow:

```bash
python scripts/run_all_phases.py
```
