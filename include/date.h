class Date {
    public:
        Date(int year, int month, int day, int time);
        bool operator<(const Date& other_date) const;
    private:
        int year;
        int month;
        int day;
        int time;
}
