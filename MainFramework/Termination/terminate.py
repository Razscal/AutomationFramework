import psutil
import os
class Terminate:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def program() -> None:
        """
            Close all application and end the process
            Return: None
        """
        # Get the list of all running processes
        try:
            print("Terminate...")
            all_processes = psutil.process_iter()

            # Iterate through each process and terminate it
            for process in all_processes:
                try:
                    process.terminate()
                except Exception as e:
                    print(f"Error occurred while terminating process: {e}")
                    pass
        except Exception as e:
            raise Exception(f"{os.path.basename(__name__)}-{e}")
