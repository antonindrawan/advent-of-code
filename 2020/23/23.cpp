#include <iostream>
#include <vector>
#include <array>
#include <set>

using namespace std;

struct Node
{
    explicit Node(int aNumber) {
        number = aNumber;
    }
    int number {0};
    Node* next {nullptr};
};

int get_destination(Node* current_node, const set<int>& pick_up_numbers, int max_number)
{
    int destination = current_node->number - 1;
    if (destination == 0) destination = max_number;

    while (pick_up_numbers.find(destination) != pick_up_numbers.end()) {
        destination -= 1;
        if (destination == 0) destination = max_number;
    }
    return destination;
}


void move_cycle(vector<Node>& node_list, Node* start_node, int cycles)
{
    int nodes_count = node_list.size() - 1;
    int cycle = 0;
    Node* current_node = start_node;
    while (cycle < cycles) {
        set<int>pick_up_numbers {current_node->next->number, current_node->next->next->number, current_node->next->next->next->number};
        vector<Node*>pick_up_nodes {current_node->next, current_node->next->next, current_node->next->next->next};

        int destination = get_destination(current_node, pick_up_numbers, nodes_count);
        Node* destination_node = &node_list[destination];
        Node* destination_next_node = destination_node->next;

        // set the next node of the current to the next node of the last pick up node
        // 3 -> 8 -> 9 -> 1 -> 2..
        // pick up nodes: 8 -> 9 -> 1
        // becomes: 3 -> 2 after shifting the picked up nodes
        current_node->next = pick_up_nodes[pick_up_nodes.size()-1]->next;

        // Set the current node for the next cycle, before it is updated
        current_node = current_node->next;

        // Set the pick up nodes to be the next node of the destination node
        destination_node->next = pick_up_nodes[0];

        // Update the next node of the last node in the pick up nodes
        pick_up_nodes[pick_up_nodes.size()-1]->next = destination_next_node;

        cycle++;
    }
}


int main()
{
    vector<int> input {5, 3, 8, 9, 1, 4, 7, 6, 2};

    input.resize(1000000);
    for (int i = 10; i < 1000001; ++i) {
        input[i-1] = i;
    }

    vector<Node> node_list {input.size() + 1, Node{-1}};
    node_list[input[0]] = Node{input[0]};
    Node* first_node = &node_list[input[0]];


    Node* current_node = first_node;
    for (int i = 1, len = input.size(); i < len; ++i) {
        node_list[input[i]] = Node{input[i]};

        auto node = &node_list[input[i]];
        current_node->next = node;
        current_node = node;
    }
    current_node->next = first_node;

    move_cycle(node_list, first_node, 10000000);

    Node* node_one = &node_list[1];
    int64_t result = int64_t(node_one->next->number) * int64_t(node_one->next->next->number);
    cout << "[part 2] Result " << result << endl;

    //g++ -O2 -g 23.cpp && time ./a.out
    // [part 2] Result 157410423276
    // ./a.out  1,43s user 0,01s system 99% cpu 1,435 total
    return 0;
}