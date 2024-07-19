import serial
import csv
import os

# Replace '/dev/tty.usbmodemXXXX' with your actual serial port
ser = serial.Serial('/dev/tty.usbmodem21301', 9600)

# Define the path where the CSV file will be saved
csv_dir = '/Users/archismanbasu/Documents/heattt'
csv_path = os.path.join(csv_dir, 'matrix_data.csv')

# Create the directory if it doesn't exist
os.makedirs(csv_dir, exist_ok=True)

# Print the path to confirm where the CSV file will be saved
print("CSV file will be saved in:", csv_path)

# Open a CSV file to write the data
with open(csv_path, mode='a', newline='') as file:
    writer = csv.writer(file)
    
    while True:
        try:
            if ser.in_waiting > 0:
                # Read a line of data from the serial port
                line = ser.readline()
                try:
                    # Attempt to decode the line using UTF-8
                    decoded_line = line.decode('utf-8').strip()
                    if "End of Loop" not in decoded_line:
                        # Split the decoded line into individual values
                        data = decoded_line.split(',')
                        # Write the data to the CSV file
                        writer.writerow(data)
                        print(data)  # Print the data to the console (optional)
                    else:
                        print("End of Loop")
                except UnicodeDecodeError:
                    print("UnicodeDecodeError: Skipping line due to decoding issue")
        except KeyboardInterrupt:
            print("Data logging stopped")
            break
        except serial.SerialException as se:
            print(f"Serial error: {se}")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

ser.close()
