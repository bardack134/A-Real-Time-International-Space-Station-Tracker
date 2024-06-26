# A-Real-Time-International-Space-Station-Tracker

This project is a real-time tracker for the International Space Station (ISS). It checks the current location of the ISS and compares it with the user’s location. If the ISS is overhead and it’s either before sunrise or after sunset (dark outside), the program sends an email alert to the user.

## Table of Contents
- Description
- Tools Used
- APIs Used
- Screenshots

## Description
The A-Real-Time-International-Space-Station-Tracker is a Python application that tracks the real-time location of the ISS. It compares the ISS's location with the user’s location. If the ISS is overhead and it’s dark outside (either before sunrise or after sunset), the program sends an email alert to the user.


## Tools Used
- **Requests:** A Python library used for making HTTP requests to the Open Notify and Sunrise-Sunset APIs.
- **smtplib:** A Python library used for sending emails using the Simple Mail Transfer Protocol (SMTP).
- **datetime:** A Python module used to determine the current date and time. It allows us to compare the current time with the sunrise and sunset times, helping us determine whether it’s dark outside.
- **time:** A Python module used for time-related tasks. In this project, it’s used to make the program wait for 60 seconds between each check of the ISS’s location.

## APIs Used
- **Open Notify API:** Used to fetch the real-time location of the ISS.
- **Sunrise-Sunset API:** Used to fetch the real-time sunrise and sunset times for the user’s location. This helps determine whether it’s dark outside.


## Screenshots

![app img](https://github.com/bardack134/A-Real-Time-International-Space-Station-Tracker/assets/142977989/70a01a4d-6e4b-4657-92a8-6d5019b9ea8e)

