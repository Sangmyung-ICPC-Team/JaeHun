#include <stdio.h>

void print_star(int i, int j, int n)
{
	if ((i / n) % 3 == 1 && (j / n) % 3 == 1)
		printf(" ");
	else
	{
		if (n / 3 == 0)
			printf("*");
		else
			print_star(i, j, n / 3);
	}
}

int main(void)
{
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			print_star(i, j, n);
		}
		printf("\n");
	}
	return 0;
}
