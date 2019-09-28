# defines scenario upon which the world is built
class BaseScenario(object):
    # initialize environment parameters
    def __init__(self, num_agents=None):
        self.num_agents = num_agents

    # create elements of the world
    def make_world(self):
        raise NotImplementedError()

    # create initial conditions of the world
    def reset_world(self, world):
        raise NotImplementedError()
