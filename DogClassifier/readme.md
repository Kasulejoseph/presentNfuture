Setup conda environment: `conda create -n env python=3 anaconda`
Activate conda env: `conda activate env`
install dependencies: `conda install -n yourenvname [package]`

Run bash script to test the model on the 3 CNN model archictecture
Run bash:  `sh run_models_batch.sh`


## Principle Objectives
Below you will find the principle objectives, a summary of the results, and discussion as to how `check_images.py` achieved these four objectives.

### Principle Objectives
[*] Correctly identify which pet images are of dogs (even if breed is misclassified) and which pet images aren't of dogs.
 
[*] Correctly classify the breed of dog, for the images that are of dogs.
 
[*] Determine which CNN model architecture (ResNet, AlexNet, or VGG), "best" achieve the objectives _1_ and _2_.
 
[*] Consider the time resources required to best achieve objectives _1_ and _2_, and determine if an alternative solution would have given a "good enough" result, given the amount of time each of the algorithms takes to run.
