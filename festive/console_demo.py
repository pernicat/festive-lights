import sys
import math

# Pixel color order constants
RGB = (0, 1, 2)
"""Red Green Blue"""
GRB = (1, 0, 2)
"""Green Red Blue"""
RGBW = (0, 1, 2, 3)
"""Red Green Blue White"""
GRBW = (1, 0, 2, 3)
"""Green Red Blue White"""


class ConsoleDemo:
    """
        A sequence of neopixels.

        :param None _: The pin to output neopixel data on.
        :param int n: The number of neopixels in the chain
        :param int bpp: Bytes per pixel. 3 for RGB and 4 for RGBW pixels.
        :param float brightness: Brightness of the pixels between 0.0 and 1.0 where 1.0 is full
          brightness
        :param bool auto_write: True if the neopixels should immediately change when set. If False,
          `show` must be called explicitly.
        :param tuple pixel_order: Set the pixel color channel order. GRBW is set by default.

        Example for Circuit Playground Express:

        .. code-block:: python

            import neopixel
            from board import *

            RED = 0x100000 # (0x10, 0, 0) also works

            pixels = neopixel.NeoPixel(NEOPIXEL, 10)
            for i in range(len(pixels)):
                pixels[i] = RED

        Example for Circuit Playground Express setting every other pixel red using a slice:

        .. code-block:: python

            import neopixel
            from board import *
            import time

            RED = 0x100000 # (0x10, 0, 0) also works

            # Using ``with`` ensures pixels are cleared after we're done.
            with neopixel.NeoPixel(NEOPIXEL, 10) as pixels:
                pixels[::2] = [RED] * (len(pixels) // 2)
                time.sleep(2)
        """

    def __init__(self, _, n, *, bpp=3, brightness=1.0, auto_write=True, pixel_order=None):
        # self.pin = digitalio.DigitalInOut(pin)
        # self.pin.direction = digitalio.Direction.OUTPUT
        self.n = n
        if pixel_order is None:
            self.order = GRBW
            self.bpp = bpp
        else:
            self.order = pixel_order
            self.bpp = len(self.order)
        self.buf = bytearray(self.n * self.bpp)
        # Set auto_write to False temporarily so brightness setter does _not_
        # call show() while in __init__.
        self.auto_write = False
        self.brightness = brightness
        self.auto_write = auto_write

    def deinit(self):
        """Blank out the NeoPixels and release the pin."""
        for i in range(len(self.buf)):
            self.buf[i] = 0
        # neopixel_write(self.pin, self.buf)
        # self.pin.deinit()
        sys.stdout.write("\n")

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.deinit()

    def __repr__(self):
        return "[" + ", ".join([str(x) for x in self]) + "]"

    def _set_item(self, index, value):
        if index < 0:
            index += len(self)
        if index >= self.n or index < 0:
            raise IndexError
        offset = index * self.bpp
        # r = 0
        # g = 0
        # b = 0
        # w = 0
        if isinstance(value, int):
            if value >> 24:
                raise ValueError("only bits 0->23 valid for integer input")
            r = value >> 16
            g = (value >> 8) & 0xff
            b = value & 0xff
            w = 0
            # If all components are the same and we have a white pixel then use it
            # instead of the individual components.
            if self.bpp == 4 and r == g and g == b:
                w = r
                r = 0
                g = 0
                b = 0
        elif (len(value) == self.bpp) or ((len(value) == 3) and (self.bpp == 4)):
            r, g, b, w = value if len(value) == 4 else value + (0,)
        else:
            raise ValueError("Color tuple size does not match pixel_order.")

        self.buf[offset + self.order[0]] = r
        self.buf[offset + self.order[1]] = g
        self.buf[offset + self.order[2]] = b
        if self.bpp == 4:
            self.buf[offset + self.order[3]] = w

    def __setitem__(self, index, val):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self.buf) // self.bpp)
            length = stop - start
            if step != 0:
                length = math.ceil(length / step)
            if len(val) != length:
                raise ValueError("Slice and input sequence size do not match.")
            for val_i, in_i in enumerate(range(start, stop, step)):
                self._set_item(in_i, val[val_i])
        else:
            self._set_item(index, val)

        if self.auto_write:
            self.show()

    def __getitem__(self, index):
        if isinstance(index, slice):
            out = []
            for in_i in range(*index.indices(len(self.buf) // self.bpp)):
                out.append(tuple(self.buf[in_i * self.bpp + self.order[i]]
                                 for i in range(self.bpp)))
            return out
        if index < 0:
            index += len(self)
        if index >= self.n or index < 0:
            raise IndexError
        offset = index * self.bpp
        return tuple(self.buf[offset + self.order[i]]
                     for i in range(self.bpp))

    def __len__(self):
        return len(self.buf) // self.bpp

    @property
    def brightness(self):
        """Overall brightness of the pixel"""
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        # pylint: disable=attribute-defined-outside-init
        self._brightness = min(max((brightness, 0.0)), 1.0)
        if self.auto_write:
            self.show()

    def fill(self, color):
        """Colors all pixels the given ***color***."""
        auto_write = self.auto_write
        self.auto_write = False
        for i, _ in enumerate(self):
            self[i] = color
        if auto_write:
            self.show()
        self.auto_write = auto_write

    def write(self):
        """.. deprecated: 1.0.0

             Use ``show`` instead. It matches Micro:Bit and Arduino APIs."""
        self.show()

    def show(self):
        output = ""
        for pixel in self:
            output += "\033[48;2;%d;%d;%dm \033[0m" % tuple([int(i * self.brightness) for i in pixel][:3])

        sys.stdout.write("\r" + output)
