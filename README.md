# Student Performance Predictor

This project is an end to end data science project that provide a web interface to help users to predict student math scores based on various demographic and academic factors. It uses machine learning models to make predictions and provides a user-friendly interface for input and result display.

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
- `src/pipeline/train_pipeline.py`: Pipeline for training the model
- `src/components/data_ingestion.py`: Handles data loading and splitting
- `src/components/data_transformation.py`: Performs data preprocessing and feature engineering
- `src/components/model_trainer.py`: Trains and evaluates various machine learning models
- `src/utils.py`: Utility functions for model operations
- `src/logger.py`: Logging configuration
- `src/exception.py`: Custom exception handling
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

The model training process is comprehensive and includes several steps:

1. **Data Ingestion** (`data_ingestion.py`):
   - Loads the dataset
   - Splits data into training and testing sets

2. **Data Transformation** (`data_transformation.py`):
   - Handles missing values
   - Encodes categorical variables
   - Scales numerical features

3. **Model Training** (`model_trainer.py`):
   - Trains multiple models:
     - Random Forest
     - Decision Tree
     - Gradient Boosting
     - Linear Regression
     - XGBoost
     - CatBoost
     - AdaBoost
   - Performs hyperparameter tuning using RandomizedSearchCV
   - Evaluates models using R-squared score
   - Selects the best performing model

4. **Model Evaluation**:
   - Uses R-squared score to assess model performance
   - Compares predicted vs actual values

The best model is saved and used for making predictions in the web application.

## Results Interpretation

The model predicts a student's math score based on the input features. Here's how to interpret the results:

1. **Predicted Score**: The output is a numerical value representing the predicted math score.

2. **Score Range**: The predicted score typically falls between 0 and 100, aligning with standard grading scales.

3. **Influential Factors**:
   - Higher reading and writing scores generally correlate with higher math scores.
   - The impact of demographic factors (gender, race/ethnicity) may indicate systemic educational disparities.
   - Parental education level often shows a positive correlation with student performance.
   - Students who completed the test preparation course tend to score higher.

4. **Limitations**:
   - The model provides an estimate based on historical data and may not account for individual circumstances.
   - Predictions should be used as a guideline rather than a definitive assessment.

5. **Using the Results**:
   - Educators can use these predictions to identify students who might need additional support.
   - Students and parents can gain insights into potential areas for improvement.
   - Administrators can use aggregate predictions to allocate resources and develop targeted programs.

## Ethical Considerations

It's important to use this predictive model responsibly:
- The model should not be used as the sole factor in making educational decisions.
- Be aware of potential biases in the training data that could affect predictions.
- Regularly update and retrain the model to ensure its relevance and accuracy.

## Future Improvements

- Incorporate more features such as study habits, extracurricular activities, and school resources.
- Experiment with advanced models like neural networks or ensemble methods.
- Develop a time-series component to track student progress over multiple assessments.

## Contact

Project Link: [https://github.com/your-username/student-performance-predictor](https://github.com/your-username/student-performance-predictor)
