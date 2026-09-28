---
name: wan-3.0-spicy
description: Generate bold, high-contrast, high-motion AI videos with relaxed content moderation using Wan 3.0 Spicy (by Alibaba).
version: 1.0.0
metadata:
  openclaw:
    requires:
      env:
        - MUAPI_API_KEY
      bins:
        - python3.11
    emoji: 🌶️
    homepage: https://muapi.ai
    os: ["macos", "linux"]
---

# Wan 3.0 Spicy

Wan 3.0 Spicy is the relaxed-moderation tier of Alibaba's Wan 3.0 video model, delivered via MuAPI. It generates bold, high-contrast, high-motion video with synchronized audio from text, an image, or a mix of reference images/videos/audio, with reduced content-safety filtering for broader creative freedom.

## Prerequisites

- **MUAPI_API_KEY**: You must have an API key from [muapi.ai](https://muapi.ai). Set it as an environment variable.

## Usage Guide

### Text-to-Video
```bash
python3.11 skills/wan-3.0-spicy/wan_3_0_spicy_cli.py t2v --prompt "A dramatic cinematic scene with bold camera movement through a neon-lit city at night" --resolution 1080p --wait
```

### Image-to-Video
```bash
python3.11 skills/wan-3.0-spicy/wan_3_0_spicy_cli.py i2v --image_url "https://example.com/storm.jpg" --prompt "The camera pushes through the storm as dramatic light and high-energy motion build around the subject" --wait
```

### Image-to-Video with end frame
```bash
python3.11 skills/wan-3.0-spicy/wan_3_0_spicy_cli.py i2v --image_url "https://example.com/start.jpg" --last_image "https://example.com/end.jpg" --prompt "Transition from calm to chaos" --wait
```

### Reference-to-Video
Condition a video on up to 10 reference images, 5 reference videos, and 5 reference audios.
```bash
python3.11 skills/wan-3.0-spicy/wan_3_0_spicy_cli.py r2v --prompt "The two people from the reference images meet on the rainy street shown in the reference video" --images "https://example.com/person1.jpg" "https://example.com/person2.jpg" --videos "https://example.com/street.mp4" --wait
```

## Tips for Best Results

- **Be Descriptive**: Detailed, high-motion prompts get the best results out of the Spicy tier's bolder style.
- **Wait for Completion**: Use `--wait` to receive the final video URL directly. Without it, you get a `request_id` to check later with `status`.
- **Thinking Mode**: Enable `--thinking_mode` for complex prompts/scenes that need extra planning before generation.
- **Audio**: All endpoints generate a synchronized audio track by default; use `--no_audio` to disable it.
- **Reproducibility**: Pass `--seed` to reproduce a specific generation; omit (or `-1`) for a random seed.
- **Duration Range**: 2-30 seconds on every endpoint.

## Commands Reference

| Command | Arguments | Description |
| :--- | :--- | :--- |
| `t2v` | `--prompt`, `--resolution`, `--aspect_ratio`, `--duration`, `--thinking_mode`, `--no_audio`, `--seed`, `--wait` | Text to Video |
| `i2v` | `--prompt`, `--image_url`, `--last_image`, `--resolution`, `--aspect_ratio`, `--duration`, `--thinking_mode`, `--no_audio`, `--seed`, `--wait` | Image to Video |
| `r2v` | `--prompt`, `--images`, `--videos`, `--audios`, `--resolution`, `--aspect_ratio`, `--duration`, `--thinking_mode`, `--no_audio`, `--seed`, `--wait` | Reference to Video |
| `status` | `--request_id` | Check Task Status |
