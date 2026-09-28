import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Wan30SpicyAPI:
    def __init__(self, api_key=None):
        """
        Initialize the Wan 3.0 Spicy API client.
        :param api_key: Your MuAPI.ai API key. Defaults to MUAPI_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv("MUAPI_API_KEY")
        if not self.api_key:
            raise ValueError("API Key is required. Set MUAPI_API_KEY in .env or pass it to the constructor.")

        self.base_url = "https://api.muapi.ai/api/v1"
        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }

    def text_to_video(self, prompt, resolution="720p", aspect_ratio="16:9", duration=5,
                       thinking_mode=False, enable_audio=True, seed=-1):
        """
        Submits a Wan 3.0 Spicy Text-to-Video task. Generates a bold, high-contrast,
        high-motion video with synchronized audio directly from a text prompt.

        :param prompt: Describe the bold, high-motion video you want to create.
        :param resolution: '480p', '720p', or '1080p'.
        :param aspect_ratio: 'adaptive', '16:9', '9:16', '1:1', '4:3', or '3:4'.
        :param duration: Video length in seconds (2-30).
        :param thinking_mode: Enable deep-thinking mode for complex prompts.
        :param enable_audio: Include a generated audio track with the video.
        :param seed: Random seed for reproducibility. Use -1 for a random seed.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/wan3.0-spicy-text-to-video"
        payload = {
            "prompt": prompt,
            "resolution": resolution,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "thinking_mode": thinking_mode,
            "enable_audio": enable_audio,
            "seed": seed,
        }
        return self._post_request(endpoint, payload)

    def image_to_video(self, prompt, image_url, last_image=None, resolution="720p",
                        aspect_ratio="16:9", duration=5, thinking_mode=False,
                        enable_audio=True, seed=-1):
        """
        Submits a Wan 3.0 Spicy Image-to-Video task. Animates a source image into a
        bold, high-contrast, high-motion video with synchronized audio, with an
        optional end-frame image.

        :param prompt: Describe the bold, high-motion scene you want to create.
        :param image_url: Source image to animate.
        :param last_image: Optional end-frame image to guide how the video should end.
        :param resolution: '480p', '720p', or '1080p'.
        :param aspect_ratio: 'adaptive', '16:9', '9:16', '1:1', '4:3', or '3:4'.
        :param duration: Video length in seconds (2-30).
        :param thinking_mode: Enable deep-thinking mode for complex prompts.
        :param enable_audio: Include a generated audio track with the video.
        :param seed: Random seed for reproducibility. Use -1 for a random seed.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/wan3.0-spicy-image-to-video"
        payload = {
            "prompt": prompt,
            "image_url": image_url,
            "resolution": resolution,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "thinking_mode": thinking_mode,
            "enable_audio": enable_audio,
            "seed": seed,
        }
        if last_image:
            payload["last_image"] = last_image
        return self._post_request(endpoint, payload)

    def reference_to_video(self, prompt, images_list=None, videos_list=None, audios_list=None,
                            resolution="720p", aspect_ratio="16:9", duration=5,
                            thinking_mode=False, enable_audio=True, seed=-1):
        """
        Submits a Wan 3.0 Spicy Reference-to-Video task. Generates a bold,
        high-contrast, high-motion video guided by a prompt plus up to 10 reference
        images, 5 reference videos, and 5 reference audios for visual and audio
        coherence. Reference media are identified by their array order.

        :param prompt: Describe the bold, high-motion video you want to create.
        :param images_list: Up to 10 reference image URLs for visual coherence guidance.
        :param videos_list: Up to 5 reference video clip URLs (1-15s each); total
                            reference + generated duration must not exceed 30s.
        :param audios_list: Up to 5 reference audio clip URLs (total duration up to 15s).
        :param resolution: '480p', '720p', or '1080p'.
        :param aspect_ratio: 'adaptive', '16:9', '9:16', '1:1', '4:3', or '3:4'.
        :param duration: Video length in seconds (2-30).
        :param thinking_mode: Enable deep-thinking mode for complex scene understanding.
        :param enable_audio: Include a generated audio track with the video.
        :param seed: Random seed for reproducibility. Use -1 for a random seed.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/wan3.0-spicy-reference-to-video"
        payload = {
            "prompt": prompt,
            "resolution": resolution,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "thinking_mode": thinking_mode,
            "enable_audio": enable_audio,
            "seed": seed,
        }
        if images_list:
            payload["images_list"] = images_list
        if videos_list:
            payload["videos_list"] = videos_list
        if audios_list:
            payload["audios_list"] = audios_list
        return self._post_request(endpoint, payload)

    def _post_request(self, endpoint, payload):
        response = requests.post(endpoint, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def upload_file(self, file_path):
        """
        Uploads a file (image, video, or audio) to MuAPI for use in generation tasks.

        :param file_path: Path to the local file to upload.
        :return: JSON response from the MuAPI containing the URL of the uploaded file.
        """
        endpoint = f"{self.base_url}/upload_file"

        # Omit Content-Type to let requests set the multipart boundary automatically
        headers = {
            "x-api-key": self.api_key
        }

        with open(file_path, "rb") as file_data:
            files = {"file": file_data}
            response = requests.post(endpoint, headers=headers, files=files)

        response.raise_for_status()
        return response.json()

    def get_result(self, request_id):
        """
        Polls for the result of a generation task.
        """
        endpoint = f"{self.base_url}/predictions/{request_id}/result"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def wait_for_completion(self, request_id, poll_interval=5, timeout=600):
        """
        Waits for the video generation to complete and returns the result.
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            result = self.get_result(request_id)
            status = result.get("status")

            if status == "completed":
                return result
            elif status == "failed":
                raise Exception(f"Video generation failed: {result.get('error')}")

            print(f"Status: {status}. Waiting {poll_interval} seconds...")
            time.sleep(poll_interval)

        raise TimeoutError("Timed out waiting for video generation to complete.")


if __name__ == "__main__":
    try:
        api = Wan30SpicyAPI()
        prompt = "A dramatic cinematic scene with bold camera movement through a neon-lit city at night"

        print(f"Submitting Wan 3.0 Spicy T2V task with prompt: {prompt}")
        submission = api.text_to_video(prompt=prompt, duration=5)
        request_id = submission.get("request_id")
        print(f"Task submitted. Request ID: {request_id}")

        print("Waiting for completion...")
        result = api.wait_for_completion(request_id)
        print(f"Generation completed! Video URL: {result.get('outputs', [result.get('url')])[0]}")

    except Exception as e:
        print(f"Error: {e}")
