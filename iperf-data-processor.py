import pandas as pd
import matplotlib.pyplot as plt
import os

def process_iperf_data(csv_path):
    try:
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Validate DataFrame
        if 'Zeit' not in df.columns or 'Mbits' not in df.columns:
            raise ValueError("CSV file lacks required 'Zeit' and 'Mbits' columns")
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.plot(df['Zeit'], df['Mbits'], marker='o')
        plt.title("Network Throughput Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Throughput (Mbits/s)")
        plt.grid(True)
        
        # Save the plot
        plot_path = 'network_throughput.png'
        plt.savefig(plot_path)
        plt.close()
        
        # Calculate statistics
        stats = {
            'Average Throughput': df['Mbits'].mean(),
            'Maximum Throughput': df['Mbits'].max(),
            'Minimum Throughput': df['Mbits'].min()
        }
        
        return stats, plot_path
    
    except Exception as e:
        print(f"Error processing iPerf3 data: {e}")
        return None, None

def main():
    # Default path where Jenkins typically stores artifacts
    csv_path = 'iperf_data.csv'
    
    if not os.path.exists(csv_path):
        print(f"Error: CSV file {csv_path} not found")
        return
    
    stats, plot_path = process_iperf_data(csv_path)
    
    if stats:
        print("\nNetwork Performance Statistics:")
        for key, value in stats.items():
            print(f"{key}: {value:.2f} Mbits/s")
        
        print(f"\nPlot saved to: {plot_path}")

if __name__ == "__main__":
    main()
