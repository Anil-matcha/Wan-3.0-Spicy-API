import sys
import os
import argparse
import json

# Add the parent directory to the path so we can import the existing Wan30SpicyAPI
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from wan_3_0_spicy_api import Wan30SpicyAPI


def main():
    parser = argparse.ArgumentParser(description="Wan 3.0 Spicy CLI Wrapper for OpenClaw Skill")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    t2v = subparsers.add_parser("t2v", help="Generate video from text (Spicy)")
    t2v.add_argument("--prompt", required=True, help="Text prompt")
    t2v.add_argument("--resolution", default="720p", choices=["480p", "720p", "1080p"], help="Output resolution")
    t2v.add_argument("--aspect_ratio", default="16:9", help="Aspect ratio")
    t2v.add_argument("--duration", type=int, default=5, help="Duration in seconds (2-30)")
    t2v.add_argument("--thinking_mode", action="store_true", help="Enable deep-thinking mode")
    t2v.add_argument("--no_audio", action="store_true", help="Disable generated audio track")
    t2v.add_argument("--seed", type=int, default=-1, help="Random seed (-1 for random)")
    t2v.add_argument("--wait", action="store_true", help="Wait for completion")

    i2v = subparsers.add_parser("i2v", help="Generate video from image (Spicy)")
    i2v.add_argument("--prompt", required=True, help="Text prompt")
    i2v.add_argument("--image_url", required=True, help="Source image URL")
    i2v.add_argument("--last_image", help="Optional end-frame image URL")
    i2v.add_argument("--resolution", default="720p", choices=["480p", "720p", "1080p"], help="Output resolution")
    i2v.add_argument("--aspect_ratio", default="16:9", help="Aspect ratio")
    i2v.add_argument("--duration", type=int, default=5, help="Duration in seconds (2-30)")
    i2v.add_argument("--thinking_mode", action="store_true", help="Enable deep-thinking mode")
    i2v.add_argument("--no_audio", action="store_true", help="Disable generated audio track")
    i2v.add_argument("--seed", type=int, default=-1, help="Random seed (-1 for random)")
    i2v.add_argument("--wait", action="store_true", help="Wait for completion")

    r2v = subparsers.add_parser("r2v", help="Generate video from reference images/videos/audio (Spicy)")
    r2v.add_argument("--prompt", required=True, help="Text prompt")
    r2v.add_argument("--images", nargs="*", help="Up to 10 reference image URLs")
    r2v.add_argument("--videos", nargs="*", help="Up to 5 reference video URLs")
    r2v.add_argument("--audios", nargs="*", help="Up to 5 reference audio URLs")
    r2v.add_argument("--resolution", default="720p", choices=["480p", "720p", "1080p"], help="Output resolution")
    r2v.add_argument("--aspect_ratio", default="16:9", help="Aspect ratio")
    r2v.add_argument("--duration", type=int, default=5, help="Duration in seconds (2-30)")
    r2v.add_argument("--thinking_mode", action="store_true", help="Enable deep-thinking mode")
    r2v.add_argument("--no_audio", action="store_true", help="Disable generated audio track")
    r2v.add_argument("--seed", type=int, default=-1, help="Random seed (-1 for random)")
    r2v.add_argument("--wait", action="store_true", help="Wait for completion")

    status = subparsers.add_parser("status", help="Get task status")
    status.add_argument("--request_id", required=True, help="Request ID")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        api = Wan30SpicyAPI()

        if args.command == "t2v":
            res = api.text_to_video(args.prompt, args.resolution, args.aspect_ratio, args.duration,
                                     args.thinking_mode, not args.no_audio, args.seed)
        elif args.command == "i2v":
            res = api.image_to_video(args.prompt, args.image_url, args.last_image, args.resolution,
                                      args.aspect_ratio, args.duration, args.thinking_mode,
                                      not args.no_audio, args.seed)
        elif args.command == "r2v":
            res = api.reference_to_video(args.prompt, args.images, args.videos, args.audios,
                                          args.resolution, args.aspect_ratio, args.duration,
                                          args.thinking_mode, not args.no_audio, args.seed)
        elif args.command == "status":
            res = api.get_result(args.request_id)
            print(json.dumps(res, indent=2))
            return

        request_id = res.get("request_id")

        if args.wait and request_id:
            print(f"Task submitted: {request_id}. Waiting for completion...")
            result = api.wait_for_completion(request_id)
            print(json.dumps(result, indent=2))
        else:
            print(json.dumps(res, indent=2))

    except Exception as e:
        print(json.dumps({"error": str(e)}, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
