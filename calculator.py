import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Simple command line calculator")
    parser.add_argument('x', type=float, help='First number')
    parser.add_argument('op', choices=['+', '-', '*', '/'], help='Operator')
    parser.add_argument('y', type=float, help='Second number')
    args = parser.parse_args()

    if args.op == '+':
        result = args.x + args.y
    elif args.op == '-':
        result = args.x - args.y
    elif args.op == '*':
        result = args.x * args.y
    elif args.op == '/':
        if args.y == 0:
            print('Error: Division by zero')
            sys.exit(1)
        result = args.x / args.y
    else:
        print('Unknown operation')
        sys.exit(1)

    print(result)


if __name__ == '__main__':
    main()
