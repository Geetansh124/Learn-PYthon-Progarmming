import os

def print_directory_contents(path='C:'):
   
    try:
        entries = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for entry in entries:
            print(entry)
    except Exception as e:
        print("Error:", e) 

if __name__ == "__main__":
    
    print_directory_contents()
    