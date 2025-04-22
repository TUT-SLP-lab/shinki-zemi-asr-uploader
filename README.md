# Audio Uploader

A simple Python script to upload a `.wav` audio file along with presenter information to a server using an HTTP POST request.

## 📄 Main Files

- `main.py`: the main script that performs the upload
- `.env`: contains the `SERVER_URL` environment variable (e.g., `http://abcd`)
- `sample.wav`: a sample audio file (must exist in the same folder)

## ▶️ How to Use

1. Create a `.env` file with the following content:
SERVER_URL=Insert-sever-link-here
2. Run the script:

```bash
python main.py
```

3.	Enter the following values in the terminal when prompted:
- presenter_name
- date (format: YYYYMMDD)
-	start_time (format: hhmm)
-	end_time (format: hhmm)

The script will:
-	Copy sample.wav to a new file named presentername_date_start_end.wav
  -	Upload the file to the server specified in the .env file

📌 Notes
	-	Ensure the server is running and accessible at the SERVER_URL
