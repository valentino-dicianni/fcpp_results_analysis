import pandas as pd
import os
import matplotlib.pyplot as plt

DATA_PATH = "data/6drones-s"

def read_and_process_logs(directory_path):
    all_data = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"): 
            file_path = os.path.join(directory_path, filename)
            df = pd.read_csv(file_path, header=None, names=["Timestamp", "Value"])
            df["Timestamp"] = pd.to_datetime(df["Timestamp"])
            all_data.append(df)

    combined_data = pd.concat(all_data)
    result = combined_data.groupby("Timestamp").mean().reset_index()

    return result

def plot_data(data):
    plt.figure(figsize=(10, 5))  
    plt.plot(
        data["Timestamp"], data["Value"], marker="o", linestyle="-"
    )  
    plt.title("Errore Medio Formazione Droni")  
    plt.xlabel("Timestamp")  
    plt.ylabel("Errore Medio")  
    plt.grid(True) 
    plt.xticks(
        rotation=45
    )  
    plt.tight_layout()  
    plt.show() 


avg_error = read_and_process_logs(DATA_PATH)
plot_data(avg_error)
