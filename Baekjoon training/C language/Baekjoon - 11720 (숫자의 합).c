#include <stdio.h>

int main(void)
{
    int n, sum;
    scanf("%d", &n);
    char arr[n];
    scanf("%s", arr);
    sum = 0;
    for(int i = 0; i < n; i++)
        sum += arr[i] - '0';
    printf("%d\n", sum);
    return 0;
}
