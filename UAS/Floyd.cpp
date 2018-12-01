#include <algorithm>
#include <climits>
#include <cstdio>
#include <iostream>
#include <vector>

#define oo INT_MAX

using namespace std;

class Graph {
private:
	int N;
	vector<vector<int> > adj;
	
protected:
	/* Get Updated Shortest Path Matrix with mid as Intermediate Vertex */
	vector<vector<int> > getCurrentShortestPath(vector<vector<int> > &prev, int mid) {
		vector<vector<int> > curr = prev;
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				/* 
				 * Shortest path will update if one of the new path
				 * (either from start vertex to intermadiate vertex or from intermadiate vertex to end vertex)
				 * doesn't has INT_MAX as distance value (can reach)
				 */
				if (max(prev[i][mid], prev[mid][j]) != oo) {
					curr[i][j] = min(prev[i][j], (prev[i][mid] + prev[mid][j]));
				}
			}
		}
		
		return curr;
	}

public:
	Graph() {
		this->adj = vector<vector<int> >();
		this->N = 0;
	}
	
	Graph(vector<vector<int> > adj) {
		this->adj = adj;
		this->N = adj.size();
	}
	
	/* Setter */
	void setAdj(vector<vector<int> > adj) {
		this->adj = adj;
		this->N = adj.size();
	}
	
	/* Getter */
	vector<vector<int> > getAdj() {
		return this->adj;
	}
	
	/* Result Getter */
	vector<vector<int> > getShortestPath() {
		vector<vector<int> > shortest_path = adj;
		
		for (int i = 0; i < N; i++) {
			shortest_path = getCurrentShortestPath(shortest_path, i);
		}
		
		return shortest_path;
	}
	
	~Graph() {
		adj.clear();
	}
};


class Table {
private:
	int N;
	
protected:
	/* Horizontal Line */
	void horizontalLine() {
		for (int i = 0; i < N + 1; i++) {
			cout << "+-----";
		}
		cout << "+" << endl;
	}
	
	/* Table Header */
	void header() {
		cout << "|     ";  // First Column
		
		for (int i = 0; i < N; i++) {  // Main Column
			printf("|%5d", i);
		}
		
		cout << "|" << endl;  // End Line
	}
	
	/* Table Rows */
	void row(int i, vector<int> &col) {
		printf("|%5d", i);  // First Column
		
		for (int j = 0; j < N; j++) {  // Main Column
			if (col[j] == oo) {
				printf("|  INF");
			} else {
				printf("|%5d", col[j]);
			}
		}
		
		puts("|"); // End Line
	}
	
	void rows(vector<vector<int> > &matrix) {
		for (int i = 0; i < N; i++) {
			row(i, matrix[i]);
		}
	}

public:
	Table(int N) {
		this->N = N;
	}
	
	showTable(vector<vector<int> > &matrix) {
		horizontalLine();
		header();
		horizontalLine();
		rows(matrix);
		horizontalLine();
	}
};


class Interface {
public:
	Instruction() { }
	
	void showHeader() {
		cout << "------------------------------------------------" << endl;
		cout << "Shortest Path For Every Node (Floyd's Algorithm)" << endl;
		cout << "Created by : Aditya Pratama (0511540000101)" << endl;
		cout << "------------------------------------------------" << endl;
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
		cout << "Input your edges (start <space> end <space> weight):" << endl;
	}
	
	void showEdgeInputing(int i) {
		cout << "Edge " << i << ": ";
	}
	
	void showTable(vector<vector<int> > &matrix) {
		int N = matrix.size();
		Table table = Table(N);
		
		cout << "\nYour result table:" << endl;
		table.showTable(matrix); 
	}
};


class App {
private:
	int N;
	vector<vector<int> > adj;
	Interface iface;

protected:
	/* Initial Adj */
	vector<vector<int> > getInitialAdj() {
		vector<vector<int> > new_adj = vector<vector<int> >(N, vector<int>(N, oo));
		
		for (int i = 0; i < N; i++) {
			new_adj[i][i] = 0;
		}
		
		return new_adj;
	}
	
	/* Setter */
	void setN() {
		int N;
		iface.showVertexNumberInput();
		cin >> N;
		iface.showVertexNumberInputed(N);
		
		this->N = N;
	}
	
	void setAdj() {
		vector<vector<int> > adj = getInitialAdj();
		
		int E;
		iface.showEdgeNumberInput();
		cin >> E;
		iface.showEdgeNumberInputed();
		
		for (int i = 0; i < E; i++) {
			iface.showEdgeInputing(i);
			
			int start, end, dist;
			cin >> start >> end >> dist;
			
			adj[start][end] = dist;
		}
		
		this->adj = adj;
	}

public:
	App() {
		reset();
	}
	
	void reset() {
		this->adj = vector<vector<int> >();
		this->N = adj.size();
		this->iface = Interface();
	}
	
	/* Main Function */
	void run() {
		iface.showHeader();
		setN();
		setAdj();
		
		Graph floyd = Graph(adj);
		vector<vector<int> > result = floyd.getShortestPath();
		
		iface.showTable(result);
	}
	
	~App() {
		adj.clear();
	}
};


int main()
{
	App app;
	app.run();
	
	return 0;
}

