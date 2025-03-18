#!/usr/bin/env python
"""
Script to test the getCookiesFromDomain method from the Client class.
This allows retrieving browser cookies for specific domains.
"""

import argparse
from dotenv import load_dotenv

# Import the Client class
from job_search.tools.client import Client


def run():
    """Run the cookie extraction test."""
    # Load environment variables from .env file if it exists
    load_dotenv()

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Extract cookies from Fire browser for a specific domain"
    )
    parser.add_argument(
        "--domain",
        type=str,
        default="linkedin.com",
        help="Domain to extract cookies for (default: linkedin.com)",
    )
    parser.add_argument(
        "--cookie-name",
        type=str,
        default="li_at",
        help="Specific cookie name to extract (optional)",
    )
    args = parser.parse_args()

    try:
        print(f"Extracting cookies for domain: {args.domain}")

        # Call the static method on the Client class
        cookies = Client.getCookiesFromDomain(
            args.domain,
            args.cookie_name
        )

        # If a specific cookie name was requested
        if args.cookie_name:
            if cookies:
                print(f"\nFound cookie '{args.cookie_name}':")
                print(f"{cookies}")
                
            else:
                print(f"Cookie '{args.cookie_name}' not found")
        else:
            # Print number of cookies found
            print(f"Found {len(cookies)} cookies")

            # Print all cookies
            for name, value in cookies.items():
                # Split long values
                if len(value) > 60:
                    part1 = value[:60]
                    part2 = value[60:]
                    print(f"\n{name}:")
                    print(f"  {part1}")
                    print(f"  {part2}")
                else:
                    print(f"\n{name}: {value}")

    except Exception as e:
        print(f"Error occurred: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(run())
