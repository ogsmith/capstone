import numpy as np
import pandas as pd

class Node():
    def __init__(self, port_number):
        self.port_number = port_number
        self.on_off = False
        self.enabled = True
        self.pulse_length = .0002
        self.wave_length = .5
        self.iteration = 0
        self.system_period = .0001
        self.c = .01 / self.system_period

    def get_port_number(self):
        return self.port_number

    def toggle_onoff(self):
        self.on_off = not self.on_off

    def set_onoff(self, state):
        self.on_off = state

    def get_onoff(self):
        return self.on_off

    def toggle_enabled(self):
        self.enabled = not self.enabled

    def set_enabled(self, state):
        self.enabled = state

    def get_enabled(self):
        return self.enabled

    def get_wave_length(self):
        return self.wave_length

    def get_pulse_length(self):
        return self.pulse_length

    def set_system_period(self, system_period):
        self.system_period = system_period

    def get_system_period(self):
        return self.system_period

    def set_wave_length(self, wave_length):
        self.wave_length = wave_length

    def set_pulse_length(self, pulse_length):
        self.pulse_length = pulse_length

    def get_state(self):
        # print(self.wave_length/self.system_period)
        # print(self.iteration * self.system_period)
        # print(self.pulse_length)
        # print(self.iteration)
        if self.on_off:
            if (self.iteration * self.c) > (self.wave_length / self.system_period):
                self.iteration = 0
            if ((self.iteration * self.c) * self.system_period) < self.pulse_length:
                self.iteration = self.iteration + 1

                return True
            else:
                self.iteration = self.iteration + 1
                return False
        else:
            self.iteration = 0
            return False

# Node states
class Node_State_Model():
    def __init__(self):
        self.port_numbers = 14
        self.ports = []
        for i in range(self.port_numbers):
            self.ports.append(Node(i))

    # sends the state of a paticular port
    # Port_Number as int -> binary int
    def get_state_firing(self, port_number):
        return self.ports[port_number].send_state()

    def get_states_firing(self):
        return map(Node.get_state, self.ports)

    def get_state_onoff(self, port_number):
        return self.ports[port_number].get_onoff()

    def get_states_onoff(self):
        return map(Node.get_onoff, self.ports)

    # toggle the state to paticular node
    # Port_Number as int -> null
    def toggle_port_onoff(self, port_number):
        self.ports[port_number].toggle_onoff()

    def toggle_port_enabled(self, port_number):
        self.ports[port_number].toggle_enabled()

    # sets the state to paticular node to a given value
    # Port_Number as int, bool -> null
    def set_port_to(self, port_number, state):
        self.ports[port_number].set_onoff(state)

    def set_pulse_lengths(self, port_number, time):
        self.ports[port_number].set_pulse_length(time)

    def set_wave_lengths(self, port_number, time):
        self.ports[port_number].set_wave_length(time)

    def get_pulse_length(self, port_number):
        return self.ports[port_number].get_pulse_lengths()

    def get_wave_length(self, port_number):
        return self.ports[port_number].get_wave_lengths()

    def get_pulse_lengths(self):
        return map(Node.get_pulse_lengths, self.ports)

    def get_wave_lengths(self):
        return map(Node.get_wave_lengths, self.ports)

if __name__ == '__main__':
    test_class = Node_State_Model()
    test_class.send_states()
    print "state all"
    print test_class.send_states()
    print "state 4"
    print test_class.send_state(4)
    print "state 7"
    print test_class.send_state(7)

    print "toggle 7"
    test_class.toggle_port(7)
    print "set 4 to True"
    test_class.set_port_to(4,True)

    print "state all"
    print test_class.send_states()
    print "state 4"
    print test_class.send_state(4)
    print "state 7"
    print test_class.send_state(7)

    print "toggle 7"
    test_class.toggle_port(7)
    print "state 7"
    print test_class.send_state(7)
