class Compass(object):
    '''Compass facade.

    .. versionadded:: 1.2.0
    '''

    @property
    def orientation(self):
        '''Property that returns values of the current compass
        (magnetic field) sensors, as a (x, y, z) tuple.
        Returns (None, None, None) if no data is currently available.
        '''
        return self.get_orientation()

    def enable(self):
        '''Activate the compass sensor.
        '''
        self._enable()

    def disable(self):
        '''Disable the compass sensor.
        '''
        self._disable()

    def get_orientation(self):
        return self._get_orientation()

    # private

    def _enable(self):
        raise NotImplementedError()

    def _disable(self):
        raise NotImplementedError()

    def _get_orientation(self):
        raise NotImplementedError()
