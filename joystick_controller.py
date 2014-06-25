import pygame
import numpy as np

class joystick():

    def __init__(self):
        print 'init-ing'
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() == 1:
            j = pygame.joystick.Joystick(0)
            self.j = j
            print 'Joystick connected'

        elif pygame.joystick.get_count() == 0:
            print 'No joystick found :( '

        else:
            print 'Too many joysticks!'

        j.init()
        self.num_axes = j.get_numaxes()
        self.axes = np.zeros((self.num_axes, ))

    def get_axes(self):
        pygame.event.pump()
        for ax in range(self.num_axes):
            self.axes[ax] = self.j.get_axis(ax)
