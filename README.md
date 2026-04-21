# YouTube Tech Video Recommender

This project is a machine learning-powered web application that recommends YouTube videos on Computer Science topics based on predicted performance. 

## Overview
The application consists of three core components:
1. **Data Collection (`scrap.py`)**: Gathers metadata from YouTube across 50 predefined Computer Science topics without downloading the actual videos.
2. **Machine Learning Pipeline (`main.ipynb`)**: Analyzes the dataset and trains a classification model to predict video performance based on engagement metrics (likes, views, duration).
3. **Web Interface (`main.py`)**: A Flask-based website where users can search for a keyword. The app filters the dataset and uses the ML model to rank and display the best video recommendations with a custom "Performance Score."

## Project Structure
- `scrap.py`: YouTube data scraper.
- `main.ipynb`: Jupyter notebook for exploratory data analysis and model training.
- `main.py`: The Flask web server.
- `templates/`, `static/`: Frontend HTML and assets.
- `*.csv`: Datasets (raw, preprocessed, and final).
- `*.pkl`: Pre-trained ML models and label encoders.

## How to Run

### Setup Virtual Environment (Optional but recommended)
```bash
python -m venv venv_name
venv_name\Scripts\activate  # On Windows
```

### Install Dependencies
Ensure you have the required libraries installed:
```bash
pip install flask pandas scikit-learn yt-dlp jupyter
```

### Start the Web Application
```bash
python main.py
```
Open your browser and navigate to `http://127.0.0.1:5000/`.
