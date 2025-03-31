import argparse

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Check the possibility of parsing from the site.")
    parser.add_argument("url", type=str, help="URL to parse")
    parser.add_argument("-r", "--use-requests", type=bool, default=True, help="Use requests for parsing")
    parser.add_argument("-p", "--use-playwright", type=bool, default=True, help="Use playwright for parsing")

    args = parser.parse_args()

    url = args.url
    use_requests = args.use_requests
    use_playwright = args.use_playwright

    is_requests_parsing_successful = False
    is_playwright_parsing_successful = False

    if use_requests:
        from requests_parser import try_parse

        page = try_parse(url)
        if page:
            with open("C:\\Users\\anato\\Downloads\\page_requests.html", "w", encoding="utf-8") as file:
                file.write(page)
            is_requests_parsing_successful = True
        
    if use_playwright:
        from playwright_parser import try_parse

        page = try_parse(url)
        if page:
            with open("C:\\Users\\anato\\Downloads\\page_playwright.html", "w", encoding="utf-8") as file:
                file.write(page)
            is_playwright_parsing_successful = True

    print("Parsing completed.")
    print("Results:\n")
    print(f"Requests parsing successful: {is_requests_parsing_successful}")
    print(f"Playwright parsing successful: {is_playwright_parsing_successful}")
    print("\nCheck the files in Downloads folder.")

if __name__ == "__main__":
    main()