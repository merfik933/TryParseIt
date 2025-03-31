import argparse

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Check the possibility of parsing from the site.")
    parser.add_argument("url", type=str, help="URL to parse")
    parser.add_argument("-r", "--use-requests", type=bool, default=True, help="Use requests for parsing")
    parser.add_argument("-p", "--use-playwright", type=bool, default=True, help="Use playwright for parsing")


if __name__ == "__main__":
    main()