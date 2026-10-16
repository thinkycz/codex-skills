# Game interaction acceptance

Use when the confirmed task concerns an interactive playfield, HUD or game feel; ordinary application forms do not need game styling.

- Translate the selected interaction into direct controls, state feedback and animation rather than exposing implementation sliders by default. Preserve meaningful health/turn/wind/timer information and keep the playfield usable at the requested viewport sizes.
- For hold-to-charge/release-to-fire or similar controls, verify pointer and keyboard input, press/release/cancel, focus loss, touch gestures and disabled/out-of-turn states. Do not let a stuck input or repeated event submit two actions.
- Keep rendered terrain, collision rules and state synchronization consistent. A visual smoothing change must preserve craters, holes and valid tank/projectile positions; do not silently replace authoritative physics to match an illustration.
- Verify motion and sound against confirmed direction, legibility, reduced-motion preferences and actual interaction timing. Rebuild expensive terrain assets when their data changes rather than every frame where the renderer supports caching.
- Exercise real turns, hits, misses, reconnect/rematch and relevant solo/multiplayer paths. Build success and a still screenshot do not establish animation quality or touch/device performance; report untested physical devices explicitly.
