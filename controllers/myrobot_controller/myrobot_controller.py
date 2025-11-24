from controller import Robot, DistanceSensor, Motor

robot = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getMotor("left_wheel")
right_motor = robot.getMotor("right_wheel")
left_back_motor = robot.getMotor("left_back_wheel")
right_back_motor = robot.getMotor("right_back_wheel")

for motor in [left_motor, right_motor, left_back_motor, right_back_motor]:
    motor.setPosition(float('inf'))
    motor.setVelocity(0.0)

ds = robot.getDistanceSensor("ds_front")
ds.enable(timestep)

max_speed = 6.0

while robot.step(timestep) != -1:
    distance = ds.getValue()
    if distance < 800:
        left_motor.setVelocity(max_speed)
        left_back_motor.setVelocity(max_speed)
        right_motor.setVelocity(-max_speed)
        right_back_motor.setVelocity(-max_speed)
    else:
        for motor in [left_motor, right_motor, left_back_motor, right_back_motor]:
            motor.setVelocity(max_speed)
