"""
:mod:`randvis.simulation` provides the user interface to the package.

Each simulation is represented by a :class:`DVSim` instance. On each
instance, the :meth:`DVSim.simulate` method can be called as often as
you like to simulate a given number of steps.

The state of the system is visualized as the simulation runs, at intervals
that can be chosen. The graphics can also be saved to file at regular
intervals. By calling :meth:`DVSim.make_movie` after a simulation is complete,
individual graphics files can be combined into an animation.

Example
--------
::

    sim = DVSim((10, 15), 0.1, 12345, '../data')
    sim.simulate(50, 1, 5)
    sim.make_movie()

This code

#. creates a system with a 10x15 matrix, sets the noise level to 0.1,
   the random number generator seed to 12345 and specifies the filename
   for output;
#. performs a simulation of 50 steps, updating the graphics after each
   step and saving a figure after each 5th step;
#. creates a movie from the individual figures saved.

"""

import numpy as np
from .diffsys import DiffSys
from .graphics import Graphics


class DVSim:
    """Provides user interface for simulation, including visualization."""

    def __init__(self, sys_size, noise, seed,
                 img_dir=None, img_name=None, img_fmt=None):
        """
        :param sys_size:  system size, e.g. (5, 10)
        :type sys_size: (int, int)
        :param noise: noise level
        :type noise: float
        :param seed: random generator seed
        :type seed: int
        :param img_dir: directory for image files; no images if None
        :type img_dir: str
        :param img_name: beginning of name for image files
        :type img_name: str
        :param img_fmt: image file format suffix
        :type img_fmt: str

        .. note:: For default values for img_* parameters, see :mod:`randvis.graphics`.
        """

        np.random.seed(seed)
        self._system = DiffSys(sys_size, noise)
        self._graphics = Graphics(img_dir, img_name, img_fmt)

        self._step = 0
        self._final_step = None

    def simulate(self, num_steps, vis_steps=1, img_steps=None):
        """
        Run simulation while visualizing the result.

        :param num_steps: number of simulation steps to execute
        :param vis_steps: interval between visualization updates
        :param img_steps: interval between visualizations saved to files
                          (default: vis_steps)

        .. note:: Image files will be numbered consecutively.
        """

        if img_steps is None:
            img_steps = vis_steps

        if img_steps % vis_steps != 0:
            raise ValueError('img_steps must be multiple of vis_steps')

        self._final_step = self._step + num_steps
        self._graphics.setup(self._final_step, img_steps)

        while self._step < self._final_step:
            self._system.update()
            self._step += 1

            if self._step % vis_steps == 0:
                self._graphics.update(self._step,
                                      self._system.get_status(),
                                      self._system.mean_value())

    def make_movie(self, movie_fmt=None):
        """
        Creates MPEG4 movie from visualization images saved.

        .. :note:
            Requires ffmpeg for MP4 and magick for GIF

        The movie is stored as img_base + movie_fmt.
        """

        self._graphics.make_movie(movie_fmt)
