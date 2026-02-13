import argparse

def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--name")
    parser.add_argument("--env")

    parsed_args = parser.parse_args(args)

    print(f"Hello {parsed_args.name}")
    print(f"Environment: {parsed_args.env}")


if __name__ == "__main__":
    main()
