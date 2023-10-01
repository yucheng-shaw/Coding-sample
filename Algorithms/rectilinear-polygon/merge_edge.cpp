// c++ programto that takes in two Intervals sets as vectors and output the merged vector//
//in descending order//
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

// An interval has start time and end time
struct Interval
{
    int64_t start, end;
};

// Compares two intervals according to their staring time.
// This is needed for sorting the intervals using library
bool compareInterval(Interval i1, Interval i2)
{
    return (i1.start < i2.start);
}

// The main function that takes a set of intervals, merges
// overlapping intervals and prints the result
vector<int64_t> mergeIntervals(Interval arr[], int n)
{
    // Test if the given set has at least one interval
    if (n <= 0)
        return {0};

    // Create an empty stack of intervals
    stack<Interval> s;

    // sort the intervals in increasing order of start time
    sort(arr, arr+n, compareInterval);

    // push the first interval to stack
    s.push(arr[0]);

    // Start from the next interval and merge if necessary
    for (int i = 1 ; i < n; i++)
    {
        // get interval from stack top
        Interval top = s.top();

        // if current interval is not overlapping with stack top,
        // push it to the stack
        if (top.end < arr[i].start)
            s.push(arr[i]);

        // Otherwise update the ending time of top if ending of current
        // interval is more
        else if (top.end < arr[i].end)
        {
            top.end = arr[i].end;
            s.pop();
            s.push(top);
        }
    }

    // Print contents of stack
    /*cout << "\n The Merged Intervals are: ";
    while (!s.empty())
    {
        Interval t = s.top();
        cout << "[" << t.start << "," << t.end << "] ";
        s.pop();
    }*/

    //save the merged vector
    vector<int64_t> merged_vect = {};
    while (!s.empty())
    {
        Interval t = s.top();
        merged_vect.push_back(t.start);
        merged_vect.push_back(t.end);
        s.pop();
    }
    cout << "while over " << endl;
    return merged_vect;
}

// Driver program
vector<int64_t> merge_vect(vector<int64_t>* a, vector<int64_t>* b)
{
    vector<int64_t> v1 = *a;
    vector<int64_t> v2 = *b;

    int arr_size = (v1.size() + v2.size()) / 2;
    Interval arr[arr_size];
    int idx_interval = 0;
    int idx_arr = 0;
    Interval temp = {0,0};

    //put vector v2 to arr in 'Interval' form
    vector<int64_t>::iterator it;
    for (it = v2.begin(); it != v2.end(); ++it){
        int decide = idx_interval%2;
        cout << "decide " << decide << endl;
        if (decide == 0) {
            temp.start = *it;
            cout << "temp.start " << temp.start << endl;
        }
        else {
            temp.end = *it;
            cout << "temp.end " << temp.end << endl;
            arr[idx_arr] = temp;
            temp = {0,0};
            idx_arr += 1;
        }
        idx_interval += 1;
    }


    //put vector v1 to arr in 'Interval' form
    for (it = v1.begin(); it != v1.end(); ++it){
        int decide = idx_interval%2;
        cout << decide << endl;
        if (decide == 0) {
            temp.start = *it;
            cout << temp.start << endl;
        }
        else {
            temp.end = *it;
            cout << "temp.end" << temp.end << endl;
            arr[idx_arr] = temp;
            temp = {0,0};
            idx_arr += 1;
        }
        idx_interval += 1;
    }
    //cout << arr[0].start << endl;
    //Interval arr[] =  { {6,8}, {1,9}, {2,4}, {4,7} };

    //calling the mergeIntervals function
    int n = sizeof(arr)/sizeof(arr[0]);
    cout << sizeof(arr[0]) << endl;
    cout << "sizeof arr " << sizeof(arr) << endl;
    for (int i = 0; i < n; ++i){
        cout << "arr[i].start " << arr[i].start << endl;
    }
    cout << "n= " << n << endl;

    //this line will compile but execute nonstop
    //cout << typeid(mergeIntervals(arr, n)[0]).name() << endl;
    return mergeIntervals(arr, n);
}

int main()
{
    vector<int64_t> bob = {0,3,5,8};
    vector<int64_t> alice = {4,7};
    cout << "reult: " << merge_vect(&bob, &alice)[1] << endl;
    return 0;
}
