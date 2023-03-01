from application import create_app
import config


def main():
    """
    entry point for RailInventory
    """

    app = create_app()
    app.run(host="localhost", port=5000, ssl_context=config.Config.SSL_CONTEXT)


if __name__ == "__main__":
    main()
