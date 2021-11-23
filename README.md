![Python version](https://img.shields.io/badge/Python-3.10.0-blue)

# Image Kernel in Python
Simple 3x3 image kernel implemented in python using Numpy, opencv, and scikit image libraries.

# Setup & run
`pip install -r requirements.txt`

`python image_kernels.py`

# Images

Original image:

![Lenna](https://raw.githubusercontent.com/Adilius/image-kernel-python/main/Lenna.png)

Scaled image and removed color channels:

![Lenna scaled](https://raw.githubusercontent.com/Adilius/image-kernel-python/main/Lenna_scaled.png)

Applying sharpen kernel:

```
kernel_sharpen = [
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
]
```

![Lenna sharp](https://raw.githubusercontent.com/Adilius/image-kernel-python/main/Lenna_sharpen.png)


Applying blur kernel:

```
kernel_blur = [
    [0.05, 0.1, 0.05],
    [0.1, 0.4, 0.1],
    [0.05, 0.1, 0.05]
]
```

![Lenna blur](https://raw.githubusercontent.com/Adilius/image-kernel-python/main/Lenna_blur.png)
