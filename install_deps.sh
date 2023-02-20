#!/bin/bash
# echo "enabling xcode build permissions"
# sudo xcodebuild -license accept
echo "brew isntalling portaudio as needed for pyaudio"
brew install portaudio espeak
echo "updating pip"
pip install --upgrade pip
echo "using pip to install python depencancies nltk"
pip install clang SpeechRecognition pyaudio nltk numpy matplotlib keras_cv tensorflow pycocotools