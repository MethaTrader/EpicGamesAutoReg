![Cover Image](CoverImage.png)


# About Epic Games Auto-Reg

Epic Games Auto-Reg is a Python script that automates the process of creating new accounts on Epic Games. It uses the Selenium WebDriver to interact with the Epic Games registration form and fill it out with randomly generated user data.

> **Warning**
> Please note that this project is still under development, and as of now, it only fills out the form. It does not handle CAPTCHA challenges or email activation.

## Installation and Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/EpicGamesAutoReg.git
cd EpicGamesAutoReg
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Download the appropriate [ChromeDriver](https://chromedriver.chromium.org/downloads) for your system and place it in the project directory.

4. Create a file called `emails.txt` in the project directory and add the email addresses you want to use for registration, one per line.

5. Run the script:

```bash
python main.py
```


## Contributions

The project is actively seeking contributions for the following features:

- Handling CAPTCHA challenges.
- Reading and processing activation emails.

If you can help with any of these, please consider becoming a contributor to the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
