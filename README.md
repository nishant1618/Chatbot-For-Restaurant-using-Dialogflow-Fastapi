# Chatbot Project

This project is a chatbot application built using FastAPI for the backend, Dialogflow for natural language understanding, and HTML/CSS for the frontend. The application includes intents and entities JSON files for Dialogflow integration, which are stored in the backend folder.

## Project Overview

The chatbot application allows users to interact with a virtual assistant through a web interface. The backend handles user queries using FastAPI and integrates with Dialogflow to process natural language inputs. The frontend presents a user-friendly interface for interaction.

## Project Structure

- **backend/**: Contains the backend files including FastAPI scripts and Dialogflow intents/entities JSON files.
- **frontend/**: Contains the HTML and CSS files for the frontend interface.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **README.md**: This README file.
- **requirements.txt**: Lists the Python dependencies required for the project.

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- FastAPI
- Dialogflow
- Node.js (optional, for additional tooling)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/chatbot-project.git
   cd chatbot-project
2.  Set up a virtual environment and activate it:
3.  ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
5. Update the .env file.Use the envExample file and add the required details and save it as .env.

6. Set up Dialogflow:
- Go to the Dialogflow console and create a new agent.  
- Import the intents.json and entities.json files into your Dialogflow agent.
7. Run the FastAPI server:
     ```sh
    uvicorn backend.main:app --reload
8. Expose your FastAPI server using Ngrok:
- Download and install Ngrok from ngrok.com and move the application to the backend folder.
- Run Ngrok to create an HTTPS tunnel to your local FastAPI server
    ```sh
     ngrok http 8000
- Ngrok will provide you with a public HTTPS URL. Use this URL to set up    webhooks and test your chatbot.
    
9. Open the index.html file in your browser to view the frontend.

# Database Dump

This repository contains a MySQL database dump.

## Import Instructions

To import this database, use the following command:

    ```sh
    mysql -u [username] -p [database_name] < database_dump.sql

### Usage
- Start the FastAPI server using the command above.
- Run Ngrok to get an HTTPS URL for your local server.
- Open the index.html file in a web browser to access the chatbot interface.
- Interact with the chatbot by typing messages into the chat input.
  
## Contributing
Contributions are welcome! Please fork this repository and submit pull requests for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For any questions or issues, please open an issue on GitHub or contact [nishantbehera2002@gmail.com].

