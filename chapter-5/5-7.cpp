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

class Graph {
  public:

    map<string, set<string>> g;

    set<string>& operator[] (string& node) {
      return g[node];
    }

    void print() {
      for (auto it = g.begin(); it != g.end(); it++) {
        cout << it->first << endl;
      }
    }

    void print_set() {
      for (auto it = g.begin(); it != g.end(); it++) {
        cout << it->first << ": ";
        for (auto it2 = it->second.begin(); it2 != it->second.end(); it2++) {
          cout << *it2 << " ";
        }
        cout << endl;
      }
    }
};

Graph build_tree(map<string, deque<string>>& orders) {
  Graph g;
  deque<string> pre = orders["pre"];
  deque<string> in = orders["in"];

  for (auto i : pre) {
    set<string> init;
    g[i] = init;
  }

  int i = 0;
  int j = 0;
  while (pre[i] != in[j]) {
    i++;
  }

  for (int i = 0; i < pre.size(); i++) {
    if (i < pre.size() - 1) {
      g[pre[i]].insert(pre[i + 1]);
    }
    for (int j = 0; j < in.size(); j++) {
      if (pre[i] == in[j]) {

      }
    }
  }
}

int main() {
  Graph graph;
  int nodes;
  cin >> nodes >> ws;

  for (int i = 0; i < nodes; i++) {
    string node;
    cin >> node >> ws;

    string line;
    getline(cin, line);

    istringstream iss(line);

    string adj;
    set<string> adj_nodes;
    while (iss >> adj) {
      if (adj != "NULL") {
        adj_nodes.insert(adj);
      }
    }

    graph[node] = adj_nodes;
  }
  graph.print_set();

  map<string, deque<string>> orders;
  for (int i = 0; i < 3; i++) {
    string order_type;
    cin >> order_type >> ws;

    string line;
    getline(cin, line);
    istringstream iss(line);

    string node;
    deque<string> nodes;
    while (iss >> node) {
      nodes.push_back(node);
    }

    orders[order_type] = nodes;
  }
}
