from bridges.bridges import *
from bridges.line_chart import *

def task1(bridges):
    plot = LineChart()
    plot.title = "Task 1"
    plot.x_label = "Amount of Data"
    plot.y_label = "Runtime"

    # Data size ranging from 1 to 10^5
    data_x1 = [(10 ** 3), (2 * 10 ** 3), (3 * 10 ** 3), (4 * 10 ** 3), (5 * 10 ** 3), (6 * 10 ** 3), (7 * 10 ** 3),
               (8 * 10 ** 3), (9 * 10 ** 3),
               (10 ** 4), (2 * 10 ** 4), (3 * 10 ** 4), (4 * 10 ** 4), (5 * 10 ** 4), (6 * 10 ** 4), (7 * 10 ** 4),
               (8 * 10 ** 4), (9 * 10 ** 4), (10 ** 5)]
    data_y11 = []
    data_y12 = []
    data_y13 = []
    for n in range(len(data_x1)):
        data_y11.append(data_x1[n] * (10 ** 4) * (1 / (10 ** 6)))  # 10^4 n on a machine at 1 MHz
        data_y12.append(data_x1[n] * (5 * (10 ** 4)) * (1 / (10 ** 6)))  # 5.10^4 n on a machine at 1MHz
        data_y13.append((data_x1[n] ** 2) * (10 ** 2) * (1 / (100 * (10 ** 6))))  # 10^2 n^2 on a machine at 100MHz

    plot.set_data_series("10^4 n at 1MHz", data_x1, data_y11)
    plot.set_data_series("5*10^4 n at 1MHz", data_x1, data_y12)
    plot.set_data_series("10^2 n^2 at 100MHz", data_x1, data_y13)
    bridges.set_data_structure(plot)

    plot.mouse_track = True
    bridges.visualize()

def task2(bridges):
    plot = LineChart()
    plot.title = "Task 2"
    plot.x_label = "Amount of Data"
    plot.y_label = "Runtime"

    # Data size ranging from 1 to 10^4
    data_x2 = [(10 ** 2), (2 * 10 ** 2), (3 * 10 ** 2), (4 * 10 ** 2), (5 * 10 ** 2), (6 * 10 ** 2), (7 * 10 ** 2),
               (8 * 10 ** 2), (9 * 10 ** 2),
               (10 ** 3), (2 * 10 ** 3), (3 * 10 ** 3), (4 * 10 ** 3), (5 * 10 ** 3), (6 * 10 ** 3), (7 * 10 ** 3),
               (8 * 10 ** 3), (9 * 10 ** 3), (10 ** 4)]
    data_y21 = []
    data_y22 = []
    data_y23 = []
    for n in range(len(data_x2)):
        data_y21.append(data_x2[n] * (10 ** 4) * (1 / (10 ** 6)))  # 10^4 n on a machine at 1 MHz
        data_y22.append((data_x2[n] ** 2) * (10 ** 2) * (1 / (100 * (10 ** 6))))  # 10^2 n^2 on a machine at 100MHz
        data_y23.append((data_x2[n] ** 4) * (1 / (10 * (10 ** 9))))  # n^4 on a machine at 10GHz

    plot.set_data_series("10^4 n at 1MHz", data_x2, data_y21)
    plot.set_data_series("10^2 n^2 at 100MHz", data_x2, data_y22)
    plot.set_data_series("n^4 at 10GHz", data_x2, data_y23)
    bridges.set_data_structure(plot)

    plot.mouse_track = True
    bridges.visualize()

def task3(bridges):
    plot = LineChart()
    plot.title = "Task 3"
    plot.x_label = "Amount of Data"
    plot.y_label = "Runtime"

    # Data size ranging from 1 to 10^2
    data_x3 = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    data_y31 = []
    data_y32 = []
    data_y33 = []
    data_y34 = []
    for n in range(len(data_x3)):
        data_y31.append(data_x3[n] * (10 ** 4) * (1 / (10 ** 6)))  # 10^4 n on a machine at 1 MHz
        data_y32.append((data_x3[n] ** 2) * (10 ** 2) * (1 / (100 * (10 ** 6))))  # 10^2 n^2 on a machine at 100MHz
        data_y33.append((data_x3[n] ** 4) * (1 / (10 * (10 ** 9))))  # n^4 on a machine at 10GHz
        data_y34.append(2 ** (data_x3[n]) * (1 / (10 ** 15)))   # 2^n on a machine at 1PHz

    plot.set_data_series("10^4 n at 1MHz", data_x3, data_y31)
    plot.set_data_series("10^2 n^2 at 100MHz", data_x3, data_y32)
    plot.set_data_series("n^4 at 10GHz", data_x3, data_y33)
    plot.set_data_series("2^n at 1PHz", data_x3, data_y34)
    bridges.set_data_structure(plot)

    plot.mouse_track = True
    bridges.visualize()

def main():

    # create the Bridges object and set credentials
    bridges = Bridges(1, "YOUR_USER_ID", "YOUR_API_KEY")

    # title and description
    bridges.set_title("Complexity Matters")
    bridges.set_description("This project aims to observe whether using a slightly faster machine would help"
                            "processing high complexity of data and to understand why we use Big-Oh notations to judge"
                            " the efficiency of algorithms.")
    task1(bridges)
    task2(bridges)
    task3(bridges)


if __name__ == "__main__":
    main()
