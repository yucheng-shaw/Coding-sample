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

// The function that takes a set of intervals, merges
// overlapping intervals and prints the result
vector<int64_t> c_mergeIntervals(Interval origin[], int n_origin, Interval clip[], int n_clip)
{
    // Test if the given set has at least one interval
    if (n_origin <= 0)
        return {0};

    // Create an empty stack of clip merged intervals
    stack<Interval> s;

    // sort the intervals in increasing order of start time
    sort(origin, origin+n_origin, compareInterval);
    sort(clip, clip+n_clip, compareInterval);

    // push the first interval to stack
    s.push(origin[0]);
    cout << "s.top().end " << s.top().end << endl;

    // Start from the next interval and clip merge if necessary
    // i is the clip array index
    int i = 0;
    // j is the origin array index
    int j = 0;
    while ((i < n_clip) && (j < n_origin))
    {
        // get interval from stack top
        Interval top = s.top();

        // if current clip interval is completely below the origin stack top,
        // move to inspect the next interval in the clip array
        while (top.start > clip[i].end){
            cout << "i is mistakingly added " << endl;
            cout << "top.start " << top.start << " clip[i].end " << clip[i].end << endl;

            i += 1;
        }
        //check if i+1 is out of range for clip
        if (i == n_clip){cout << "out of clip range" << endl; break;}

        // if the current clip end is less than s.top end
        // there are two circumstances:

        //lower cross
        if ((top.end >= clip[i].end) && (top.start >= clip[i].start))
        {
            cout << "lower cross " << endl;
            Interval temp;
            temp.end = s.top().end;
            temp.start = clip[i].end;
            s.pop();
            s.push(temp);
            //check if there exist degeneracy like [8,8] interval
            if (s.top().end == s.top().start){s.pop();}
            i += 1;
        }
        //clip totally inside origin
        else if((top.end >= clip[i].end) && (top.start <= clip[i].start))
        {
            cout << "totally inside " << endl;
            Interval temp;
            temp.end = clip[i].start;
            temp.start = s.top().start;
            Interval temp_2;
            temp_2.end = s.top().end;
            temp_2.start = clip[i].end;
            s.pop();
            s.push(temp);
            //check if there exist degeneracy like [8,8] interval
            if (s.top().end == s.top().start){s.pop();}
            s.push(temp_2);
            //check if there exist degeneracy like [8,8] interval
            if (s.top().end == s.top().start){s.pop();}
            i += 1;
        }

        // if the current clip end is larger than s.top end
        // there are three circumstances:

        //upper cross
        else if ((top.end <= clip[i].end) && (top.start <= clip[i].start) && top.end >= clip[i].start)
        {
            cout << "upper cross " << endl;
            cout << "i-value " << i << endl;
            cout << "clip[i].start " << clip[i].start << endl;
            cout << "top.end " << top.end << "top.start" << top.start << endl;

            Interval temp;
            temp.end = clip[i].start;
            temp.start = s.top().start;
            s.pop();
            s.push(temp);
            //check if there exist degeneracy like [8,8] interval
            if (s.top().end == s.top().start){s.pop();}
            //check if the j+1 term is out of range for "origin"
            if (j+1 == n_origin){break;}
            s.push(origin[j+1]);
            j += 1;
        }

        //completely covered
        else if ((top.end <= clip[i].end) && (top.start >= clip[i].start))
        {
            cout << "completely covered " << endl;
            cout << "i-value " << i << endl;
            cout << "clip[i].start " << clip[i].start << endl;
            cout << "top.end " << top.end << "top.start" << top.start << endl;
            s.pop();
            //check if the j+1 term is out of range for "origin"
            if (j+1 == n_origin){cout << "out of range" << endl;break;}
            s.push(origin[j+1]);
            j += 1;
        }

        //clip totally above origin
        else if(clip[i].start >= top.end)
        {
            cout << "completely above " << endl;
            cout << "i-value " << i << endl;
            cout << "clip[i].start " << clip[i].start << endl;
            cout << "top.end " << top.end << "top.start" << top.start << endl;
            //check if the j+1 term is out of range for "origin"
            if (j+1 == n_origin){break;}
            s.push(origin[j+1]);
            j += 1;
        }

    }


    //save the merged vector
    vector<int64_t> merged_vect = {};
    while (!s.empty())
    {
        Interval t = s.top();
        merged_vect.push_back(t.start);
        merged_vect.push_back(t.end);
        cout << "merged_vec " << t.start << "merged_vec" << t.end << endl;
        s.pop();
    }
    cout << "while over " << endl;
    return merged_vect;
}

// input: (origin, clip)
// v1=original vector, v2=vector to clip
vector<int64_t> c_merge_vect(vector<int64_t>* a, vector<int64_t>* b)
{
    vector<int64_t> v1 = *a;
    vector<int64_t> v2 = *b;

    //n_origin & n_clip are the numbers of intervals respectively
    int n_origin = v1.size()/ 2;
    int n_clip = v2.size()/ 2;
    Interval origin[n_origin];
    Interval clip[n_clip];

    int idx_interval = 0;
    int idx_origin = 0;
    Interval temp = {0,0};

    //put vector v1 (origin vector) to origin in 'Interval' form
    vector<int64_t>::iterator it;
    for (it = v1.begin(); it != v1.end(); ++it){
        int decide = idx_interval%2;
        cout << "decide " << decide << endl;
        if (decide == 0) {
            temp.start = *it;
            cout << temp.start << endl;
        }
        else {
            temp.end = *it;
            cout << "temp.end" << temp.end << endl;
            origin[idx_origin] = temp;
            temp = {0,0};
            idx_origin += 1;
        }
        idx_interval += 1;
    }

    //put vector v2(clip vector) to clip in 'Interval' form
    idx_interval = 0;
    int idx_clip = 0;

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
            clip[idx_clip] = temp;
            temp = {0,0};
            idx_clip += 1;
        }
        idx_interval += 1;
    }

    //calling the c_mergeIntervals function
    //n_origin is the number of intervals of origin
    return c_mergeIntervals(origin, n_origin, clip, n_clip);
}

int main()
{
    vector<int64_t> origin = {0,3,6,7,10,15,19,23};
    vector<int64_t> clip = {2,11,14,20};
    //the final function is called c_merge_vect
    cout << "result: " << c_merge_vect(&origin, &clip)[2] << "end of result " << endl;
    return 0;
}
