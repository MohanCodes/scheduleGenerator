# scheduleGenerator
a tkinter application that generates an example xlsx
i'll turn it in to a website maybe

![Screenshot 2024-08-13 155706.png](https://github.com/MohanCodes/scheduleGenerator/blob/8a9d1f0d860e12fb5115cc27dac2bb2b9654d21e/Screenshot%202024-08-13%20155706.png)

This project is a Python-based GUI application built with Tkinter that allows users to generate a random schedule based on specified day configurations, time probabilities, and comments. The generated schedule can be saved as an Excel file.

## Features

- **Date Selection**: Choose the start and end dates for the schedule.
- **Day Configuration**: Add multiple day configurations, including:
  - Day of the week.
  - Probability of the day being selected.
  - Time range and probability for generating random times.
  - Comments with the option to randomize them.
- **Flexible Day and Time Selection**: The application uses a weighted random approach to select days and times based on user-defined probabilities.
- **Save Schedule**: The generated schedule can be saved as an Excel file.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `tkinter`
  - `tkcalendar`
  - `pandas`

## Installation

1. Clone the repository or download the source code.
   
2. Install the required packages using pip:

    ```sh
    pip install tkcalendar pandas
    ```

3. Run the application:

    ```sh
    python schedule_generator.py
    ```

## How to Use

1. **Start and End Date**: Select the start and end dates for the schedule using the date pickers.

2. **Add Day Configuration**: Click the "Add Day Configuration" button to add a new day configuration. You can add as many configurations as needed.

   - **Day**: Select the day of the week.
   - **Day Probability**: Enter the probability (in percentage) that the selected day will be chosen for the schedule.
   - **Time Probability**: Enter the probability (in percentage) that the generated times will be within the specified time range.
   - **Start and End Times**: Specify the start and end times for the schedule on that day.
   - **Comments**: Add comments by clicking the "Comments" button. You can also choose to randomize the comments.

3. **Delete Day Configuration**: Use the "Delete" button next to each day configuration to remove it.

4. **Generate Schedule**: Once all configurations are set, click the "Generate Schedule" button. You will be prompted to enter a filename for the Excel file. The schedule will be saved with this filename.

5. **Save and View Schedule**: After saving, you can view the generated schedule in the Excel file.

## Example

An example use case would be generating a weekly schedule for a month where different days have different probabilities and time ranges for planned activities. The schedule can include random comments like "Meeting with Team A" or "Project Review," with options to randomize when these comments appear.

## License

This project is licensed under the MIT License.

## Acknowledgments

- This application was built using the Tkinter library for the GUI and Pandas for data handling.
- Special thanks to the developers of `tkcalendar` for providing an easy-to-use date picker widget.

## Author

- Mohan Atkuri