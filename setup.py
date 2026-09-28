from setuptools import setup

setup(
    name="wan-3-0-spicy-api",
    version="0.1.0",
    author="Anil Matcha",
    description="Python wrapper for Alibaba's Wan 3.0 Spicy API — bold, high-contrast, high-motion video with synchronized audio and relaxed content moderation, delivered via MuAPI. Text-to-Video, Image-to-Video, and Reference-to-Video.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    py_modules=["wan_3_0_spicy_api", "mcp_server"],
    install_requires=[
        "requests",
        "python-dotenv",
        "mcp[cli]"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
