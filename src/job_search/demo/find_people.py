#!/usr/bin/env python
"""
Script to run the find_people method from the Client class.
This allows searching for people on LinkedIn based on specified skills.
"""

import argparse
import os
from dotenv import load_dotenv

# Update the import to use the correct module path
from job_search.tools.client import Client


def run():
    """Main function to parse arguments and run the find_people method."""
    # Load environment variables from .env file if it exists
    load_dotenv()

    # Check if LinkedIn cookie is set
    if "LINKEDIN_COOKIE" not in os.environ:
        print("Error: LINKEDIN_COOKIE environment variable is not set.")
        print("Please set it in your .env file or environment variables.")
        return 1

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Search for people on LinkedIn based on skills"
    )
    parser.add_argument(
        "--skills",
        type=str,
        default="full,stack,develop",
        help="Comma-separated list of skills to search for",
    )
    args = parser.parse_args()

    try:
        # Initialize the client
        client = Client()

        print(f"Searching for people with skills: {args.skills}")
        # Run the find_people method
        results = client.find_people(args.skills)

        # Print summary
        print(f"Found {len(results)} people matching the criteria.")

        # Print each result in a readable format
        print("\n=== SEARCH RESULTS ===")
        for i, person in enumerate(results, 1):
            print(f"\n[{i}]")
            print(f"Name: {person.get('name', 'Unknown')}")
            print(f"Profile: {person.get('profile_link', 'N/A')}")
            # Print any other fields that are available
            for key, value in person.items():
                if key not in ['name', 'profile_link']:
                    print(f"{key.capitalize()}: {value}")

        # Close the client
        client.close()

    except Exception as e:
        print(f"Error occurred: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(run())
