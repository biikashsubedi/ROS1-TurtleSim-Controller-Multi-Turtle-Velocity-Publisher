# Project 1 — TurtleSim Controller
<img width="1919" height="1151" alt="Screenshot 2026-05-30 at 1 07 08 PM" src="https://github.com/user-attachments/assets/19e22396-c4a9-42dc-a909-b8dccb3efbba" />


A ROS1 keyboard controller for TurtleSim that supports multiple turtles simultaneously.

## Features
- Control any turtle by passing its name as an argument
- Publishes `geometry_msgs/Twist` to `/<turtle_name>/cmd_vel`
- Steady 10 Hz publish rate
- Supports 8-directional movement
- Turtle stops when no key is pressed

## Dependencies
- ROS Melodic
- Python 2.7
- `rospy`
- `geometry_msgs`

## Setup

```bash
mkdir -p ~/proj1_ws/src
cd ~/proj1_ws/src
git clone https://github.com/YOUR_USERNAME/proj1_turtlesim.git
cd ~/proj1_ws
catkin_make
source devel/setup.bash
```

## Usage

**Terminal 1 — roscore**
```bash
roscore
```

**Terminal 2 — TurtleSim**
```bash
rosrun turtlesim turtlesim_node
```

**Terminal 3 — Controller**
```bash
rosrun proj1_turtlesim controller.py turtle1
```

**Spawn a second turtle**
```bash
rosservice call /spawn 3.0 3.0 0.0 turtle2
```

**Terminal 4 — Second controller**
```bash
rosrun proj1_turtlesim controller.py turtle2
```

## Key Bindings

| Key | Action |
|-----|--------|
| `w` | Forward |
| `s` | Backward |
| `a` | Turn left |
| `d` | Turn right |
| `q` | Forward + Left |
| `e` | Forward + Right |
| `z` | Backward + Left |
| `c` | Backward + Right |

## Verify Publishing

```bash
rostopic echo /turtle1/cmd_vel
rostopic hz /turtle1/cmd_vel
```

## Project Structure

```
proj1_turtlesim/
├── scripts/
│   └── controller.py
├── CMakeLists.txt
├── package.xml
└── README.md
```
