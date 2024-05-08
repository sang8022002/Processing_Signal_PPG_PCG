ppg_data = []
pcg_data = []
fs1 = 250
fs2 = 4000
import matplotlib.pyplot as plt
import scipy.signal as signal
# from scipy.signal import find_peaks
#file_name = "pvs_manh_nhe.txt"
# file_name = "pcg_ppg.txt"
file_name1 = "data_9_5_2024/107 57 90 long/PPG.TXT"
file_name2 = "data_9_5_2024/107 57 90 long/PCG.TXT"

import csv
import pandas as pd
windowsize = int(fs1/8)
# with open(file_name1, mode='r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     # Duyệt qua từng dòng trong tệp CSV
#     for row in csv_reader:
#         if len(row) >= 2:  # Đảm bảo có ít nhất 2 cột trong mỗi dòng
#             column_0_data = float(row[0])
#             pcg_data.append(column_0_data)
with open(file_name2, 'r') as file:
    # Đọc từng dòng trong tệp
    for line in file:
        # Loại bỏ khoảng trắng ở đầu và cuối dòng
        stripped_line = line.strip()
        # Kiểm tra xem dòng có rỗng không
        if stripped_line:
            # Thử chuyển đổi dòng thành số nguyên
            try:
                number = int(stripped_line)
                pcg_data.append(number)
            except ValueError:
                print(f"Ignoring invalid literal: {stripped_line}")
# Mở tệp văn bản
# with open(file_name1, 'r') as file:
#     # Đọc tất cả các dòng trong tệp và chuyển đổi thành một danh sách các số nguyên
#     pcg_data.append([int(line.strip()) for line in file])

with open(file_name1, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Duyệt qua từng dòng trong tệp CSV
    for row in csv_reader:
        if len(row) >= 2:  # Đảm bảo có ít nhất 2 cột trong mỗi dòng
            column_0_data = float(row[1])
            ppg_data.append(column_0_data)  

indices_ppg = [i for i in range(0, len(ppg_data) * 16, 16)]
# pcg_data = pcg_data[2300:]
indices_pcg = [i for i in range(len(pcg_data))]
fig, axs = plt.subplots(2, 1, sharex = True)
axs[0].plot(indices_ppg, ppg_data)
# for value in ampl_ppg_data_filtered:
#     axs[0].plot(value, median_data[value], "r*")
axs[0].set_xlabel("Indice")
axs[0].set_ylabel("Value adc from LED")
axs[0].set_title("Data from red LED")

axs[1].plot(indices_pcg, pcg_data)
# for value in ampl_pcg_data_filtered:
#     axs[1].plot(value, pcg_filtered[value], "r*")
axs[1].set_xlabel("Indice")
axs[1].set_ylabel("Value adc from speaker")
axs[1].set_title("Data from speaker")
# plt.show()

ppg_data_filtered = pd.Series(ppg_data).rolling(window=windowsize, center=True).median()

# Define the filter parameters
lowcut = 25
highcut = 120
nyquist = 0.5 * fs2
low = lowcut / nyquist
high = highcut / nyquist

# Apply the bandpass filter to pcg_data
b, a = signal.butter(4, [low, high], btype='band')
pcg_data_filtered = signal.lfilter(b, a, pcg_data)

peaks_ppg, _ = signal.find_peaks(ppg_data_filtered, height=0, distance = 0.34*fs1)
peaks_pcg, _ = signal.find_peaks(pcg_data_filtered, height=0, prominence= 500, distance = 0.1*fs2)

# peaks_ppg = [peak * 16 for peak in peaks_ppg]
print(peaks_ppg)

fig, axs = plt.subplots(2, 1, sharex=True)
axs[0].plot(indices_ppg, ppg_data_filtered)

for value in peaks_ppg:
    axs[0].plot(indices_ppg[value], ppg_data_filtered[value], "r*")
axs[0].set_xlabel("Indice")
axs[0].set_ylabel("Value adc from LED (Filtered)")
axs[0].set_title("Data from red LED (Filtered)")

# Plot the filtered pcg_data
axs[1].plot(indices_pcg, pcg_data_filtered)
for value in peaks_pcg:
    axs[1].plot(value, pcg_data_filtered[value], "r*")
axs[1].set_xlabel("Indice")
axs[1].set_ylabel("Value adc from speaker (Filtered)")
axs[1].set_title("Data from speaker (Filtered)")

plt.show()