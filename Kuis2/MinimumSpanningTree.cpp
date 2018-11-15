/*
 *	Minimum Spanning Tree (Kruskal's Algorithm)
 *	Created by : Aditya Pratama (05111540000101)
 */

#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

class Instruction {
public:
	Instruction() { }
	
	void showHeader() {
		cout << "--------------------------------------------" << endl;
		cout << "Minimum Spanning Tree (Kruskal's Algorithm)" << endl;
		cout << "Created by : Aditya Pratama (05111540000101)" << endl;
		cout << "--------------------------------------------" << endl;
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
};

Instruction instruction = Instruction();

/* Define Types */
struct Vertex {
	int parent;
	int rank;
};

struct Edge {
	int src;
	int dest;
	int weight;
};

/* New Element Creator Methods */
struct Vertex *newV(int v) {
	struct Vertex *vertex = new (struct Vertex);
	
	vertex->parent = v;
	vertex->rank = 0;
	
	return vertex;
}

struct Edge *newE(int src, int dest, int weight) {
	struct Edge *edge = new (struct Edge);
	
	edge->src = src;
	edge->dest = dest;
	edge->weight = weight;
	
	return edge;
}

/* Sorting Comparator Method */
bool comp(struct Edge *a, struct Edge *b) {
	return a->weight < b->weight;
}

class Graph {
private:
	vector<struct Edge *> e;
	vector<struct Vertex *> v;
	vector<struct Edge *> mstE;
	
	/* Initialization Methods */
	void initV() {
		int V;
		instruction.showVertexNumberInput();
		cin >> V;
		instruction.showVertexNumberInputed(V);
		
		v = vector<struct Vertex *>();
		for (int i = 0; i < V; i++) {
			struct Vertex *vertex = newV(i);
			v.push_back(vertex);
		}
	}
	
	void initE() {
		int E;
		instruction.showEdgeNumberInput();
		cin >> E;
		instruction.showEdgeNumberInputed();
		
		e = vector<struct Edge *>();
		for (int i = 0; i < E; i++) {
			instruction.showEdgeInputing(i);
			
			int src, dest, weight;
			cin >> src >> dest >> weight;
			
			struct Edge *edge = newE(src, dest, weight);
			e.push_back(edge);
		}
	}
	
	void initMstE() {
		mstE = vector<struct Edge *>();
	}
	
	/* Parent Finder Method */
	int findParent(int i) {
		if (v[i]->parent != i) {
			v[i]->parent = findParent(v[i]->parent);
		}
		
		return v[i]->parent;
	}
	
	/* Union Set Method */
	void unionV(int x, int y) {
		int xRoot = findParent(x);
		int yRoot = findParent(y);
		
		if (v[xRoot]->rank < v[yRoot]->rank) {
			v[xRoot]->parent = yRoot;
		} else if (v[xRoot]->rank > v[yRoot]->rank) {
			v[yRoot]->parent = xRoot;
		} else {
			v[yRoot]->parent = xRoot;
			v[xRoot]->rank++;
		}
	}

public:
	Graph() {
		reset();
	}
	
	void reset() {
		initV();
		initE();
		initMstE();
	}
	
	/* MST Builder Method */
	void buildMST() {
		int eCount = 0;
		int i = 0;
		
		sort(e.begin(), e.end(), comp);
		
		int V = v.size();
		
		mstE.clear();
		while (eCount < V - 1) {
			struct Edge *nextE = e[i];
			
			int x = findParent(nextE->src);
			int y = findParent(nextE->dest);
			
			// If parent of src and dest aren't same
			if (x != y) {
				mstE.push_back(nextE);
				unionV(x, y);
				
				eCount++;
			}
			
			i++;
		}
	}
	
	/* Show MST Method */
	void showMST() {
		cout << "\nFollowing are the edges in the constructed MST\n";
		for (int i = 0; i < mstE.size(); i++) {
			cout << mstE[i]->src;
			cout << " --- ";
			cout << mstE[i]->dest;
			cout << " == ";
			cout << mstE[i]->weight << endl;
		}
	}
	
	~Graph() {
		e.clear();
		v.clear();
		mstE.clear();
	}
};

int main()
{
	instruction.showHeader();
	
	Graph graph = Graph();
	graph.buildMST();
	graph.showMST();
	
	return 0;
}
