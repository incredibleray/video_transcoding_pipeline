from setuptools import setup

setup(
    name='video_transcoding',
    version='1.0.1',
    url='https://github.com/incredibleray/video_transcoding_pipeline',

    packages=['video_transcoding'],
    python_requires='>=3.6, <4',
    install_requires=['absl-py'],

    extras_require={
        'dev': ['yapf'],
    },
)
