#include <unordered_map>
#include <string>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;


void solve(vector<int> sequence, int max_turn)
{
    int sequence_len = sequence.size();
    int last_number = sequence[sequence_len - 1];
    int current_turn = sequence_len + 1;

    // <number, last index of the number>
    unordered_map<int, int> numbers;
    for (int i = 0; i < sequence_len -1; ++i) {
        numbers[sequence[i]] = i + 1;
    }
    while (current_turn <= max_turn) {
        auto it = numbers.find(last_number);
        if (it != numbers.end()) {
            int new_number = (current_turn - 1) - it->second;
            numbers[last_number] = current_turn - 1;
            last_number = new_number;
        }
        else {
            numbers[last_number] = sequence_len;
            last_number = 0;
        }
        sequence_len++;
        current_turn++;
    }


    cout << "Turn " << current_turn-1 << "; last_number = " << last_number << endl;
}

int main()
{
    freopen("in.txt", "r", stdin);
    string line;
    std::cin >> line;
    cout << line << endl;

    vector<int> sequence;
    stringstream ss(line);
    while (ss.good()) {
        getline(ss, line, ',');
        sequence.push_back(stoi(line));
    }

    solve(sequence, 2020);
    solve(sequence, 30000000);

    return 0;
}