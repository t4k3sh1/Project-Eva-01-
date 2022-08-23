# Project Eva 01

This repository will hold all files relative to the construction, AI and microcontroller programming necessary to build a scaled down model of Evangelion unit 01.

Files will be split up into 3 branches: main, custom eva and stock figure; #main will contain all the code, mostly built in python, qt and arduino-cpp; custom eva will hold all the 3d models and design assets we used to build the actual figure, and, once we'll be happy with how the casing turned out, it'll also have a zip file containing STLs and printing instructions. Stock figure is a mirror for the stock 3d files we obtained on [thingiverse](https://www.thingiverse.com/thing:1805621)

## Requirements
Since this project is being built with cross-platform interfaces and interoperability in mind, we are 100% going to port the code to windows, or atleast make an installer with all the required dependencies, but for now, we have shifted most of our focus to linux based OSs for a variety of reasons, please keep it in mind if you want to build/collaborate
- Python >= 3.8
- PyQt5 (Qmake, working on linux systems only for now)
- PySerial
- Python.sys
- OpenCV3*
- Numpy*
- Logging*

## Tests
Since aug. 9th, our development team started posing some of the groundwork necessary for the bulk of the software we'll need, the AI system for navigation, walking, interfacing and other features that we don't want to spoil yet. All of the tests we are currently working on will be uploaded in the /tests/ folder so you'll be able to see for yourself how we are actively working on the project. Eventually we will delete the test folder and integrate everything into main.py, but for now, have fun exploring the little demos our team has worked on :D

Additional requirements for tests will be written in the requirements section, but they'll be marked with an asterisk

## Python-esp interfacing

We thought about building the eva on a drunken night while in vacation so we really had no clue on what to build, once we returned back to our city we decided it was a good idea to use python as a host for all the heavy processing, and an esp-8266 as the client, alongside two arduino nanos to control the body. At the time of writing we already put down a somewhat decent base for this communication protocol, and we are currently working on a bluetooth fallback method in case pyserial over wifi fails.

## Building instructions

Sadly, as we are still actively working on the [design](https://media.discordapp.net/attachments/704041576195686421/1004119796620734584/unknown.png), we have no idea how much longer it'll take us until some acceptable building instructions will be published; make sure to watch this repository to stay posted on the latest updates from the team

## Contributing

Feel free to contribute to both the code and the 3d design :) to do so, fork our repository, work with your changes and create a merge request, in it, write a small description of all the changes you've made
