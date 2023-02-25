#!/bin/bash
# echo "enabling xcode build permissions"
# sudo xcodebuild -license accept
echo "brew isntalling portaudio as needed for pyaudio"
brew install portaudio espeak ffmpeg
echo "updating pip"
pip install --upgrade pip
echo "using pip to install python depencancies nltk"
pip install --upgrade clang SpeechRecognition pyaudio nltk numpy matplotlib keras_cv keras-nlp tensorflow pycocotools opencv-python tensorflow_text natsort tensorflow_io pydub