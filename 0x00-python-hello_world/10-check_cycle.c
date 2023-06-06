#include "lists.h"

/**
 * check_cycle - A function that checks if a singly linked list has a cycle
 * @list: list to check
 * Return: 0 if no cycle is present, or 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *check1 = list;
	listint_t *check2 = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (check1 && check2 && check2->next)
	{
		check1 = check1->next;
		check2 = check2->next->next;

		if (check1 == check2)
			return (1);
	}
	return (0);
}
