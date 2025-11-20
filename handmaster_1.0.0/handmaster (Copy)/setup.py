from setuptools import setup, find_packages

setup(
    name='handmaster',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'opencv-python', 'mediapipe', 'numpy', 'pyautogui'
    ],
)
