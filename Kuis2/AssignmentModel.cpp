/*
 *	Assignment Model (Hungarian Method)
 *	Created by : Aditya Pratama (05111540000101)
 */

#include <algorithm>
#include <climits>
#include <cstdio>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

#define N_CHARS 26

using namespace std;

string toUpperString(int n) {
	string upper_string = "";
	
	while (n > 0) {
		int mod = n % N_CHARS;
		
		if (mod == 0) {
			upper_string = "Z" + upper_string;
			n = (n / N_CHARS) - 1;
		} else {
			upper_string = (char)('A' + (mod - 1)) + upper_string;
			n = (n / N_CHARS);
		}
	}
	
	return upper_string;
}

bool comp(pair<int,int> a, pair<int,int> b) {
	return a.first < b.first;
}


class Instruction {
public:
	Instruction() { }
	
	void showHeader() {
		puts("-------------------------------------------");
		puts("Assignment Model (Hungarian Algorithm)");
		puts("Created by : Aditya Pratama (0511540000101)");
		puts("-------------------------------------------");
	}
	
	void showInput() {
		printf("\nEnter Cost Matrix size: ");
	}
	
	void showMatrixInput(int N) {
		printf("\nInput your matrix (Size %d x %d):\n", N, N);
	}
};

Instruction instruction = Instruction();


class Table {
private:
	int N;
	
protected:
	/* HORIZONTAL LINE CREATOR */
	void horizontalLine() {
		for (int i = 0; i < N + 1; i++) {
			cout << "+-----";
		}
		cout << "+" << endl;
	}
	
	/* HEADER CREATOR */
	void header() {
		cout << "|     ";  // FIRST COLUMN
		
		for (int i = 0; i < N; i++) {  // MAIN COLUMN
			string s = toUpperString(i + 1);
			
			cout << "|" << s;
			for (int j = s.length() + 1; j < 6; j++) {
				cout << " ";
			}
		}
		
		cout << "|" << endl;  // END LINE
	}
	
