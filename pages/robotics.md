# Robotics

## Vex Robot Code
Having been my team's programmer for all four years of high school, I wrote quite a few robot programs. I've included some of the more notable ones below.

### Worlds 2018
This was the first time that I used PROS, an open-source C(++) framework for Vex robots, rather than the relatively limited RobotC. This codebase includes PID controllers, automated macros, recording and playback of actions, and a custom (and very bad) sensor fusion algorithm.

- View the source code at [github.com/77788J/77788J-Mark_VII](https://github.com/77788J/77788J-Mark_VII)
- Watch the robot in action
  - Autonomous routine: [https://youtu.be/3ucRSPnvfCc](https://youtu.be/3ucRSPnvfCc)
  - Another autonomous routine: [https://youtu.be/Mr4lmr4Meqw](https://youtu.be/Mr4lmr4Meqw)

### Late 2018
The first robot we built for the 2018-2019 season used a transmission between the chassis and lift to conserve motors. Controlling both systems simultaneously required carefully tuned control loops as well as a dynamic priority system to ensure that both subsystems remained stable.

- View the source code at [github.com/77788J/77788J-TP-Mark-I](https://github.com/77788J/77788J-TP-Mark-I)

### Early 2019
This code was written for a later robot that did away with the transmission. It included a Pixy camera that was used to automate intaking balls, aiming the catapult (the game involved shooting balls at targets), and following objects during the autonomous period.

- View the source code at [github.com/77788J/77788J-TP-Mark-II](https://github.com/77788J/77788J-TP-Mark-II)
- Watch the robot in action
  - Autonomous routine: [https://youtube.com/shorts/iE0eHTyWHIA](https://youtube.com/shorts/iE0eHTyWHIA)

### Mid-Season Rebuild 2019-2020
With this robot, we bit off much more than we could chew. The robot only lasted for a few weeks before we reverted to our previous design, so the code did not get much use. It was, however, the first time I used OkapiLib, a library included with PROS 3 that provided lots of useful functionality such as PID controllers, odometry, and motion profiling. This robot also had a transmission, this time between the chassis and the 'tilter'. This transmission was much more complicated (and, apparently, fragile) than the one used in the previous season, and it required a more complicated control system. A state machine was needed on top of the PID controllers and priority system to keep the transmission working properly.

- View the source code at [github.com/77788Y/77788Y-Mark-II](https://github.com/77788Y/77788Y-Mark-II)

### States 2020
This code was based on our first robot for the 2019-2020 season, so it does not include OkapiLib. It instead uses custom PID and motion profiling (based on a sine wive, which was not a good idea).

- View the source code at [github.com/77788Y/77788Y-Mark-1.5](https://github.com/77788Y/77788Y-Mark-1.5)
- Watch the robot in action
  - Early season "reveal" video: [https://youtu.be/MkmrA7s2rX0](https://youtu.be/MkmrA7s2rX0)
  - Autonomous routine: [https://youtu.be/h7xMGhkN6eA](https://youtu.be/h7xMGhkN6eA)

## ITZ Auto Planner
This was a simple Java program that I wrote to help plan autonomous routines for our robot. It allowed the user to draw a path on the game field and would provide angles and distances for each path segment.

- View the source code at [github.com/77788J/ITZ-Auto-Planner](https://github.com/77788J/ITZ-Auto-Planner)
- Download the latest release at [github.com/77788J/ITZ-Auto-Planner/releases](https://github.com/77788J/ITZ-Auto-Planner/releases)

![Screenshot of the ITZ Auto Planner](/res/itzautoplanner/sc-path.png)

## Vex Auto Generator
An improvement of "ITZ Auto Planner" from the previous season, this web-based program allowed the user to draw paths comprised of both lines and arcs. Paths could be saved to a file and loaded later. They could also be exported as C++ code for use in the robot's autonomous period.

- View the source code at [github.com/77788Y/Vex-Auto-Generator](https://github.com/77788Y/Vex-Auto-Generator)

- Visit the site at [77788y.github.io/Vex-Auto-Generator/](https://77788y.github.io/Vex-Auto-Generator/)

![Screenshot of the Vex Auto Generator](/res/tpautoplanner/sc-editpoint.png)