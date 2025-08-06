"""
Patch for audioop module compatibility with Python 3.13
This provides basic audioop functionality that pydub needs
"""

import sys
import numpy as np

# Create a mock audioop module
class MockAudioop:
    def __init__(self):
        pass
    
    def avg(self, fragment, width):
        """Calculate average of audio fragment"""
        if not fragment:
            return 0
        data = np.frombuffer(fragment, dtype=np.int16)
        return int(np.mean(data))
    
    def max(self, fragment, width):
        """Calculate maximum of audio fragment"""
        if not fragment:
            return 0
        data = np.frombuffer(fragment, dtype=np.int16)
        return int(np.max(data))
    
    def minmax(self, fragment, width):
        """Calculate min and max of audio fragment"""
        if not fragment:
            return (0, 0)
        data = np.frombuffer(fragment, dtype=np.int16)
        return (int(np.min(data)), int(np.max(data)))
    
    def rms(self, fragment, width):
        """Calculate RMS of audio fragment"""
        if not fragment:
            return 0
        data = np.frombuffer(fragment, dtype=np.int16)
        return int(np.sqrt(np.mean(data**2)))
    
    def cross(self, fragment, width):
        """Calculate zero crossings"""
        if not fragment:
            return 0
        data = np.frombuffer(fragment, dtype=np.int16)
        crossings = np.sum(np.diff(np.sign(data)) != 0)
        return crossings

# Create the mock module
mock_audioop = MockAudioop()

# Add the mock module to sys.modules
sys.modules['audioop'] = mock_audioop
sys.modules['pyaudioop'] = mock_audioop 