#include <stdio.h>

int main(void)
{
	int n, *a, *b, result;
	scanf("%d", &n);

	a = (int*)malloc(sizeof(a) * n);
	b = (int*)malloc(sizeof(b) * n);

	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);

	for (int i = 0; i < n; i++)
		scanf("%d", &b[i]);

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < i; j++)
		{
			if (a[i] > a[j])
			{
				int temp;
				temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}

			if (b[i] < b[j])
			{
				int temp;
				temp = b[i];
				b[i] = b[j];
				b[j] = temp;
			}
		}
	}

	result = 0;
	for (int i = 0; i < n; i++)
		result += a[i] * b[i];
	printf("%d\n", result);
	return 0;
}
