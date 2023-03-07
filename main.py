from application import create_app
from config import Config


def main():
    """
    entry point for RailInventory
    """

    app = create_app()
    app.run(host="localhost", ssl_context=Config.SSL_CONTEXT)


if __name__ == "__main__":
    main()
