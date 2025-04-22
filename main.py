import requests
import os
from datetime import datetime
from pathlib import Path
import shutil
from dotenv import load_dotenv

def upload_recording(
        server_url: str,
        presenter_name: str,
        date: str,
        start_time: str,
        end_time: str,
        audio_file_path: str,
        ):
    files = {
        "audio_file": (os.path.basename(audio_file_path), open(audio_file_path, "rb"), "audio/wav")
    }

    data = {
        "presenter_name": presenter_name,
        "date": date,
        "start_time": start_time,
        "end_time": end_time,
    }

    try:
        response = requests.post(
            server_url,
            files=files,
            data=data
        )

        if response.status_code == 200:
            print(f"Upload successful: {response.json()}")
            return response.json()
        else:
            print(f"Upload failed: {response.status_code}, {response.text}")
            return {"error": response.text}
    except Exception as e:
        print(f"Error upload recording: {str(e)}")
        return {"error": str(e)}
    finally:
        files["audio_file"][1].close()

if __name__ == "__main__":
    load_dotenv()
    SERVER_URL = os.getenv("SERVER_URL")

    presenter_name = input("presenter_name: ")
    date = input("date (YYYYMMDD): ")
    start_time = input("start_time (hhmm): ")
    end_time = input("end_time (hhmm): ")

    INPUT_FILE_PATH = "./sample.wav"
    output_filename = f"{presenter_name}_{date}_{start_time}_{end_time}.wav"
    AUDIO_FILE_PATH = Path(__file__).resolve().parent / output_filename

    shutil.copy(INPUT_FILE_PATH, AUDIO_FILE_PATH)

    print(f"File uploading: {AUDIO_FILE_PATH}")

    result = upload_recording(SERVER_URL, presenter_name, date, start_time, end_time, str(AUDIO_FILE_PATH))