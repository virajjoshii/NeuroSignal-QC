# NeuroSignal-QC — Notebook Index

This research is organized into five phases.

## Phase 1 — Data Acquisition and Inspection

Dataset access, EEG annotations, waveform inspection,
and initial signal-quality investigation.

## Phase 2 — Signal Quality and Spectral Analysis

Signal integrity, flatline investigation,
Welch PSD, and exploratory spectral analysis.

## Phase 3 — Detector Development and Evaluation

Interpretable spectral features, threshold selection,
and participant-disjoint evaluation.

## Phase 4 — Cross-Hospital Generalization

Cross-institutional testing, confidence intervals,
and participant-level reliability assessment.

## Phase 5 — Final Research Results

Consolidated results, scientific figures,
and reproducibility metadata.

## Execution Outputs

Each notebook includes its original scientific code
and saved execution outputs.

## Reproducibility

The five notebooks share variables.
They must be executed sequentially in one kernel.

Run the full pipeline:

    python scripts/run_all_phases.py

This runner combines all phases in memory
and executes them in a fresh Python kernel.

The runner requires access to the public NEMAR datasets.

This is a retrospective exploratory study,
not a clinically validated EEG quality-control system.
