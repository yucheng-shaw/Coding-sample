#include <iostream>
#include<fstream>
#include <string>
#include <vector>
#include <list>

using namespace std;

int main(){
    ofstream file;
    file.open ("sample*.out");
    file << "Please writr this text to a file.\n this text is written using C++\n";
    file.close();
}



/*
vector<char> row;
row.assign(inputContent[0].length(), 0);
vector< vector<char> > input2D;
input2D.assign(inputContent.size(), row);
cout << inputContent[4] << endl;
for (int i = 0; i < inputContent.size(); i++){
    .push_back(k.c_str()[4]);

    //argv takes in the arguments passed in while executing exec file
    //argc counts the number of input arguments
    int main(int argc, char *argv[]) {
        string k = "asdfgyhjklo";
        cout << k[3] << endl;
        cout << k.c_str() << endl;
        cout << typeid(k.c_str()).name();
        vector<char> vec;
        vec.push_back(k.c_str()[4]);
        vec.push_back(k.c_str()[5]);

        list<int> *adj;
        int k = 5;
        adj = new list<int>[k];
        cout << typeid(adj).name() << endl;
        cout << adj << endl;
        cout << &k << endl;

        //int q = 4;
        //adj[k].push_back(q);
        cout << typeid(adj[5]).name() << endl;
        vector<int> vec;
        cout << typeid(vec).name() << endl;

    //transform char to int
        cout << inputContent[0][0] << endl;
        int num_row = inputContent[0][0] - '0';
        int num_col = inputContent[0][2] - '0';
        cout << num_col*num_row << endl;

*/
