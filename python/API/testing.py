import speedtest

def run_speed_test():
    print("Initializing speed test... Please wait...")
    
    # Create an instance of the Speedtest client
    st = speedtest.Speedtest()
    
    # Find the best server based on ping/location
    print("Finding the optimal server...")
    st.get_best_server()
    
    # Test download speed
    print("Testing download speed...")
    download_speed = st.download() / 1_000_000  # Convert bps to Mbps
    
    # Test upload speed
    print("Testing upload speed...")
    upload_speed = st.upload() / 1_000_000      # Convert bps to Mbps
    
    # Retrieve ping latency
    ping_result = st.results.ping
    
    # Print the final results
    print("\n--- RESULTS ---")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed:   {upload_speed:.2f} Mbps")
    print(f"Ping:           {ping_result:.2f} ms")

if __name__ == "__main__":
    run_speed_test()
