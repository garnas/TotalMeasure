import subprocess


class LogReader:

    @staticmethod
    def journalctl() -> str:
        """Filters and retrieves logs from journalctl for the Gunicorn process."""
        # Replace 'your_gunicorn_process_name' with the actual process name
        try:
            # Run the journalctl command and capture the output
            result = subprocess.run(["journalctl"], capture_output=True, check=True)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            # Handle potential errors from the subprocess call
            return f"An error occurred: {e}"
