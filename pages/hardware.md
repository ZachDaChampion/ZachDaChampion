# Hardware

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