#import matplotlib.pyplot as plt
from collections import Counter


def analyze_and_visualize_lottery_numbers(winning_numbers):
    all_numbers = [number for sublist in winning_numbers for number in sublist]
    number_count = Counter(all_numbers)
    sorted_numbers = sorted(number_count.items(), key=lambda x: x[1], reverse=True)

    numbers, counts = zip(*sorted_numbers)

    #plt.figure(figsize=(10, 6))
    # plt.bar(numbers, counts, color='blue')
    # plt.xlabel('Number')
    # plt.ylabel('Frequency')
    # plt.title('Number Frequency Analysis')
    # plt.xticks(numbers)
    # plt.show()


# Example winning numbers (replace with your own data)
winning_numbers = [
    [4, 8, 15, 23, 42],
    [7, 11, 16, 28, 36],
    [2, 9, 17, 22, 31],
    [5, 12, 19, 25, 37],
    [1, 6, 14, 20, 29]
]

analyze_and_visualize_lottery_numbers(winning_numbers)
from collections import Counter


def analyze_lottery_numbers(winning_numbers):
    all_numbers = [number for sublist in winning_numbers for number in sublist]
    number_count = Counter(all_numbers)
    sorted_numbers = sorted(number_count.items(), key=lambda x: x[1], reverse=True)

    print("Number Frequency Analysis:")
    for number, count in sorted_numbers:
        print(f"Number {number}: {count} times")

    total_draws = len(winning_numbers)
    print(f"\nTotal Draws: {total_draws}")


# Example winning numbers (replace with your own data)


if __name__ == '__main__':
    winning_numbers = [
        [4, 8, 15, 23, 42],
        [7, 11, 16, 28, 36],
        [2, 9, 17, 22, 31],
        [5, 12, 19, 25, 37],
        [1, 6, 14, 20, 29]
    ]
    analyze_lottery_numbers(winning_numbers)
