/*
  [4] Given pre-order and in-order traversals of a binary tree,
  is it possible to recon- struct the tree? If so, sketch an
  algorithm to do it. If not, give a counterexample. Repeat the
  problem if you are given the pre-order and post-order traversals.
*/

#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <deque>
#include <iterator>
#include <algorithm>
#include <utility>
#include <cmath>
#include <set>

using namespace std;

void print_graph()

int main() {
  map<string, set<string>> graph;
  int nodes;
  cin >> nodes;

  for (int i = 0; i < nodes; i++) {
    string node;
    cin >> node;

    string line;
    getline(cin, line);
    istringstream iss(line);

    string adj;
    set<string> adj_nodes;
    while (iss >> adj) {
      adj_nodes.insert(adj);
    }

    graph.insert(make_pair(node, adj_nodes));
  }
}
