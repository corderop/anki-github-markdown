# GitHub Markdown on Anki
Anki addon to generate cards with markdown using the public GitHub API

## Contributing

We are fully open to having new contributors. If you have found a bug, please consider opening an issue. Also, please open a pull request if you want to contribute to the code. We will be happy to review it.

### Development setup

To make the process easier, we have created a bash file to set up your development environment. After running it, you will find the addon installed in Anki. Please consider the following requirements before running the script:

- Disable/Uninstall any other version of the addon you have installed in Anki.
- Modify `ANKI_ADDONS_FOLDER` in the script to point to your Anki addons folder if it is not the default one.

The script has two main behaviors:

- **Install the addon in Anki**. It will create a symlink from the src folder to the Anki addons folder. Any change in your code will be reflected in the addon in Anki.

    ```bash
    ./development.sh
    ```

- If you run with the following flag, it will delete the development folder in Anki.

    ```bash
    ./development.sh --delete
    ```
