#include <iostream>
#include <vector>

using namespace std;

void insertion_sort(vector<int>& nums) {
    for(size_t j = 1; j < nums.size(); j++) {
        int key = nums[j];
        int i = j - 1;
        while(i >= 0 && nums[i] > key) {
            nums[i + 1] = nums[i];
            i--;
        }
        nums[i + 1] = key;
    }
}

void merge_sort() {
    

}

void printVector(const vector<int>& input) {
    for(int i = 0; i < input.size(); i++) {
        cout << input[i] << " ";
    }
    cout << endl;
}

int main(int argc, const char* argv[]) {
    if(argc < 2) {
        printf("usage: sort \"3 2 1\"\n ");
        exit(1);
    }

    const char* nums_array = argv[1];
    int i = 0;
    int value = 0;
    vector<int> nums;
    while(i >= 0 && nums_array[i] != '\0') {
        //printf("char: %c\n", nums_array[i]);
        if(nums_array[i] != ' ') {
            value = value * 10 + nums_array[i] - '0';
        }
        else {
            nums.push_back(value);
            value = 0;
        }
        i++;
        if(nums_array[i] == '\0') nums.push_back(value);
    }
    cout << "input numbers are: ";
    printVector(nums);

    insertion_sort(nums);
    cout << "After sorting: ";
    printVector(nums);

}
