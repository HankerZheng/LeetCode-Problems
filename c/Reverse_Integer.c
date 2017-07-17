int reverse(int x) {
    int temp = x;
    int sol = 0;
    for (; temp != 0; )
    {
        sol = sol * 10 + temp % 10;
        temp = temp / 10;
    }
}