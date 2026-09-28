import json
from mcp.server.fastmcp import FastMCP
from wan_3_0_spicy_api import Wan30SpicyAPI

# Initialize FastMCP server
mcp = FastMCP("Wan 3.0 Spicy API Server")


def get_api():
    return Wan30SpicyAPI()


@mcp.tool()
def text_to_video(prompt: str, resolution: str = "720p", aspect_ratio: str = "16:9", duration: int = 5,
                   thinking_mode: bool = False, enable_audio: bool = True, seed: int = -1) -> str:
    """
    Generate a bold, high-contrast, high-motion video with synchronized audio from a text prompt using Wan 3.0 Spicy.

    :param resolution: '480p', '720p', or '1080p'.
    :param aspect_ratio: 'adaptive', '16:9', '9:16', '1:1', '4:3', or '3:4'.
    :param duration: Video length in seconds (2-30).
    :param thinking_mode: Enable deep-thinking mode for complex prompts.
    :param enable_audio: Include a generated audio track.
    :param seed: Random seed; -1 for random.
    """
    api = get_api()
    result = api.text_to_video(prompt, resolution, aspect_ratio, duration, thinking_mode, enable_audio, seed)
    return json.dumps(result, indent=2)


@mcp.tool()
def image_to_video(prompt: str, image_url: str, last_image: str = None, resolution: str = "720p",
                    aspect_ratio: str = "16:9", duration: int = 5, thinking_mode: bool = False,
                    enable_audio: bool = True, seed: int = -1) -> str:
    """
    Animate a source image into a bold, high-motion video using Wan 3.0 Spicy, with an optional end-frame image.
    """
    api = get_api()
    result = api.image_to_video(prompt, image_url, last_image, resolution, aspect_ratio, duration, thinking_mode, enable_audio, seed)
    return json.dumps(result, indent=2)


@mcp.tool()
def reference_to_video(prompt: str, images_list: list[str] = None, videos_list: list[str] = None,
                        audios_list: list[str] = None, resolution: str = "720p", aspect_ratio: str = "16:9",
                        duration: int = 5, thinking_mode: bool = False, enable_audio: bool = True, seed: int = -1) -> str:
    """
    Generate a bold, high-motion video guided by up to 10 reference images, 5 reference videos, and 5 reference audios using Wan 3.0 Spicy.
    """
    api = get_api()
    result = api.reference_to_video(prompt, images_list, videos_list, audios_list, resolution, aspect_ratio, duration, thinking_mode, enable_audio, seed)
    return json.dumps(result, indent=2)


@mcp.tool()
def upload_file(file_path: str) -> str:
    """
    Upload a local file (image, video, or audio) to MuAPI for use in generation tasks.
    """
    api = get_api()
    result = api.upload_file(file_path)
    return json.dumps(result, indent=2)


@mcp.tool()
def get_task_status(request_id: str) -> str:
    """
    Check the status and get results of a generation task.
    """
    api = get_api()
    result = api.get_result(request_id)
    return json.dumps(result, indent=2)


if __name__ == "__main__":
    mcp.run()
