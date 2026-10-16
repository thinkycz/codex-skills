# Stem separation

Confirm the requested source and output roles. Vocal audio contains sung notes and rap phrasing; an instrumental stem does not extract those notes as MIDI. Stem extraction alone does not create a new singer.

1. Inspect duration, channels, sample rate and available separation tools. Record a source checksum. Select a writable output directory before starting; the earlier UVR UI attempt failed because its export directory was invalid.
2. Use an installed separator with an appropriate vocal/instrumental model. UVR/MDX-Net worked in the reviewed local workflow; inspect current model files and supported runtimes rather than assuming the same bundle path or backend exists. Try a representative section before a costly full pass.
3. Export both requested roles with matching duration and timeline, preferably lossless WAV for further editing. Preserve stereo/phase behavior when mixing. Keep the original and derived files distinguishable.
4. Verify files decode, contain finite non-silent audio, align in duration and remain below clipping. Audition vocal bleed, missing consonants, instrumental leakage and rap sections. Treat an ASR transcript as a diagnostic, not proof of faithful lyrics.

Deliver playable stems and explain their roles. If the user actually needs a finished new-vocal cover, switch to cover mode rather than reporting separation as completion.
