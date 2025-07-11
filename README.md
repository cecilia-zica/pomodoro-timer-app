# Pomodoro Timer

This is a simple Pomodoro timer application created as part of my Day 28 project for the #100DaysOfCode challenge. The app provides a graphical user interface to help manage work and break intervals based on the Pomodoro Technique.

![pomodoro_img.png](pomodoro_img.png)

The Pomodoro Technique is a time management method that uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks.

This application follows a classic Pomodoro workflow:

1.  **Work:** A 25-minute focused work session.
2.  **Short Break:** A 5-minute break after one work session.
3.  **Long Break:** A 20-minute break after four consecutive work sessions.

The timer will automatically cycle through these sessions. A checkmark is added at the bottom for each completed Pomodoro session to track your progress.

## What I Learned

Building this project helped me to understand and practice several important concepts:

* **GUI with Tkinter:** I learned the basics of creating a graphical user interface using Python's built-in Tkinter library. This included creating widgets like windows, labels, buttons, and canvases.
* **Event-Driven Programming:** I gained experience with event-driven programming, where the flow of the program is determined by events such as button clicks. The `after()` method in Tkinter was key to implementing the countdown timer without freezing the application.
* **Structuring Application Layout:** I practiced how to position and arrange GUI elements on the screen using Tkinter's grid layout manager to create a clean and user-friendly interface.
* **Implementing Logic:** I wrote the logic to handle the countdown mechanism, reset the timer, and automatically switch between work and break sessions.

## How to Run

To run this project locally, follow these steps:

1.  Clone the repository:
    ```sh
    git clone [https://github.com/your-username/pomodoro-timer-app.git](https://github.com/your-username/pomodoro-timer-app.git)
    ```
2.  Navigate to the project directory:
    ```sh
    cd pomodoro-timer-app
    ```
3.  Run the application:
    ```sh
    python main.py
    ```
