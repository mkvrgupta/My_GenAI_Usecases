# 🧠 My GenAI Usecases

This repository showcases practical applications of Generative AI across data analysis, sentiment modeling, and synthetic test data generation. Built with Python, LangChain, and Jupyter notebooks, it serves as a modular playground for experimenting with GenAI workflows in QA automation, NLP, and data augmentation.

## 📁 Project Structure
├── data/ │   ├── banking_sentiment_data.csv │   ├── chinook.db │   └── sample_data.csv ├── my_scripts/ │   ├── langgraph_usecase.py │   ├── sentiment_analysis.ipynb │   └── test_data_generator.ipynb ├── requirements.txt


## 🚀 Usecases

### 1. **Sentiment Analysis**
Classifies customer sentiment using synthetic banking data and GenAI-assisted labeling.

![Sentiment Analysis Demo](assets/sentiment_analysis_demo.gif)

### 2. **Test Data Generator**
Generates realistic test data using LLMs for QA automation and edge case validation.

![Test Data Generator Demo](assets/test_data_generator_demo.gif)

### 3. **LangGraph Workflow**
Demonstrates LangChain + LangGraph integration for multi-step GenAI pipelines.

![LangGraph Workflow Demo](assets/langgraph_workflow_demo.gif)

## 🛠️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/mkvrgupta/My_GenAI_Usecases.git
cd My_GenAI_Usecases

# Create virtual environment
python -m venv .venv
source .venv/Scripts/activate  # Windows
# or
source .venv/bin/activate      # Unix/Mac

# Install dependencies
pip install -r requirements.txt



🤝 Contribution
Feel free to fork, experiment, and submit pull requests. This repo is a living lab for GenAI exploration.
