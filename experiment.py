from flask import Flask, request, jsonify, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    """
    This function initializes the database by creating a connection to the
    'database.db' file and creating a table named 'tasks' if it does not
    already exist.
    """
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS tasks (task_TEXT)')
    conn.commit()
    conn.close()

# Comment describing the function to reverse the string
def reverse_string(string):
    """
    This function takes a string as input and returns the reversed string.
    """
    return string[::-1]

# Example 2: Variable Naming
# Comment describing data to be stored
# List of user's favorite books
favorite_books = []

# Implement bubble sort algorithm
# 1. Iterate through the list n-1 times
# 2. For each iteration:
#    a. Compare adjacent elements
#    b. Swap elements if they are in the wrong order
# 3. The largest unsorted element "bubbles up" to its correct position
def bubble_sort(arr):
    """
    This function implements the bubble sort algorithm to sort a list of
    elements in ascending order.
    """
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage of the bubble_sort function
if __name__ == '__main__':
    init_db()
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted list:", sample_list)
    bubble_sort(sample_list)
    print("Sorted list:", sample_list)
    app.run(debug=True)

