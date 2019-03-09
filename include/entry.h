#include <string>
#include <date.h>
using std::string

class Entry {
    public:
        Entry(string name, Date deadline, int priority);
        string get_name() const;
        Date get_date() const;
        int get_priority() const; 
    private: 
        string name;
        Date deadline;
        int priority;
};
