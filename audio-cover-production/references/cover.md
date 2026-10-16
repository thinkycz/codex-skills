# Melody-preserving cover production

## Establish the musical contract

Use the latest user decision for retained versus synthesized lead vocals, backing arrangement, melody, words, key, timing and creative references. Do not generalize one past request into a rule that every cover must replace the singer. If a new singer is requested, retaining the original vocal in the final mix does not satisfy that request.

Analyze the provided recordings rather than asserting how a reference artist produced them. Mark production-method inferences as inferences. Preserve the source melody and phrasing when requested, including rap and endings; new composition from a style prompt is a different deliverable.

## Proven local approach and its limits

The reviewed Apple-silicon workflow used UVR/MDX-Net for guide stems, ACE-Step 1.5 with MLX for replacement backing, and Seed-VC singing conversion conditioned on source F0 for a replacement voice. These are dated working examples, not pinned requirements or promises about other machines. Verify current upstream instructions and the actual installed models before reuse.

- Start with a representative singing-and-rap preview, about 30–45 seconds when appropriate. Compare the source, reference and preview before committing to a full render. Reuse current-session acceptance; do not repeatedly ask for the same choice.
- For the tested melody-preserving Seed-VC route, use the singing/F0 model rather than a speech-only model, retain original pitch, and keep length adjustment at 1.0. The successful model family was `DiT_seed_v2_uvit_whisper_base_f0_44k_bigvgan_pruned_ft_ema_v2`. Match current CLI/configuration names instead of pasting stale flags.
- The tested MPS setup used float32 Whisper features to avoid half-precision instability. Check finite/non-silent output before scaling up. For long audio, overlap chunks, preserve the exact source timeline, smooth joins and inspect the transitions.
- Generate or adapt backing with enough source influence to preserve timing and harmony. A text-only arrangement that drifts from the vocal is not an aligned cover. Mix only the intended lead vocal and backing; when new vocals are required, verify the original lead waveform was not mixed into the final result.

## Export and acceptance

Export a playable final mix plus requested editable vocal/instrumental stems. Check source integrity, decoding, duration/alignment, finite samples, peaks/clipping and section joins, including after lossy encoding. Where melody fidelity matters, compare extracted source/output pitch and timing, while stating the diagnostic's limits.

Listen to representative verses, chorus, rap, joins and ending. Vietnamese diction, tonal clarity and musical quality need listening review even when pitch correlation and clipping checks pass. If listening was not possible or acceptance remains pending, say so precisely. Preserve the selected full-song structure instead of silently delivering only a preview.
