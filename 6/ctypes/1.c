int sum(int *arr, int len) {
    int s = 0;
    for (int i = 0; i < len; ++i) {
        s += arr[i];
    }
    return s;
}


