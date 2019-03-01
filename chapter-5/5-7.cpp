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

using namespace std;



int main() {

  int cases;
  cin >> cases;

  vector<tuple<int, int, int>> tasks;
  vector<int> jobs;
  for (int i = 0; i < cases; i++) {
    string empty_line;
    getline(cin, empty_line);

    tasks.clear();
    jobs.clear();

    int tasks_number;
    cin >> tasks_number;
    for (int j = 0; j < tasks_number; j++) {
      int time;
      int fine;
      cin >> time >> fine;

      tasks.push_back(make_tuple(j + 1, time, fine));
    }
    //cout << endl;
    //cout << "Task: " << i << " " << tasks_number << endl;

    //int best_min = min_job_cost(tasks, false);
    //cout << "Min cost: " << best_min << endl;

    stable_sort(tasks.begin(), tasks.end(), job_compare);
    //cout << "Found cost: " << job_cost(tasks) << endl;

    //print_job_tuple(tasks);
    print_job_order(tasks);

    if (i < cases - 1) {
      cout << endl;
    }
  }
}
