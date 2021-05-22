#include <stdio.h>

int main(void)
{
	int n;
    long long arr[100001] = {0, };
	scanf("%d", &n);
	
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j * j <= i; j++)
		{
			if ((arr[i] > arr[i - j * j] + 1) || arr[i] == 0)
				arr[i] = arr[i - j * j] + 1;
		}
	}

	printf("%lld\n", arr[n]);
	return 0;
}
