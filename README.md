# Project Overview

## Description

This project is a fork of the project from the tutorial [Job Search 2.0 Turbo](https://medium.com/towards-data-science/job-search-2-0-turbo-579e1bdb5177)

A list of additions, improvements and modifications is provided below.

## Project Structure Overview

![Project Overview](./files/overview.png)

## Key Components

- **`configs/`**: Contains configurations for agents that dynamically adjust their behavior based on project needs.
- **`data/`**: Houses essential data files like sample jobs and resumes for testing and demonstration purposes.
- **`models/`**: Includes sophisticated data models that support robust data interaction and manipulation.
- **`utils/`**: Provides utility functions that enhance functionality and simplify repetitive operations across the project.
- **`agents_factory.py` and `tasks_factory.py`**: These scripts implement factory patterns to efficiently create instances as per the configuration specified.
- **`main.py`**: The main script that serves as the entry point, bringing together various components and driving the application.

## TODO
- [x] use "openai/gpt-4o-mini" instead of Azure hosted solution

## Installation

To set up this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone git@github.com:mrPronin/job-search-2.0.git
   ```

2. Go to project folder
   ```bash
   cd job-search-2.0
   ```

3. Create virtual environment
   ```bash
   python -m venv venv
   ```

4. Activate virtual environment
   ```bash
   source venv/bin/activate
   ```

5. Upgrade pip
   ```bash
   pip install --upgrade pip
   ```

6. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

7. Upgrade setuptools and packages
   ```bash
   pip install --upgrade setuptools
   pip install --upgrade crewai crewai-tools clarifai
   ```

8. Set up the environment variables within the .env file (copy .env.example):
   ```bash
   SERPER_API_KEY=<ENTER KEY HERE>
   OPENAI_API_KEY=<ENTER KEY HERE>
   ```

9. Run the application
   ```bash
    python main.py
    ```
