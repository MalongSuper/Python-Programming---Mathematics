# This program imports RandomSampleValues.py
# To find values of the random sample given as a table of
# The values and the frequencies
import RandomSampleValues as rsv


def main():
    print("Random Sample Table")
    sequence = []
    n = int(input("Enter the length of the table: "))
    for i in range(n):
        # Input a value and its frequency
        x, f = eval(input(f"Enter x{i + 1} and its frequency: "))
        for j in range(f):
            sequence.append(x)
    # Display result
    print("n:", rsv.length(sequence))
    print("sample x:", rsv.sample_mean(sequence))
    print("s^2:", rsv.sample_variance(sequence))
    print("s:", rsv.sample_sd(sequence))


# Avoid running the main function
# when importing the 'module' to another program
if __name__ == "__main__":
    main()
