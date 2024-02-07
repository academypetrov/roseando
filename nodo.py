class PositionSensorsNode(Node):
    def __init__(self):
        super().__init__('position_sensors_node')
        self.joint_state_publisher = self.create_publisher(JointState, 'joint_states', 10)
        self.joint_names = ['joint1', 'joint2', 'joint3']
        self.joint_states = JointState()
        self.joint_states.name = self.joint_names
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        # Read position sensor data here
        # ...
        self.joint_states.position = [1.0, 2.0, 3.0]
        self.joint_state_publisher.publish(self.joint_states)