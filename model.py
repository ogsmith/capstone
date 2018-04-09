WAVE_LENGTH = .1
PULSE_LENGTH = .0002

class Node():
    def __init__(self, port_number):
        self.port_number = port_number
        self.on_off = False
        self.pulse_length = PULSE_LENGTH
        self.wave_length = WAVE_LENGTH
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
        self.port_numbers = 17
        self.ports = []
        self.changes = False
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
        self.changes = True

    def toggle_port_enabled(self, port_number):
        self.ports[port_number].toggle_enabled()
        self.changes = True

    def get_port_enabled(self, port_number):
        return self.ports[port_number].get_enabled()

    # sets the state to paticular node to a given value
    # Port_Number as int, bool -> null
    def set_port_to(self, port_number, state):
        self.ports[port_number].set_onoff(state)
        self.changes = True

    def set_pulse_lengths(self, port_number, time):
        self.ports[port_number].set_pulse_length(time)
        self.changes = True

    def set_wave_lengths(self, port_number, time):
        self.ports[port_number].set_wave_length(time)
        self.changes = True

    def get_pulse_length(self, port_number):
        return self.ports[port_number].get_pulse_length()

    def get_wave_length(self, port_number):
        return self.ports[port_number].get_wave_length()

    def get_pulse_lengths(self):
        return map(Node.get_pulse_length, self.ports)

    def get_wave_lengths(self):
        return map(Node.get_wave_length, self.ports)

    def reset_pulse_and_wave_lengths(self):
        for port in self.ports:
            port.set_wave_length(WAVE_LENGTH)
            port.set_pulse_length(PULSE_LENGTH)

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
