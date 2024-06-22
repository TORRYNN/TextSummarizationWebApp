# 📜 **Text Summarization Web App**

Welcome to the `Text Summarization` Web App! This web application allows users to easily summarize text by either providing a URL or directly pasting text. It leverages the power of the Hugging Face Transformers for generating concise and informative summaries.

## <img  width="100%" height=""  src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" alt="torrynn" /> ✨ **Features**

- 🌐 **Summarize from URL**: Fetches and summarizes text content from a provided URL.
- 📝 **Summarize from Text**: Allows users to input text directly and get a summary.
- ⚙️ **Dynamic Length**: Users can specify the desired length of the summary using a slider.
- 📱 **Responsive Design**: Ensures the application adapts well to various screen sizes and devices.


## <img  width="100%" height=""  src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" alt="torrynn" /> 🛠️ **Technologies Used**

- ![Flask](https://img.shields.io/badge/-Flask-E34F26?logo=Flask&logoColor=white&style=flat) **Flask**: For creating the web application.
- ![BeautifulSoup](https://img.shields.io/badge/-BeautifulSoup-4E8EF7?logo=BeautifulSoup&logoColor=white&style=flat) **BeautifulSoup**: For scraping text data from HTML.
- ![Hugging Face Transformers](https://img.shields.io/badge/-Hugging%20Face%20Transformers-FFD700?logo=hugging%20face&logoColor=white&style=flat) **Hugging Face Transformers**: For text summarization.
- ![dotenv](https://img.shields.io/badge/-dotenv-6534AC?logo=dotenv&logoColor=white&style=flat) **dotenv**: For environment variable management.
- ![HTML5](https://img.shields.io/badge/-HTML5-E34F26?logo=html5&logoColor=white&style=flat) **HTML**: For structuring the front-end interface.
- ![CSS](https://img.shields.io/badge/-CSS-1572B6?logo=css3&logoColor=white&style=flat) **CSS**: For styling the front-end interface.



## <img  width="100%" height=""  src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" alt="torrynn" /> 🚀 **Getting Started**

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip

### `Installation`

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/text-summarization-webapp.git
    cd text-summarization-webapp
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    Create a `.env` file in the root directory and add your Hugging Face API key:

    ```env
    API_KEY=your_huggingface_api_key
    ```

### `Running the App`

Start the Flask application:

    ```sh
    python app.py
    ```

Navigate to `http://127.0.0.1:5000` in your browser to use the app.

## <img  width="100%" height=""  src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" alt="torrynn" /> 🧭 **Usage**

1. **Home Page**: Enter a URL or paste the text you want to summarize.
2. **Specify Length**: Input the maximum length of the summary.
3. **Get Summary**: Click the 'Summarize' button to get the summarized text.

## <img  width="100%" height=""  src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" alt="torrynn" /> 📁 **Code Overview**

### `app.py`

This is the main Flask application file.

- **Routes**:
    - `/`: Renders the main page.
    - `/Summarize`: Handles the summarization logic.

- **Functions**:
    - `Index()`: Renders the `index.html` template.
    - `Summarize()`: Processes the URL or text input and fetches the summary from the Hugging Face API.

### `templates/index.html`

The main HTML template for the web interface.

### `static/css/styles.css`

Contains custom styles for the web app.

## <img  width="100%" height=""  src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" alt="torrynn" /> 🖼️ **Example**

Here is an example of how the summarized output looks:
<details>
  <summary>Preview 1 📱</summary>
  <br>
  <img src="https://github.com/TORRYNN/TextSummarizationWebApp/assets/101942128/fb0f4d2c-047c-45de-8340-3b9f3c343367" alt="iPhone 13 PRO" width="25%" height="25%"> 
</details>

<details>
  <summary> Preview 2 💻</summary>
  <br>
  <img src="https://github.com/TORRYNN/TextSummarizationWebApp/assets/101942128/632e09cc-36da-4049-b018-9ace28855b9d" alt="Macbook Air" width="500" height="300">
</details>

<details>
  <summary> Preview 3 📟</summary>
  <br>
  <img src="https://github.com/TORRYNN/TextSummarizationWebApp/raw/main/assets/101942128/7efcdd54-e362-4c87-862d-e70b2ef41589" alt="iPad Air 4" width="500" height="300">
</details>


## <img  width="100%" height=""  src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" alt="torrynn" /> 📑 **Presentation**

For a deeper understanding of text summarization, you can refer to my [`Text Summarization PowerPoint Presentation`](https://www.canva.com/design/DAF9z0gtY7Y/mNDQi3fvh9tD2cmXEwQQsQ/view?utm_content=DAF9z0gtY7Y&utm_campaign=designshare&utm_medium=link&utm_source=editor).

## <img  width="100%" height=""  src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" alt="torrynn" /> 🤝 **Contributing**

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## <img  width="100%" height=""  src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" alt="torrynn" /> 📜 **License**

This project is licensed under the [`MIT License`](LICENSE).

## <img  width="100%" height=""  src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" alt="torrynn" /> 🙏 **Acknowledgements**

- [`Hugging Face`](https://huggingface.co/) for their powerful Transformers library.
- [`Flask`](https://flask.palletsprojects.com/) for providing a lightweight web framework.

## <img  width="100%" height=""  src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" alt="torrynn" /> 🌐 **Social**

Follow me on social media for updates and more:
<a href="https://linkedin.com/in/pratham-chauhan-265a8b15a" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="pratham-chauhan-265a8b15a" height="30" width="40" /></a>
---

Feel free to explore, use, and contribute to this project! If you have any questions or suggestions, please open an issue or reach out.

Happy summarizing! 😊

<img  width="100%" height=""  src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" alt="torrynn" />

