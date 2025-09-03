# Meeting-Manager 📅

Ideal for streamlining post-meeting tasks, Meeting Manager 📅 is designed to enhance meeting productivity. It automates the summarization of meeting transcripts, provides a Q/A feature for quick information retrieval, and identifies upcoming meetings to notify participants via email.

## Table of Contents 📚
- Features
- Installation
- Usage
- Contributing
- License

## Features 👨🏻‍💻

- **Summarizes Meeting Transcripts:** Provides concise summaries of meeting discussions.
- **Future Meetings Identification:** Detects future meetings within the transcript and sends email notifications to the relevant participants.
- **Q/A Section:** Allows users to query specific questions and get relevant answers from the meeting transcript.

## Installation 📲

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies.
4. Obtain a Developer API key from https://aistudio.google.com/app/u/1/apikey.
5. Obtain a Courier API Production key from https://app.courier.com/settings/api-keys.
6. Start the application.

## Usage 🛒

1. **Prepare Your Files:**
   - Ensure you have a `.txt` file with the meeting transcript.
   - Create a `.csv` file containing employee records with columns for Name, Email, and Role.

2. **Place Files in Directory:**
   - Move both the transcript and employee records files into the project directory.
   - Create a folder titled `data` within the project directory and copy the transcript file into this folder.

3. **Open the Jupyter Notebook:**
   - Launch Jupyter Notebook in your terminal:
     ```bash
     jupyter notebook
     ```
   - Open `Meeting Manager.ipynb` from the notebook interface.

4. **Run the Notebook:**
   - Follow the instructions within the notebook cells.

## Contributing 💡

Contributions are welcome! If you have any ideas for improvements, bug fixes, or new features, please open an issue or submit a pull request.

## License ⚖️

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.
