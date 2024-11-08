import math
import csv

g = 9.8 

def statistics(filename):
    statistics_dict = {}
    with open(filename, mode = 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['NAME']
            leg_length = float(row['LEG_LENGTH'])
            statistics_dict[name] = {
                'leg_length':leg_length
                }
    return statistics_dict

def additional_data(filename):
    additional_data_dict = {}
    with open(filename, mode = 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['NAME']
            stride_length = float(row['STRIDE_LENGTH'])
            stance = row['STANCE']
            additional_data_dict[name] = {
                'stride_length': stride_length,
                'stance': stance
                }
        return additional_data_dict
    
def calculate_fun(statistics_dict, additional_data_dict):
    speed_total = []
    for key, value in additional_data_dict.items():
        if value['stance'].lower() == 'bipedal' and key in statistics_dict:
            leg_length = statistics_dict[key]['leg_length']
            stride_length = value['stride_length']
            speed = ((stride_length  / leg_length) - 1) * math.sqrt(leg_length * g)
            speed_total.append((key,speed))
    return speed_total

def sort1(speed_total):
    speed_total.sort(key = lambda x:x[1], reverse = True)
    print("bipedal dinosaurs from fastest to slowest")
    for name, speed in speed_total:
        print(f"{name}: {speed:.2f} m/s")
    print("top3")
    for name, _ in speed_total[:3]:
        print(name)

if __name__ == '__main__':
    file1 = '/Users/prernagarsole/Desktop/CSVnew1.csv'
    file2 = '/Users/prernagarsole/Desktop/csvnew2.csv'
    file_store1 = statistics(file1)
    file_store2 = additional_data(file2)
    speed = calculate_fun(file_store1, file_store2)
    sort1(speed)

