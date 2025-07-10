#include <stdio.h>

// Function to find max profit
int maxProfit(int* prices, int pricesSize) {
    if (pricesSize == 0) return 0;

    int left = 0; // Buy day
    int right = 1; // Sell day
    int maxP = 0;

    while (right < pricesSize) {
        if (prices[right] > prices[left]) {
            int profit = prices[right] - prices[left];
            if (profit > maxP) {
                maxP = profit;
            }
        } else {
            left = right; // Move buy day to current day
        }
        right++;
    }

    return maxP;
}

// Driver code for testing
int main() {
    int prices[] = {7, 1, 5, 3, 6, 4};
    int size = sizeof(prices) / sizeof(prices[0]);

    int result = maxProfit(prices, size);
    printf("Maximum Profit: %d\n", result);

    return 0;
}
