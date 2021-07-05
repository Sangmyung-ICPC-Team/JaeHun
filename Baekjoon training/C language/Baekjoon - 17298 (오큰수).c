#include <stdio.h>
#include <stdlib.h>
#define MAX 1000001

int element[MAX];
int result[MAX];

typedef struct {
	int data[MAX];
	int top;
}StackType;

void init_stack(StackType* s)
{
	s->top = -1;
}

int is_empty(StackType* s)
{
	return (s->top == -1);
}

int is_full(StackType* s)
{
	return (s->top == (MAX - 1));
}

void push(StackType* s, int item)
{
	if (is_full(s))
		return;
	else
		s->data[++(s->top)] = item;
}

int pop(StackType* s)
{
	if (is_empty(s))
		return;
	else
		return s->data[(s->top)--];
}

int main(void)
{
	StackType *s = (StackType *)malloc(sizeof(StackType));
	
	int n;

	init_stack(s);
	scanf("%d", &n);
	
	for (int i = 0; i < n; i++)
		scanf("%d", &element[i]);

	for (int i = 0; i < n; i++)
	{
		while (!is_empty(s) && element[s->data[s->top]] < element[i])
		{
			result[s->data[s->top]] = element[i];
			pop(s);
		}
		push(s, i);
	}

	for (int i = 0; i < n; i++)
	{ 
		if (result[i] == 0)
			printf("-1 ");
		else
			printf("%d ", result[i]);
	}
	return 0;
}
