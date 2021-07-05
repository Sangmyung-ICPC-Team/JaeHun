#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_QUEUE_SIZE 2000000

typedef struct {
	int data[MAX_QUEUE_SIZE];
	int front, rear;
}QueueType;

void init_queue(QueueType* q)
{
	q->front = q->rear = -1;
}

int is_empty(QueueType* q)
{
	return (q->front == q->rear);
}

int is_full(QueueType* q)
{
	return ((q->rear + 1) % MAX_QUEUE_SIZE == q->front);
}

int size(QueueType* q)
{
	if (is_empty(q))
		return 0;
	return (q->rear - q->front);
}

void enqueue(QueueType* q, int item)
{
    q->data[++(q->rear)] = item;
}

int dequeue(QueueType* q)
{
	if (is_empty(q))
		return -1;
    return q->data[++(q->front)];
}

int front(QueueType* q)
{
	if (is_empty(q))
		return -1;
	return q->data[q->front + 1];
}

int back(QueueType* q)
{
	if (is_empty(q))
		return -1;
	return q->data[q->rear];
}

int main(void)
{
	QueueType q;
	init_queue(&q);

	int n;
	scanf("%d", &n);

	while (n--) {
		char str[6];
		scanf("%s", str);
		if (!strcmp(str, "push")) {
			int data = 0;
			scanf("%d", &data);
			enqueue(&q, data);
		}
		else if (!strcmp(str, "front"))
			printf("%d\n", front(&q));
		else if (!strcmp(str, "back"))
			printf("%d\n", back(&q));
		else if (!strcmp(str, "pop"))
			printf("%d\n", dequeue(&q));
		else if (!strcmp(str, "size"))
			printf("%d\n", size(&q));
		else if (!strcmp(str, "empty"))
			printf("%d\n", is_empty(&q));
	}
	return 0;
}
