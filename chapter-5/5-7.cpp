/*
  [4] Given pre-order and in-order traversals of a binary tree,
  is it possible to reconstruct the tree? If so, sketch an
  algorithm to do it. If not, give a counterexample. Repeat the
  problem if you are given the pre-order and post-order traversals.
*/

/*
Counter Example:
    A
  B   C
D
pre
A B D C
post
D B C A
in
D B A C

     A
  B     C
    D
pre
A B D C
post
D B C A
in
B D A C
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

void print_vec(vector<string> v) {
  cout << "vec: ";
  for (auto el : v) {
    cout << el << " ";
  }
  cout << endl;
}

string recurse_tree(
  Graph& g,
  vector<string> children,
  deque<string>& pre
) {

  if (children.size() == 0) {
    return "";
  }

  string child;
  string root = pre[0];
  pre.pop_front();

  if (children.size() == 1) {
    return children[0];
  }

  auto node = find(children.begin(), children.end(), root);

  child = recurse_tree(g, vector<string> (children.begin(), node), pre);
  if (child != "") g[root].insert(child);

  child = recurse_tree(g, vector<string> (node + 1, children.end()), pre);
  if (child != "") g[root].insert(child);

  return root;
}

Graph build_tree(map<string, vector<string>>& orders) {
  Graph g;
  deque<string> pre(orders["pre"].begin(), orders["pre"].end());
  vector<string> in = orders["in"];

  for (auto i : pre) {
    set<string> init;
    g[i] = init;
  }

  recurse_tree(g, in, pre);
  return g;
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

  map<string, vector<string>> orders;
  for (int i = 0; i < 3; i++) {
    string order_type;
    cin >> order_type >> ws;

    string line;
    getline(cin, line);
    istringstream iss(line);

    string node;
    vector<string> nodes;
    while (iss >> node) {
      nodes.push_back(node);
    }

    orders[order_type] = nodes;
  }

  Graph g = build_tree(orders);
  if (g.g == graph.g) {
    cout << "Graph rebuild successful" << endl;
  } else {
    g.print_set();
  }
}
