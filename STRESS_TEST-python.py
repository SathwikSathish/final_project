import os
import subprocess
import logging


# Configure logging with various levels
logging.basicConfig(filename='stress_test.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Stress Testing Functions
def memory_stress():
    logging.info("Starting memory stress test")
    try:
        subprocess.run("stress-ng --vm 1 --vm-bytes 80% -t 30s", shell=True, check=True)
        logging.info("Memory stress test completed")
    except subprocess.CalledProcessError as e:
        logging.error(f"Memory stress test failed: {e}")

def disk_stress():
    logging.info("Starting disk stress test")
    try:
        subprocess.run("stress-ng --hdd 1 --hdd-bytes 80% -t 30s", shell=True, check=True)
        logging.info("Disk stress test completed")
    except subprocess.CalledProcessError as e:
        logging.error(f"Disk stress test failed: {e}")

def network_stress():
    logging.info("Starting network stress test")
    try:
        subprocess.run("iperf3 -s & iperf3 -c 192.168.31.192 -t 30", shell=True, check=True)
        logging.info("Network stress test completed")
    except subprocess.CalledProcessError as e:
        logging.error(f"Network stress test failed: {e}")

def cpu_stress():
    logging.info("Starting CPU stress test")
    try:
        subprocess.run("stress-ng --cpu 4 --cpu-load 80 -t 30s", shell=True, check=True)
        logging.info("CPU stress test completed")
    except subprocess.CalledProcessError as e:
        logging.error(f"CPU stress test failed: {e}")


def mysql_stress():
    logging.info("Starting MySQL stress test")
    try:
        # Use IP address of vm_2 and correct password
        subprocess.run(
            "sysbench --mysql-host=192.168.31.192 --mysql-user=root "
            "--mysql-password=PCSathwik@2703 --db-driver=mysql oltp_read_write "
            "--tables=10 --table-size=1000 --threads=4 --time=60 run",
            shell=True,
            check=True
        )
        logging.info("MySQL stress test completed")
    except subprocess.CalledProcessError as e:
        logging.error(f"MySQL stress test failed: {e}")

# Main menu
def main_menu():
    while True:
        print("\nStress Testing Menu:")
        print("1. Memory Stress Testing")
        print("2. Disk Stress Testing")
        print("3. Network Stress Testing")
        print("4. CPU Stress Testing")
        print("5. MySQL Stress Testing")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            memory_stress()
        elif choice == '2':
            disk_stress()
        elif choice == '3':
            network_stress()
        elif choice == '4':
            cpu_stress()
        elif choice == '5':
            mysql_stress()
        elif choice == '6':
            logging.info("Exiting stress test script")
            print("Exiting...")
            break
        else:
            logging.warning("Invalid choice selected")
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main_menu()
