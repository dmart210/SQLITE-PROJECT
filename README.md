
# Note
Project is still in development... 

# Database Interaction Program

## Overview

This Python program facilitates user interaction with an SQLite database. It allows users to insert data into any table by dynamically adapting to the table's schema. The program is designed to handle different data types and ensures the data is correctly formatted for SQL queries.

## Features

- **Dynamic Table Handling:** The program can interact with any specified table in the database.
- **Data Type Awareness:** Supports integer, text, decimal, and timestamp data types.
- **Automatic Date Handling:** Automatically inserts the current date and time for fields requiring a timestamp.

## Prerequisites

Before running this program, ensure that you have Python installed on your system. This program is compatible with Python 3.x.

## Installation

1. **Download the Script**: Download `main.py` to your local machine.
2. **Database Connection**: Ensure that `test.db` (SQLite database file) is in the same directory as the script, or modify the connection string in the script to point to the correct location.

## Usage

To use the program, follow these steps:

1. **Run the Program**: Open a terminal or command prompt, navigate to the directory containing `main.py`, and run the script using the command:
   ```
   python main.py
   ```
2. **Enter Table Name**: When prompted, enter the name of the table you wish to insert data into.
3. **Input Data**: Input data as prompted for each column of the table. The prompts will adapt based on the column's data type.
4. **Insert Data**: After all data is inputted, the program will automatically generate and execute an SQL `INSERT` statement.

## Error Handling

The program includes basic error handling for database connectivity issues and data type mismatches. If an error occurs, it will output "ERROR" to the console.

## Limitations

- The program assumes the database schema is pre-defined and does not support creating tables or modifying existing schemas.
- It does not provide detailed error messages which might be necessary for debugging database issues.

## Conclusion

This Python script is a straightforward tool for inserting data into an SQLite database. It is especially useful for testing and small-scale database interaction projects.
