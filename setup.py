from setuptools import setup, find_packages

setup(
    name="weather-checker",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "weather=weather.checker:get_weather"
        ]
    }
)