	/* ROWS CREATOR */
	void row(int i, vector<int> &col) {
		printf("|%5d", i);  // FIRST COLUMN
		
		for (int j = 0; j < N; j++) {  // MAIN COLUMN
			printf("|%5d", col[j]);
		}
		
		puts("|"); // END LINE
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


class Task {
private:
	int N;
	vector<vector<int> > cost;
	vector<vector<int> > matrix;
	vector<vector<int> > lookup;
	vector<pair<int,int> > result;

protected:
	/* INITIATOR */
	void initCost() {
		vector<vector<int> > new_cost = vector<vector<int> >(N, vector<int>(N, INT_MAX));
		
		instruction.showMatrixInput(N);
		for (int i = 0; i < N; i++) {
			printf(">> ");
			
			for (int j = 0; j < N; j++) {
				int x;
				scanf("%d", &x);
				
				new_cost[i][j] = x;
			}
		}
		
		this->cost = new_cost;
	}
	
	void initMatrix() {
		this->matrix = this->cost;
	}
	
	void initLookup() {
		this->lookup = this->matrix;
	}
	
	void initResult() {
		this->result = vector<pair<int,int> >();
	}
		
	/* ROW MODIFIER */
	int minimumValueAtRow(int i) {
		int min_val = INT_MAX;
		
		for (int j = 0; j < N; j++) {
			min_val = min(min_val, matrix[i][j]);
		}
		
		return min_val;
	}
	
	void rowSubtract(int i) {
		int min_val = minimumValueAtRow(i);
		
		for (int j = 0; j < N; j++) {
			matrix[i][j] -= min_val;
		}
	}
	
	void rowOperation() {
		for (int i = 0; i < N; i++) {
			rowSubtract(i);
		}
	}
	
	/* COLUMN MODIFIER */
	int minimumValueAtCol(int j) {
		int min_val = INT_MAX;
		
		for (int i = 0; i < N; i++) {
			min_val = min(min_val, matrix[i][j]);
		}
		
		return min_val;
	}
	
	void colSubtract(int j) {
		int min_val = minimumValueAtCol(j);
		
		for (int i = 0; i < N; i++) {
			matrix[i][j] -= min_val;
		}
	}
	
	void colOperation() {
		for (int j = 0; j < N; j++) {
			colSubtract(j);
		}
	}
	
	/* RESULT CREATOR */
	// ROW RESULT CREATOR
	pair<pair<int,int>,pair<int,int> > choosenCellAtRow(int i) {
		int value = INT_MAX;
		int counter = 1;
		
		int cell_i = -1;
		int cell_j = -1;
		
		for (int j = 0; j < N; j++) {
			if (lookup[i][j] <= value) {
				if (lookup[i][j] < value) {
					value = lookup[i][j];
					counter = 1;
					
					cell_i = i;
					cell_j = j;
					
				} else {
					counter++;
				}
			}
		}
		
		return make_pair(
			make_pair(value, counter),
			make_pair(cell_i, cell_j)
		);
	}
	
	void createResultAtRow(int i) {
		pair<pair<int,int>,pair<int,int> > cell = choosenCellAtRow(i);
		
		int value = cell.first.first;
		int counter = cell.first.second;
		
		int cell_i = cell.second.first;
		int cell_j = cell.second.second;
		
		if ((value != INT_MAX) && (counter == 1)) {
			result.push_back(make_pair(cell_i, cell_j));
			updateLookupAt(cell_i, cell_j);
		}
	}
	
	void createRowResult() {
		for (int i = 0; i < N; i++) {
			createResultAtRow(i);
		}
	}
	
	// COLUMN RESULT CREATOR
	pair<pair<int,int>,pair<int,int> > choosenCellAtCol(int j) {
		int value = INT_MAX;
		int counter = 1;
		
		int cell_i = -1;
		int cell_j = -1;
		
		for (int i = 0; i < N; i++) {
			if (lookup[i][j] <= value) {
				if (lookup[i][j] < value) {
					value = lookup[i][j];
					counter = 1;
					
					cell_i = i;
					cell_j = j;
				} else {
					counter++;
				}
			}
		}
		
		return make_pair(
			make_pair(value, counter),
			make_pair(cell_i, cell_j)
		);
	}
	
	void createResultAtCol(int j) {
		pair<pair<int,int>,pair<int,int> > cell = choosenCellAtCol(j);
		
		int value = cell.first.first;
		int counter = cell.first.second;
		
		int cell_i = cell.second.first;
		int cell_j = cell.second.second;
		
		if (value != INT_MAX) {
			result.push_back(make_pair(cell_i, cell_j));
			updateLookupAt(cell_i, cell_j);
		}
	}
	
	void createColResult() {
		for (int j = 0; j < N; j++) {
			createResultAtCol(j);
		}
	}
	
	// LOOKUP MODIFIER
	void updateLookupRow(int i) {
		for (int j = 0; j < N; j++) {
			lookup[i][j] = INT_MAX;
		}
	}
	
	void updateLookupCol(int j) {
		for (int i = 0; i < N; i++) {
			lookup[i][j] = INT_MAX;
		}
	}
	
	void updateLookupAt(int i, int j) {
		updateLookupRow(i);
		updateLookupCol(j);
	}
	
	// MAIN CREATOR
	void createResult() {
		initResult();
		createRowResult();
		createColResult();
		
		sort(result.begin(), result.end());
	}
	
	/* TOTAL COST COUNTER */
	int getCostTotal() {
		int cost_total = 0;
		
		for (int i = 0; i < result.size(); i++) {
			cost_total += cost[result[i].first][result[i].second];
		}
		
		return cost_total;
	}
	
	/* FORMATTED TABLE VIEWER */
	void showTable(vector<vector<int> > &matrix) {
		Table table = Table(N);
		table.showTable(matrix);
	}

public:
	Task(int N) {
		reset(N);
	}
	
	void reset(int N) {
		this->N = N;
		initCost();
	}
	
	void calculate() {
		initMatrix();
		rowOperation();
		colOperation();
		
		initLookup();
		createResult();
	}
	
	void showCost() {
		puts("\nCost Table:");
		showTable(cost);
	}
	
	void showMatrix() {
		puts("\nMatrix Calculation Table:");
		showTable(matrix);
	}
	
	void showResult() {
		puts("\nResult:");
		for (int i = 0; i < result.size(); i++) {
			printf("%d - ", result[i].first);
			cout << toUpperString(result[i].second + 1) << endl;
		}
	}
	
	void showCostTotal() {
		int cost_total = getCostTotal();
		
		printf("\nCost Total: %d unit%c\n", cost_total
										  , (cost_total > 1 ? 's' : '\0'));
	}
};


int main()
{
	instruction.showHeader();
	
	int N;
	instruction.showInput();
	scanf("%d", &N);
	
	Task task = Task(N);
	task.calculate();
	
	task.showCost();
	task.showMatrix();
	task.showResult();
	task.showCostTotal();
	
	return 0;
}

