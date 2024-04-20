import os

from dotenv import load_dotenv, dotenv_values

if __name__ == "__main__":
    load_dotenv(override=False)
    config = dotenv_values(".env")
    print(os.getenv("NAME"))
    print(config)
