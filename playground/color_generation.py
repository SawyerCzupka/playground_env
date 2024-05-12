import numpy as np
import matplotlib.pyplot as plt
from gym.spaces import Box

n_colors = 10


def plot_colors(color, shade):
    """
    Plots a sample of colors from the color x shade color class.

    Parameters
    ----------
    color: str
        Color in red, blue, green.
    shade: str
        Shade in light, dark.

    """
    color_class = Color(color, shade)
    array = np.zeros([n_colors, n_colors, 3])
    for i in range(n_colors):
        for j in range(n_colors):
            array[i, j, :] = color_class.sample()
    plt.figure()
    plt.imshow(array)


class Color:
    def __init__(self, color, shade):
        """
        Implements a color class characterized by a color and shade attributes.
        Parameters
        ----------
        color: str
            Color in red, blue, green.
        shade: str
            Shade in light, dark.
        """
        self.color = color
        self.shade = shade
        if color == "blue":
            if shade == "light":
                self.space = Box(
                    low=np.array([0.3, 0.7, 0.9]),
                    high=np.array([0.5, 0.8, 1.0]),
                    dtype=np.float32,
                )
            elif shade == "dark":
                self.space = Box(
                    low=np.array([0.0, 0.0, 0.8]),
                    high=np.array([0.2, 0.2, 0.9]),
                    dtype=np.float32,
                )
            else:
                raise NotImplementedError("shade is either 'light' or 'dark'")
        elif color == "red":
            if shade == "light":
                self.space = Box(
                    low=np.array([0.9, 0.4, 0.35]),
                    high=np.array([1, 0.6, 0.65]),
                    dtype=np.float32,
                )
            elif shade == "dark":
                self.space = Box(
                    low=np.array([0.5, 0.0, 0.0]),
                    high=np.array([0.7, 0.1, 0.1]),
                    dtype=np.float32,
                )
            else:
                raise NotImplementedError("shade is either 'light' or 'dark'")
        elif color == "green":
            if shade == "light":
                self.space = Box(
                    low=np.array([0.4, 0.8, 0.4]),
                    high=np.array([0.6, 1, 0.5]),
                    dtype=np.float32,
                )
            elif shade == "dark":
                self.space = Box(
                    low=np.array([0.0, 0.4, 0.0]),
                    high=np.array([0.1, 0.6, 0.1]),
                    dtype=np.float32,
                )
            else:
                raise NotImplementedError
        elif color == "dark":
            if shade == "dark":
                self.space = Box(
                    low=np.array([0.0, 0.0, 0.0]),
                    high=np.array([0.3, 0.3, 0.3]),
                    dtype=np.float32,
                )
            elif shade == "light":
                self.space = Box(
                    low=np.array([1.0, 1.0, 1.0]),
                    high=np.array([2.0, 2.0, 2.0]),
                    dtype=np.float32,
                )
            else:
                raise NotImplementedError
        else:
            raise NotImplementedError("color is 'red', 'blue' or 'green'")

    def contains_old(self, rgb):
        """
        Whether the class contains a given rgb code.
        Parameters
        ----------
        rgb: 1D nd.array of size 3

        Returns
        -------
        contains: Bool
            True if rgb code in given Color class.
        """
        contains = self.space.contains(rgb)
        if self.color == "red" and self.shade == "light":
            contains = contains and (rgb[2] - rgb[1] <= 0.05)
        return contains

    def contains(self, rgb):
        """
        Check if the given rgb array is within the bounds of the color space.
        This should return True if each component of rgb is >= to the corresponding component of self.space.low
        and < the corresponding component of self.space.high.
        """
        return np.all((rgb >= self.space.low) & (rgb < self.space.high))

    def sample(self):
        """
        Sample an rgb code from the Color class

        Returns
        -------
        rgb: 1D nd.array of size 3
        """
        rgb = np.random.uniform(self.space.low, self.space.high, 3)
        if self.color == "red" and self.shade == "light":
            print("touched")
            rgb[2] = rgb[1] + np.random.uniform(-0.05, 0.05)

        # print(f"Sampled color: {rgb}")
        rgb = np.clip(rgb, self.space.low, self.space.high)
        # print(f"Clipped color: {rgb}")

        # print(f"Contains: {self.contains(rgb)}")
        # print(f"Contains_2: {self.contains(rgb)}")
        # print(f"Space: {self.space.low} - {self.space.high}")

        assert self.contains(rgb), "Sampled RGB value out of bounds"
        return rgb


def sample_color(color, shade):
    """
    Sample an rgb code from the Color class

    Parameters
    ----------
    color: str
        Color in red, blue, green.
    shade: str
        Shade in light, dark.

    Returns
    -------
    rgb: 1D nd.array of size 3
    """
    color_class = Color(color, shade)
    return color_class.sample()
