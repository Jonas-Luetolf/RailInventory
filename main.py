from application import create_app
from config import Config

app = create_app()

def main():
    """
    entry point for RailInventory
    """
    
    app = create_app()
    app.run(host="localhost")


if __name__ == "__main__":
    main()
