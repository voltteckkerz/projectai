# Principles of Artificial Intelligence: Orchid Classification

This project aims to automate the classification of orchid subfamilies using Deep Learning. It was developed as part of the **Principles of Artificial Intelligence** coursework (UNIKL SEM 4).

## 👥 Authors
- Amir Raif Bin Mizlan (52213223142)
- Amir Keizrul Bin Mudzir (52213223121)
- Ahmad Afif Abdul Hadi bin A Rahim (52213223199)

## 🌺 Overview
The project is divided into several main sections:
1. **Data Preparation & Collection**: Web scraping using Selenium (`main.py`) to gather images of different orchid classes.
2. **Data Modelling**: Training deep learning models on the collected dataset (`projectai.ipynb`).
3. **Data Visualization**: Evaluating the models' accuracy and loss, and comparing their performance.

### Orchid Classes
The models predict the following 5 orchid subfamilies:
- Apostasioideae
- Cypripedioideae
- Epidendroideae
- Orchidoideae
- Vanilloideae

## 📁 Repository Structure
- `main.py`: Python script utilizing `selenium` to automate Google Images search and download 2000 images per class.
- `projectai.ipynb`: Jupyter Notebook containing the full pipeline—data preprocessing, model architecture, training, and evaluation.
- `dataset/`: Contains the scraped images divided by training and testing subsets, augmented and formatted for training.
- `*.h5`: Saved trained models including DenseNet121, MobileNet, MobileNetV3, and ResNet50.
- `*_history.json`: Training history logs (accuracy, loss etc.) for visualization.

## 🛠️ Setup & Installation
1. Install the required dependencies:
   ```bash
   pip install selenium requests pillow tensorflow scikit-learn scipy matplotlib
   ```
2. For scraping new data, ensure [ChromeDriver](https://chromedriver.chromium.org/downloads) is installed and accessible in your system PATH.
3. Open `projectai.ipynb` in Jupyter Notebook or Google Colab to run the training and visualization cells.

*Note: The `.h5` model files are tracked via Git LFS due to their large file sizes.*