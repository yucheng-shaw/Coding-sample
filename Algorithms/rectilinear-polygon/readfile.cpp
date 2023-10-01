#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
using namespace std;

static string str_buf;
static string operation;
//typedef pair<class _T1, class _T2>

bool read_input_file (const string& input_file)
{
    // opening file
    ifstream ifs(input_file.c_str());
    if (!ifs) {
        cerr << "Cannot open file \"" << input_file << "\"!" << endl;
        return false; }

    // get first line
    getline(ifs, str_buf, '\n');
    operation = str_buf;
    cout << operation << endl;

    // get middle line
    for (int i=0; i<4; ++i) {
        getline(ifs, str_buf, '\n');
        //check if the line is DATA MERGE M1, DATA CLIPPER C2, END DATA

        int begin = 0;
        int end = 1;
        vector<int> line;

        // parse each token
        for (string::iterator it=str_buf.begin(); it!=str_buf.end(); ++it) {
            if ((*it == ' ') || (*it == '\t')) {
                line.push_back(atoi(str_buf.substr(begin, end - begin).c_str()));
                begin = end;
            }
            end += 1;
        }

        vector<int>::iterator it_i;
        for(it_i=line.begin(); it_i!=line.end(); ++it_i) cout << *it_i << " ";
        // get the last token
        //line.push_back(atoi(str_buf.substr(begin, end - begin).c_str()));
        //_input_table.push_back(line);
    }

    vector<pair<int, vector<int>*>> pizza;
    return true;
}

int main(int argc, char *argv[]){
    read_input_file(argv[1]);
}
