from application import create_app

def main():
    """
    entry point for RailInventory
    """

    app = create_app()
    app.run(host="localhost", port=5000)


if __name__ == "__main__":
    main()
