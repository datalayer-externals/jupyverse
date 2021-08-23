from setuptools import setup, find_packages  # type: ignore

setup(
    name="fps_retrolab",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["fps", "retrolab", "fps-contents", "fps-kernels"],
    entry_points={"fps_router": ["fps-retrolab = fps_retrolab.routes"]},
)