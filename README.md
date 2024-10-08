# Student Performance Predictor

This project is a web application that predicts student math scores based on various demographic and academic factors. It uses machine learning models to make predictions and provides a user-friendly interface for input and result display.

## Features

- Predicts math scores based on:
  - Gender
  - Race/Ethnicity
  - Parental Level of Education
  - Lunch Type
  - Test Preparation Course
  - Reading Score
  - Writing Score
- User-friendly web interface for data input
- Displays prediction results

## Technology Stack

- Python 3.x
- Flask (Web Framework)
- Scikit-learn (Machine Learning)
- Pandas (Data Manipulation)
- NumPy (Numerical Operations)
- HTML/CSS (Frontend)

## Project Structure

- `app.py`: Main Flask application
- `src/pipeline/predict_pipeline.py`: Contains prediction pipeline and data processing
- `src/utils.py`: Utility functions for model operations
- `templates/`: HTML templates for the web interface
- `artifacts/`: Stored model and preprocessor files

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/student-performance-predictor.git
   ```

2. Navigate to the project directory:
   ```
   cd student-performance-predictor
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and go to `http://localhost:5001`

3. Use the web interface to input student data and get predictions

## Model Training

The model has been pre-trained on student performance data. The training process includes:

- Data preprocessing
- Feature engineering
- Model selection and hyperparameter tuning
- Model evaluation

## Contributing

Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

[Specify your license here]

## Contact

[Your Name] - [Your Email]

Project Link: [https://github.com/your-username/student-performance-predictor](https://github.com/your-username/student-performance-predictor)