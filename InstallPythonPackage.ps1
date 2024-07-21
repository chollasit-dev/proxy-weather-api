@(
    # devDependency
    'ruff'
    'mypy'
    'pytest'

    # dependency
    'flask'
    'requests'

    # optional
    'watchdog'  # auto-reload flask on change
    'python-dotenv'  # auto-load existing .env file for development

) | ForEach-Object { pip install -U --no-cache-dir --require-virtualenv $_ }

pip freeze > requirements.txt
