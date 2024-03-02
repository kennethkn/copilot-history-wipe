# bing-clear-chat-history

A python script that uses Selenium to automate the process of clearing the chat history in Bing Chat/Copilot (since Microsoft hasn't provided an official way to remove all chat history in one click...)

## Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
  - Using brew: `brew install python`
- [ChromeDriver](https://chromedriver.chromium.org/downloads)
  - Using brew: `brew install chromedriver`

## Usage

1. Clone this repository
2. Optional: Use a venv

    ```shell
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies

    ```shell
    pip install -r requirements.txt
    ```

4. Run the script

    ```shell
    python bing-clear-chats.py
    ```

    The script launches the Edge browser, opens the Bing chat page, and waits for you to log in to your Microsoft account. Then, it clicks the delete button on each chat to clear all history eventually.

    Note: If you have a long chat history, the website may not display the entire history at once because the earlier chats are not recent enough to be shown. Therefore, it is recommended to reload the page after the script says "DONE" to confirm that all chat history has been cleared. You can rerun the script as needed.

    The script provides instructions and updates on its progress as it runs, so simply follow them.

5. Give the repo a star if it helped!

## Is it safe?

Look at the [code](bing-clear-chats.py). Look at my [LinkedIn](https://www.linkedin.com/in/kenneth-kwan-6bb396262). I am a good guy.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

[MIT License](LICENSE)
