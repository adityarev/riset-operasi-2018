/*
 *	Shortest Path Problem (Djikstra's Algorithm)
 *	Created by : Aditya Pratama (05111540000101)
 */


#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <vector>

#define oo INT_MAX

using namespace std;

string toString(int n) {
	if (n == 0) {
		return "0";
	}
	
	string s = "";
	while (n > 0) {
		s = (char)('0' + (n % 10)) + s;
		n /= 10;
	}
	
	return s;
}


class Instruction {
public:
	Instruction() { }
	
	void showHeader() {
		cout << "-------------------------------------------" << endl;
		cout << "Shortest Path (Djikstra's Algorithm)" << endl;
		cout << "Created by : Aditya Pratama (0511540000101)" << endl;
		cout << "-------------------------------------------" << endl;
		cout << endl;
	}
	
	void showVertexNumberInput() {
		cout << "Enter number of vertex: ";
	}
	
	void showVertexNumberInputed(int n) {
		cout << n << " vertexes created numbered from 0 to " << (n - 1) << endl;
		cout << endl;
	}
	
	void showEdgeNumberInput() {
		cout << "Enter number of edge: ";
	}
	
	void showEdgeNumberInputed() {
		cout << "Input your edges (source <space> destination <space> weight):" << endl;
	}
	
	void showEdgeInputing(int i) {
		cout << "Edge " << i << ": ";
	}
	
	void showFromInput() {
		cout << "\nSet your current position: ";
	}
	
	void showToInput() {
		cout << "Set your destination: ";
	}
};

Instruction instruction = Instruction();


class Graph {
private:
	vector<vector<pair<int,int> > > adj;
	vector<int> dist;
	
protected:
	void initV() {
		int V;
		instruction.showVertexNumberInput();
		cin >> V;
		instruction.showVertexNumberInputed(V);
		
		adj = vector<vector<pair<int,int> > >(V+2, vector<pair<int,int> >());
		dist = vector<int>(V+2, oo);
	}
	
	void initE() {
		int E;
		instruction.showEdgeNumberInput();
		cin >> E;
		instruction.showEdgeNumberInputed();
		
		for (int i = 0; i < E; i++) {
			instruction.showEdgeInputing(i);
			
			int a, b, dist;
			cin >> a >> b >> dist;
			
			adj[a].push_back(make_pair(dist, b));
		}
	}

public:
	Graph() {
		reset();
	}
	
	void reset() {
		initV();
		initE();
	}
	
	pair<int,string> shortestPath (int from, int to) {
		priority_queue <pair<int,pair<int,string> >,
						vector<pair<int,pair<int,string> > >,
						greater<pair<int,pair<int,string> > > > que;
		
		dist[from] = 0;
		que.push(make_pair(0, make_pair(from, toString(from))));
		
		while (!que.empty()) {
			pair<int,pair<int,string> > curr = que.top();
			que.pop();
			
			int ftemp = curr.first;
			pair<int,string> stemp = curr.second;
			
			int pos = stemp.first;
			string path = stemp.second;
			
			if (pos == to) {
				return make_pair(dist[to], path);
			}
			
			int adj_size = adj[pos].size();
			for (int i = 0; i < adj_size; i++) {
				int cost = adj[pos][i].first;
				int next = adj[pos][i].second;
				
				if (cost + ftemp < dist[next]) {
					dist[next] = cost + ftemp;
					string curr_path = (path + " -> " + toString(next));
					
					que.push(make_pair(dist[next], make_pair(next, curr_path)));
				}
			}
		}
		
		return make_pair(-1, "Not Found!");
	}
	
	~Graph() {
		adj.clear();
		dist.clear();
	}
};

int main()
{
	instruction.showHeader();
	Graph graph = Graph();
	
	instruction.showFromInput();
	int from;
	cin >> from;
	
	instruction.showToInput();
	int to;
	cin >> to;
	
	pair<int,string> res = graph.shortestPath(from, to);
	cout << "\nShortest Path Calculated!" << endl;
	
	int minCost = res.first;
	cout << "Minimum cost: " << minCost << endl;
	
	string path = res.second;
	cout << "Path: " << path << endl;
	
	return 0;
}
