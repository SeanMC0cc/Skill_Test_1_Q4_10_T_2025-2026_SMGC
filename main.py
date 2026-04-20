from pyscript import document
import numpy as np
import matplotlib.pyplot as plt

def Calculate(x):
    document.getElementById("output").innerHTML = ' '
    abs_value = document.getElementById('Absent').value
    day_value = document.getElementById('Months').value
    if not abs_value:
        document.getElementById("output").innerHTML = '<p style="color:red;">Please enter a number.</p>'
        return
    
    missing = np.array([int(abs_value)])
    days = np.array([str(day_value)])

    plt.plot(days, missing, marker='o')
    plt.show()
    plt.title("Topaz Absents")
    plt.xlabel("Days of the Week")
    plt.ylabel("Sales")