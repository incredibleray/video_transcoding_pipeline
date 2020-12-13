from setuptools import setup, find_packages

setup(
    name='video_transcoding',
    version='1.0.0',
    url='https://github.com/incredibleray/video_transcoding_pipeline',

    package_dir={'': 'video_transcoding'},
    # packages=find_packages(where='video_transcoding'),
    python_requires='>=3.7, <4',
    install_requires=['absl-py'],

    extras_require={
        'dev': ['yapf'],
    },
)