#include <iostream>
#include <vector>

using namespace std;

    int dietPlanPerformance(vector<int>& calories, int k, int lower, int upper) {
        int size = calories.size();
        if(size < k) return 0;
        int points = 0;
        int sum = 0;
        int j;
        for(j = 0;j < k;++j) {
            sum += calories[j];
        }
        if(sum < lower) {
            --points;
        }
        else if(sum > upper) {
            ++points;
        }
        for(int i = 0; j < calories.size();++i, ++j) {
            sum = sum - calories[i] + calories[j];
            if(sum < lower) {
                --points;
            }
            else if(sum > upper) {
                ++points;
            }
        }
        return points;
    }

int main() {
    vector<int> calories = {};
    cout << dietPlanPerformance(calories, 49135, 34392866, 213587275);
    return 0;
}

