#include <iostream>
#include<fstream>
#include <string>
#include <vector>
#include <list>

using namespace std;

// This class represents a directed graph using
// adjacency list representation
// adjacency list is done by <list> + vector
class Graph
{
	int V; // No. of vertices

	// Pointer to an array containing adjacency
	// lists
	list<int> *adj;
public:
	Graph(int V); // Constructor

	// function to add an edge to graph
	void addEdge(int v, int w);

	// prints BFS traversal from a given source s
	void BFS(int s);

    vector<int> selected_pixel;
};

Graph::Graph(int V)  // scope resolution operaotr ::
{
	this->V = V;
	adj = new list<int>[V];  //assign adj to point to the newly created V
}

void Graph::addEdge(int v, int w)
{
	adj[v].push_back(w); // Add w to v’s list.
}							//what is the data type of adj[int]? vector!

void Graph::BFS(int s)
{
	// Mark all the vertices as not visited
	bool *visited = new bool[V];
	for(int i = 0; i < V; i++)
		visited[i] = false;  //visited[i] is a one component vecotor

	// Create a queue for BFS
	list<int> queue;

	// Mark the current node as visited and enqueue it
	visited[s] = true;
	queue.push_back(s);

	// 'i' will be used to get all adjacent
	// vertices of a vertex
	list<int>::iterator i;  //iterator is like a smart pointer

	while(!queue.empty())
	{
		// Dequeue a vertex from queue and print it
		s = queue.front();
		cout << s << " ";
		queue.pop_front();

        int sel = s;
        selected_pixel.push_back(sel);

		// Get all adjacent vertices of the dequeued
		// vertex s. If a adjacent has not been visited,
		// then mark it visited and enqueue it
		for (i = adj[s].begin(); i != adj[s].end(); ++i)
		{
			if (!visited[*i])  //*i : dereference to get the boolean value
			{
				visited[*i] = true;
				queue.push_back(*i);
			}
		}
	}
}

//argv takes in the arguments passed in while executing exec file
//argc counts the number of input arguments
int main(int argc, char *argv[]) {
//This part of code read in the input file and transform data into 1D vector of string
    cout << "We have " << argc << " arguments" << endl;
    for (int i = 0; i < argc; ++i){
        cout << "[" << i << "] " << argv[i] << endl;
    }

    ifstream in(argv[1]);  //input file stream stream in a file named argv[1]
    string inputStr;
    vector<string> inputContent;  //a vector of type string
    while(getline(in, inputStr)){  //getline get each lines of input file as string
        inputContent.push_back(inputStr);  //inputContent has M strings with length N
    }
    in.close();

	//cout << inputContent[3][6] << endl;  //will output the char

//This part of code go through the 1D vector and make each entries a node of a graph
	//objection now: construct node containing position and keep a color map
	//linked them to make a graph
    int num_row = inputContent[0][0] - '0';   // cols & rows of color data
    int num_col = inputContent[0][2] - '0';


    Graph g(num_col*num_row);  // Create a graph with # of nodes = # of pixels

    for (int i = 0; i < num_row-1; i++){  // color data start from inputContent[1]
        for (int j = 0; j < num_col-1; j++){
            // Notice inputContent contains 'space' between characters
            if (inputContent[i+1][2*j] == inputContent[i+1][2*(j+1)]){  // Same color as right
                g.addEdge(num_col*i + j, num_col*i + j + 1);
                g.addEdge(num_col*i + j + 1, num_col*i + j);
            }
            else if (inputContent[i+1][2*j] == inputContent[i+2][2*j]){  //Same color as down
                g.addEdge(num_col*i + j, num_col*(i+1) + j);
                g.addEdge(num_col*(i+1) + j, num_col*i + j);
            }  // My way of labeling color data: left up = 0 [[0,1,2,3,4,5,6,7],[8,9,10...]]
        }
    }

    // Deal with the last line
    int i = num_row-1;
    for (int j = 0; j < num_col-1; j++){
        if (inputContent[i+1][2*j] == inputContent[i+1][2*(j+1)]){  // Same color as right
            g.addEdge(num_col*i + j, num_col*i + j + 1);
            g.addEdge(num_col*i + j + 1, num_col*i + j);
        }
    }

// This part of code BFS traverse the graph constructed above
// with the starting point = the given (x,y) corrdinate of color data h*w
    int x = *argv[2] - '0';
    int y = *argv[3] - '0';
    int start = y * num_col + x;  // x and y range from 0 <= x < w ; 0 <= y <h
    g.BFS(start);

// This part of code change the color of the designated pixel and its neighbor
// according to the terminal input
    for (int i = 0; i < g.selected_pixel.size(); i++){
        int char_x;
        int char_y;
        char_y = g.selected_pixel[i] / (num_col);
        char_x = 2 * (g.selected_pixel[i] - char_y * num_col);

        inputContent[char_y + 1][char_x] = *argv[4];
    }

// This part of code put back the newly assigned pixels

// This part of code recount the connected components

// This part of code write the output file
    // Objective: what kind of file shold we output?
    ofstream file;
    file.open (argv[5]);
    for (i = 0; i < inputContent.size(); i++){
        file << inputContent[i] << "\n";
    }
    file.close();
    return 0;
}
