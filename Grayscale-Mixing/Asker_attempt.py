import numpy as np
import scipy.misc
import matplotlib.pyplot as plt


# matplotlib inline

# Adapted from the answers of Ivan Kuckir and Royi here:
# https://dsp.stackexchange.com/questions/688/what-is-the-algorithm-behind-photoshops-black-and-white-adjustment-layer?newreg=77420cc185fd44099d8be961e736eb0c

def rgb2hls(img):
    """Adapted to use numpy from
       https://github.com/python/cpython/blob/2.7/Lib/colorsys.py"""
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]

    maxc = np.max(img, axis=-1)
    minc = np.min(img, axis=-1)
    l = (minc + maxc) / 2

    mask = np.ones_like(r)
    mask[np.where(minc == maxc, minc, maxc)] = 0
    mask = mask.astype(np.bool)

    smask = np.greater(l, 0.5).astype(np.float32)

    s = (1.0 - smask) * ((maxc - minc) / (maxc + minc)) + smask * ((maxc - minc) / (2.0 - maxc - minc))
    s[~mask] = 0
    rc = np.where(mask, (maxc - r) / (maxc - minc), 0)
    gc = np.where(mask, (maxc - g) / (maxc - minc), 0)
    bc = np.where(mask, (maxc - b) / (maxc - minc), 0)

    rmask = np.equal(r, maxc).astype(np.float32)
    gmask = np.equal(g, maxc).astype(np.float32)
    rgmask = np.logical_or(rmask, gmask).astype(np.float32)

    h = rmask * (bc - gc) + gmask * (2.0 + rc - bc) + (1.0 - rgmask) * (4.0 + gc - rc)
    h = np.remainder(h / 6.0, 1.0)
    h[~mask] = 0
    return np.stack([h, l, s], axis=-1)


def black_and_white_adjustment(image, weights):  
    # normalize input image to (0, 1) if uint8
    if 'uint8' in (image).dtype.name:
        image = image / 255

    # linearly remap input coeff [-200, 300] to [-2.5, 2.5]
    weights = (weights - 50) / 100
    n_weights = len(weights)
    h, w = image.shape[:2]

    # convert rgb to hls
    hls_img = rgb2hls(image)

    output = np.zeros((h, w), dtype=np.float32)

    # see figure 9 of https://en.wikipedia.org/wiki/HSL_and_HSV
    # to understand the algorithm
    for y in range(h):
        for x in range(w):
            hue_val = 6 * hls_img[y, x, 0]

            # Use distance on a hexagone (maybe circular distance is better?)
            diff_val = min(abs(0 - hue_val), abs(1 - (0 - hue_val)))
            luminance_coeff = weights[0] * max(0, 1 - diff_val)

            for k in range(1, n_weights):
                luminance_coeff += weights[k] * max(0, 1 - abs(k - hue_val))

            # output[y, x] = min(max(hls_img[y, x, 1] * (1 + luminance_coeff), 0), 1)
            output[y, x] = hls_img[y, x, 1] * (1 + luminance_coeff)


    return output


image = scipy.misc.imread("lavee.jpg")
w = np.array([40, 85, 204, 60, 20, 80])
out = black_and_white_adjustment(image, w)
plt.figure(figsize=(15, 20))
plt.imshow(out, cmap='gray')