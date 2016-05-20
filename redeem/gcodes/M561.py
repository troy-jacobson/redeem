"""
GCode M561 

Example: M561

This cancels any bed-plane fitting as the result of probing (or anything else) and returns the machine to moving in the user's coordinate system.

Author: Elias Bakken
License: CC BY-SA: http://creativecommons.org/licenses/by-sa/2.0/
"""

from GCodeCommand import GCodeCommand
import numpy as np
import logging


class M561(GCodeCommand):

    def execute(self, g):
        self.printer.matrix_bed_comp = np.identity(3)

    def get_description(self):
        return "Reset bed level matrix to identity"
    
    def get_long_description(self):
        return ("This cancels any bed-plane fitting as the result of probing"
                " (or anything else) and returns the machine "
                "to moving in the user's coordinate system.")
