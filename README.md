# Privacy Preference Learning Framework

An interactive learning framework that learns user privacy preferences through direct user edits and applies these preferences to future responses.

## Project Overview
The framework learns user privacy preferences by:
1. Generating responses based on given contexts
2. Learning from user's edits to understand privacy preferences
3. Incorporating learned preferences into future responses
4. Evaluating the effectiveness through edit distance and information alignment metrics

## Installation

### Prerequisites
- Python 3.6+
- Virtual environment management tool (conda recommended)

### Setup
1. Create and activate a virtual environment:
```bash
# Create virtual environment
conda create -n privacy_learner python=3.8
# Activate environment
conda activate privacy_learner
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Learning Process
```bash
python main.py
```
This will:
- Start an interactive session
- Allow you to choose between Basic Mode and Reasoning Mode
- Go through multiple rounds of interaction
- Generate an interaction log file

### Running Evaluation
To evaluate the results from an interaction log:
```bash
python src/evaluation/run_evaluation.py "logs/interaction_log_[filename].json"
```

### Modes Available
1. Basic Mode:
   - Direct comparison and preference learning
   - No user justification required

2. Reasoning Mode:
   - Interactive preference learning
   - Includes follow-up questions for user justification
   - More detailed preference analysis

## Project Structure
```
privacy_learning/
├── src/
│   ├── data_loader.py           # Loads scenario data
│   ├── scenario_manager.py      # Manages scenario selection and formatting
│   ├── gpt_interface.py         # Handles GPT API interactions
│   ├── preference_learner.py    # Manages learned preferences
│   ├── modes/
│   │   ├── base_mode.py        # Abstract base class for modes
│   │   ├── basic_mode.py       # Basic learning mode
│   │   └── reasoning_mode.py   # Reasoning-based learning mode
│   ├── evaluation/
│   │   ├── edit_distance_metrics.py      # Token-based evaluation
│   │   └── information_alignment_metrics.py  # Information-based evaluation
│   └── logging/
│       └── interaction_logger.py   # Handles interaction logging
├── logs/                          # Stores interaction logs
├── context_data/                  # Contains scenario data
├── main.py                        # Main entry point
└── requirements.txt               # Project dependencies
```

## Evaluation Metrics
1. Edit Distance:
   - Measures token-based differences between responses
   - Normalized score (0-1)

2. Information Alignment:
   - Measures how well responses align with learned privacy preferences
   - Analyzes information disclosure patterns

## Contributing
Zhiping Zhang https://www.zhipingzhang.com/ 

## License
