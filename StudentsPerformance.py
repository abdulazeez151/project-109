import pandas as pd
import statistics
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv") 

reading_list = df["reading score"].to_list()

mean = statistics.mean(reading_list)
median = statistics.median(reading_list)
mode = statistics.mode(reading_list)
std_deviation = statistics.stdev(reading_list)

print("Mean of the data is ", mean)
print("Median of the data is " , median)
print("Mode of the data is ", mode)
print("Standard Deviation of the data is ", std_deviation)

first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2*std_deviation), mean + (2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3*std_deviation), mean + (3*std_deviation)

list_of_data_within_1_standard_deviation = [result for result in reading_list if result > first_std_deviation_start and result < first_std_deviation_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_standard_deviation)*100.0/len(reading_list)))

list_of_data_within_2_standard_deviation = [result for result in reading_list if result > second_std_deviation_start and result < second_std_deviation_end]
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_standard_deviation)*100.0/len(reading_list)))

list_of_data_within_3_standard_deviation = [result for result in reading_list if result > third_std_deviation_start and result < third_std_deviation_end]
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_standard_deviation)*100.0/len(reading_list)))

fig = ff.create_distplot([reading_list],["Result"],show_hist = False)
fig.show()