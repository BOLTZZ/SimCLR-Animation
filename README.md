# SimCLR-Animation
This is my repo containing the code for my SimCLR animation. SimCLR is a contrastive learning framework, originally designed for images (you can learn about SimCLR [here](https://www.datascientistsden.com/post/contrastive-learning-paper-simclr)). I've created this animation to visually demonstrate how SimCLR works and make the process more intuitive. 

To create this animation, I used [manim](https://github.com/3b1b/manim).
# Imports/Running
Run the following code to get the nessecary imports:
```python
!sudo apt update
!sudo apt install libcairo2-dev ffmpeg texlive texlive-latex-extra texlive-fonts-extra texlive-latex-recommended texlive-science tipa libpango1.0-dev
!pip install manim
!pip install IPython --upgrade
```
To run the animation, use the following code:
```python
%%manim -ql -p SimCLR2D
%%manim -ql -p SimCLR3D
```
# 2D Scene
To show what images correspond to what vectors, I start off with a 2D scene at first. Here, I show the vector-image pairs, showing the anchor (white cat), positive example (black cat), and negative example (puppy). Here's the [code](https://github.com/BOLTZZ/SimCLR-Animation/blob/main/Code/2D%20Scene.py) for the 2D scene. And, here's how the 2D Scene looks:

![2D scene](https://github.com/BOLTZZ/SimCLR-Animation/blob/main/Media/imageVectorPairs.gif)

# 3D Scene
To show the latent space, I used a 3D scene. Here, I demonstrate how the vectors are manipulated, using NT-Xent loss, to push the similar vectors together and push away the negativ example. Here's the [code](https://github.com/BOLTZZ/SimCLR-Animation/blob/main/Code/3D%20Scene.py) for the 3D scene. And, here's how the 3D Scene looks:

![3D scene](https://github.com/BOLTZZ/SimCLR-Animation/blob/main/Media/latentSpace.gif)

# Full Animation
I combine both scenes to get an overall animation:

![Full Animation](https://github.com/BOLTZZ/SimCLR-Animation/blob/main/Media/SimCLR%20Animation.gif)
