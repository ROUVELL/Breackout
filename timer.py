from pygame.time import get_ticks


class Timer:
    def __init__(self, duration, func=None, activate=False):
        self._last_update = get_ticks()
        self._duration = duration
        self._func = func
        ##########
        self._is_active = False  # Чи активний таймер в данний момент
        self._state = False  # True коли заданий час минув
        if activate:
            self.activate()

    @property
    def is_active(self):
        return self._is_active

    def get_remaining_time(self):
        return self._duration - (get_ticks() - self._last_update)

    def update(self):
        if self._is_active and not self._state:
            now = get_ticks()
            if now - self._last_update >= self._duration:
                self._state = True
                if self._func:
                    self._func()

    def activate(self):
        if not self._is_active:
            self._last_update = get_ticks()
            self._state = False
            self._is_active = True

    def deactivate(self):
        self._is_active = False

    def __bool__(self):
        return self._state


class TimerGroup:
    def __init__(self, **timers):
        self._items = timers

    def update(self):
        [timer.update() for timer in self._items.values()]

    def is_active(self, name):
        return self._items[name].is_active

    def activate(self, name):
        self._items[name].activate()

    def deactivate(self, name):
        self._items[name].deactivate()

    def get_remaining_time(self, name):
        return self._items[name].get_remaining_time()

