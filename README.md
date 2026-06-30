# simple-gazebo-games

A beginner-level ROS 2 Jazzy and Gazebo Harmonic micro-project demonstrating differential-drive robots, ROS-Gazebo communication, sensors, and basic autonomous gameplay.

---

## Prerequisites

* **OS:** Ubuntu 24.04 (tested)
* **ROS 2:** Jazzy Jalisco
* **Gazebo:** Harmonic

---

## ROS 2 Installation

If ROS 2 is not installed, follow the [official ROS 2 Jazzy installation guide](https://docs.ros.org/en/jazzy/Installation.html)

---

## Gazebo Installation

If Gazebo is not installed, follow the [official Gazebo Harmonic installation guide](https://gazebosim.org/docs/harmonic/install_ubuntu/)

---

## Install required packages

```bash
sudo apt install ros-jazzy-ros-gz
sudo apt install ros-jazzy-teleop-twist-keyboard
```

## Workspace Setup

Create a ROS 2 workspace and clone the repository:

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

git clone https://github.com/Bhagabanta-Giri/simple-gazebo-games.git
```

Install missing dependencies:

```bash
rosdep install --from-paths src --ignore-src -r -y
```

Build the workspace:

```bash
cd ~/ros2_ws
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

---

## How to Play

Due to how ROS 2 handles raw keyboard inputs, this game requires a two-terminal setup.

The above setup steps must be done in both the terminals.

Launch the simulation:

```bash
ros2 launch game_gz police.launch.py
```

Once Gazebo starts:

Open the second terminal and run:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=/police/cmd_vel
```

Controls:

For Moving around:

```bash
   u    i    o
   j    k    l
   m    ,    .
```

For Holonomic mode (strafing), hold down the shift key:

```bash
   U    I    O
   J    K    L
   M    <    >
```

t : up (+z)
b : down (-z)

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

CTRL-C to quit

* Control the **Police** robot using the keyboard.
* The **Thief** robot moves autonomously with randomly generated velocity commands.
* Catch the thief before it escapes.

When the red pole on police collides with the thief, the game ends.

---

## Features

* Differential-drive robots
* ROS 2 ↔ Gazebo topic bridging
* Gazebo Harmonic simulation
* Autonomous thief movement
* Keyboard teleoperation
* Camera sensors
* Contact sensor based collision detection
* Modular ROS 2 package structure

---

## Experimental Branch

The repository also contains a branch named **`thief-game`**.

This branch contains an experimental version of the project based on a different gameplay idea. Development was paused after running into a few technical limitations, but the branch has been kept for future experimentation instead of being deleted.

If you have ideas, suggestions, or possible solutions, feel free to contribute through issues or pull requests.

---

## Reporting Issues

Found a bug or unexpected behavior?

Please open a GitHub Issue.

---

## Contributing

Suggestions and improvements are always welcome.

If you have an idea to improve the project, feel free to submit a pull request.

### Workflow

1. Fork the repository.

2. Clone your fork:

    ```bash
    git clone https://github.com/Bhagabanta-Giri/simple-gazebo-games.git
    ```

3. Create a feature branch:

    ```bash
    git checkout -b feature/your-feature-name
    ```

4. Make your changes.

5. Commit your work:

    ```bash
    git commit -m "Add brief description of feature"
    ```

6. Push the branch:

    ```bash
    git push origin feature/your-feature-name
    ```

7. Open a Pull Request.

---

## License

This project is licensed under the MIT License.

---

## Maintainer

[bhagabantagiri@gmail.com](mailto:bhagabantagiri@gmail.com)
