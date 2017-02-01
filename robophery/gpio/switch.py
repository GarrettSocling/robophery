#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from robophery.gpio import GpioModule

logger = logging.getLogger("robophery.gpio.switch")


class SwitchModule(GpioModule):


    def __init__(self, kwargs):
        self.name = kwargs.get('name')
        self.set_port(kwargs.get('port'))


    @property
    def get_data(self):
        """
        Switch status readings.
        """

        GPIO.setup(port, GPIO.IN)
        state = GPIO.input(self.port)

        press_count = press_delta = state
     
        values = [
            ('%s.press_count' % self.name, press_count, ),
            ('%s.press_delta' % self.name, press_delta, ),
        ]
        return values


    @property
    def get_meta_data(self):
        """
        Get the readings meta-data.
        """
        return {
            'press_count': {
                'type': 'counter',
                'unit': 's',
                'precision': 0.1,
                'range_low': 0,
                'range_high': None,
                'sensor': 'switch'
            },
            'press_delta': {
                'type': 'delta',
                'unit': 's',
                'precision': 0.1,
                'range_low': 0,
                'range_high': None,
                'sensor': 'switch'
            }
        }
