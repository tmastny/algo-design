/*
  [5] The square of a directed graph G = (V,E) is the graph G^2 = (V,E^2)
  such that (u,w) ∈ E^2 iff there exists v ∈ V such that (u,v) ∈ E and
  (v,w) ∈ E; i.e., there is a path of exactly two edges from u to w.

  Give efficient algorithms for both adjacency lists and matrices.
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

    void bfs() {

    }

    void square() {
      // bfs, counting the number of times I visit from root
      // however, bfs
    }

    void stdin_make() {
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

        g[node] = adj_nodes;
      }
    }
};

int main() {
  Graph graph;
  graph.stdin_make();

  graph.print_set();
}
