# Project Overview

**DISCALIMER** This example uses cookies to authenticate to LinkedIn, and it's meant only as an example or the selenium tool, using this for real-world applications may violate LinkedIn's terms of service and could lead to your account being banned. We do not endorse or encourage the use of this tool for any real-world applications.

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
- **`tools/`**: Contains tool classes used by the agents.
- **`agents_factory.py` and `tasks_factory.py`**: These scripts implement factory patterns to efficiently create instances as per the configuration specified.
- **`main.py`**: The main script that serves as the entry point, bringing together various components and driving the application.

## TODO
- [x] feat: use "openai/gpt-4o-mini" instead of Azure hosted solution
- [x] doc: update installation section, fix existign issues, use virtual environment
- [x] fix: adjust evaluate_company task description
- [x] build: use poetry for dependency management
- [x] refactor: update project structure with src in root
- [ ] feat: update job_search_expert to use a real source of positions (Ln)
   - [x] feat: define Driver to wrap selenium
   - [x] feat: automatically fetch Linkedin auth cookie
   - [ ] feat: define LinkedInClient to find positions
   - [ ] feat: define LinkedInTool to retreive positions
- [ ] refactor: use CrewAI decorators (@CrewBase, @agent and @task), create entities from conig/*.yml
- [ ] feat: try to use local llama3.2 for some tasks

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

## Steps to get Linkedin Cookie (LI_AT)
- Navigate to www.linkedin.com and log in
- Open browser developer tools (Ctrl-Shift-I or right click -> inspect element)
- Select the appropriate tab for your browser (Application on Chrome, Storage on Firefox)
- Click the Cookies dropdown on the left-hand menu, and select the www.linkedin.com option
- Find and copy the li_at value and add it to your .env file
- Be sure to fetch the cookies again if selenium doesnt login to linkedin after a while
