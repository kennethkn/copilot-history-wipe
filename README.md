# copilot-history-wipe

Wipe Copilot/Bing AI chat history with Selenium automation in Python.

Microsoft hasn't provided a way to clear chat history in one click, so this script does the job of clicking "Delete" repeatedly for you.

## Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
  - Using brew: `brew install python`
- [Microsoft Edge](https://www.microsoft.com/en-us/edge)
  - Usig brew: `brew install microsoft-edge`
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
    python script.py
    ```

    It launches the Edge browser, opens the Bing chat page, and waits for you to log in to your Microsoft account. Then, it clicks the delete button on each chat to clear all history eventually.

    Note: If you have a long chat history, the website may not display the entire history at once because the earlier chats are not recent enough to be shown. Therefore, it is recommended to reload the page after the script says "DONE" to confirm that all chat history has been cleared. You will be prompted to rerun the script.

    The script provides instructions and updates on its progress as it runs, so simply follow them.

5. Give the repo a star if it helped!

## Is it safe?

Look at the [code](del_bing_chat_hist.py). Look at my [LinkedIn](https://www.linkedin.com/in/kenneth-kwan-6bb396262). I am a good guy.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
