# Hi, I'm Zach
I'm a computer engineering student interested in robotics and embedded programming. I have experience in C, C++, Python, and JavaScript.

# Projects
<details>
<summary>Web Dev</summary>
Web development isn't my favorite thing to do, but I think it's an important skill to have. I've become fairly comfortable with web technologies, both frontend and backend, and I have a few projects that I'm proud of.

## Rankr
A website for ranking TV episodes. This was my first project done with a modern web framework and I chose to learn Vue.
I primarily used this project to improve my design skills, focusing on making a good-looking site with natural animations.
I also wanted to build my own backend, so I used Node.js and Express to create a REST API.

- View the source code at [github.com/ZachDaChampion/rankr](https://github.com/ZachDaChampion/rankr)
- Visit the site at [rankr.zachchampion.tech](https://rankr.zachchampion.tech)

![Image of the Rankr homepage](/res/rankr/sc-mainpage.png)
![Image of a search for "Star Wars"](/res/rankr/sc-search-sw.png)
![Image of a comparison of two episodes from Star Wars: Andor (2022)](/res/rankr/sc-compare.png)

## Hat Picker
A website for picking a random "card" out of a virtual hat.
I originally made this for some friends who wanted to pick a random movie to watch from a list that we had made.
The site allows you to create multiple hats, each with a different set of cards.
You can also configure the hat to select more than one card at a time to give you a small list of options.

This was my second web project. This time I used Svelte, a framework that compiles to vanilla JavaScript. I found it much easier to use than Vue. This project is entirely client-side, so I didn't need to worry about a backend; everything is stored in the browser's local storage.

I did extend this site for a class project, adding a backend with PHP and MySQL to enable live collaboration between users. However, this version is not currently hosted.

- View the source code at [github.com/ZachDaChampion/hat-picker](https://github.com/ZachDaChampion/hat-picker)
- Visit the site at [zachdachampion.github.io/hat-picker](https://zachdachampion.github.io/hat-picker/)
- 
![Image of the Hat Picker main page](/res/hatpicker/sc-mainpage.png)
![Image of the contents of the 'Movies' hat](/res/hatpicker/sc-moviehat.png)
![Image of two cards that were drawn from the 'Movies' hat](/res/hatpicker/sc-drawn.png)
</details>

---

<details>
<summary>Robotics</summary>
In high school I participated in Vex Robotics. This is where I first learned C and C++. Most of my time in high school was spent in robotics, so I have quite a few projects from that time.

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
</details>

---

<details>
<summary>Hardware</summary>
I've also made some hardware projects (apart from robotics).

## Quadrature Encoder
I designed and 3d-printed a simple quadrature encoder. It uses two photointerruptors to measure the rotation of a spinning disk. The disk has a series of slits around its perimeter that the photointerruptors can detect.

Due to 3d-printing limitations, I could not get very high precision. The disk has 15 slits, giving it 60 pulses per revolution. The encoder can therefore measure rotations to an accuracy of 1/60th of a revolution, or 6 degrees. I was unable to get the encoder to count accurately with higher precision because the slits were too small to be reliably detected.

That being said, the final encoder was perfectly accurate. It accumulated zero error even when spinning at high speeds.

This encoder was used in a school project in which dynamic band-stop filter was generated and applied to a live audio signal. The encoder controlled the frequency range of the filter.

![Image of the encoder in its casing](/res/encoder/casing.jpg)
![Image of the inside of the encoder](/res/encoder/inside.jpg)
![Image of the encoder's disk](/res/encoder/closeup.jpg)
![Screenshot of the filter editor](/res/encoder/sc-filter-ui.png)

## Roomba Experimentation Platform
I wanted to use a Roomba to learn ROS and experiment with antonomous mapping and navigation, so I designed and printed a platform that could be attached to the top of the Roomba. The platform has a Raspberry Pi, a lidar sensor, and a battery pack. 

![Image of the platform on a Roomba](/res/roomba/roomba.jpg)
</details>