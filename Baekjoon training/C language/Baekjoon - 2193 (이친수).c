#include <stdio.h>

int main(void)
{
	int n;
	long long arr[91] = { 0, 1, 0 };

	scanf("%d", &n);

	for (int i = 2; i <= n; i++)
	{
		arr[i] = arr[i - 2] + arr[i - 1];
	}

	printf("%lld\n", arr[n]);
	return 0;
}
