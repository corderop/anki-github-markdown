# 👥 Contributing

We are fully open to having new contributors. If you have found a bug, please consider opening an issue. Also, please open a pull request if you want to submit any changes. We will be happy to review it.

---

1. [Development setup](#development-setup)
2. [Environment setup](#environment-setup)
3. [Commit naming](#commit-naming)

---

## Development setup

We have created a bash file to set up your development environment to make the process easier. After running it, you will find the addon installed in Anki. Please consider the following requirements before running the script:

- Disable/Uninstall any other version of the addon you have installed in Anki.
- Modify `ANKI_ADDONS_FOLDER` in the script to point to your Anki addons folder if it is not the default one.

The script has two main behaviors:

- **Install the addon in Anki**. It will create a symlink from the src folder to the Anki addons folder. Any change in your code will be reflected automatically in the addon in Anki.

  ```bash
  ./development.sh
  ```

- If you run with the following flag, it will delete the development folder in Anki.

  ```bash
  ./development.sh --delete
  ```

## Environment setup

1. Install python dependencies. We recommend using a virtual environment with Python 3.10. Note that you will only need python dependencies for development purposes. The addon does not use any external dependencies other than the ones provided by Anki.

   ```bash
   pip install -r requirements.txt
   ```

2. Install pre-commit. It will create a git hook to run the linter before each commit. So we won't merge any PR with failing linting.

   ```bash
   pre-commit install
   ```

3. Run the tests. For this, we use `pytest`. Please, make sure tests pass before submitting a PR.

   ```bash
   pytest
   ```

## Commit naming

For the commit messages, we follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.
