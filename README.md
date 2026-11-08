# Wan 3.0 Spicy API: Python Wrapper for Alibaba's Relaxed-Moderation AI Video Generator

[![Powered by MuAPI](https://img.shields.io/badge/Powered%20by-MuAPI-6366f1?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxNHYtNGgtMnYtMmg0djZoLTJ6bTAtOFY2aDJ2MmgtMnoiLz48L3N2Zz4=)](https://muapi.ai?utm_source=github&utm_medium=badge&utm_campaign=wan-3.0-spicy-api)

[![PyPI version](https://img.shields.io/pypi/v/wan-3-0-spicy-api.svg)](https://pypi.org/project/wan-3-0-spicy-api/)
[![GitHub stars](https://img.shields.io/github/stars/Anil-matcha/Wan-3.0-Spicy-API.svg)](https://github.com/Anil-matcha/Wan-3.0-Spicy-API/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

The most comprehensive Python wrapper for the **Wan 3.0 Spicy API** (developed by Alibaba), delivered via [muapi.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=wan-3.0-spicy-api). Wan 3.0 Spicy is the relaxed-moderation tier of [Wan 3.0](https://github.com/Anil-matcha/Wan-3.0-API) — the same bold, high-contrast, high-motion video generation with synchronized audio, but with **reduced content-safety filtering** for broader creative freedom.

> ⚠️ **Content policy notice**: "Spicy" means reduced automated content-safety filtering, not an anything-goes endpoint. Generated content still must comply with MuAPI's and the underlying provider's terms of service and applicable law. Do not use this API to generate content involving minors, non-consensual imagery, or other prohibited material.

## Related Projects

- [Spicy AI Video Generator API](https://github.com/Anil-matcha/Spicy-AI-Video-Generator-API) — compare spicy video endpoints across Seedance 2.5/2, Wan 3.0 and MiniMax H3 in one guide.
- [Wan-3.0-API](https://github.com/Anil-matcha/Wan-3.0-API) — Python SDK and MCP server for the standard-moderation Wan 3.0 API.
- [Wan-3.0-Prime-API](https://github.com/Anil-matcha/Wan-3.0-Prime-API) — Python SDK and MCP server for the higher-fidelity Wan 3.0 Prime tier.
- [wan-3.0-comfyui](https://github.com/Anil-matcha/wan-3.0-comfyui) — Run Wan 3.0 inside ComfyUI.
- [Seedance-2-Spicy-API](https://github.com/Anil-matcha/Seedance-2-Spicy-API) — Python SDK and MCP server for the Seedance 2 Spicy tier.
- [Seedance-2.5-Spicy-API](https://github.com/Anil-matcha/Seedance-2.5-Spicy-API) — Python SDK and MCP server for the Seedance 2.5 Spicy tier.
- [Seedance-2-API](https://github.com/Anil-matcha/Seedance-2-API) — Python wrapper for the standard-moderation Seedance 2.0/2.5/2 Mini API.
- [awesome-ai-video-models](https://github.com/Anil-matcha/awesome-ai-video-models) — Curated list of AI video generation models and APIs.

## 🚀 Why Use Wan 3.0 Spicy API?

- **Relaxed Content Filtering**: Broader creative range than the standard Wan 3.0 tier, while keeping the same underlying model quality.
- **Bold, High-Contrast Motion**: Tuned for dramatic camera movement and expressive, high-energy scenes.
- **Synchronized Audio**: Every endpoint can include a generated audio track matched to the video.
- **Text-to-Video, Image-to-Video, and Reference-to-Video**: Three generation modes in one SDK.
- **Reference-to-Video**: Condition a single generation on up to 10 images, 5 videos, and 5 audio clips for visual and audio coherence.
- **Thinking Mode**: Optional deep-thinking mode for complex prompts and multi-subject scenes.
- **Developer-First**: Simple Python SDK plus a matching MCP server for Claude Desktop, Cursor, and other AI assistants.

## 🌟 Key Features

- ✅ **Text-to-Video**: Generate bold, high-motion video directly from a text prompt.
- ✅ **Image-to-Video**: Animate a source image, with an optional end-frame image for controlled transitions.
- ✅ **Reference-to-Video**: Guide generation with up to 10 reference images, 5 reference videos, and 5 reference audio clips, identified by array order.
- ✅ **Selectable Resolution**: `480p`, `720p`, or `1080p`.
- ✅ **Flexible Aspect Ratios**: `adaptive`, `16:9`, `9:16`, `1:1`, `4:3`, `3:4`.
- ✅ **Durations up to 30 seconds** on every endpoint.
- ✅ **Reproducible Seeds**: Pass a `seed` to reproduce a specific generation.
- ✅ **File Upload**: Upload local images/videos/audio directly via `upload_file()`.

---

## 🛠 Installation

### Via Pip (Recommended)
```bash
pip install wan-3-0-spicy-api
```

### From Source
```bash
git clone https://github.com/Anil-matcha/Wan-3.0-Spicy-API.git
cd Wan-3.0-Spicy-API
pip install -r requirements.txt
```

### Configuration
Create a `.env` file in the root directory and add your [MuAPI](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=wan-3.0-spicy-api) API key:
```env
MUAPI_API_KEY=your_muapi_api_key_here
```

---

## 🤖 Wan 3.0 Spicy MCP Server

Use Wan 3.0 Spicy as an **MCP (Model Context Protocol)** server so AI assistants (Claude Desktop, Cursor, etc.) can invoke the tools directly.

```bash
python3 mcp_server.py
```

Test with the MCP Inspector:
```bash
npx -y @modelcontextprotocol/inspector python3 mcp_server.py
```

---

## 💻 Quick Start (Python)

```python
from wan_3_0_spicy_api import Wan30SpicyAPI

api = Wan30SpicyAPI()

# Text-to-Video
submission = api.text_to_video(
    prompt="A dramatic cinematic scene with bold camera movement through a neon-lit city at night",
    resolution="1080p",
    aspect_ratio="16:9",
    duration=5,
)
result = api.wait_for_completion(submission["request_id"])
print(f"Video: {result['outputs'][0]}")
```

---

## 📡 API Endpoints & Reference

### 1. Wan 3.0 Spicy Text-to-Video
**Endpoint**: `POST https://api.muapi.ai/api/v1/wan3.0-spicy-text-to-video`

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `prompt` | string | Yes | — | Describe the bold, high-motion video you want to create. |
| `resolution` | enum | No | `720p` | `480p`, `720p`, `1080p` |
| `aspect_ratio` | enum | No | `16:9` | `adaptive`, `16:9`, `9:16`, `1:1`, `4:3`, `3:4` |
| `duration` | int | No | `5` | Seconds (2-30) |
| `thinking_mode` | boolean | No | `false` | Deep-thinking mode for complex prompts |
| `enable_audio` | boolean | No | `true` | Include a generated audio track |
| `seed` | int | No | `-1` | Random seed; `-1` for random |

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/wan3.0-spicy-text-to-video" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A dramatic cinematic scene with bold camera movement through a neon-lit city at night",
      "resolution": "1080p",
      "aspect_ratio": "16:9",
      "duration": 5
  }'
```

### 2. Wan 3.0 Spicy Image-to-Video
**Endpoint**: `POST https://api.muapi.ai/api/v1/wan3.0-spicy-image-to-video`

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `prompt` | string | Yes | — | Describe the bold, high-motion scene you want to create. |
| `image_url` | string | Yes | — | Source image to animate. |
| `last_image` | string | No | — | Optional end-frame image to guide how the video should end. |
| `resolution` | enum | No | `720p` | `480p`, `720p`, `1080p` |
| `aspect_ratio` | enum | No | `16:9` | `adaptive`, `16:9`, `9:16`, `1:1`, `4:3`, `3:4` |
| `duration` | int | No | `5` | Seconds (2-30) |
| `thinking_mode` | boolean | No | `false` | Deep-thinking mode for complex prompts |
| `enable_audio` | boolean | No | `true` | Include a generated audio track |
| `seed` | int | No | `-1` | Random seed; `-1` for random |

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/wan3.0-spicy-image-to-video" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "The camera pushes through the storm as dramatic light and high-energy motion build around the subject",
      "image_url": "https://example.com/storm.jpg",
      "resolution": "1080p"
  }'
```

### 3. Wan 3.0 Spicy Reference-to-Video
**Endpoint**: `POST https://api.muapi.ai/api/v1/wan3.0-spicy-reference-to-video`

Guides generation with a prompt plus up to 10 reference images, 5 reference videos, and 5 reference audios. Reference media are identified by their array order.

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `prompt` | string | Yes | — | Describe the bold, high-motion video you want to create. |
| `images_list` | array[string] | No | — | Up to 10 reference image URLs for visual coherence. |
| `videos_list` | array[string] | No | — | Up to 5 reference video URLs (MP4/MOV, 1-15s each; total reference + generated duration ≤ 30s). |
| `audios_list` | array[string] | No | — | Up to 5 reference audio clip URLs (total duration up to 15s). |
| `resolution` | enum | No | `720p` | `480p`, `720p`, `1080p` |
| `aspect_ratio` | enum | No | `16:9` | `adaptive`, `16:9`, `9:16`, `1:1`, `4:3`, `3:4` |
| `duration` | int | No | `5` | Seconds (2-30) |
| `thinking_mode` | boolean | No | `false` | Deep-thinking mode for complex scene understanding |
| `enable_audio` | boolean | No | `true` | Include a generated audio track |
| `seed` | int | No | `-1` | Random seed; `-1` for random |

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/wan3.0-spicy-reference-to-video" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "The two people from the reference images meet on the rainy street shown in the reference video",
      "images_list": ["https://example.com/person1.jpg", "https://example.com/person2.jpg"],
      "videos_list": ["https://example.com/street.mp4"]
  }'
```

---

## 💰 Pricing

| Endpoint | Cost |
|---|---|
| Wan 3.0 Spicy Text-to-Video | $0.55 / generation |
| Wan 3.0 Spicy Image-to-Video | $0.55 / generation |
| Wan 3.0 Spicy Reference-to-Video | $0.55 / generation |

Pricing is illustrative and subject to change — check [muapi.ai/wan-spicy](https://muapi.ai/wan-spicy?utm_source=github&utm_medium=readme&utm_campaign=wan-3.0-spicy-api) for current rates.

---

## 📖 Method Reference

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `text_to_video` | `prompt`, `resolution`, `aspect_ratio`, `duration`, `thinking_mode`, `enable_audio`, `seed` | Text to Video. |
| `image_to_video` | `prompt`, `image_url`, `last_image`, `resolution`, `aspect_ratio`, `duration`, `thinking_mode`, `enable_audio`, `seed` | Image to Video. |
| `reference_to_video` | `prompt`, `images_list`, `videos_list`, `audios_list`, `resolution`, `aspect_ratio`, `duration`, `thinking_mode`, `enable_audio`, `seed` | Reference to Video. |
| `upload_file` | `file_path` | Upload a local file (image, video, or audio) to MuAPI. |
| `get_result` | `request_id` | Check task status. |
| `wait_for_completion` | `request_id`, `poll_interval`, `timeout` | Blocking helper for generation tasks. |

---

## 🔗 Official Resources
- **Landing page**: [Wan 3.0 Spicy on MuAPI](https://muapi.ai/wan-spicy?utm_source=github&utm_medium=readme&utm_campaign=wan-3.0-spicy-api)
- **Playground**: [Text-to-Video](https://muapi.ai/playground/wan3.0-spicy-text-to-video?utm_source=github&utm_medium=readme&utm_campaign=wan-3.0-spicy-api) · [Image-to-Video](https://muapi.ai/playground/wan3.0-spicy-image-to-video?utm_source=github&utm_medium=readme&utm_campaign=wan-3.0-spicy-api)
- **Access Keys**: [muapi.ai/access-keys](https://muapi.ai/access-keys?utm_source=github&utm_medium=readme&utm_campaign=wan-3.0-spicy-api)
- **API Reference**: [muapi.ai/docs/api-reference](https://muapi.ai/docs/api-reference?utm_source=github&utm_medium=readme&utm_campaign=wan-3.0-spicy-api)
- **API Provider**: [MuAPI.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=wan-3.0-spicy-api)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Keywords**: Wan 3.0 Spicy API, Wan 3.0 Spicy, Alibaba Wan video, uncensored AI video generator, relaxed content moderation video API, Text-to-Video AI, Image-to-Video API, Reference-to-Video, Wan Python SDK, MuAPI, Video Generation API, Cinematic AI Video, Python Video API.
